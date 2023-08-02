import logging

import httpx
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.exceptions import InvalidCountryCodes
from consts import TARGET_COUNTRY_CODES
from infra.google_trends import daily_trends
from infra.gpt import num_tokens_from_messages, regenerate
from infra.news_crawler import from_trends
from infra.translate import translate_crawled_trends

router = APIRouter(prefix='/trends', tags=["trends"])




mocked_crawled_trends = [
  {
    "keywords": [
      "태풍",
      "태풍경로",
      "태풍 카눈",
      "카눈"
    ],
    "texts": [
      "# Title:공포의 '카눈' 한반도 노려보나‥휴가철 태풍 북상에 '초비상'\n\n# Lead:중심 부근 초속 49미터로 매우 강한 태풍으로 덩치를 키운 6호 태풍 카눈이 일본 오키나와로 접근하고 있습니다. 기상청에 따르면 오늘 오전 9시 일본 오키나와 남남동쪽 260㎞ 해...\n\n# Body:Previous Next\n전체재생\n중심 부근 초속 49미터로 매우 강한 태풍으로 덩치를 키운 6호 태풍 카눈이 일본 오키나와로 접근하고 있습니다.\n기상청에 따르면 오늘 오전 9시 일본 오키나와 남남동쪽 260㎞ 해상을 지난 카눈은 중심기압 935hPa(헥토파스칼), 중심 최대풍속은 초속 49m로 '매우 강'한 태풍으로 발달했습니다.\n이에 따라 오키나와에는 강풍을 동반한 폭우가 쏟아지는 등 비상이 걸렸습니다.\n오늘 이후 카눈은 서북서진을 거듭하다가 이번 주말 대만 북동쪽에서 정체할 것으로 예상됐는데 이후 경로는 유동적입니다.\n당초 중국을 향할 것으로 보였지만 방향을 틀어 한반도로 오거나 일본을 향할 가능성이 높아지고 있습니다.\n이동속도가 매우 느린 카눈은 이번 주말 동중국해에 머물며 고온다습한 공기를 우리나라에 주입해 무더위를 부추길 것으로 기상청은 내다봤습니다.\n한편 중국에 상륙한 5호 태풍 독수리는 중국 내륙에 물폭탄을 퍼붓고 소멸했습니다.",
      "# Title:태풍 ‘카눈’ 예상경로 변경...한반도 향할 수도\n\n# Lead:중국으로 향하던 6호 태풍 ‘카눈’이 진로를 바꾸고 있습니다. 중국이 아닌 한반도와 일본을 향할 가능성이 있습니다.\n\n# Body:중국으로 향하던 6호 태풍 ‘카눈’이 진로를 바꾸고 있습니다. 중국이 아닌 한반도와 일본을 향할 가능성이 있습니다.\n한국 기상청이 31일 발표한 태풍 예상 경로에 따르면 카눈은 8월 1일 오키나와 남쪽 약 180km 부근 해상을 지나 2일 오후 9시경 오키나와 서남서쪽 약 260km 해상을 지날 것으로 보입니다.\n이후 카눈은 북서진하면서 3일에서 5일 당초 예상 경로였던 상하이 남동쪽 해상에서 한반도 쪽으로 방향을 틀 것으로 전망됩니다.\n태풍 카눈의 세력은 ‘매우 강함’으로 예측됩니다.\n기상청은 \"카눈 진행 방향 정면에서 북서풍이 불어 이동속도가 느려지고 있다\"며 \"태풍 예상 경로에 변화가 생겼다\"라고 설명했습니다.\n미국 합동태풍경보센터(JTWC)와 일본·중국 기상당국도 카눈이 상하이와 오키나와 사이 바다에서 진로를 바꿀 것으로 보고 있습니다.\nVOA 뉴스"
    ],
    "images": [
      {
        "url": "https://image.imnews.imbc.com/news/2023/society/article/__icsFiles/afieldfile/2023/08/01/joo230801_vo4.jpg",
        "source": "MBC뉴스"
      },
      {
        "url": "https://gdb.voanews.com/01000000-0a00-0242-c4e5-08db91bdebdb_w1200_r1.jpg",
        "source": "VOA Korea"
      }
    ]
  }
]

