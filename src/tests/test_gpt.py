import pytest

from domain.entities import ArticleImage, TranslatedCrawledTrend
from infra.gpt import regenerate_articles


@pytest.mark.asyncio
async def test_to_gpt_invalid_char():
    trend = [TranslatedCrawledTrend(keywords=['입추'],
                        articles=["# Title: 'Yipchu Magic' doesn't "
                                  "work...Typhoon 'Kanun' comes between "
                                  'Gyeongnam and Jeollanam-do\n'
                                  '\n'
                                  '# Lead: Today, Ipchu, most of the region '
                                  'will experience extreme heat, and Typhoon '
                                  "Kanun's path will turn westward.\n"
                                  '\n'
                                  '# Body: Most of the region will be under '
                                  'severe heat advisory today, Lunar New Year\n'
                                  "Typhoon Kanun's path veers further west\n"
                                  'People wash their faces at Namsan Mountain '
                                  'in Seoul on the morning of Sept. 7, a day '
                                  'ahead of the Lunar New Year, but still '
                                  'under a heat wave. Yonhap\n'
                                  'The scorching heat is expected to persist '
                                  'across the country, except for Gangwon-do '
                                  'and the east coast of North Gyeongsang '
                                  'Province, during the Lunar New Year, which '
                                  'marks the beginning of the fall season.\n'
                                  'Typhoon No. 6, Kanun, is expected to take a '
                                  'slightly more westerly course than expected '
                                  'and make landfall on the south coast '
                                  'between Gyeongnam and Jeonnam. However, '
                                  "Kanun's wind radius (the area with winds of "
                                  '15㎧ or more) is more than 300 kilometers, '
                                  'so the entire country is still under its '
                                  'influence.\n'
                                  'The Korea Meteorological Administration '
                                  '(KMA) forecasts that the maximum '
                                  'temperature will be around 30 degrees on '
                                  'the 8th as easterly winds enter the east '
                                  'coast of Gangwon-do and Gyeongbuk-do, while '
                                  'heat warnings will continue in most other '
                                  'areas. The heat advisory is expected to be '
                                  'lifted on the 9th and 10th as Typhoon '
                                  'Kanun, the sixth typhoon in the country, '
                                  'brings rain across the country.\n'
                                  'As of 9 a.m. on the 9th, Kanun was moving '
                                  'northward in the sea south of Kagoshima, '
                                  'Japan, and is expected to move into the sea '
                                  'about 150 kilometers west of Kagoshima at 3 '
                                  'p.m. and pass over Kyushu. At 3 a.m. on the '
                                  '10th, Kanun is expected to move offshore '
                                  'about 170 kilometers east of Seogwipo '
                                  'before making landfall 30 kilometers '
                                  'southwest of Tongyeong the same morning as '
                                  "a 'strong' storm.\n"
                                  "Due to Kanun's influence, a typhoon warning "
                                  'has been issued for the outer eastern '
                                  'waters of the South Sea. Strong wind '
                                  'warnings are in effect for Geomundo and '
                                  'Chodo, Jeollanam-do, and wind warnings are '
                                  'in effect for most of the East and South '
                                  'Seas. The wind advisory is expected to '
                                  'gradually extend to the entire sea, and is '
                                  'expected to change to a typhoon advisory as '
                                  'Kanun advances northward.\n'
                                  'Showers due to atmospheric instability are '
                                  'expected in inland areas where the heat '
                                  'wave persists. The Korea Meteorological '
                                  'Administration forecast showers in southern '
                                  'Gyeonggi and southern Gangwon, inland '
                                  'Chungcheong, and southern regions '
                                  '(excluding the east coast of North '
                                  'Gyeongsang) from this afternoon to '
                                  'evening.\n'
                                  'In particular, rainfall is expected to '
                                  'reach 5 to 60 millimeters in the Jeolla and '
                                  'Gyeongsang regions, with up to 80 '
                                  'millimeters in Chungcheongnam-do and more '
                                  'than 100 millimeters in inland Jeolla, '
                                  'Gwangju, and Jeonnam-do. In the Seoul '
                                  'metropolitan area and the eastern parts of '
                                  'Gangwon-do, Busan, Ulsan, and Gyeongnam, '
                                  'the expected rainfall is 5 to 40 '
                                  'millimeters.\n'
                                  'Reporter Soyoon Shin yoon@hani.co.kr',
                                  "#Title: It's Lunar New Year and it's 37 "
                                  'degrees... Heat illnesses soar 47% over '
                                  'last year\n'
                                  '\n'
                                  '# Lead: Today is the Mid-Autumn Festival, '
                                  "and it's 37 degrees... Heat illnesses soar "
                                  '47% over last year Typhoon pushes heat '
                                  'north Typhoon pushes heat even at the '
                                  'threshold of autumn It will be very hot in '
                                  'most parts of the country, with daytime '
                                  'temperatures soaring to 37 degrees on the '
                                  'eighth day of the Mid-Autumn Festival. The '
                                  'Japan Meteorological Agency said that on '
                                  'the 8th, the temperature will rise in the '
                                  'sun and the humidity ca\n'
                                  '\n'
                                  '# Body: None'],
                        images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/494/imgdb/child/2023/0808/16914569375954_20230808500551.jpg',
                                             source='한겨레'),
                                ArticleImage(url='https://images.chosun.com/resizer/gNphVKPPUhnGfcXHi-o1brE-qOo=/1200x630/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/BXL7SV646VLHFEL4SAIAQRSBWI.jpg',
                                             source='조선일보')])]
    print(trend.articles[0])
    # response = await regenerate_articles(invalid_char_included)
    # print(response)
    assert True