@router.get("/")
async def generate_news(country: str):
    # 0. cronjob per 나라 05:00 am 기준 (우리나라는 그 나라에 맞춰서)
    # 1. coutries
    # 2. news link unique
    # 3. check is_unique url
    # 4. url 저장 
    # cronjob-hook > countries > trends > articles > crawl > regenerate > translate > to_markdown > push github, sns
    a = num_tokens_from_messages([{
                "role": "system",
                # "content": "Korean researchers' paper on 'first room-temperature superconductor' controversial...'It needs to be verified'\nEntered 2023.07.28 (19:11)Edited 2023.07.28 (19:23)Society\n06가\n\nA paper by Korean researchers claiming to have developed a room-temperature, normal-pressure superconductor, which has been considered one of the challenges in the scientific community, has sparked controversy not only in Korea but also abroad.\n\nWhile foreign countries have taken notice of the paper, foreign academics are critical and domestic academics are cautious, saying that it still needs to be verified.\n\nThe researchers claim that one author uploaded the paper to an online site without the permission of the other authors, and they plan to publish the paper through a formal peer-review process.\n\nTwo papers related to superconductors exhibiting superconductivity at room temperature and atmospheric pressure were posted on the pre-publication site 'Archive' on the 22nd.\n\nThe authors included Lee Seok-bae, president of Quantum Energy Research Institute, and researchers from the company; Kwon Young-wan, a research professor at Korea University; Oh Geun-ho, an emeritus professor at Hanyang University; and Kim Hyun-tak, who worked at the Korea Electronics and Telecommunications Research Institute (ETRI) until last year.\n\nThe archive is a site for the rapid publication of non-peer-reviewed papers. The papers featured here have not yet been validated by the academic community.\n\nRoom temperature superconductors are a long-standing challenge for the scientific community. The phenomenon of superconductivity is when the electrical resistance of a material, such as a metal, goes to zero below a certain temperature.\n\nEliminating electrical resistance reduces the energy that resistance consumes, which has numerous applications in maglev trains and power grids, but currently superconductivity can only be realized at extremely low temperatures or very high pressures, limiting its use.\n\nIn their paper, the researchers claim to have developed a new material called 'LK-99,' a crystalline structure of lead and apatite, and that the critical temperature at which superconductivity occurs is 127 degrees Celsius (400 K), meaning that when the temperature is below 127 degrees, superconductivity occurs.\n\nThe researchers said they had been conducting research for more than 20 years based on a theory proposed by Choi Dong-sik, an emeritus professor of chemistry at Korea University in the 1990s. Quantum Energy Research Institute was founded by researchers at Korea University in 2008.\n\nThe findings have been spreading rapidly in the Korean internet community, and foreign media have been covering them overseas.\n\nHowever, the scientific community is skeptical about the findings.\n\nThere have been several announcements that overseas researchers have developed room-temperature superconductors, but even recently, there have been controversies, with papers being retracted due to lack of reproducibility.\n\nIn 2020, a research team led by Professor Langer Dias of the University of Rochester in the United States announced in the international journal Nature that they had developed a room-temperature superconductor at 1 million times atmospheric pressure, but the paper was retracted because it was not reproducible.\n\nProfessor Dias published another room-temperature superconductor paper in Nature this year, but his 2021 paper in the international journal Physical Review Letters was once again retracted for data manipulation.\n\nThe Korean researchers' paper has also been criticized for the lack of details in the published data, and the difficulty of superconductivity due to the nature of the material.\n\nThe international journal Science published a review of the paper on Nov. 27 (local time), saying that the lack of details in the paper has left physicists skeptical.\n\nScience noted that the Argonne National Laboratory and others are trying to reproduce the material in the paper, and that physicists could verify the claims within a week.\n\nThe Korean scientific community is also saying that the researchers have not had any interaction with the domestic superconductor community and should be viewed with caution before verification.\n\nThe authors of the paper have stated that it is not a finished paper and was not intended for publication.\n\n[Photo source: Yonhap / YouTube capture]\n\n■ Reporting\n▷ KakaoTalk: Search for 'KBS Report', add channel\n▷ Phone : 02-781-1234, 4444\n▷ Email : kbs1234@kbs.co.kr\n▷ Subscribe to KBS News on YouTube, Naver, and Kakao!\n",
                "content": "‘상온 초전도체 최초 구현’ 한국 연구진 논문 논란…“검증 거쳐야”\n입력 2023.07.28 (19:11)수정 2023.07.28 (19:23)사회\n06가\n\n한국 연구진이 과학계 난제 중 하나로 꼽혀온 상온 상압 초전도체를 개발했다는 논문이 알려지면서 국내뿐 아니라 해외에서도 논란이 커지고 있습니다.\n\n해당 논문에 외신도 주목하고 나섰지만, 외국 학계는 비판적이고 국내 학계 역시 아직 검증이 필요하다며 신중한 분위기입니다.\n\n해당 연구진은 한 저자가 다른 저자들의 허락 없이 논문을 온라인 사이트에 올린 것이라며 정식 동료 평가 절차를 거쳐 논문을 게재하겠다는 입장입니다.\n\n지난 22일 논문 사전공개 사이트 ‘아카이브’에 상온과 대기압 조건에서 초전도 현상을 보이는 초전도체와 관련된 두 개의 논문이 올라왔습니다.\n\n저자로는 이석배 퀀텀에너지연구소 대표와 회사 연구자, 권영완 고려대 연구교수, 오근호 한양대 명예교수, 지난해까지 한국전자통신연구원(ETRI)에 근무했던 김현탁 박사 등이 포함됐습니다.\n\n아카이브는 동료 평가를 거치지 않은 논문을 빠르게 공개하기 위한 사이트로, 누구나 쉽게 게재할 수 있는 구조입니다. 이곳에 나온 논문은 아직 학계의 검증을 받지 않은 것입니다.\n\n상온 초전도체는 과학계의 오랜 난제 중 하나입니다. 초전도 현상은 금속 등에서 전기저항이 어느 온도 아래에서 0이 되는 현상을 말합니다.\n\n전기 저항을 없애면 저항이 소모하는 에너지를 줄일 수 있어 자기부상열차나 전력망 등에 사용처가 무궁무진하지만, 현재는 극저온이나 초고압에서만 초전도 현상을 구현할 수 있어 활용도가 낮습니다.\n\n연구진은 논문에서 납과 인회석 결정 구조인 ‘LK-99’라는 새로운 물질을 개발했다며 초전도 현상이 일어나는 임계 온도가 섭씨 127도(400K)라고 주장했습니다. 온도가 127도 이하일 때는 초전도 현상이 일어난다는 뜻입니다.\n\n이들은 1990년대 고려대 화학과 최동식 명예교수가 주장한 이론을 바탕으로 20여 년에 걸쳐 연구를 진행했다고 밝혔습니다. 퀀텀에너지연구소는 2008년 고려대 연구자들이 창업한 기업입니다.\n\n이번 연구결과는 국내 인터넷 커뮤니티를 중심으로 빠르게 확산하고 있고, 해외에서는 외신들이 잇따라 소개하는 등 주목을 받고 있습니다.\n\n하지만 과학계는 이번 연구결과에 대해 회의적인 분위기입니다.\n\n해외에서도 상온 초전도체를 개발했다는 발표가 여러 차례 있었지만, 최근에도 재현성이 없다며 논문이 철회되는 등 논란이 있기 때문입니다.\n\n앞서 미국 로체스터대 랭거 디아스 교수 연구팀이 2020년 국제학술지 ‘네이처’에 대기압 100만 배 압력에서 상온 초전도체를 개발했다고 발표했지만, 재현이 불가능하다며 논문이 철회됐습니다.\n\n디아스 교수는 올해 네이처에 다시 상온 초전도체 논문을 발표했지만, 2021년 국제학술지 ‘피지컬 리뷰 레터스’에 낸 논문이 또다시 데이터 조작을 이유로 철회되면서 의심의 눈초리를 받고 있습니다.\n\n한국 연구진의 이번 논문 역시 발표한 데이터가 세부 사항이 부족하다는 지적과 물질 특성상 초전도성이 발현되기 어렵다는 지적이 나오고 있습니다.\n\n국제학술지 사이언스는 27일(현지시간) 이번 논문에 대해 조망하며 “논문의 세부사항이 부족해 물리학자들이 회의감에 휩싸여 있다”고 학계의 반응을 실었습니다.\n\n사이언스는 미국 아르곤국립연구소 등이 논문 내 물질을 재현하려고 시도하고 있다며 1주일 내로 물리학자들이 이번 주장을 검증할 수 있다고 전했습니다.\n\n국내 과학계도 이들 연구자가 국내 초전도체 학계와 교류가 전혀 없었던 상황인 만큼 검증이 되기 전에는 신중하게 바라봐야 한다는 의견을 내놓고 있습니다.\n\n논문 저자들은 이번 논문이 완성된 논문이 아니며 공개도 의도한 바가 아니라는 입장을 밝혔습니다.\n\n[사진 출처 : 연합뉴스 / 유튜브 캡처]\n\n■ 제보하기\n▷ 카카오톡 : 'KBS제보' 검색, 채널 추가\n▷ 전화 : 02-781-1234, 4444\n▷ 이메일 : kbs1234@kbs.co.kr\n▷ 유튜브, 네이버, 카카오에서도 KBS뉴스를 구독해주세요!\n"
                },])
    
    if country not in TARGET_COUNTRY_CODES:
        raise InvalidCountryCodes()

    google_trends = await daily_trends(country)
    crawled_trends = await from_trends(google_trends)
    translated_trends = await translate_crawled_trends(crawled_trends)


    # regenerated_articles = await regenerate(mocked_crawled_trends)
    # translated_articles = await translate(regenerated_articles)
    # markdowned_articles = await to_markdown(translated_articles)
    # await push(markdowned_articles)
    # return JSONResponse(content=jsonable_encoder(regenerated_articles))
