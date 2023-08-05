import datetime

from domain.entities import (Article, ArticleContent, ArticleImage,
                             CrawledTrend, Folder, GoogleTrend, Language,
                             Markdown, QnA, TranslatedCrawledTrend,
                             TrendArticleMeta)

######################### STEP 1 ##########################
step_1 = [GoogleTrend(query='잼버리',
             related_quries=['잼버리 대회', '새만금', '새만금 잼버리', '잼버리 여가부'],
             articles=[TrendArticleMeta(url='https://www.mindlenews.com/news/articleView.html?idxno=4464',
                                        source='시민언론 민들레'),
                       TrendArticleMeta(url='http://www.monews.co.kr/news/articleView.html?idxno=325623',
                                        source='메디칼업저버')]),
 GoogleTrend(query='임지연',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://biz.chosun.com/entertainment/enter_general/2023/08/04/D3XFVGQGM2YTZC5SLIGGJT5OLY/',
                                        source='조선비즈'),
                       TrendArticleMeta(url='https://news.mt.co.kr/mtview.php?no=2023080308080533315',
                                        source='머니투데이')]),
 GoogleTrend(query='류현진',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://www.hani.co.kr/arti/sports/baseball/1102657.html',
                                        source='한겨레'),
                       TrendArticleMeta(url='https://imnews.imbc.com/news/2023/sports/article/6510102_36154.html',
                                        source='MBC뉴스')]),
 GoogleTrend(query='리버풀',
             related_quries=[],
             articles=[TrendArticleMeta(url='http://www.fourfourtwo.co.kr/news/articleView.html?idxno=38661',
                                        source='포포투')]),
 GoogleTrend(query='일본',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://www.beautynury.com/news/view/102114/cat/10',
                                        source='뷰티누리(화장품신문)'),
                       TrendArticleMeta(url='http://www.monthlypeople.com/news/articleView.html?idxno=620216',
                                        source='월간인물')])]


########################## STEP 2 ##########################
step2 = [CrawledTrend(keywords=['류현진'],
              articles=['# Title: 류현진, 최고 구속 146㎞로는 AL 승률 1위 팀 막지 못했다\n'
                        '\n'
                        '# Lead: 2일 볼티모어전 선발 등판…5이닝 9피안타 4실점\n'
                        '\n'
                        '# Body: 2일 볼티모어전 선발 등판…5이닝 9피안타 4실점\n'
                        '토론토 블루제이스 류현진이 2일(한국시각) 캐나다 온타리오주 토론토의 로저스센터에서 열린 '
                        '2023 메이저리그(MLB) 볼티모어 오리올스와 안방 경기에 선발로 등판해 공을 던지고 있다. '
                        '토론토/AP 연합뉴스\n'
                        '426일 만의 빅리그 등판. 초반은 불안했다. 하지만 점차 ‘코리안 몬스터’다운 안정을 '
                        '되찾았다. 재활 기간 13㎏ 감량한 류현진(36)이 건강하게 돌아왔다.\n'
                        '류현진은 2일(한국시각) 캐나다 온타리오주 토론토의 로저스센터에서 열린 2023 '
                        '메이저리그(MLB) 볼티모어 오리올스와 안방 경기에 선발 등판해 5이닝 9피안타(1피홈런) '
                        '1볼넷 3탈삼진 4실점 했다. 투구 수는 80개(스트라이크 54개). 왼 팔꿈치 인대 접합 수술 '
                        '이후 14개월 만의 등판 성적으로는 나쁘지 않은 기록이었다. 류현진의 빅리그 등판은 작년 '
                        '6월2일 로저스센터에서 열린 시카고 화이트삭스와 경기 이후 426일 만이었다. 이날 '
                        '로저스센터에는 4만691명의 관중이 찾아 류현진의 복귀전을 지켜봤다.\n'
                        '아메리칸리그 승률 1위 팀인 볼티모어를 상대로 출발은 아주 안 좋았다. 류현진은 1회초 볼티모어 '
                        '1번 타자인 포수 애들리 러츠맨에게 초구 시속 88.2마일(142㎞) 포심패스트볼을 던졌다가 '
                        '2루타를 얻어맞았다. 2번 타자 라이언 마운트캐슬에게도 3구째 시속 84.7마일(136㎞)의 '
                        '커터가 공략당하며 2루타를 허용, 선제점을 헌납했다. 뒤이어 앤서니 산탄데르에게도 초구에 좌전 '
                        '안타를 허용해 3연속 안타를 두들겨 맞았다. 14개월 만에 오른 빅리그 마운드가 류현진에게 '
                        '버거워 보일 정도였다. 하지만 무사 1, 3루에서 오스틴 헤이스를 뜬공으로 잡아내며 점차 안정을 '
                        '되찾았다. 거너 헨더슨의 내야 땅볼 때 2점째를 허용했으나 1회 실점은 거기까지였다.\n'
                        '류현진은 2회초 2사 3루에서 적시타를 내주면서 3점째를 내줬으나 3~5회는 커브 제구가 잘 '
                        '되면서 실점 없이 안정적인 투구를 선보였다. 그러나 3-3이던 6회초 선두 타자 헨더슨에게 던진 '
                        '시속 77.4마일(124.6㎞)의 체인지업이 가운데로 몰리면서 우월 솔로포를 두들겨 맞았다. '
                        '류현진은 곧바로 트레버 리처즈에게 마운드를 넘기고 내려왔다.\n'
                        '류현진의 이날 포심 패스트볼 최고 구속은 시속 91마일(146.5㎞)이 찍혔다. 평균 구속은 '
                        '시속 89마일(143.3㎞). 체인지업의 제구도 들쑥날쑥해 류현진 본인도 어이없어 할 만큼 '
                        '실투가 나왔다. 그나마 3회, 5회 실점 위기에서 병살타를 유도해내며 위기를 탈출하는 모습은 '
                        '예전 그대로였다. ‘MLB닷컴’ 토론토 담당 기자 키건 매티슨은 경기 뒤 자신의 트위터에 '
                        '“류현진이 빅리그에 복귀한 것은 매우 고무적이고, 다음 등판도 흥미로울 것”이라면서 “특히 '
                        '구속이 중요하다”고 평했다.\n'
                        '토론토는 불펜진이 볼티모어 화력을 견디지 못하면서 3-13으로 대패했다. 산탄데르가 만루홈런 등 '
                        '4타수 3안타 4타점, 류현진에게 일격을 가한 헨더슨이 5타수 3안타 4타점으로 활약했다. '
                        '토론토가 역전에 실패하며 류현진은 복귀전에서 패전 투수가 됐다. 토론토는 3연패. 6인 선발 '
                        '로테이션을 운영 중인 팀 사정상 류현진의 다음 등판은 8일 클리블랜드 가디언스 전이 될 것으로 '
                        '보인다.\n'
                        '김양희 기자 whizzer4@hani.co.kr',
                        '# Title: 류현진, 복귀전서 5이닝 4실점 패전‥최고 구속 146km\n'
                        '\n'
                        '# Lead: 메이저리그 토론토의 류현진 선수가 작년 6월 팔꿈치 인대 접합 수술을 받은 뒤 '
                        '1년 2개월 만에 나선 복귀전에서 5이닝동안 4실점했습니다. 류현진은 볼티모어와 홈경기에 선발 '
                        '등판해...\n'
                        '\n'
                        '# Body: 전체재생\n'
                        '메이저리그 토론토의 류현진 선수가 작년 6월 팔꿈치 인대 접합 수술을 받은 뒤 1년 2개월 만에 '
                        '나선 복귀전에서 5이닝동안 4실점했습니다.류현진은 볼티모어와 홈경기에 선발 등판해 1회 연속 '
                        '3안타를 내주며 2실점했고 2회에도 한 점을 더 내줬지만 이후 병살타 2개를 유도하며 5회까지는 '
                        '추가 실점없이 안정된 투구를 펼쳤습니다.6회에도 마운드에 오른 류현진은 첫 타자 헨더슨에게 솔로 '
                        '홈런을 내준 뒤 3대 4로 뒤진 상황에서 교체됐습니다.5이닝 9피안타 4실점을 기록한 류현진은 '
                        '볼넷 하나를 내주는 동안 삼진 3개를 잡았고 투구수 80개에 최고 구속은 146km까지 '
                        '나왔습니다.토론토가 13대 3으로 크게 패하면서 류현진은 시즌 첫 패전을 떠안았고 평균자책점은 '
                        '7.20을 기록했습니다.'],
              images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg',
                                   source='한겨레'),
                      ArticleImage(url='https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg',
                                   source='MBC뉴스')],
              language='ko')]

########################## STEP 3 ##########################
json_error_step_3 = [TranslatedCrawledTrend(keywords=['안보현', '지수 안보현', '안보현 지수', '블랙핑크 지수'], articles=['# Title: [Official] BLACKPINK\'s Jisoo - Actor Bo Bo Hyun admits to romance, "We\'re getting to know each other little by little"\n\n# Lead: Jisoo (28) of the group BLACKPINK and actor Bo Bo Hyun (35) are in a relationship. On the 3rd, Jisoo\'s agency, YG Entertainment, said, "They are getting to know each other with good feelings...\n\n# Body: viewer Actor Bo Bo Hyun and BLACKPINK\'s Jisoo / Photo by Seoul Economic Star DB\n< Copyright ⓒ The Seoul Economic Times, All rights reserved >.\nJisoo (28) of the group Blackpink and actor Bo Bo Hyun (35) are in a relationship.On March 3, Jisoo\'s agency YG Entertainment said, "They are getting to know each other little by little with good feelings. We would appreciate it if you could watch them with a warm gaze."Anbo Hyun\'s agency, FN Entertainment, also said, "They are in the stage of getting to know each other carefully with good feelings. We would appreciate it if you could watch them with a warm gaze."Earlier in the day, media outlet Dispatch reported that Jisoo and Anbo Hyun were spotted dating at Jisoo\'s home in Seoul. "They have a lot of common denominators, from acting to singing to fashion," a source close to the pair told the dispatch.Jisoo debuted with the group BLACKPINK in 2016, releasing a slew of hits including "Whistle," "Boom Boom," "Like the Last Time," "Doo Doo Doo," and "Kill This Love," before becoming a global girl group. In 2021, she made her acting debut in the JTBC drama "Seolganghwa."Bo Bo Hyun made her acting debut in the 2014 drama "Golden Cross," and has since appeared in the drama "Descendants of the Sun" and the movie "Hija. Since 2020, he has gained popularity for his roles in the dramas "Itaewon Class," "Yumi\'s Cells," and the Netflix series "My Name. He recently appeared in the tvN drama "Please Take Care of Me This Time" as the lead character, Doc Ha.', "# Title: The Ultimate Boyfriend Look #Boonhyun #Allure Korea\n\n# Lead: Actor Bo Bo Hyun is the first actor to admit to a romantic relationship with Jisoo. The model-turned-actor is known for his impeccable height of 187 centimeters and his dedication to acting. What is it that makes him so attractive? We got a glimpse through five characteristics of his casual look.\n\n# Body: This browser does not support sharing.\nAddress.\nActor Bo Bo Hyun cautiously acknowledged his love affair with Jisoo. The model-turned-actor is known for his impeccable height of 187 centimeters and his dedication to acting. Is his warm and attentive personality reflected in his looks? We've picked out the top 5 characteristics of Bo Bo-hyun's off-duty look.\n1) A man who knows how to wear a shirt\nAs a former boxer in his student days, Boo-hyun has maintained his superior physique. Perhaps that's why his muscular upper body really shines when he wears a shirt. He's definitely in our top 5 best shirt-fitting men.\n2) Utilize sunglasses\nINFJ Boo-hyun loves to travel, and when he does, he relies heavily on hats and masks to cover his face. If there's one thing he can't live without, it's sunglasses. He can wear them nonchalantly on top of a hat or with a beanie and never feel out of place.\n3) Nerdiness with glasses\nOn the other hand, we can see that Boo-hyun loves his glasses on a regular basis. He often wears clear horn-rimmed glasses with a sweatshirt, black horn-rimmed glasses with a baggy white tee, and despite his chic first impression, he transforms into a friendly handsome brother when he puts on his glasses. If you're a fan of nerdiness, check out Boo-hyun's casual look!\n4) Love the hoodie\nThere's nothing better than a hoodie when you're just heading out the door. You don't have to worry about matching the color of your outfit to your hat, you can just throw it over your head. With his bangs down and his innocent smile, Bo Bo Hyun is a man who can't help but pull off a hoodie.\n5) Watch collector\nIf you scroll through his Instagram feed, you'll notice a lot of wristwatches. From his favorite Bulgari aluminum pieces to his no-frills Apple Watch, it's easy to see why he's been photographed with watches so many times. They pair perfectly with his go-to outfits, like a simple jacket or denim."], images=[ArticleImage(url='https://newsimg.sedaily.com/2023/08/03/29T9HS4184_1.jpg', source='서울경제신문'), ArticleImage(url='https://www.allurekorea.com/wp_data/allure/2023/08/style_64cb5029288c0-700x500-1691046194.jpg', source='얼루어 코리아 (Allure Korea)')])]
step_3 = [TranslatedCrawledTrend(keywords=['안보현', '지수 안보현', '안보현 지수', '블랙핑크 지수'],
                        articles=["# Title: [Official] BLACKPINK's Jisoo - "
                                  'Actor Bo Bo Hyun admits to romance, "We\'re '
                                  'getting to know each other little by '
                                  'little"\n'
                                  '\n'
                                  '# Lead: Jisoo (28) of the group BLACKPINK '
                                  'and actor Bo Bo Hyun (35) are in a '
                                  "relationship. On the 3rd, Jisoo's agency, "
                                  'YG Entertainment, said, "They are getting '
                                  'to know each other with good feelings...\n'
                                  '\n'
                                  '# Body: viewer Actor Bo Bo Hyun and '
                                  "BLACKPINK's Jisoo / Photo by Seoul Economic "
                                  'Star DB\n'
                                  '< Copyright ⓒ The Seoul Economic Times, All '
                                  'rights reserved >.\n'
                                  'Jisoo (28) of the group Blackpink and actor '
                                  'Bo Bo Hyun (35) are in a relationship.On '
                                  "March 3, Jisoo's agency YG Entertainment "
                                  'said, "They are getting to know each other '
                                  'little by little with good feelings. We '
                                  'would appreciate it if you could watch them '
                                  'with a warm gaze."Anbo Hyun\'s agency, FN '
                                  'Entertainment, also said, "They are in the '
                                  'stage of getting to know each other '
                                  'carefully with good feelings. We would '
                                  'appreciate it if you could watch them with '
                                  'a warm gaze."Earlier in the day, media '
                                  'outlet Dispatch reported that Jisoo and '
                                  "Anbo Hyun were spotted dating at Jisoo's "
                                  'home in Seoul. "They have a lot of common '
                                  'denominators, from acting to singing to '
                                  'fashion," a source close to the pair told '
                                  'the dispatch.Jisoo debuted with the group '
                                  'BLACKPINK in 2016, releasing a slew of hits '
                                  'including "Whistle," "Boom Boom," "Like the '
                                  'Last Time," "Doo Doo Doo," and "Kill This '
                                  'Love," before becoming a global girl group. '
                                  'In 2021, she made her acting debut in the '
                                  'JTBC drama "Seolganghwa."Bo Bo Hyun made '
                                  'her acting debut in the 2014 drama "Golden '
                                  'Cross," and has since appeared in the drama '
                                  '"Descendants of the Sun" and the movie '
                                  '"Hija. Since 2020, he has gained popularity '
                                  'for his roles in the dramas "Itaewon '
                                  'Class," "Yumi\'s Cells," and the Netflix '
                                  'series "My Name. He recently appeared in '
                                  'the tvN drama "Please Take Care of Me This '
                                  'Time" as the lead character, Doc Ha.',
                                  '# Title: The Ultimate Boyfriend Look '
                                  '#Boonhyun #Allure Korea\n'
                                  '\n'
                                  '# Lead: Actor Bo Bo Hyun is the first actor '
                                  'to admit to a romantic relationship with '
                                  'Jisoo. The model-turned-actor is known for '
                                  'his impeccable height of 187 centimeters '
                                  'and his dedication to acting. What is it '
                                  'that makes him so attractive? We got a '
                                  'glimpse through five characteristics of his '
                                  'casual look.\n'
                                  '\n'
                                  '# Body: This browser does not support '
                                  'sharing.\n'
                                  'Address.\n'
                                  'Actor Bo Bo Hyun cautiously acknowledged '
                                  'his love affair with Jisoo. The '
                                  'model-turned-actor is known for his '
                                  'impeccable height of 187 centimeters and '
                                  'his dedication to acting. Is his warm and '
                                  'attentive personality reflected in his '
                                  "looks? We've picked out the top 5 "
                                  "characteristics of Bo Bo-hyun's off-duty "
                                  'look.\n'
                                  '1) A man who knows how to wear a shirt\n'
                                  'As a former boxer in his student days, '
                                  'Boo-hyun has maintained his superior '
                                  "physique. Perhaps that's why his muscular "
                                  'upper body really shines when he wears a '
                                  "shirt. He's definitely in our top 5 best "
                                  'shirt-fitting men.\n'
                                  '2) Utilize sunglasses\n'
                                  'INFJ Boo-hyun loves to travel, and when he '
                                  'does, he relies heavily on hats and masks '
                                  "to cover his face. If there's one thing he "
                                  "can't live without, it's sunglasses. He can "
                                  'wear them nonchalantly on top of a hat or '
                                  'with a beanie and never feel out of place.\n'
                                  '3) Nerdiness with glasses\n'
                                  'On the other hand, we can see that Boo-hyun '
                                  'loves his glasses on a regular basis. He '
                                  'often wears clear horn-rimmed glasses with '
                                  'a sweatshirt, black horn-rimmed glasses '
                                  'with a baggy white tee, and despite his '
                                  'chic first impression, he transforms into a '
                                  'friendly handsome brother when he puts on '
                                  "his glasses. If you're a fan of nerdiness, "
                                  "check out Boo-hyun's casual look!\n"
                                  '4) Love the hoodie\n'
                                  "There's nothing better than a hoodie when "
                                  "you're just heading out the door. You don't "
                                  'have to worry about matching the color of '
                                  'your outfit to your hat, you can just throw '
                                  'it over your head. With his bangs down and '
                                  'his innocent smile, Bo Bo Hyun is a man who '
                                  "can't help but pull off a hoodie.\n"
                                  '5) Watch collector\n'
                                  'If you scroll through his Instagram feed, '
                                  "you'll notice a lot of wristwatches. From "
                                  'his favorite Bulgari aluminum pieces to his '
                                  "no-frills Apple Watch, it's easy to see why "
                                  "he's been photographed with watches so many "
                                  'times. They pair perfectly with his go-to '
                                  'outfits, like a simple jacket or denim.'],
                        images=[ArticleImage(url='https://newsimg.sedaily.com/2023/08/03/29T9HS4184_1.jpg',
                                             source='서울경제신문'),
                                ArticleImage(url='https://www.allurekorea.com/wp_data/allure/2023/08/style_64cb5029288c0-700x500-1691046194.jpg',
                                             source='얼루어 코리아 (Allure Korea)')]),
 TranslatedCrawledTrend(keywords=['서현역', '서현역 칼부림'],
                        articles=["# Title: Suspect arrested in 'weapon "
                                  "rampage' near Seohyeon Station in "
                                  'Bundang...10 people injured\n'
                                  '\n'
                                  '# Lead: [Seongnam=newsfim] Reporter '
                                  'Seungbong Park = More than 10 people were '
                                  "reportedly injured in a 'don't ask, don't "
                                  "tell weapon rampage' near Seohyeon Station "
                                  'in Bundang-gu, Seongnam-si, Gyeonggi-do on '
                                  'the afternoon of the 3rd.Police '
                                  'logo[=newsfimDB]According to police and '
                                  'fire officials, there were multiple reports '
                                  'of people being injured by wielding a '
                                  'weapon at AK Plaza near Seohyeon Station on '
                                  'the 3rd.\n'
                                  '\n'
                                  '# Body: Choi Won-jin [=newsfimDB]Chinese '
                                  'secondary battery companies are stepping up '
                                  'investments in setting up new factories in '
                                  'the Saemangeum industrial complex in North '
                                  'Jeolla Province, which has been designated '
                                  'as a specialized zone for secondary '
                                  'batteries, Bloomberg reported on Sept. 30 '
                                  '(local time), citing officials from the '
                                  'Saemangeum Development and Investment '
                                  'Agency. Over the past four months, Chinese '
                                  'companies and their South Korean joint '
                                  'venture partners have announced investments '
                                  'worth about 5.1 trillion won in five new '
                                  'battery plants, according to the report. '
                                  "For example, China's Ningbo Longbai New and "
                                  'Renewable Energy Science and Technology Co. '
                                  'Ltd. said in a press release on Sept. 24 '
                                  'that the Saemangeum Development and '
                                  'Investment Agency has approved its '
                                  'application for the "6th Saemangeum '
                                  'National Industrial Complex Entry '
                                  'Examination in 2023. The company plans to '
                                  'establish a production base for secondary '
                                  'battery ternary precursors and sulfates '
                                  'with an annual output of 80,000 tons (t). '
                                  'Precursors are key raw materials for '
                                  'cathode materials, and cathode materials '
                                  'are key materials for electric vehicle (EV) '
                                  'batteries. Charging an EV [Photo: '
                                  'Bloomberg] At least one other province '
                                  'besides Saemangeum is also discussing '
                                  'investment in new battery plants like this, '
                                  'officials said. The sources did not specify '
                                  'which other provinces are being discussed, '
                                  'but they are believed to be Cheongju in '
                                  'North Chungcheong Province, Pohang in North '
                                  'Gyeongsang Province, and Ulsan Metropolitan '
                                  'City, which has been designated as a '
                                  'specialized secondary battery complex. '
                                  'Bloomberg analyzed that Chinese battery '
                                  'companies are investing in South Korea to '
                                  'take advantage of electric vehicle '
                                  'subsidies under the U.S. Inflation '
                                  'Reduction Act (IRA). The IRA requires that '
                                  "at least 40% of a battery's key minerals "
                                  'come from the U.S. or a country with a free '
                                  'trade agreement (FTA) with the U.S. to '
                                  'qualify for the EV tax credit. "South Korea '
                                  'is a country that has signed a free trade '
                                  'agreement with the United States and is a '
                                  'major supplier of power batteries and '
                                  'battery materials to the Western world," '
                                  'Ningbo Longbai said in a release, adding '
                                  'that the products produced at the South '
                                  'Korean production base meet the detailed '
                                  'guidelines of the U.S. IRA law. Joint '
                                  'ventures (JVs) between Chinese and South '
                                  'Korean companies have also been on the '
                                  'rise. In March, SK Innovation subsidiary SK '
                                  'On announced a joint venture with a Chinese '
                                  'company to build a precursor plant in South '
                                  'Korea, while Chinese secondary battery '
                                  'maker Zhejiang Yucobalt announced plans '
                                  'earlier this year to build a production '
                                  'base in collaboration with LG Chem and '
                                  'POSCO Futurem. In June, POSCO Holdings '
                                  'announced that it would build a plant to '
                                  'produce nickel and precursors for secondary '
                                  "batteries with China's Zhongwei New "
                                  'Materials (CNGR). While some worry that the '
                                  'U.S. could at any time exclude batteries '
                                  'made in joint ventures with China from EV '
                                  'subsidies under the IRA, South Korean '
                                  'experts are optimistic that domestic '
                                  'companies will be able to maintain their '
                                  'partnerships with Chinese firms, at least '
                                  'for now, Bloomberg reported. "The U.S. '
                                  "can't exclude Chinese companies from the EV "
                                  'supply chain," said James Oh, vice '
                                  'president of secondary battery market '
                                  'researcher SNE Research. "If the U.S. bans '
                                  'Sino-U.S. partnerships, the U.S. will never '
                                  'make EVs," he said. wonjc6@newspim.com',
                                  '# Title: "I hid in the fitting room" "I '
                                  'fell down holding my stomach" ... Seo '
                                  'Hyun-rok stabbing eyewitness account\n'
                                  '\n'
                                  '# Lead: "I hid in the fitting room" "I '
                                  'grabbed my stomach and fell down" Seohyeon '
                                  'Station stabbing eyewitness account On the '
                                  'afternoon of the 3rd, a stabbing incident '
                                  'occurred near Seohyeon Station on '
                                  'Suinbundang Line, Bundang-gu, Seongnam-si, '
                                  'Gyeonggi-do. According to the police, a '
                                  'report of a rampage with a weapon was '
                                  'received on 112 at around 5:59 p.m. that '
                                  'day. The suspect was arrested at around '
                                  '6:09 pm.\n'
                                  '\n'
                                  '# Body: None'],
                        images=[ArticleImage(url='http://img.newspim.com/news/2023/07/25/2307251622587430_w.jpg',
                                             source='뉴스핌'),
                                ArticleImage(url='https://images.chosun.com/resizer/Op8cfAPTfawTZaXimCfldgpmjtw=/572x300/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/SLPL4YX35BFWXKFX2I2JRBQU34.PNG',
                                             source='조선일보')]),
 TranslatedCrawledTrend(keywords=['중국'],
                        articles=["# Title: Shin Hee-sup's Politics - The "
                                  'Meaning of 279.7% and 46.5% in China\n'
                                  '\n'
                                  '# Lead: There is a lot of talk about '
                                  "China's economy being in crisis. There are "
                                  'grim predictions of deflation. Some are '
                                  'even predicting that the crisis will spread '
                                  'to the rest of the world. There are also '
                                  'realistic analyses that the Korean economy '
                                  'will be hit hard without going far. The '
                                  'Chinese economy is heading towards a crisis '
                                  'by several indicators. The most serious is '
                                  "the Chinese government's debt. Estimates "
                                  'from various organizations vary from 279% '
                                  'to 297% of the national debt, contrary to '
                                  'the hard-to-believe Chinese government '
                                  'data. Before the 2008 financial crisis, the '
                                  'Chinese government had a debt of around '
                                  '60%.\n'
                                  '\n'
                                  '# Body: HeeSup Shin, PhD in Political '
                                  'Science\n'
                                  'Professor at Veritas Law School / Author of '
                                  'Everyday Politics\n'
                                  "There is a lot of talk about China's "
                                  'economy being in crisis. There are also '
                                  'grim predictions of deflation. Some are '
                                  'even predicting that the Chinese economic '
                                  'crisis will hit the rest of the world. '
                                  'There are also realistic analyses that the '
                                  'Korean economy will be hit hard without '
                                  'going far. China has certainly become '
                                  'important.\n'
                                  'The Chinese economy is heading towards a '
                                  'crisis by several indicators. The most '
                                  "serious is the Chinese government's debt. "
                                  'Estimates from various organizations range '
                                  'from 279% to 297% of the national debt, '
                                  'contrary to the hard-to-believe Chinese '
                                  'government data. Before the financial '
                                  'crisis of 2008, the Chinese government was '
                                  'about 60% indebted. Since then, the '
                                  'desperation to grow the economy has pushed '
                                  'the government to nearly 300% debt.\n'
                                  "It is estimated that nearly 100% of China's "
                                  'government debt is held by local '
                                  'governments. Chinese local governments have '
                                  'been generating revenue through real estate '
                                  'development, but as the real estate market '
                                  'has recently gone into an ice age, local '
                                  'governments have been unable to service '
                                  'their debt. According to the Financial '
                                  'Times, real estate revenue accounted for '
                                  '21% of local government revenue in China in '
                                  '2022. Tianjin and Jilin provinces saw '
                                  'record declines of 62% and 61% '
                                  'respectively.\n'
                                  'The real estate market is so important that '
                                  "it accounts for a quarter of China's GDP. "
                                  "But the market has stalled. And there's no "
                                  'sign of any growth coming from the real '
                                  'estate sector.\n'
                                  'Real estate has dried up and consumption '
                                  'has dried up. While the rest of the world '
                                  'is suffering from inflation, China has a 0% '
                                  'inflation rate. Even as commodity prices '
                                  'soar, the Chinese are not spending enough '
                                  'to keep inflation at 0%.\n'
                                  "There's another number that starkly "
                                  "illustrates China's crisis. 46.5%. This is "
                                  'the youth unemployment rate in China, as '
                                  'analyzed by Professor Zhang Dandan of '
                                  "Peking University. The Chinese government's "
                                  'official urban youth unemployment rate is '
                                  "21.3%. That's pretty high. But that's where "
                                  'the 46.5% figure comes from. Worse yet, '
                                  'more than 10 million people graduate from '
                                  'college every year, but only about 50% of '
                                  'them find jobs.\n'
                                  'This situation in China can lead to a youth '
                                  'bulge. A youth bulge is when the number of '
                                  "young people grows, but there aren't enough "
                                  'jobs available for them, leading to '
                                  'protests and riots.\n'
                                  'However, it is not easy to predict that '
                                  'Chinese youth will create a second '
                                  'Tiananmen. Given the social conditions, '
                                  'youth discontent, and bleak prospects for '
                                  'the future, Chinese youth should strongly '
                                  'resist the Chinese government. However, '
                                  'there are many young people in China who '
                                  'are afraid of meeting people, which is '
                                  'called shi kung (社恐). They reject the '
                                  '"social animal proposition" of humans. They '
                                  'are in the Fosi (Buddhist system). They '
                                  "don't care about making money or advancing "
                                  'in life, they suppress their desires, and '
                                  'spend their time fiddling with their '
                                  "smartphones as if they've achieved Buddhist "
                                  'enlightenment. They are called con lao, '
                                  'which means "old man" because they eat '
                                  'their parents. They are also called '
                                  'tangping (dàngping: 躺平) for just lying '
                                  'around at home.\n'
                                  'The meaning of the recent neologisms '
                                  "referring to China's new generation is "
                                  "clear. It's that the young adults who were "
                                  'raised as petty emperors under the '
                                  'one-child policy see unemployment as a '
                                  'personal problem. Instead of fixing '
                                  "society, they're just sucking up to their "
                                  'parents, who are easier to deal with. Of '
                                  'course, there are some conscious, socially '
                                  'just people among the Chinese youth. But '
                                  "it's hard to organize a generation of young "
                                  "people who have been brainwashed by Xi's "
                                  'patriotic education to resist the '
                                  'government. Unless something extraordinary '
                                  'happens.\n'
                                  "It's also the external conditions that make "
                                  'it difficult for the Chinese economy. The '
                                  'exports that made China a world factory and '
                                  'got it to where it is today are declining. '
                                  'Foreign investment is being lost to '
                                  'countries like Vietnam. The semiconductors '
                                  'and advanced technologies needed to build '
                                  'the next wave of high-tech industries after '
                                  'manufacturing are already dominated by the '
                                  'United States.\n'
                                  'Nevertheless, China, with its 1.4 billion '
                                  'people, has potential. With a population of '
                                  '1.4 billion, it has the potential to '
                                  'develop through domestic demand if incomes '
                                  'rise a bit more and consumption is '
                                  'supported. It also has strong manufacturing '
                                  'capabilities. However, the political power '
                                  'that allows this potential to be realized '
                                  'is another factor that makes the Chinese '
                                  "economy difficult. In 2020, Xi Jinping's "
                                  'government promised to achieve distributive '
                                  'justice with its "common wealth" policy. It '
                                  'also promised to boost domestic consumption '
                                  'to drive economic development. With per '
                                  'capita income now above $10,000, China '
                                  'still needs to grow through exports.\n'
                                  'How the Chinese Communist Party, with '
                                  'nearly 100 million members, understands the '
                                  'current situation and how it will address '
                                  "it is crucial. That's where China needs "
                                  "leaders like Deng Xiaoping again. I'm not "
                                  "worried about China, I'm worried about "
                                  'South Korea, which could be hit by a '
                                  'Chinese economic downturn.\n'
                                  'CF. I created a Naver blog to make my past '
                                  'columns more accessible. The address is '
                                  'blog.naver.com/heesup1990. The name of the '
                                  'blog is "Everyday Politics."\n'
                                  'HeeSup Shin, PhD in Political Science\n'
                                  'Former Professor at Veritas Law School / '
                                  'Author of Everyday Politics\n'
                                  '<* Manuscripts written by external authors '
                                  'may not be consistent with the editorial '
                                  'direction of this journal.\n'
                                  'Copyright © Law Journal All Rights '
                                  'Reserved'],
                        images=[ArticleImage(url='http://www.lec.co.kr/news/thumbnail/202308/743858_78889_4346_v150.jpg',
                                             source='법률저널')]),
 TranslatedCrawledTrend(keywords=['미국 신용등급 강등'],
                        articles=["# Title: World stocks 'rocked' by U.S. "
                                  'credit rating downgrade\n'
                                  '\n'
                                  '# Lead: Global financial markets are '
                                  'reeling after Fitch downgraded the '
                                  'sovereign credit rating of the United '
                                  "States. Following the previous day's "
                                  'declines in European and Asian markets, the '
                                  'New York Stock Exchange today...\n'
                                  '\n'
                                  '# Body: Play Full\n'
                                  '◀ Anchor ▶World financial markets are in '
                                  'turmoil after Fitch Ratings downgraded the '
                                  'sovereign credit rating of the United '
                                  'States of America.Following a day of losses '
                                  'in Europe and Asia, stocks in New York are '
                                  'down today.Kang Na-rim is reporting from '
                                  'New York.◀ Report ▶Stocks in New York are '
                                  "down across the board.The Standard & Poor's "
                                  '500 Index was down 1.38%, the Dow Jones '
                                  'Industrial Average was down 0.98%, and the '
                                  'tech-heavy Nasdaq Composite Index was down '
                                  '2.17%.The impact of the US sovereign credit '
                                  'rating downgrade was felt by international '
                                  'rating agency Fitch, which downgraded the '
                                  'US sovereign credit rating by one notch to '
                                  'AA+ from the highest rating of AAA.3It was '
                                  'the first time in 12 years that a major '
                                  'international rating agency had downgraded '
                                  'the U.S. sovereign credit rating since '
                                  '2011.Fitch cited "the expected '
                                  'deterioration of the U.S. fiscal position '
                                  'over the next three years and the rising '
                                  'national debt burden."The White House and '
                                  'U.S. Treasury Secretary Janet Yellen '
                                  "reacted to Fitch's action, calling it "
                                  '"arbitrary and based on outdated metrics." '
                                  '[Janet Yellen/U.S. Treasury Secretary]"At a '
                                  "time when America's economic strength is so "
                                  "visible, Fitch's decision is disturbing. I "
                                  "strongly disagree with Fitch's "
                                  'decision."Financial markets around the '
                                  'world have been shaken by the downgrade, '
                                  'with Asian and European stocks, including '
                                  'the Kospi and Nikkei, falling in tandem on '
                                  'Tuesday.However, experts say that because '
                                  'this is not the first time the U.S. has '
                                  'been downgraded, and because U.S. economic '
                                  'growth has been robust, the impact on '
                                  'financial markets may not be as severe as '
                                  'it was in 2011.["While there may be some '
                                  "short-term disruption, we don't expect the "
                                  'long-term reaction to the change in '
                                  'sovereign credit rating to be '
                                  'significant."When Standard & Poor\'s first '
                                  'downgraded the U.S. credit rating in 2011, '
                                  'it sent financial markets reeling, with '
                                  'U.S. stocks plunging 15 percent within a '
                                  "week.I'm Kang Na-rim from New York.▷ Call "
                                  '02-784-4000▷ Email mbcjebo@mbc.co.kr▷ '
                                  'KakaoTalk @mbcnews',
                                  '# Title: U.S. sovereign credit rating '
                                  'downgraded for first time in 12 '
                                  'years...Asian stocks slammed\n'
                                  '\n'
                                  '# Lead: The US sovereign credit rating has '
                                  "been downgraded. It's been 12 years since "
                                  "2011, and the world's financial markets are "
                                  'nervous. As Korea cannot be safe if there '
                                  'is a turbulence in the U.S. financial '
                                  'market, the changes in the financial market '
                                  'caused by the U.S. sovereign credit rating '
                                  'downgrade will be closely watched.Fitch '
                                  'downgrades U.S. sovereign credit rating '
                                  'after 12 yearsFitch, an international '
                                  'credit rating agency, downgraded the '
                                  'sovereign credit rating of the United '
                                  "States from 'AAA' to 'AA+' on January 1 "
                                  '(local time). It is the first time in 12 '
                                  'years since 2011 that the three major '
                                  'international credit rating agencies have '
                                  'downgraded the sovereign credit rating of '
                                  'the United States, and the impact on '
                                  'financial markets and the real economy will '
                                  'be closely watched.Fitch\n'
                                  '\n'
                                  '# Body: Ratings agency Fitch headquarters '
                                  'in New York, U.S. [EPA Yonhap photo]\n'
                                  'The sovereign credit rating of the United '
                                  'States has been downgraded. It was the '
                                  'first time in 12 years since 2011, and the '
                                  "world's financial markets are nervous. As "
                                  'Korea cannot be safe from the turbulence in '
                                  'the U.S. financial market, it will be '
                                  'interesting to see how the U.S. sovereign '
                                  'credit rating downgrade will affect the '
                                  'financial market.\n'
                                  'Fitch downgrades US sovereign rating after '
                                  '12 years\n'
                                  'International credit rating agency Fitch '
                                  'downgraded the sovereign credit rating of '
                                  "the United States from 'AAA' to 'AA+' on "
                                  'January 1 (local time). This is the first '
                                  'time in 12 years since 2011 that the three '
                                  'major international credit rating agencies '
                                  'have downgraded the U.S. sovereign credit '
                                  'rating, and the implications for financial '
                                  'markets and the real economy will be '
                                  'closely watched.\n'
                                  'Fitch today downgraded the U.S. long-term '
                                  'issuer default ratings (IDRs) by one notch '
                                  'to AA+ from AAA and revised the rating '
                                  "outlook to 'stable' from 'negative watch'. "
                                  '"The downgrade reflects the expected fiscal '
                                  'deterioration in the United States over the '
                                  'next three years, as well as the rising '
                                  'sovereign debt burden and deteriorating '
                                  'governance," Fitch said in a report. In '
                                  'particular, Fitch noted that governance has '
                                  'deteriorated compared to other countries '
                                  'with AA or AAA ratings, as U.S. politicians '
                                  'have repeatedly stalled over raising the '
                                  'debt ceiling, only to resolve the issue at '
                                  'the last minute.\n'
                                  'Trends in U.S. sovereign credit ratings\n'
                                  '"Governance standards in the United States '
                                  'have been steadily deteriorating for more '
                                  'than two decades," Fitch said, noting that '
                                  '"fiscal and debt problems remain despite a '
                                  'bipartisan agreement in June to suspend the '
                                  'debt limit until January 2025." Meanwhile, '
                                  'Fitch expects the U.S. deficit as a '
                                  'percentage of gross domestic product (GDP) '
                                  'to surge from 3.7% in 2022 to 6.3% in 2023, '
                                  'followed by 6.6% in 2024 and 6.9% in 2025, '
                                  'as a result of lower tax revenues, higher '
                                  'deficit spending, and higher interest '
                                  'burdens.\n'
                                  'Fitch also warned about the economic future '
                                  'of the U.S., stating that "over the next '
                                  'decade, rising interest rates and rising '
                                  'debt will increase interest payments, while '
                                  'an aging population and rising healthcare '
                                  'costs will increase spending on seniors in '
                                  'the absence of fiscal reform," and even '
                                  'predicted that a recession could be coming '
                                  'to the U.S. sooner rather than later, '
                                  'stating that "deteriorating credit '
                                  'conditions, lower investment, and falling '
                                  'consumption will push the U.S. economy into '
                                  'a mild recession in the fourth quarter of '
                                  'this year and the first quarter of next '
                                  'year".\n'
                                  'Fitch downgraded the U.S. sovereign rating '
                                  "by one notch to AA+ from AAA, while Moody's "
                                  'maintained its Aaa rating and Standard & '
                                  "Poor's affirmed its AA+ rating.\n"
                                  'Will there be a repeat of the 2011 '
                                  'sovereign downgrade shock?\n'
                                  "It's been 12 years since the last time a "
                                  'major international credit rating agency '
                                  'downgraded the U.S. sovereign rating, when '
                                  "Standard & Poor's (S&P) lowered it from AAA "
                                  'to AA+ in 2011. At the time, S&P cited '
                                  'political impasse over raising the U.S. '
                                  'debt ceiling as the reason for the '
                                  'downgrade. The move sent shockwaves through '
                                  'international financial markets, with the '
                                  'dollar depreciating and stock prices '
                                  'plummeting. The large-cap S&P500 index '
                                  'dropped 15% in just a few days, and panic '
                                  'spread across European and Asian stock '
                                  'markets. However, the price of US Treasury '
                                  'bonds, which are considered a safe haven '
                                  'asset, rose due to the combination of risk '
                                  'aversion and safe-haven sentiment.\n'
                                  "The question is whether Fitch's downgrade "
                                  'of the U.S. will follow in the footsteps of '
                                  "Standard & Poor's downgrade of the U.S. in "
                                  '2011. There is a strong case to be made '
                                  "that the impact of Fitch's downgrade of the "
                                  'U.S. will be limited, given the proximity '
                                  'of the 2011 default to the federal debt '
                                  'limit, the proximity of the 2008 global '
                                  'financial crisis, the fact that Fitch had '
                                  'already warned of a downgrade in May when '
                                  'it placed the U.S. sovereign rating outlook '
                                  'on "negative watch," and the fact that, '
                                  'unlike in 2011, the U.S. economy is on a '
                                  'soft landing.\n'
                                  'On the other hand, with U.S. equity markets '
                                  "near historic highs, Fitch's downgrade "
                                  'could trigger a correction, and any further '
                                  'downgrades could be devastating to the '
                                  "federal government's fiscal health.\n"
                                  'Is a Stronger Dollar and Lower Treasury '
                                  'Yields Best for the U.S.?\n'
                                  'According to Bloomberg, the market reaction '
                                  'to the downgrade was relatively subdued. '
                                  'Futures for the S&P 500 and Nasdaq '
                                  'Composite were each down less than 0.5%, '
                                  'while the yield on the 10-year U.S. '
                                  'Treasury note was at 4.03% as of 4:40 p.m. '
                                  'ET, down one basis point (bp=0.01 '
                                  'percentage point) from the previous day. A '
                                  'decline in bond yields implies a rise in '
                                  'bond prices. Meanwhile, U.S. equity futures '
                                  'showed a sharp correction as the market '
                                  'opened.\n'
                                  'The U.S. sovereign credit rating downgrade '
                                  'continues to strengthen the dollar. In this '
                                  'photo, employees organize dollar bills at '
                                  'the head office of Hana Bank in Euljiro, '
                                  'Jung-gu, Seoul. Oct. 6, 2022\n'
                                  "Fitch's downgrade of the U.S. sovereign "
                                  'credit rating is hitting Asian stocks and '
                                  'currencies hard. Asian stocks and '
                                  'currencies weakened in unison on Oct. 2. '
                                  'This is because the growing preference for '
                                  'safe assets such as the U.S. dollar and '
                                  'government bonds is causing investors to '
                                  'pull out of Asian markets categorized as '
                                  'risky. According to the Korea Exchange, the '
                                  'Kospi fell 50.60 points, or 1.9%, to close '
                                  'at 2616.47, a day after hitting a yearly '
                                  'high of 2667.07 the day before, while the '
                                  'KOSPI fell 29.91 points, or 3.18%, to '
                                  "909.76. Japan's Nikkei 225 ended the day "
                                  "down 2.30% at 32,707.69, while Hong Kong's "
                                  "Hang Seng (-2.47%), China's Shanghai "
                                  "Composite (-0.89%) and Taiwan's KMT "
                                  '(-1.85%) were also down. European markets, '
                                  'which open after the Asian close, are also '
                                  'in the red, with the pan-European index, '
                                  'the Euro Stoxx 50, down more than 1%.\n'
                                  'The main focus is on the exchange rate. '
                                  'This is because the stronger dollar is '
                                  'making a comeback after a recent lull. At '
                                  'the Seoul foreign exchange market, the '
                                  'won/dollar exchange rate soared to 1,298.5 '
                                  'won, up 14.7 won from the previous trading '
                                  'day. It was the biggest one-day surge since '
                                  'March 24, when it rose 16.0 won amid '
                                  'financial turmoil in the U.S. banking '
                                  'sector, and the first time in about three '
                                  'weeks that it has touched the 1,300-won '
                                  'level since March 10 (1306.5 won). The '
                                  'dollar index, which measures the '
                                  "greenback's value against a basket of six "
                                  'major currencies, stood at 102.21 as of '
                                  '3:30 p.m. KST. A dollar index above the 100 '
                                  'mark indicates that the greenback is '
                                  'stronger against a basket of major '
                                  'currencies.\n'
                                  "It's unclear how much of a ripple Fitch's "
                                  'downgrade of the U.S. will cause or where '
                                  'it will go. What is clear is that global '
                                  "money's preference for the dollar and U.S. "
                                  'Treasuries is a blessing in disguise for '
                                  'the United States. A strong dollar is a way '
                                  'to export domestic inflation abroad, and '
                                  'greater demand for Treasuries will lead to '
                                  'lower Treasury yields, reducing the '
                                  "government's interest burden."],
                        images=[ArticleImage(url='https://image.imnews.imbc.com/replay/2023/nw930/article/__icsFiles/afieldfile/2023/08/03/0930_20230803_093536_1_4_Large.jpg',
                                             source='MBC뉴스'),
                                ArticleImage(url='https://cdn.mindlenews.com/news/thumbnail/202308/4446_11292_2019_v150.jpg',
                                             source='시민언론 민들레')]),
 TranslatedCrawledTrend(keywords=['고딩엄빠 인플루언서'],
                        articles=["# Title: 'High School Dad 4' influencer's "
                                  "ex-husband accused of 'assaulting his "
                                  'full-term wife\' says "I got hit too" [full '
                                  'text]\n'
                                  '\n'
                                  '# Lead: Suspected full-term wife assault '
                                  '\'Going Dad 4\' influencer ex-husband "I '
                                  'was also hit" [Full text] While the story '
                                  'of a cast member who was assaulted by an '
                                  "influencer's ex-husband on Going Dad 4 was "
                                  'revealed, the ex-husband, Mr. A, came '
                                  'forward and revealed his position. Mr. A '
                                  'uploaded a video to his YouTube channel on '
                                  'the 3rd. The day before, MB\n'
                                  '\n'
                                  '# Body: None',
                                  '# Title: High school dad 1.6 million '
                                  'influencer ex-husband identity chunghni?\n'
                                  '\n'
                                  "# Lead: Ryu Hye-lin, a cast member of MBN's "
                                  '"Going to School Dad 4" (hereinafter "Going '
                                  'to School Dad 4"), revealed on air that the '
                                  'ex-husband of a 1.6 million influencer '
                                  'assaulted her and forced her to sleep with '
                                  'him while she was pregnant, attracting '
                                  'attention as the influencer revealed his '
                                  'identity.Ryu Hye-lin, who gave birth to a '
                                  'child at the age of 23 and is raising a '
                                  "two-year-old daughter, appeared on MBN's "
                                  '"Going Dad 4," which aired on the 2nd of '
                                  'this month. Ryu Hye-lin, who started living '
                                  'together as soon as they started dating, '
                                  'found out that she was pregnant and '
                                  'registered her marriage with her '
                                  'boyfriend.\n'
                                  '\n'
                                  "# Body: Ryu Hye-lin, a cast member of MBN's "
                                  '"High School Dad 4" (hereinafter referred '
                                  'to as "High School Dad 4"), revealed on air '
                                  'that the ex-husband of a 1.6 million '
                                  'influencer assaulted her and forced her to '
                                  'sleep with him while she was pregnant, '
                                  'attracting attention as the influencer '
                                  'revealed her identity.\n'
                                  'Ryu Hye-lin, who gave birth to a child at '
                                  'the age of 23 and is raising a two-year-old '
                                  'daughter, appeared on MBN\'s "Going Dad 4," '
                                  'which aired on March 2.\n'
                                  'Ryu Hye-lin, who started living together as '
                                  'soon as they started dating, found out she '
                                  'was pregnant and registered her marriage '
                                  'with her boyfriend.\n'
                                  '"His injections became more and more '
                                  'severe, and he even became abusive while I '
                                  'was pregnant," she said. "After a while, he '
                                  'became an influencer who made videos, and '
                                  'he made unreasonable demands, such as '
                                  'asking me to slap my cheeks to get more '
                                  "views. He also insulted me, saying, 'Will "
                                  "you sleep with me,' 'Will you do me a "
                                  "favor,' and 'I really have no use for "
                                  'you,\'" she revealed.\n'
                                  '"My ex-husband was an influencer and had '
                                  'about 1.6 million fans," she said, '
                                  'explaining that the abusers were his fans.\n'
                                  '"There are usually 30 to 40 malicious '
                                  'comments every day," she said, adding, "I '
                                  'get so many alarms that my watch is dead in '
                                  "an hour or two. I'm afraid that they know "
                                  'where I live and will come to visit me, and '
                                  'that\'s my biggest fear."\n'
                                  '"It was also hard when I received malicious '
                                  'comments about me, but it was crazy because '
                                  'they were directed at my child," she said, '
                                  'adding, "There were comments like, \'I\'m '
                                  "pregnant with another man's child,' and 'I "
                                  'want to kill the baby,\'" she said.\n'
                                  "Photo via Chungni's Instagram\n"
                                  'After the broadcast, the husband of the 1.6 '
                                  'million influencer revealed his identity.\n'
                                  'On March 3, YouTuber Chungni posted several '
                                  'videos on his YouTube channel with the '
                                  'title, "I\'m the YouTuber who assaulted my '
                                  'full-term wife...?\n'
                                  'He said, "That\'s right. I am a divorced '
                                  "man. But on the show, I'm being introduced "
                                  'as a man who assaulted his full-term wife," '
                                  'he said, breaking down in tears.\n'
                                  'Referring to the assault episode mentioned '
                                  'on the show, he said, "I\'ve been beaten. '
                                  'He had bad hands. I was also beaten in bed '
                                  'that day. I threw a pillow at him because '
                                  'it hurt and I was frustrated, and I said, '
                                  "'You should get hit too, see how much it "
                                  "hurts,' and I hit him hard in the knee. The "
                                  'next day, I checked his knee and there was '
                                  'a bruise on it," he explains.\n'
                                  'Chungni added that the next day he went to '
                                  'work and was informed of the divorce, which '
                                  'he begged for forgiveness and ended '
                                  'quietly. "I punched her in the stomach? I '
                                  "hit my pregnant wife's stomach? I hit OO "
                                  "(child's name)? Why are you making me do "
                                  'that...?" he said.\n'
                                  'He refuted the allegations of binge '
                                  'drinking, assault, verbal abuse, and '
                                  'coercion for sex, describing the situation '
                                  'as it happened. He also released additional '
                                  'videos of his KakaoTalk conversations with '
                                  'Ryu Hye-lin, explaining about child support '
                                  'and the lawsuit.\n'
                                  'YouTuber Chunghni (Oh Chun-geun) started as '
                                  'a YouTuber in 2020. He became popular for '
                                  'posting videos of his daily life with his '
                                  'girlfriend. As of three days ago, he had '
                                  'more than 100 million YouTube views and 22 '
                                  'million TikTok likes.'],
                        images=[ArticleImage(url='https://biz.chosun.com/resizer/OzWm5zbHZgPosTTDyJbsKxtO7Vk=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/3DGCCITC2SDZVH2H2HEZUAHUWI.jpg',
                                             source='조선비즈'),
                                ArticleImage(url='http://cdn.ggilbo.com/news/photo/202308/986830_822137_722.jpg',
                                             source='금강일보')])
]
########################## STEP 4 ##########################
step4 = [Article(category='Crime',
         keywords='대전 칼부림,대전 고등학교 칼부림,대전,대전 대덕구 칼부림',
         contents=[ArticleContent(title='Knife Attack at Daejeon High School: '
                                        'Suspect Arrested',
                                  lead='A man in his 20s brandished a knife at '
                                       'a teacher in his 40s at a high school '
                                       'in Daejeon. The suspect was caught '
                                       'within two hours, and police '
                                       'investigations revealed intriguing '
                                       "details about the suspect's past.",
                                  body1='At a high school in Daejeon, a man in '
                                        'his 20s brandished a weapon at a '
                                        'teacher in his 40s. The suspect was '
                                        'caught within two hours and told '
                                        'police he had been a priest in the '
                                        'past. According to the police, the '
                                        'suspect entered the school without '
                                        'being stopped by the learning guard '
                                        'at the main gate. He then sought out '
                                        'a teacher in the staff room and '
                                        'attacked the teacher with the weapon.',
                                  body2='The victim teacher was taken to a '
                                        'hospital and underwent emergency '
                                        'surgery. Police caught the suspect on '
                                        'a nearby road two hours after the '
                                        'crime. When questioned about the '
                                        'motive for the crime, the suspect '
                                        'remained silent. Police plan to '
                                        'further investigate the motive and '
                                        'circumstances of the crime.',
                                  qna_list=[QnA(question='What happened at the '
                                                         'high school in '
                                                         'Daejeon?',
                                                answer='A man in his 20s '
                                                       'brandished a knife at '
                                                       'a teacher in his 40s.'),
                                            QnA(question='Was the suspect '
                                                         'caught?',
                                                answer='Yes, the police caught '
                                                       'the suspect within two '
                                                       'hours.'),
                                            QnA(question='What did the suspect '
                                                         'reveal about his '
                                                         'past?',
                                                answer='The suspect told '
                                                       'police that he had '
                                                       'been a priest.'),
                                            QnA(question='How did the suspect '
                                                         'enter the school '
                                                         'without being '
                                                         'stopped?',
                                                answer='The suspect entered '
                                                       'the school without '
                                                       'being stopped by the '
                                                       'learning guard at the '
                                                       'main gate.'),
                                            QnA(question='What happened to the '
                                                         'victim teacher?',
                                                answer='The victim teacher was '
                                                       'taken to a hospital '
                                                       'and underwent '
                                                       'emergency surgery.'),
                                            QnA(question='Where was the '
                                                         'suspect caught?',
                                                answer='The suspect was caught '
                                                       'on a nearby road two '
                                                       'hours after the crime.'),
                                            QnA(question='What is the next '
                                                         'step in the '
                                                         'investigation?',
                                                answer='Police plan to further '
                                                       'investigate the motive '
                                                       'and circumstances of '
                                                       'the crime.')],
                                  language='EN-US')],
         images=[ArticleImage(url='https://image.imnews.imbc.com/replay/2023/nwtoday/article/__icsFiles/afieldfile/2023/08/05/today_20230805_071028_1_6_Large.jpg',
                              source='MBC뉴스'),
                 ArticleImage(url='http://www.goodmorningcc.com/news/thumbnail/202308/293936_325538_1955_v150.jpg',
                              source='굿모닝충청')]),
 Article(category='Crime',
         keywords='고속터미널,고속터미널 흉기',
         contents=[ArticleContent(title='Arrests Made at Gangnam High-Speed '
                                        'Terminal with Weapons',
                                  lead='A man in his 20s was apprehended at '
                                       'Gangnam Express Bus Terminal in Seoul '
                                       'for carrying weapons, raising concerns '
                                       'about a potential crime spree.',
                                  body1='The Seocho Police Station in Seoul '
                                        'reported that they arrested a man, '
                                        'identified as Mr. A, in his 20s at '
                                        'the Gangnam Express Bus Terminal. The '
                                        'arrest was made after a security '
                                        'guard alerted the police about a man '
                                        'carrying a weapon near the terminal. '
                                        'Within six minutes of receiving the '
                                        'report, the police were able to '
                                        'apprehend the suspect.',
                                  body2='It was discovered that the man had a '
                                        'knife and a toy gun in his bag. '
                                        'Fortunately, he did not use the '
                                        'weapons to harm anyone. The police '
                                        'are currently investigating the '
                                        'incident and the motive behind it.',
                                  qna_list=[QnA(question='Who was arrested at '
                                                         'Gangnam Express Bus '
                                                         'Terminal?',
                                                answer='A man in his 20s, '
                                                       'known as Mr. A, was '
                                                       'apprehended at the '
                                                       'terminal.'),
                                            QnA(question='What weapons did the '
                                                         'arrested man have?',
                                                answer='The man was found in '
                                                       'possession of a knife '
                                                       'and a toy gun.'),
                                            QnA(question='Were there any '
                                                         'casualties or '
                                                         'injuries?',
                                                answer='Fortunately, there '
                                                       'were no casualties or '
                                                       'injuries reported in '
                                                       'this incident.'),
                                            QnA(question='What is the current '
                                                         'status of the '
                                                         'investigation?',
                                                answer='The police are '
                                                       'currently '
                                                       'investigating the '
                                                       'incident and the '
                                                       'motive behind it.')],
                                  language='EN-US')],
         images=[ArticleImage(url='http://news.kbs.co.kr/data/news/2023/08/04/20230804_vxxJFM.jpg',
                              source='KBS뉴스'),
                 ArticleImage(url='https://image.imnews.imbc.com/news/2023/society/article/__icsFiles/afieldfile/2023/08/04/R230804-24.jpg',
                              source='MBC뉴스')]),
 Article(category='Accidents',
         keywords='롤스로이스 사고',
         contents=[ArticleContent(title="'A Hair on the Wheel' - Rolls-Royce "
                                        'Accident at Apgujeong Station',
                                  lead='A Rolls-Royce SUV worth 600 million '
                                       'won crashed into a sidewalk near '
                                       'Apgujeong Station in Seoul, severely '
                                       'injuring a woman in her 20s. The '
                                       'incident was covered by the YouTube '
                                       "channel 'Caracula Detective Agency' "
                                       'which released photos of the scene and '
                                       'the driver involved. The victim '
                                       'suffered a broken leg in the accident.',
                                  body1='A Rolls-Royce SUV collided with a '
                                        'sidewalk near Apgujeong Station in '
                                        'Gangnam-gu, Seoul, causing serious '
                                        'injuries to a woman in her 20s. The '
                                        'incident took place at around 8:10 '
                                        'p.m. on April 2. The YouTube channel '
                                        "'Caracula Detective Agency' provided "
                                        'coverage of the accident and shared '
                                        'photos showing the driver, a '
                                        '28-year-old individual named A, '
                                        'exiting the vehicle and the woman '
                                        'trapped beneath the car. The debris '
                                        'from the crash displayed a few '
                                        'strands of hair believed to belong to '
                                        'the victim.',
                                  body2='The driver, who had full-body '
                                        'tattoos, reportedly acted '
                                        'threateningly towards the police '
                                        'officers at the scene. Despite '
                                        "bystanders' warnings, the driver "
                                        'accelerated, leaving the victim in a '
                                        'critical condition. The victim '
                                        'underwent surgery for a broken leg '
                                        'and head and stomach injuries. The '
                                        'driver tested positive for ketamine '
                                        'in a drug test and is currently under '
                                        'investigation.',
                                  qna_list=[QnA(question='What happened at '
                                                         'Apgujeong Station?',
                                                answer='A Rolls-Royce SUV '
                                                       'crashed into a '
                                                       'sidewalk near '
                                                       'Apgujeong Station, '
                                                       'severely injuring a '
                                                       'woman in her 20s.'),
                                            QnA(question='Who covered the '
                                                         'accident?',
                                                answer='The YouTube channel '
                                                       "'Caracula Detective "
                                                       "Agency' provided "
                                                       'coverage of the '
                                                       'accident.'),
                                            QnA(question='What evidence was '
                                                         'found at the scene?',
                                                answer='Debris from the crash '
                                                       'included strands of '
                                                       'hair believed to '
                                                       'belong to the victim.'),
                                            QnA(question='What was the '
                                                         "driver's behavior "
                                                         'after the accident?',
                                                answer='The driver, who had '
                                                       'full-body tattoos, '
                                                       'acted threateningly '
                                                       'towards the police '
                                                       'officers and seemed '
                                                       'unconcerned about the '
                                                       'injured victim.'),
                                            QnA(question='What were the '
                                                         'injuries sustained '
                                                         'by the victim?',
                                                answer='The victim suffered a '
                                                       'broken leg and head '
                                                       'and stomach injuries.')],
                                  language='EN-US')],
         images=[ArticleImage(url='http://res.heraldm.com/content/image/2023/08/03/20230803000139_p.jpg',
                              source='헤럴드경제'),
                 ArticleImage(url='https://news.imaeil.com/photos/2023/08/05/2023080507281692897_l.jpg',
                              source='매일신문')]),
 Article(category='Entertainment',
         keywords='소방서 옆 경찰서 그리고 국과수',
         contents=[ArticleContent(title="'Police Station and Bureau of "
                                        "Investigation Next to Fire Station' "
                                        'Returns for Season 2',
                                  lead="SBS's 'The Police Station Next to the "
                                       "Fire Station and Guk Gua Soo' will "
                                       'premiere on April 4 at 10 p.m. as a '
                                       "follow-up to 'Demon'.",
                                  body1="Season 2 of 'The Police Station Next "
                                        "to the Fire Station and Guk Gua Soo' "
                                        'is a drama that depicts the upgraded '
                                        'cooperation of firefighting, '
                                        'crime-fighting, and '
                                        'evidence-gathering police officers '
                                        'who face unprecedented and '
                                        'unprecedented cases, and will be '
                                        'broadcast in 12 episodes.',
                                  body2='Season 2 picks up where Season 1 left '
                                        "off with the 'parking tower burial' "
                                        "ending and the subsequent 'fight "
                                        "against a serial arsonist,' with a "
                                        'series of near-disastrous events and '
                                        'accidents.',
                                  qna_list=[QnA(question="When will 'The "
                                                         'Police Station Next '
                                                         'to the Fire Station '
                                                         "and Guk Gua Soo' "
                                                         'premiere?',
                                                answer="'The Police Station "
                                                       'Next to the Fire '
                                                       'Station and Guk Gua '
                                                       "Soo' will premiere on "
                                                       'April 4 at 10 p.m.'),
                                            QnA(question='How many episodes '
                                                         'will Season 2 have?',
                                                answer='Season 2 will be '
                                                       'broadcast in 12 '
                                                       'episodes.'),
                                            QnA(question='What will be the '
                                                         'main focus of Season '
                                                         '2?',
                                                answer='Season 2 will depict '
                                                       'the upgraded '
                                                       'cooperation of '
                                                       'firefighting, '
                                                       'crime-fighting, and '
                                                       'evidence-gathering '
                                                       'police officers.'),
                                            QnA(question='What happened at the '
                                                         'end of Season 1?',
                                                answer='Season 1 ended with a '
                                                       "'parking tower burial' "
                                                       'and the subsequent '
                                                       "'fight against a "
                                                       "serial arsonist.'"),
                                            QnA(question='What can viewers '
                                                         'expect from Season '
                                                         '2?',
                                                answer='Viewers can expect a '
                                                       'series of '
                                                       'near-disastrous events '
                                                       'and accidents in '
                                                       'Season 2.')],
                                  language='EN-US')],
         images=[ArticleImage(url='https://biz.chosun.com/resizer/T7PaBYXeO7JRRekZISLb1oOCsSE=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/2THYHQXKAZ4LLS2VCZLTKF47UA.jpg',
                              source='조선비즈'),
                 ArticleImage(url='https://cdn.mhns.co.kr/news/thumbnail/202308/558910_683707_2921_v150.jpg',
                              source='문화뉴스')]),
 Article(category='World/International',
         keywords='뉴스',
         contents=[ArticleContent(title='Intensive Rainfall Leaves '
                                        'Gyeongsangbuk-do Region in Urgent '
                                        'Need of Precautions and Port '
                                        'Restoration',
                                  lead='Almost three weeks after heavy rains '
                                       'caused significant damage to the '
                                       'northern Gyeongsangbuk-do region, '
                                       'authorities are emphasizing the '
                                       'importance of taking preventive '
                                       'measures and restoring ports to '
                                       'address the increasing frequency of '
                                       'such disasters.',
                                  body1="It's been almost three weeks since "
                                        'torrential rains caused major damage '
                                        'in northern Gyeongsangbuk-do. '
                                        'Gyeongsangbuk-do believes that '
                                        'disasters that may or may not come '
                                        'once in 50 or 100 years will become '
                                        'more frequent in the future, and is '
                                        'taking this opportunity to prepare a '
                                        'solid alternative. The emergency '
                                        'restoration rate for this intensive '
                                        'rainfall is 89.8% overall, including '
                                        '98.2% for roads and bridges. Now that '
                                        'emergency restoration is in its final '
                                        'stages, attention is shifting to port '
                                        'restoration and preventive measures.',
                                  body2='Gyeongsangbuk-do is taking action '
                                        'through the Landslide Response System '
                                        'Innovation Task Force, saying the '
                                        'heavy rains have shown that there are '
                                        'no safe zones. It plans to build '
                                        'disaster prevention villages that can '
                                        'prevent landslides, and will begin a '
                                        'large-scale safety diagnosis of risk '
                                        'factors such as artificial objects in '
                                        'the mountains. In addition, we will '
                                        'improve the warning, evacuation, and '
                                        'rescue and relief systems so that '
                                        'rapid dissemination and evacuation '
                                        'can be carried out in actual '
                                        'situations. With extreme weather '
                                        'events such as extreme downpours '
                                        'becoming an everyday occurrence, the '
                                        'extent of the damage will depend on '
                                        'how well we establish permanent '
                                        'recovery plans and disaster '
                                        'preparedness.',
                                  qna_list=[QnA(question='What caused the '
                                                         'major damage in the '
                                                         'northern '
                                                         'Gyeongsangbuk-do '
                                                         'region?',
                                                answer='The major damage in '
                                                       'the northern '
                                                       'Gyeongsangbuk-do '
                                                       'region was caused by '
                                                       'torrential rains.'),
                                            QnA(question='What is '
                                                         'Gyeongsangbuk-do '
                                                         'doing to address the '
                                                         'increasing frequency '
                                                         'of disasters?',
                                                answer='Gyeongsangbuk-do is '
                                                       'taking preventive '
                                                       'measures and restoring '
                                                       'ports to address the '
                                                       'increasing frequency '
                                                       'of disasters.'),
                                            QnA(question='What is the '
                                                         'emergency '
                                                         'restoration rate for '
                                                         'the intensive '
                                                         'rainfall?',
                                                answer='The emergency '
                                                       'restoration rate for '
                                                       'the intensive rainfall '
                                                       'is 89.8% overall, '
                                                       'including 98.2% for '
                                                       'roads and bridges.'),
                                            QnA(question='What action is '
                                                         'Gyeongsangbuk-do '
                                                         'taking through the '
                                                         'Landslide Response '
                                                         'System Innovation '
                                                         'Task Force?',
                                                answer='Gyeongsangbuk-do is '
                                                       'planning to build '
                                                       'disaster prevention '
                                                       'villages, conduct a '
                                                       'large-scale safety '
                                                       'diagnosis, and improve '
                                                       'warning, evacuation, '
                                                       'and rescue systems '
                                                       'through the Landslide '
                                                       'Response System '
                                                       'Innovation Task Force.'),
                                            QnA(question='What is the '
                                                         'importance of '
                                                         'permanent recovery '
                                                         'plans and disaster '
                                                         'preparedness?',
                                                answer='The extent of the '
                                                       'damage caused by '
                                                       'extreme weather events '
                                                       'depends on how well '
                                                       'permanent recovery '
                                                       'plans and disaster '
                                                       'preparedness are '
                                                       'established.')],
                                  language='EN-US')],
         images=[ArticleImage(url='http://news.kbs.co.kr/data/news/title_image/newsmp4/daegu/news9/2023/08/04/50_7741234.jpg',
                              source='KBS뉴스'),
                 ArticleImage(url='https://yonhapnewstv-prod.s3.ap-northeast-2.amazonaws.com/article/MYH/20230804/MYH20230804026100641_P1.jpg',
                              source='연합뉴스TV')]),
 Article(category='Technology',
         keywords='호신용품',
         contents=[ArticleContent(title="'I hope I never have to use "
                                        "it'...self-defense firearms in spate "
                                        'of violent crimes',
                                  lead='Delays and out-of-stock notices amid '
                                       "surge in sales 'I must protect my "
                                       "body' anxiety spreads",
                                  body1='Delayed deliveries and out-of-stock '
                                        "notices amid a sales surge 'Protect "
                                        "your body' anxiety spreads An online "
                                        'store is out of tridents. Shopping '
                                        "Mall Nurijip Galmuri 'Sales of "
                                        'self-defense products have been '
                                        'surging recently due to the ongoing '
                                        'serious incidents...We will do our '
                                        'best to deliver them as quickly as '
                                        'possible and hope that you will never '
                                        'have to use them, as our company '
                                        "motto says.' On the 4th, NAVER Smart "
                                        'Store, which sells self-defense '
                                        'products, posted a message about the '
                                        'delay in delivery. The three-piece '
                                        'baton, which costs 15,900 won, has '
                                        "over 8,100 reviews. 'I bought it for "
                                        'self-defense after seeing a vicious '
                                        'post about a murder in broad '
                                        "daylight,' most of them said. On "
                                        'March 3, 13 days after the stabbing '
                                        'in Shinlim-dong, Gwanak-gu, Seoul, '
                                        'another indiscriminate crime occurred '
                                        'at a department store near Seohyeon '
                                        'Station in Bundang-gu, Seongnam-si, '
                                        'Gyeonggi-do, and the number of '
                                        'consumers seeking self-defense '
                                        'products has surged. The news that '
                                        'the police have launched an '
                                        'investigation into the crime, with a '
                                        'series of warning posts on large '
                                        'communities, is also amplifying '
                                        "consumers' anxiety. Some products are "
                                        'even selling out. A sign for a '
                                        'company selling self-defense '
                                        'products.',
                                  body2='Nurijip Galmuri According to '
                                        'G-market, sales of self-defense '
                                        'products increased by 243 percent '
                                        'from March 22 to March 3 compared to '
                                        'the same period last year. Sales of '
                                        'truncheons for self-defense increased '
                                        'by 303%. On 11th Avenue, sales of '
                                        'self-defense products and '
                                        'self-defense sprays increased by 109% '
                                        'and 171%, respectively, compared to '
                                        "the same period last year. 'After the "
                                        'stabbing in Shinlim-dong on the 21st '
                                        'of last month, people who were '
                                        "overwhelmed by the anxiety of 'what "
                                        "could happen to me' were buying a lot "
                                        'of related products to protect '
                                        "themselves,' said an industry "
                                        "insider. 'In addition, the Seohyun "
                                        'Station incident every three days is '
                                        'expected to cause a further surge in '
                                        "self-defense product sales.' In fact, "
                                        'on the fourth day after the Seohyun '
                                        "Station incident, 'self-defense "
                                        "products' ranked at the top of the "
                                        'Naver Shopping search chart. Kubotan '
                                        'is popular among women. There were '
                                        'over 1,300 reviews. Nurijip Galmuri '
                                        "'When I go to the bathroom, take the "
                                        'train, or walk down the street, I '
                                        'find myself constantly looking '
                                        "around, and I'm sensitive to the "
                                        "slightest sound,' said Yoo "
                                        'Ah-moo-gae, a woman in her 40s who '
                                        "lives in Seongbuk-gu, Seoul. 'In a "
                                        'chat room with my family, we '
                                        'discussed whether we should all buy '
                                        "self-defense products.' Another man "
                                        'in his 30s, Yoon Ah-moo-gae, said, '
                                        "'The stabbing incident made me "
                                        'realize that women who are relatively '
                                        'weak are not the only ones who become '
                                        "victims.' 'I'm thinking of buying a "
                                        'lightweight spray, a trident, or a '
                                        'kubotan (a keychain with a pointed '
                                        "end) for self-defense,' he said. By "
                                        'Yoo Yoon-hee Lee duck@hani.co.kr',
                                  qna_list=[QnA(question='What is causing the '
                                                         'surge in sales of '
                                                         'self-defense '
                                                         'products?',
                                                answer='The surge in sales of '
                                                       'self-defense products '
                                                       'is being caused by '
                                                       'ongoing serious '
                                                       'incidents and the '
                                                       'anxiety of individuals '
                                                       'wanting to protect '
                                                       'themselves.'),
                                            QnA(question='Which online store '
                                                         'posted a message '
                                                         'about the delay in '
                                                         'delivery?',
                                                answer='NAVER Smart Store, '
                                                       'which sells '
                                                       'self-defense products, '
                                                       'posted a message about '
                                                       'the delay in delivery.'),
                                            QnA(question='How much did sales '
                                                         'of self-defense '
                                                         'products increase on '
                                                         'G-market?',
                                                answer='Sales of self-defense '
                                                       'products on G-market '
                                                       'increased by 243 '
                                                       'percent from March 22 '
                                                       'to March 3 compared to '
                                                       'the same period last '
                                                       'year.'),
                                            QnA(question='Why are people '
                                                         'buying self-defense '
                                                         'products?',
                                                answer='People are buying '
                                                       'self-defense products '
                                                       'due to the anxiety of '
                                                       'potential harm and the '
                                                       'need to protect '
                                                       'themselves.'),
                                            QnA(question='What self-defense '
                                                         'products are popular '
                                                         'among women?',
                                                answer='Kubotan, a keychain '
                                                       'with a pointed end, is '
                                                       'popular among women '
                                                       'for self-defense.')],
                                  language='EN-US')],
         images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/640/307/imgdb/original/2023/0804/20230804502176.jpg',
                              source='한겨레'),
                 ArticleImage(url='https://img.biz.sbs.co.kr/upload/2023/08/04/ixf1691116949643.jpg',
                              source='SBS Biz')]),
 Article(category='Entertainment',
         keywords='소방서 옆 경찰서',
         contents=[ArticleContent(title='Hanmyeong Butcher Shop and Gastron '
                                        'Support Production of SBS Drama '
                                        "'Police Station and Gukgwasoo Next to "
                                        "Fire Station'",
                                  lead='Hanmyeong Butcher Shop and Gastron are '
                                       'both supporting the production of '
                                       "SBS's new Friday drama 'Police Station "
                                       "and Gukgwasoo Next to Fire Station'. "
                                       'The drama tells the story of a fire '
                                       'department, a police department, and a '
                                       'gukgwasoo working together to solve '
                                       'unprecedented cases.',
                                  body1='Hanmyeong Butcher Shop and Gastron '
                                        'are actively involved in the '
                                        "production of SBS's new Friday drama "
                                        "'Police Station and Gukgwasoo Next to "
                                        "Fire Station'. This drama revolves "
                                        'around the collaboration between a '
                                        'fire department, a police department, '
                                        'and a gukgwasoo to solve complex and '
                                        'unprecedented cases. Starring actors '
                                        'such as Kim Rae Won, Son Ho Joon, and '
                                        'Gong Seung Yeon, the drama has gained '
                                        'attention since its premiere. It airs '
                                        'every Friday at 10 pm on SBS. '
                                        'Hanmyeong Butcher Shop is a renowned '
                                        'franchise brand specializing in aged '
                                        'raw meat. It provides franchisees '
                                        'with multifaceted brand promotion '
                                        'strategies to boost sales. The '
                                        'headquarters ensures the smooth '
                                        'operation of stores by supplying all '
                                        'ingredients, including meat and '
                                        'sauces, in one pack.',
                                  body2='Additionally, logistics and '
                                        'distribution are handled by the '
                                        'headquarters, reducing supply costs '
                                        'and increasing franchisee margins. '
                                        'Gastron, on the other hand, is a '
                                        'company specializing in industrial '
                                        'gas detectors. Founded in 1992, '
                                        'Gastron has achieved localization and '
                                        'globalization of gas detectors, '
                                        'becoming a leader in the industry. '
                                        "The drama's PPL (Product Placement) "
                                        "includes Gastron's portable gas "
                                        'detectors, which are frequently used '
                                        'by firefighters in the field. These '
                                        'detectors can simultaneously detect '
                                        'oxygen, carbon monoxide, hydrogen '
                                        'sulfide, and combustible gases. As '
                                        'disaster sites often involve various '
                                        'gas-related risks, wearing a gas '
                                        'detector is essential for the safety '
                                        'of firefighters. Gastron aims to '
                                        'promote its products effectively '
                                        'through its support for the drama '
                                        'production and PPL promotion.',
                                  qna_list=[QnA(question='What is the Friday '
                                                         "drama 'Police "
                                                         'Station and '
                                                         'Gukgwasoo Next to '
                                                         "Fire Station' about?",
                                                answer="'Police Station and "
                                                       'Gukgwasoo Next to Fire '
                                                       "Station' is a drama "
                                                       'that follows the '
                                                       'collaboration between '
                                                       'a fire department, a '
                                                       'police department, and '
                                                       'a gukgwasoo to solve '
                                                       'complex and '
                                                       'unprecedented cases.'),
                                            QnA(question='Who are some of the '
                                                         'actors in the drama?',
                                                answer='The drama stars actors '
                                                       'such as Kim Rae Won, '
                                                       'Son Ho Joon, and Gong '
                                                       'Seung Yeon.'),
                                            QnA(question='When does the drama '
                                                         "'Police Station and "
                                                         'Gukgwasoo Next to '
                                                         "Fire Station' air?",
                                                answer='The drama airs every '
                                                       'Friday at 10 pm on '
                                                       'SBS.'),
                                            QnA(question='What is Hanmyeong '
                                                         'Butcher Shop known '
                                                         'for?',
                                                answer='Hanmyeong Butcher Shop '
                                                       'is a renowned '
                                                       'franchise brand '
                                                       'specializing in aged '
                                                       'raw meat.'),
                                            QnA(question='How does Hanmyeong '
                                                         'Butcher Shop support '
                                                         'its franchisees?',
                                                answer='Hanmyeong Butcher Shop '
                                                       'supports its '
                                                       'franchisees through '
                                                       'multifaceted brand '
                                                       'promotion strategies '
                                                       'and by supplying all '
                                                       'ingredients, including '
                                                       'meat and sauces, to '
                                                       'franchisees in one '
                                                       'pack.'),
                                            QnA(question='What does Gastron '
                                                         'specialize in?',
                                                answer='Gastron specializes in '
                                                       'industrial gas '
                                                       'detectors.'),
                                            QnA(question='What product of '
                                                         'Gastron is featured '
                                                         'as PPL in the drama?',
                                                answer="The drama's PPL "
                                                       "includes Gastron's "
                                                       'portable gas '
                                                       'detectors.'),
                                            QnA(question='What gases can '
                                                         "Gastron's gas "
                                                         'detectors detect?',
                                                answer="Gastron's gas "
                                                       'detectors can '
                                                       'simultaneously detect '
                                                       'oxygen, carbon '
                                                       'monoxide, hydrogen '
                                                       'sulfide, and '
                                                       'combustible gases.')],
                                  language='EN-US')],
         images=[ArticleImage(url='https://cdn.mhns.co.kr/news/thumbnail/202308/558808_683527_413_v150.jpg',
                              source='문화뉴스'),
                 ArticleImage(url='https://cdn.mhns.co.kr/news/thumbnail/202308/558806_683525_3934_v150.jpg',
                              source='문화뉴스')]),
 Article(category='Politics',
         keywords='김관영',
         contents=[ArticleContent(title='Governor Kim Kwan-young Highlights '
                                        'Positive Aspects of World Scout '
                                        'Jamboree',
                                  lead='North Jeolla Province Governor Kim '
                                       'Kwan-young has expressed optimism '
                                       'about the ongoing World Scout '
                                       'Jamboree, emphasizing the enjoyable '
                                       'experiences of participants. Despite '
                                       'concerns over the recent fever '
                                       'outbreak and extreme weather '
                                       'conditions, Governor Kim remains '
                                       "committed to ensuring the event's "
                                       'success.',
                                  body1='Governor Kim Kwan-young of North '
                                        'Jeolla Province has been actively '
                                        'involved in overseeing the World '
                                        'Scout Jamboree. He has even chosen to '
                                        'stay at the campsite for the past two '
                                        'days, closely observing the '
                                        'activities and engaging with the '
                                        'participants. According to Governor '
                                        'Kim, the participants have been '
                                        'having a great time, particularly '
                                        'during the evening when they immerse '
                                        'themselves in their respective '
                                        "cultures. The governor's presence at "
                                        'the campsite serves to address safety '
                                        'concerns and ensure the smooth '
                                        'functioning of the jamboree. He has '
                                        'visited the key sites, inspected the '
                                        'facilities, and interacted with the '
                                        'scouts. Despite the challenges faced, '
                                        'Governor Kim remains optimistic about '
                                        "the event's success.",
                                  body2='Addressing the recent fever outbreak, '
                                        'he attributed it to factors such as '
                                        'jet lag and exhaustion experienced by '
                                        'athletes traveling long distances to '
                                        'participate. He noted that the '
                                        "scouts' condition has been improving "
                                        'over the course of the jamboree. In '
                                        'response to the heatwave, the '
                                        'organizers have implemented necessary '
                                        'measures to prioritize the safety of '
                                        'all participants. Governor Kim '
                                        'emphasized the indomitable spirit of '
                                        'the jamboree, highlighting the '
                                        'determination to persevere regardless '
                                        'of the weather conditions. Indoor '
                                        'activities, experience centers, and '
                                        'exhibits have been planned to provide '
                                        'a respite from the heat, while '
                                        'certain outdoor activities have been '
                                        'canceled. The governor stated that '
                                        'further decisions regarding large '
                                        'gatherings, such as K-pop concerts, '
                                        'will be made after a comprehensive '
                                        'assessment in an upcoming meeting. '
                                        'With his unwavering dedication to '
                                        'ensuring participant safety and a '
                                        'memorable jamboree experience, '
                                        'Governor Kim Kwan-young personifies '
                                        'the spirit of a responsible leader '
                                        'and an attentive father.',
                                  qna_list=[QnA(question='What has Governor '
                                                         "Kim Kwan-young's "
                                                         'role been at the '
                                                         'World Scout '
                                                         'Jamboree?',
                                                answer='Governor Kim '
                                                       'Kwan-young has been '
                                                       'overseeing the World '
                                                       'Scout Jamboree and has '
                                                       'chosen to stay at the '
                                                       'campsite for the past '
                                                       'two days to ensure '
                                                       'safety and address any '
                                                       'concerns.'),
                                            QnA(question='How have the '
                                                         'participants been '
                                                         'enjoying the '
                                                         'jamboree?',
                                                answer='According to Governor '
                                                       'Kim, the participants '
                                                       'have been having a lot '
                                                       'of fun, particularly '
                                                       'during the evening as '
                                                       'they engage in '
                                                       'cultural activities.'),
                                            QnA(question='What factors '
                                                         'contributed to the '
                                                         'recent fever '
                                                         'outbreak?',
                                                answer='Governor Kim '
                                                       'attributed the fever '
                                                       'outbreak to jet lag '
                                                       'and exhaustion '
                                                       'experienced by '
                                                       'athletes traveling '
                                                       'long distances to '
                                                       'participate in the '
                                                       'jamboree.'),
                                            QnA(question='How are the '
                                                         'organizers '
                                                         'addressing the '
                                                         'heatwave?',
                                                answer='The organizers have '
                                                       'implemented measures '
                                                       'such as moving indoor '
                                                       'activities, experience '
                                                       'centers, and exhibits '
                                                       'indoors, and canceling '
                                                       'certain outdoor '
                                                       'activities to '
                                                       'prioritize participant '
                                                       'safety during the '
                                                       'heatwave.'),
                                            QnA(question='What is the '
                                                         "governor's stance "
                                                         'regarding the '
                                                         "event's success?",
                                                answer='Governor Kim remains '
                                                       'optimistic about the '
                                                       "event's success and "
                                                       'emphasized the '
                                                       'indomitable spirit of '
                                                       'the jamboree.')],
                                  language='EN-US')],
         images=[ArticleImage(url='https://cdn.eroun.net/news/thumbnail/202308/35826_64573_3536_v150.jpg',
                              source='이로운넷'),
                 ArticleImage(url='https://cdn.pressian.com/_resources/10/2023/08/04/2023080410440197244_l.png',
                              source='프레시안')]),
 Article(category='Politics',
         keywords='박영수 구속',
         contents=[ArticleContent(title="'50 billion club' Park Young-soo "
                                        "arrested...What's the difference from "
                                        'when he was dismissed a month ago?',
                                  lead='The arrest warrant for former special '
                                       'prosecutor Park Young-soo, which the '
                                       'court dismissed once, was issued on '
                                       'March 3. Park was lobbied by a private '
                                       'businessman in Daejeon-dong...',
                                  body1='Former special prosecutor Park '
                                        'Young-soo, who is under suspicion of '
                                        "the so-called '5 billion club' for "
                                        'receiving money in exchange for '
                                        'helping private developers in '
                                        'Daejeon-dong, heads to court to '
                                        'appear for his second pre-arrest '
                                        'interrogation (warrant examination) '
                                        'at the Seoul Central District Court '
                                        'in Seocho-gu, Seoul, on Wednesday '
                                        'morning. Yonhap An arrest warrant for '
                                        'former special prosecutor Park '
                                        'Young-soo, which the court had '
                                        'dismissed once, was issued on '
                                        'Wednesday. Park is considered one of '
                                        "the members of the '5 billion club' "
                                        'that allegedly received lobbying from '
                                        'a private businessman in Daegu-dong. '
                                        'Additional charges filed by '
                                        'prosecutors in the course of the '
                                        'reinforcement investigation are '
                                        'believed to have made the difference. '
                                        'Yoon Jae-nam, deputy chief judge of '
                                        "the Seoul Central District Court's "
                                        'warrant division, announced the '
                                        'reason for issuing an arrest warrant '
                                        'for Park on the night of March 3, '
                                        "saying that 'there is a risk of "
                                        "evidence being destroyed.' Normally, "
                                        'an arrest warrant is issued on the '
                                        'premise that the charges have been '
                                        'partially proven and for reasons such '
                                        'as evidence destruction and fear of '
                                        'escape. Previously, in June, Chief '
                                        'Warrant Officer Yoo Chang-hoon '
                                        'dismissed the arrest warrant, saying '
                                        "that the charges were 'disputed in "
                                        "factual and legal terms' and did not "
                                        'recognize the charges themselves. The '
                                        'prosecution believes the new charges, '
                                        'which were filed in a reinforced '
                                        'investigation, helped reverse the '
                                        'outcome. Prosecutors added the charge '
                                        'of violating the anti-graft law, '
                                        'alleging that 1.1 billion won of the '
                                        'money Park was supposed to receive '
                                        'went to her daughter, Park '
                                        'Ah-moo-gae, in the form of loans '
                                        'while she was a special prosecutor. '
                                        'The prosecution claimed that private '
                                        'businesses in Daejeon-dong promised '
                                        'to pay Park, and that the promise was '
                                        'realized in the 1.1 billion won that '
                                        "went to Park's daughter, which the "
                                        'court accepted.',
                                  body2="Park's destruction of her cell phone "
                                        'earlier this year is also believed to '
                                        "have contributed to the court's "
                                        "determination of 'evidence "
                                        "destruction concerns.' New evidence "
                                        'obtained during the reinforcement '
                                        'investigation also played a role. '
                                        'During the reinforcement '
                                        'investigation, the prosecution '
                                        'obtained a loan agreement stating '
                                        'that Kim Man-bae, the majority '
                                        'shareholder of Hwacheon Daewoo Asset '
                                        'Management, borrowed 500 million won '
                                        'from Park, and that Park was to '
                                        'receive the money back in shares. The '
                                        'document served to support the '
                                        'allegation that Park had agreed to '
                                        "receive money. 'After carefully "
                                        'analyzing the reasons for dismissing '
                                        'the warrant, we reinforced the '
                                        'evidence with solid evidence and '
                                        "explained it in detail to the court,' "
                                        'said an official from the Seoul '
                                        "Central District Prosecutors' Office. "
                                        'Park has previously stated that she '
                                        "'did not receive or promise anything "
                                        'in exchange for participating in the '
                                        'Daejeon-dong development project or '
                                        "arranging financing.' The detention "
                                        'of Park is expected to speed up the '
                                        "rest of the '5 billion club' "
                                        'investigation. In particular, the '
                                        'investigation of former Nationalist '
                                        'Party of Korea lawmaker Kwak Sang-do, '
                                        'whose case is similarly structured in '
                                        'that he realized the money he was to '
                                        'receive through his children, is '
                                        'likely to gain momentum. Prosecutors '
                                        "called Kwak's son, Kwak Sang-do, who "
                                        'received 5 billion won in severance '
                                        'pay (2.5 billion won in error) from '
                                        'Hwacheon Daewoo, for questioning on '
                                        'the 27th of last month and again '
                                        'earlier this week. A prosecution '
                                        "official said on March 3, 'We plan to "
                                        "investigate the alleged '5 billion "
                                        "club' in a sequential manner.' Former "
                                        'Supreme Court Justice Kwon Soon-il, '
                                        "who is suspected of 'trial "
                                        "transactions,' is also being "
                                        'investigated. By Kwang-joon Jeon '
                                        'light@hani.co.kr',
                                  qna_list=[QnA(question='Why was an arrest '
                                                         'warrant issued for '
                                                         'Park Young-soo?',
                                                answer='An arrest warrant was '
                                                       'issued for Park '
                                                       'Young-soo due to the '
                                                       'risk of evidence being '
                                                       'destroyed. The '
                                                       'prosecution believes '
                                                       'that new charges filed '
                                                       'during the '
                                                       'reinforcement '
                                                       'investigation, '
                                                       'including a violation '
                                                       'of the anti-graft law, '
                                                       'helped reverse the '
                                                       'outcome.'),
                                            QnA(question="What is the '5 "
                                                         "billion club'?",
                                                answer="The '5 billion club' "
                                                       'refers to a group of '
                                                       'individuals who '
                                                       'allegedly received '
                                                       'money in exchange for '
                                                       'assisting private '
                                                       'developers in '
                                                       'Daejeon-dong.'),
                                            QnA(question='Who else is being '
                                                         'investigated in '
                                                         "relation to the '5 "
                                                         "billion club'?",
                                                answer='Former Nationalist '
                                                       'Party of Korea '
                                                       'lawmaker Kwak Sang-do '
                                                       'and former Supreme '
                                                       'Court Justice Kwon '
                                                       'Soon-il are also being '
                                                       'investigated in '
                                                       "connection with the '5 "
                                                       "billion club' case."),
                                            QnA(question='What is the '
                                                         'significance of Park '
                                                         "Young-soo's arrest "
                                                         "in the '5 billion "
                                                         "club' investigation?",
                                                answer="Park Young-soo's "
                                                       'arrest is expected to '
                                                       'accelerate the rest of '
                                                       "the '5 billion club' "
                                                       'investigation. It may '
                                                       'also lead to a further '
                                                       'investigation into '
                                                       'other members of the '
                                                       'group.')],
                                  language='EN-US')],
         images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/647/imgdb/original/2023/0804/20230804501508.jpg',
                              source='한겨레'),
                 ArticleImage(url='https://dimg.donga.com/a/800/0/95/5/wps/NEWS/IMAGE/2023/08/04/120570314.1.jpg',
                              source='동아일보')]),
 Article(category='Crime',
         keywords='칼부림예고',
         contents=[ArticleContent(title='Arrest Made in Daegu University '
                                        'Threatening Post Case',
                                  lead='A 20-year-old individual who posted a '
                                       'threatening message on the Daegu '
                                       'University bulletin board has been '
                                       'apprehended by the Gyeongsan Police '
                                       'Department. The post, which mentioned '
                                       'stabbings, triggered concerns among '
                                       'students and prompted an '
                                       'investigation.',
                                  body1='The Gyeongsan Police Department in '
                                        'Gyeongsangbuk-do, Gyeongsangbuk-do, '
                                        'announced on the afternoon of the 4th '
                                        'that it arrested A, in his 20s, for '
                                        'writing a post satirizing stabbings '
                                        'on the Everytime Daegu University '
                                        'bulletin board (threats).A wrote a '
                                        'post at 2:38 p.m. on the same day, '
                                        "saying, 'Daegu University Rollo Noir "
                                        "Zoro 3 degrees of stabbings.' He "
                                        "posted a post titled, 'Daegu "
                                        'University Rolloa Zoro. The post was '
                                        'deleted at 3:10 p.m., but students '
                                        "who saw it reported it as a 'warning "
                                        "of a weapon rampage,' prompting "
                                        'police to launch an investigation. '
                                        'Police traced his internet address '
                                        '(IP) and arrested him five hours '
                                        'later near a study cafe in Gyeongsan, '
                                        'North Gyeongsang Province.',
                                  body2='Police plan to file threatening '
                                        'charges against him. In the wake of '
                                        'the recent stabbing rampage, police '
                                        'have been applying threatening '
                                        'charges to posters of death threats '
                                        'on online communities and social '
                                        'media services (SNS). The crime of '
                                        'threatening is punishable by up to '
                                        'three years in prison and a fine of '
                                        'up to 5 million won.',
                                  qna_list=[QnA(question='Who has been '
                                                         'arrested by the '
                                                         'Gyeongsan Police '
                                                         'Department?',
                                                answer='A 20-year-old '
                                                       'individual has been '
                                                       'arrested by the '
                                                       'Gyeongsan Police '
                                                       'Department.'),
                                            QnA(question='What was the content '
                                                         'of the threatening '
                                                         'post?',
                                                answer='The post mentioned '
                                                       "'Daegu University "
                                                       'Rollo Noir Zoro 3 '
                                                       "degrees of stabbings.'"),
                                            QnA(question='How did the police '
                                                         'trace the '
                                                         'individual?',
                                                answer='The police traced the '
                                                       'individual through '
                                                       'their internet address '
                                                       '(IP).'),
                                            QnA(question='What charges will '
                                                         'the police file '
                                                         'against the arrested '
                                                         'individual?',
                                                answer='The police will file '
                                                       'threatening charges '
                                                       'against the arrested '
                                                       'individual.'),
                                            QnA(question='What is the '
                                                         'punishment for the '
                                                         'crime of '
                                                         'threatening?',
                                                answer='The crime of '
                                                       'threatening is '
                                                       'punishable by up to '
                                                       'three years in prison '
                                                       'and a fine of up to 5 '
                                                       'million won.')],
                                  language='EN-US')],
         images=[ArticleImage(url='https://newsimg.sedaily.com/2023/08/04/29TA0FROJB_1.jpg',
                              source='서울경제신문'),
                 ArticleImage(url='https://newsimg.sedaily.com/2023/08/04/29TA11XCJD_1.jpg',
                              source='서울경제신문')])]


########################## STEP 5 ##########################
step_5 = [Article(category='Sports',
         keywords='월드컵,여자월드컵,축구,여자 월드컵,한국 독일',
         contents=[ArticleContent(title='South Korea Holds Germany to a 1-1 '
                                        "Draw in Women's World Cup Group H",
                                  lead="The South Korea women's national "
                                       'soccer team, led by head coach Colleen '
                                       'Bell, played to a 1-1 draw against '
                                       'world No. 2 Germany in their final '
                                       "match of Group H at the FIFA Women's "
                                       'World Cup 2023.',
                                  body1="The South Korean women's national "
                                        'football team scored a first-half '
                                        'goal for the first time in World Cup '
                                        'history against Germany in their '
                                        'final Group H match of the 2023 FIFA '
                                        "Women's World Cup at Brisbane Stadium "
                                        'in Australia on August 3, but '
                                        'conceded a late equalizer to settle '
                                        'for a 1-1 draw. South Korea took a '
                                        '1-0 lead when Cho So-hyun opened the '
                                        'scoring with a precise right-footed '
                                        'strike in the sixth minute, but '
                                        "Germany's captain and goalkeeper "
                                        'Alexandra Pope equalized in the 42nd '
                                        'minute to level the match.',
                                  body2='With South Korea looking to secure a '
                                        'point in the group stage and Germany '
                                        'facing elimination, both teams played '
                                        'more attacking soccer in the second '
                                        'half in an attempt to secure a '
                                        'victory, but the match ended 1-1. '
                                        'South Korea (ranked 17th in the FIFA '
                                        'rankings) finished last in Group H '
                                        'with a 1-1 draw, but unlike four '
                                        'years ago in France when they '
                                        'finished with three losses, they '
                                        'finished the tournament with a '
                                        'valuable point.',
                                  qna_list=[QnA(question='What was the final '
                                                         'score of the match '
                                                         'between South Korea '
                                                         'and Germany?',
                                                answer='The match ended in a '
                                                       '1-1 draw.'),
                                            QnA(question='Who scored the '
                                                         'opening goal for '
                                                         'South Korea?',
                                                answer='Cho So-hyun scored the '
                                                       'opening goal for South '
                                                       'Korea.'),
                                            QnA(question='Who equalized for '
                                                         'Germany?',
                                                answer="Germany's captain and "
                                                       'goalkeeper Alexandra '
                                                       'Pope equalized for '
                                                       'Germany.'),
                                            QnA(question='Why was this match '
                                                         'important for South '
                                                         'Korea?',
                                                answer='South Korea was '
                                                       'looking to secure a '
                                                       'point in the group '
                                                       'stage, and they '
                                                       'finished the '
                                                       'tournament with a '
                                                       'valuable point.'),
                                            QnA(question='What was South '
                                                         "Korea's ranking in "
                                                         'the FIFA rankings?',
                                                answer='South Korea was ranked '
                                                       '17th in the FIFA '
                                                       'rankings.')],
                                  language='EN-US'),
                   ArticleContent(title='韩国队在女足世界杯 H 组中 1-1 战平德国队',
                                  lead='韩国国家女子足球队在主教练科琳-贝尔（Colleen Bell）的带领下，在 '
                                       '2023 年女足世界杯 H 组的最后一场比赛中以 1-1 '
                                       '战平世界排名第二的德国队。',
                                  body1='8月3日，在澳大利亚布里斯班体育场举行的2023年女足世界杯H组最后一场比赛中，韩国国家女子足球队在对阵德国队的比赛中上半场就取得进球，这是韩国队在世界杯历史上首次取得进球，但在最后时刻丢球扳平比分，最终以1比1战平德国队。韩国队在第 '
                                        '6 分钟由赵素贤（Cho '
                                        'So-hyun）以一记精准的右脚射门首开纪录，取得 1-0 '
                                        '领先，但德国队队长兼门将亚历山德拉-波普（Alexandra '
                                        'Pope）在第 42 分钟扳平比分。',
                                  body2='韩国队希望在小组赛中拿到一分，而德国队则面临淘汰，两队在下半场都踢出了更具攻击性的足球，试图取得胜利，但比赛最终以 '
                                        '1-1 结束。韩国队（国际足联排名第 17 位）最终在 H 组中以 1-1 '
                                        '战平对手，但与四年前在法国以三战皆负的结果不同，他们以宝贵的一分结束了比赛。',
                                  qna_list=[QnA(question='韩国队和德国队比赛的最终比分是多少？',
                                                answer='比赛最终以 1-1 平局结束。'),
                                            QnA(question='谁为韩国队首开纪录？',
                                                answer='赵昭贤为韩国队首开纪录。'),
                                            QnA(question='谁为德国队扳平了比分？',
                                                answer='德国队队长兼门将亚历山德拉-波普为德国队扳平比分。'),
                                            QnA(question='为什么这场比赛对韩国很重要？',
                                                answer='韩国队希望在小组赛中拿到一分，他们以宝贵的一分结束了比赛。'),
                                            QnA(question='韩国在国际足联的排名是多少？',
                                                answer='韩国队在国际足联排名中名列第 17 位。')],
                                  language='ZH'),
                   ArticleContent(title='한국, 독일과 여자 월드컵 H조에서 1-1 무승부 기록',
                                  lead='콜린 벨 감독이 이끄는 대한민국 여자 축구 대표팀이 2023 FIFA '
                                       '여자월드컵 조별리그 H조 최종전에서 세계랭킹 2위 독일과 1-1 '
                                       '무승부를 거뒀습니다.',
                                  body1='한국 여자 축구 대표팀은 8월 3일 호주 브리즈번 스타디움에서 열린 '
                                        '독일과의 2023 국제축구연맹(FIFA) 여자 월드컵 조별리그 H조 '
                                        '최종전에서 월드컵 사상 처음으로 전반전에 선제골을 넣었지만 후반에 '
                                        '동점골을 허용해 1-1 무승부에 만족해야 했다. 한국은 전반 6분 '
                                        '조소현이 정확한 오른발 슈팅으로 선제골을 터뜨리며 1-0으로 '
                                        '앞서나갔지만 후반 42분 독일의 주장 겸 골키퍼 알렉산드라 포프가 '
                                        '동점골을 터뜨리며 승부를 원점으로 돌렸습니다.',
                                  body2='조별리그에서 승점을 확보해야 하는 한국과 탈락이 유력한 독일, 두 '
                                        '팀 모두 승리를 위해 후반전에 공격적인 축구를 펼쳤지만 경기는 '
                                        '1-1로 끝났습니다. 한국(FIFA 랭킹 17위)은 1-1 무승부로 '
                                        'H조 최하위를 기록했지만, 4년 전 프랑스에서 3패로 대회를 마쳤던 '
                                        '것과 달리 귀중한 승점을 챙기며 대회를 마무리했습니다.',
                                  qna_list=[QnA(question='대한민국과 독일의 경기 최종 스코어는 '
                                                         '어떻게 되나요?',
                                                answer='경기는 1-1 무승부로 끝났습니다.'),
                                            QnA(question='한국의 첫 골은 누가 넣었나요?',
                                                answer='조소현이 한국의 선제골을 넣었습니다.'),
                                            QnA(question='독일은 누가 동점을 기록했나요?',
                                                answer='독일의 주장 겸 골키퍼 알렉산드라 포프가 '
                                                       '독일의 동점골을 터뜨렸습니다.'),
                                            QnA(question='이번 경기가 한국에게 중요한 이유는 '
                                                         '무엇인가요?',
                                                answer='조별리그에서 승점 확보를 노렸던 한국은 '
                                                       '귀중한 승점을 따내며 대회를 '
                                                       '마무리했습니다.'),
                                            QnA(question='FIFA 랭킹에서 한국의 순위는 '
                                                         '어떻게 되나요?',
                                                answer='한국은 FIFA 랭킹 17위를 '
                                                       '기록했습니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://img.olympicchannel.com/images/image/private/t_social_share_thumb/f_auto/primary/an8hsyg0rlbuy0cvbi32',
                              source='Olympics'),
                 ArticleImage(url='https://biz.chosun.com/resizer/LwAJb26bxlCQqjko_uBVir_Q5SM=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/FJ2ZH42M2DYNMXRDD7JKH4KRGA.png',
                              source='조선비즈')]),
 Article(category='Crime',
         keywords='서현역 칼부림,서현역,칼부림,칼부림 예고,분당 칼부림,오리역,서현역 흉기난동,살인예고,오리역 '
                  '칼부림,분당,성남 칼부림,묻지마 칼부림,분당 서현역,서현역 흉기,잠실역 살인 예고,흉기난동,분당 서현역 '
                  '칼부림,ak플라자,서현역칼부림,오리역 살인예고',
         contents=[ArticleContent(title="'Seohyun Station stabbing' video "
                                        "spreads, citizens traumatized 'red "
                                        "light'",
                                  lead="On the afternoon of the 3rd, a 'don't "
                                       "ask, don't tell' stabbing incident "
                                       'occurred at a large shopping mall near '
                                       'Seohyeon Station in Bundang, '
                                       'Seongnam-si, Gyeonggi-do.',
                                  body1="On the afternoon of the 3rd, a 'don't "
                                        "ask, don't tell' stabbing incident "
                                        'occurred at a large shopping mall '
                                        'near Seohyeon Station in Bundang, '
                                        'Seongnam-si, Gyeonggi-do. A police '
                                        'car enters the area near the incident '
                                        'site on the morning of the 4th. Photo '
                                        'by Lim Hyung-taek On the morning of '
                                        'the 4th, Hong Mo (25), a resident of '
                                        'Paju City, Gyeonggi Province, came '
                                        'across a video of the Seohyeon '
                                        'Station weapon rampage while browsing '
                                        'social media. The video showed the '
                                        'suspect walking around with a knife '
                                        "at the crime scene. 'I didn't want to "
                                        'watch it, but I ended up watching '
                                        "it,' Ms. Hong said, adding, 'There "
                                        'are a lot of posts, so I keep seeing '
                                        "it over and over again.' 'I feel "
                                        'depressed because I only see horrible '
                                        "news,' he said, adding, 'I won't look "
                                        "at social media for a while.' On the "
                                        "afternoon of the 3rd, a 'don't ask, "
                                        "don't tell' weapon rampage took place "
                                        'at a large shopping mall near '
                                        'Seohyeon Station in Bundang, '
                                        'Seongnam-si, Gyeonggi-do. Police are '
                                        'controlling the scene. Photo by Lim '
                                        'Hyung-taek Recently, citizens have '
                                        'been complaining about the '
                                        'inconvenience of being forced to '
                                        'watch videos of a series of stabbing '
                                        'incidents. The problem is that they '
                                        'are often forced to watch them on '
                                        "social media even if they don't want "
                                        'to.Since the night of the 3rd of this '
                                        'month, photos of the scene of '
                                        'Seohyeon Station, where Abi Gyu-hwan '
                                        'was found, have been posted one after '
                                        'another on various social media. '
                                        'Seohyeon Station is an everyday space '
                                        'with a large number of people and is '
                                        'often used as a meeting place. The '
                                        'photos show a devastating scene where '
                                        'all traces of everyday life have '
                                        'disappeared. The unconscious bodies '
                                        'of the victims and the blood-soaked '
                                        "scene were nakedly visible. It's not "
                                        'hard to find photos that have not '
                                        'been sensationalized, edited, or '
                                        'mosaicked. A quick Instagram search '
                                        "for the hashtag 'stabbing' yields "
                                        'more than 1,000 posts.Short-form '
                                        'video content was also created, so '
                                        "it's not hard to find footage of the "
                                        "attack if you're willing to look.",
                                  body2='The video shows a black hooded '
                                        'assailant charging at a group of '
                                        'people with a weapon. The video shows '
                                        'the perpetrator wielding the weapon, '
                                        'as well as his mugshot. Some of the '
                                        'posts were intentionally inflammatory '
                                        "in order to attract users' attention. "
                                        "'This is so horrible,' 'I don't want "
                                        "to see this,' and 'I feel sick to my "
                                        "stomach,' were some of the reactions "
                                        'to the shocking video. Some citizens '
                                        'were traumatized by the brutal video. '
                                        "'I'm scared because I keep watching "
                                        'the video of the incident and feel '
                                        "like it's no one else's business,' "
                                        'said my aunt (26, female, office '
                                        'worker) in Wonju, Gangwon Province. '
                                        "'Crazy X is everywhere, and the "
                                        'province is no exception. I feel like '
                                        'someone will suddenly enter my office '
                                        "and stab me with a knife.' My aunt, a "
                                        '25-year-old female office worker in '
                                        "Gangnam-gu, Seoul, said, 'I keep "
                                        'seeing videos and imagining all sorts '
                                        "of things,' and complained of a "
                                        "'strong sense of fear.' Last year's "
                                        'Itaewon tragedy also became a problem '
                                        'when photos and videos from the scene '
                                        'were shared online. However, there '
                                        "are no 'guidelines' for photos and "
                                        'videos. Short-form videos are '
                                        'especially problematic because they '
                                        "auto-play even if you don't choose to "
                                        'watch them, forcing users to watch '
                                        "them even if they don't want to. "
                                        "'During the Itaewon tragedy, there "
                                        'were a lot of photos and videos of '
                                        "the scene,' one user wrote, 'and it "
                                        'looks like it will be there for a '
                                        "while. 'Usually, trauma is "
                                        'experienced by the individual or when '
                                        "it happens to a close family member,' "
                                        'said Baek Jong-woo, a professor of '
                                        'psychiatry at Kyung Hee University, '
                                        "'but nowadays, as the quality of "
                                        'photos and videos has improved and it '
                                        'is easier to obtain videos, more and '
                                        'more people are complaining of severe '
                                        "traumatic pain directly.' 'Repeatedly "
                                        'viewing footage of the event can lead '
                                        'to symptoms such as anxiety and '
                                        "insomnia,' he said. 'The younger the "
                                        "age, the greater the impact. 'The "
                                        'younger you are, the more it affects '
                                        'you. The negative impact on teenagers '
                                        "is greater,' he warned.It is expected "
                                        'to be difficult to punish under the '
                                        'current law even if the video is '
                                        "distributed. 'These photos and videos "
                                        'are more for the purpose of '
                                        "publicizing the scene,' said Choi "
                                        'Jin-nyeong, a lawyer at CK Law Firm. '
                                        "'If they are not intended to cause "
                                        'sexual humiliation or slander, it is '
                                        'difficult to punish them as cyber '
                                        "defamation.' 'It is an ongoing "
                                        "problem,' he said of the spread of "
                                        "horrific scenes online, 'and it is "
                                        'necessary to legislate through social '
                                        'discussion, such as whether or not to '
                                        "criminally punish them.'Reporter Lee "
                                        'Yesol ysolzz6@kukinews.com',
                                  qna_list=[QnA(question='Where did the '
                                                         'stabbing incident '
                                                         'occur?',
                                                answer='The stabbing incident '
                                                       'occurred at a large '
                                                       'shopping mall near '
                                                       'Seohyeon Station in '
                                                       'Bundang, Seongnam-si, '
                                                       'Gyeonggi-do.'),
                                            QnA(question='What did a video of '
                                                         'the Seohyeon Station '
                                                         'weapon rampage show?',
                                                answer='The video showed the '
                                                       'suspect walking around '
                                                       'with a knife at the '
                                                       'crime scene.'),
                                            QnA(question='How are citizens '
                                                         'reacting to the '
                                                         'videos of the '
                                                         'stabbing incidents?',
                                                answer='Citizens have been '
                                                       'complaining about the '
                                                       'inconvenience of being '
                                                       'forced to watch the '
                                                       'videos, and some have '
                                                       'been traumatized by '
                                                       'the brutal footage.'),
                                            QnA(question='What are the '
                                                         'concerns regarding '
                                                         'photos and videos of '
                                                         'the stabbing '
                                                         'incidents?',
                                                answer='There are no '
                                                       'guidelines for photos '
                                                       'and videos, and '
                                                       'short-form videos '
                                                       'auto-play even if '
                                                       "users don't choose to "
                                                       'watch them, causing '
                                                       'distress and trauma.'),
                                            QnA(question='What are the '
                                                         'possible impacts of '
                                                         'repeatedly viewing '
                                                         'the footage of the '
                                                         'stabbing incidents?',
                                                answer='Repeatedly viewing the '
                                                       'footage can lead to '
                                                       'symptoms such as '
                                                       'anxiety and insomnia, '
                                                       'with a greater '
                                                       'negative impact on '
                                                       'younger individuals, '
                                                       'particularly '
                                                       'teenagers.')],
                                  language='EN-US'),
                   ArticleContent(title="西贤站刺杀事件 ''视频流传开来，市民受创 ''亮红灯",
                                  lead="3 日下午，京畿道城南市盆唐锡玄站附近的大型购物中心发生了一起 ''不问不说 "
                                       "''的刺伤事件。",
                                  body1='3 日下午，京畿道城南市盆唐锡玄站附近的大型购物中心发生了一起 '
                                        "''不问不说 ''的刺伤事件。4 "
                                        '日上午，一辆警车驶入事发地点附近。照片：Lim Hyung-taek 4 '
                                        '日上午，京畿道坡州市居民洪武（25 '
                                        "岁）在浏览社交媒体时看到了西岘站凶器暴行的视频。视频中，犯罪嫌疑人拿着刀在犯罪现场走来走去。洪女士说：''我本来不想看，但还是看了，''她补充说，''有很多帖子，所以我一直在反复看。他说：''我觉得很沮丧，因为我只看到可怕的新闻，''他补充说，''我有一段时间不看社交媒体了。3 "
                                        '日下午，京畿道城南市盆唐锡玄站附近的一家大型购物中心发生了一起 '
                                        "''不问不说 ''的凶杀案。警方正在控制现场。照片：Lim "
                                        'Hyung-taek '
                                        '最近，市民们一直在抱怨被迫观看一系列刺杀事件视频带来的不便。从本月 3 '
                                        '日晚开始，阿比奎焕被发现的西岘站的现场照片接二连三地出现在各种社交媒体上。西岘站是一个人流量很大的日常空间，经常被用作集会场所。从照片中可以看出，现场一片狼藉，日常生活的痕迹全部消失。受害者失去知觉的尸体和鲜血淋漓的现场赤裸裸地呈现在人们眼前。要找到未经煽情、编辑或打马赛克的照片并不难。在 '
                                        "Instagram 上快速搜索标签 ''刺伤''，可以找到 1000 "
                                        '多条帖子。此外，还制作了短视频内容，因此只要你愿意寻找，就不难找到袭击事件的录像。',
                                  body2="视频显示，一名黑色蒙面袭击者手持武器冲向一群人。视频中可以看到行凶者挥舞着武器，以及他的大头照。为了吸引用户的关注，一些帖子故意带有煽动性。这太可怕了''、''我不想看到这个''、''我感到恶心 "
                                        "''等是对这段令人震惊的视频的一些反应。一些市民被这段残忍的视频吓坏了。我的姑姑（26 "
                                        "岁，女，办公室职员）在江原道原州说：''我很害怕，因为我一直在看事件的视频，觉得这不关别人的事。疯狂 "
                                        'X '
                                        "无处不在，江原道也不例外。我觉得有人会突然闯进我的办公室，用刀捅我。''我的姑姑是首尔江南区的一名 "
                                        '25 '
                                        "岁女性上班族，她说，''我总是看到视频，想象着各种事情''，并抱怨说''有强烈的恐惧感''。去年梨泰院惨案的现场照片和视频被分享到网上后，也成了一个问题。然而，照片和视频没有 "
                                        "''指导原则''。短视频尤其成问题，因为即使您不选择观看，它们也会自动播放，这就迫使用户即使不想看也得看。一位用户写道：''在梨泰院惨案发生期间，有很多关于现场的照片和视频，''''看起来会持续一段时间。''庆熙大学精神病学教授白钟佑说，''通常情况下，创伤是由个人或发生在近亲属身上时经历的，''但如今，随着照片和视频质量的提高，视频的获取也更加容易，越来越多的人直接诉说严重的创伤性疼痛。''他说，''反复观看事件的录像会导致焦虑和失眠等症状。年龄越小，影响越大。年龄越小，影响越大。他警告说：''对青少年的负面影响更大。''根据现行法律，即使视频被传播，预计也很难受到惩罚。CK "
                                        '律师事务所的律师 Choi Jin-nyeong '
                                        "说：''这些照片和视频更多的是为了宣传现场。''如果不是为了造成性侮辱或诽谤，就很难作为网络诽谤进行处罚。这是一个持续存在的问题，''他在谈到网上传播的恐怖场景时说，''有必要通过社会讨论进行立法，例如是否对其进行刑事处罚。''记者 "
                                        'Lee Yesol ysolzz6@kukinews.com',
                                  qna_list=[QnA(question='刺伤事件发生在哪里？',
                                                answer='刺伤事件发生在京畿道城南市盆唐锡玄站附近的一个大型购物中心。'),
                                            QnA(question='西贤站武器暴行的视频显示了什么？',
                                                answer='视频显示，犯罪嫌疑人在犯罪现场拿着一把刀四处走动。'),
                                            QnA(question='市民对刺伤事件的视频有何反应？',
                                                answer='公民们一直在抱怨被迫观看视频带来的不便，有些人还因这些残忍的镜头而受到创伤。'),
                                            QnA(question='对刺伤事件的照片和视频有什么担忧？',
                                                answer='照片和视频没有指导原则，即使用户不选择观看，短视频也会自动播放，这给用户造成了困扰和创伤。'),
                                            QnA(question='反复观看刺伤事件的录像可能会产生什么影响？',
                                                answer='反复观看录像会导致焦虑和失眠等症状，对年轻人尤其是青少年的负面影响更大。')],
                                  language='ZH'),
                   ArticleContent(title="''서현역 칼부림'' 영상 확산, 시민들 충격 ''빨간불''",
                                  lead="3일 오후 경기도 성남시 분당 서현역 인근 대형 쇼핑몰에서 ''묻지도 "
                                       "따지지도 말라''는 식의 칼부림 사건이 발생했다.",
                                  body1='3일 오후 경기도 성남시 분당 서현역 인근 대형 쇼핑몰에서 '
                                        "''묻지도 따지지도 말라''는 식의 칼부림 사건이 발생했다. 4일 "
                                        '오전 경찰차가 사건 현장 인근으로 진입하고 있다. 사진 임형택 기자 '
                                        '4일 오전 경기도 파주시에 거주하는 홍 모(25) 씨는 SNS를 '
                                        '검색하던 중 서현역 흉기 난동 영상을 보게 됐다. 영상에는 용의자가 '
                                        '범행 현장에서 칼을 들고 돌아다니는 모습이 담겨 있었습니다. 홍 '
                                        "씨는 ''보고 싶지 않았지만 결국 보게 됐다''며 ''게시물이 너무 "
                                        "많아서 계속 반복해서 보게 된다''고 말했다. 그는 ''끔찍한 "
                                        "뉴스만 보니까 우울한 기분이 든다''며 ''당분간 SNS를 보지 "
                                        "않을 것''이라고 덧붙였다. 3일 오후 경기도 성남시 분당 서현역 "
                                        "인근 대형 쇼핑몰에서 ''묻지도 따지지도 말라''는 식의 흉기 "
                                        '난동이 벌어졌다. 경찰이 현장을 통제하고 있다. 사진 임형택 최근 '
                                        '연이은 칼부림 사건으로 인해 시민들이 강제로 영상을 시청해야 하는 '
                                        '불편함을 호소하고 있다. 문제는 원하지 않는데도 강제로 시청해야 '
                                        '하는 경우가 많다는 것. 지난 3일 밤부터 각종 소셜미디어에는 '
                                        '아비규환이 발견된 서현역 현장 사진이 잇따라 올라오고 있다. '
                                        '서현역은 유동인구가 많고 만남의 장소로 자주 이용되는 일상적인 '
                                        '공간입니다. 사진 속에는 일상의 흔적이 모두 사라진 참혹한 현장이 '
                                        '고스란히 담겨 있습니다. 의식을 잃은 희생자들의 시신과 피투성이가 '
                                        '된 현장의 모습이 적나라하게 드러났습니다. 선정적이거나 편집되거나 '
                                        '모자이크 처리되지 않은 사진을 찾는 것은 어렵지 않습니다. '
                                        "인스타그램에서 ''칼부림''이라는 해시태그를 검색하면 1,000개 "
                                        '이상의 게시물을 찾을 수 있으며, 짧은 형식의 동영상 콘텐츠도 '
                                        '제작되었기 때문에 마음만 먹으면 공격 장면을 어렵지 않게 찾을 수 '
                                        '있습니다.',
                                  body2='이 동영상에는 검은색 후드를 쓴 가해자가 무기를 들고 사람들에게 '
                                        '돌진하는 모습이 담겨 있습니다. 동영상에는 가해자가 무기를 휘두르는 '
                                        '모습과 얼굴 사진이 함께 표시됩니다. 일부 게시물은 사용자의 관심을 '
                                        "끌기 위해 의도적으로 선동적인 내용을 담고 있었습니다. ''너무 "
                                        "끔찍하다'', ''보고 싶지 않다'', ''속이 메스껍다'' 등 "
                                        '충격적인 영상에 대한 반응은 다양했습니다. 일부 시민들은 잔인한 '
                                        '영상에 충격을 받았습니다. 강원도 원주에 사는 이모(26세, 여, '
                                        "회사원)씨는 ''사건 영상을 계속 보니 남의 일이 아닌 것 같아 "
                                        "무섭다''고 말했다. ''미친X은 어디에나 있고 지방도 예외는 "
                                        '아니죠. 누가 갑자기 사무실에 들어와서 칼로 찌를 것만 같아요. '
                                        "서울 강남구에 사는 25세 여성 직장인 이모 씨는 ''계속 영상을 "
                                        "보고 온갖 상상을 한다''며 ''강한 공포감''을 호소했습니다. "
                                        '작년 이태원 참사 당시에도 현장 사진과 동영상이 온라인에 공유되면서 '
                                        "문제가 됐습니다. 하지만 사진과 동영상에 대한 ''가이드라인''은 "
                                        '없습니다. 특히 숏폼 동영상은 사용자가 시청을 선택하지 않아도 자동 '
                                        '재생되어 사용자가 원하지 않아도 강제로 시청해야 하기 때문에 더욱 '
                                        "문제가 됩니다. 한 사용자는 ''이태원 참사 당시 현장 사진과 "
                                        "동영상이 많이 올라왔고, 한동안은 계속 올라올 것 같다''고 "
                                        "썼습니다. 백종우 경희대학교 정신건강의학과 교수는 ''보통 "
                                        '트라우마는 본인이 직접 경험하거나 가까운 가족에게 일어났을 때 '
                                        "경험한다''며 ''하지만 요즘은 사진이나 영상의 화질이 좋아지고 "
                                        '영상을 구하기 쉬워지면서 직접 심한 트라우마적 고통을 호소하는 '
                                        "사람들이 늘고 있다''고 말했다. 그는 ''사건 영상을 반복적으로 "
                                        "보게 되면 불안, 불면증과 같은 증상이 나타날 수 있다''고 "
                                        "말했습니다. ''나이가 어릴수록 더 큰 영향을 받습니다. ''나이가 "
                                        '어릴수록 더 큰 영향을 받습니다. 청소년에게 미치는 부정적인 영향은 '
                                        "더 크다''고 경고하며, ''영상이 유포되더라도 현행법상 처벌이 "
                                        "어려울 것으로 예상된다''고 말했다. 최진녕 법무법인 CK 변호사는 "
                                        "''이 사진과 영상은 현장을 알리기 위한 목적이 더 크다''고 "
                                        "말했다. ''성적 수치심이나 비방을 목적으로 하지 않는다면 사이버 "
                                        "명예훼손으로 처벌하기는 어렵다''고 말했습니다. 그는 온라인에서 "
                                        "끔찍한 장면이 유포되는 것에 대해 ''현재 진행형인 문제''라며 "
                                        "''형사처벌 여부 등 사회적 논의를 통해 입법화할 필요가 있다''고 "
                                        '말했다 이예솔 기자 ysolzz6@kukinews.com',
                                  qna_list=[QnA(question='칼부림 사건은 어디에서 발생했나요?',
                                                answer='칼부림 사건은 경기도 성남시 분당 서현역 '
                                                       '인근 대형 쇼핑몰에서 발생했습니다.'),
                                            QnA(question='서현역 흉기 난동 영상은 무엇을 '
                                                         '보여주나요?',
                                                answer='영상에는 용의자가 범죄 현장에서 칼을 '
                                                       '들고 돌아다니는 모습이 담겨 있었습니다.'),
                                            QnA(question='칼부림 사건 영상에 대한 시민들의 '
                                                         '반응은 어떤가요?',
                                                answer='시민들은 영상을 강제로 시청해야 하는 '
                                                       '불편함에 대해 불만을 토로하고 있으며, '
                                                       '일부 시민들은 잔인한 영상에 충격을 '
                                                       '받았다고 합니다.'),
                                            QnA(question='칼부림 사건의 사진 및 동영상과 '
                                                         '관련하여 우려되는 점은 무엇인가요?',
                                                answer='사진 및 동영상에 대한 가이드라인이 '
                                                       '없으며, 짧은 형식의 동영상은 사용자가 '
                                                       '시청을 선택하지 않아도 자동 재생되어 '
                                                       '고통과 트라우마를 유발할 수 있습니다.'),
                                            QnA(question='칼부림 사건 영상을 반복해서 시청하면 '
                                                         '어떤 영향을 미칠 수 있나요?',
                                                answer='영상을 반복적으로 시청하면 불안, '
                                                       '불면증과 같은 증상이 나타날 수 있으며, '
                                                       '특히 청소년과 같은 젊은 층에게 더 큰 '
                                                       '부정적인 영향을 미칠 수 있습니다.')],
                                  language='KO')],
         images=[ArticleImage(url='http://www.kukinews.com/data/kuk/image/2023/08/04/kuk202308040284.jpg',
                              source='쿠키뉴스'),
                 ArticleImage(url='https://cdn.pressian.com/_resources/10/2023/08/04/2023080409461486351_l.jpg',
                              source='프레시안')]),
 Article(category='Entertainment',
         keywords='안보현,지수 안보현,안보현 지수',
         contents=[ArticleContent(title="Blackpink's Jisoo and Ahn Bo Hyun "
                                        'Confirm Relationship: Impact on the '
                                        'K-pop Industry',
                                  lead='The K-pop industry is known to be very '
                                       'pressurized, with demanding fans and '
                                       'management companies trying to monitor '
                                       "every aspect of a singer's life, so "
                                       "BLACKPINK's admission of a "
                                       'relationship has shaken up the K-pop '
                                       'world.',
                                  body1="BLACKPINK's Jisoo and Ahn Bo Hyun "
                                        'have officially confirmed their '
                                        'relationship, sparking discussions '
                                        'about the impact it will have on the '
                                        'K-pop industry. Jisoo, the lead '
                                        'vocalist of the popular K-pop group '
                                        'BLACKPINK, and Ahn Bo Hyun, an actor '
                                        "known for his roles in 'Itaewon "
                                        "Class' and 'Yumi's Cell,' started "
                                        'dating on March 3.',
                                  body2='Their agencies confirmed the '
                                        "relationship, asking for fans' "
                                        'support and understanding. This '
                                        'public acknowledgment of a '
                                        'relationship by a member of BLACKPINK '
                                        'is unusual, as K-pop stars generally '
                                        'keep their personal lives private. It '
                                        'marks a significant change in the '
                                        "industry's approach to idol "
                                        'relationships.',
                                  qna_list=[QnA(question='Who is dating in '
                                                         'BLACKPINK?',
                                                answer='Jisoo, the lead '
                                                       'vocalist of BLACKPINK, '
                                                       'is dating Ahn Bo Hyun, '
                                                       'an actor known for his '
                                                       "roles in 'Itaewon "
                                                       "Class' and 'Yumi's "
                                                       "Cell.'"),
                                            QnA(question='When did Jisoo and '
                                                         'Ahn Bo Hyun start '
                                                         'dating?',
                                                answer='Jisoo and Ahn Bo Hyun '
                                                       'started dating on '
                                                       'March 3.'),
                                            QnA(question="Why is BLACKPINK's "
                                                         'admission of a '
                                                         'relationship '
                                                         'significant?',
                                                answer='The K-pop industry is '
                                                       'known for pressuring '
                                                       'its idols to keep '
                                                       'their personal lives '
                                                       'private. This public '
                                                       'acknowledgment of a '
                                                       'relationship by Jisoo '
                                                       'is unusual and marks a '
                                                       'change in the '
                                                       "industry's approach to "
                                                       'idol relationships.'),
                                            QnA(question='How have fans '
                                                         'reacted to the news?',
                                                answer='Fans have generally '
                                                       'reacted positively to '
                                                       'the news, showing '
                                                       'support and '
                                                       'congratulations to '
                                                       'Jisoo and Ahn Bo Hyun.'),
                                            QnA(question='Have other K-pop '
                                                         'idols openly '
                                                         'acknowledged their '
                                                         'relationships?',
                                                answer='While some members of '
                                                       'other popular K-pop '
                                                       'groups have publicly '
                                                       'acknowledged '
                                                       'relationships in '
                                                       'recent years, it is '
                                                       'still rare for K-pop '
                                                       'stars to discuss their '
                                                       'personal lives.')],
                                  language='EN-US'),
                   ArticleContent(title='Blackpink 的 Jisoo 和安宝贤确认恋爱关系：对 K-pop '
                                        '行业的影响',
                                  lead='众所周知，K-pop '
                                       '行业的压力非常大，要求苛刻的歌迷和经纪公司试图监控歌手生活的方方面面，因此 '
                                       'BLACKPINK 承认恋情一事震动了 K-pop 界。',
                                  body1='BLACKPINK 的 Jisoo 和 Ahn Bo Hyun '
                                        '正式确认了他们的恋情，引发了关于这将对 K-pop '
                                        '行业产生何种影响的讨论。K-pop 人气组合 BLACKPINK 的主唱 '
                                        "Jisoo 和因出演《梨泰院教室》和《Yumi''s "
                                        'Cell》而出名的演员安宝贤于 3 月 3 日开始交往。',
                                  body2='他们的经纪公司证实了这段恋情，并请求粉丝们的支持和理解。BLACKPINK '
                                        '成员公开承认恋情是不寻常的，因为 K-pop '
                                        '明星一般都不公开自己的私生活。这标志着业界对待偶像恋情的态度发生了重大变化。',
                                  qna_list=[QnA(question='BLACKPINK 的约会对象是谁？',
                                                answer='BLACKPINK 的主唱 Jisoo '
                                                       "正在与因出演《梨泰院教室》和《Yumi''s "
                                                       'Cell》而出名的演员安宝贤约会。'),
                                            QnA(question='Jisoo '
                                                         '和安宝贤是什么时候开始约会的？',
                                                answer='Jisoo 和安宝贤于 3 月 3 '
                                                       '日开始约会。'),
                                            QnA(question='为什么 BLACKPINK '
                                                         '承认恋情意义重大？',
                                                answer='众所周知，K-pop '
                                                       '行业对偶像施加压力，要求他们保持私生活隐私。Jisoo '
                                                       '这次公开承认恋情是不寻常的，标志着业界对偶像恋情态度的转变。'),
                                            QnA(question='粉丝们对这一消息有何反应？',
                                                answer='粉丝们对这一消息普遍反应积极，对 Jisoo '
                                                       '和安宝贤表示支持和祝贺。'),
                                            QnA(question='其他 K-pop '
                                                         '偶像艺人是否公开承认过自己的恋情？',
                                                answer='虽然近年来有一些其他流行 K-pop '
                                                       '团体的成员公开承认了恋情，但 K-pop '
                                                       '明星讨论自己私生活的情况仍然很少见。')],
                                  language='ZH'),
                   ArticleContent(title='블랙핑크 지수와 안보현, 열애 사실 확인: K팝 산업에 미치는 영향',
                                  lead='까다로운 팬과 매니지먼트사가 가수의 사생활까지 감시하는 등 압박이 '
                                       '심한 것으로 알려진 K팝 업계에서 블랙핑크의 열애 인정은 K팝계를 '
                                       '뒤흔들고 있습니다.',
                                  body1='블랙핑크의 지수와 안보현이 열애를 공식적으로 확인하면서 가요계에 '
                                        '미칠 영향에 대한 논의가 활발해지고 있습니다. 인기 K팝 그룹 '
                                        "블랙핑크의 리드보컬 지수와 ''이태원 클라쓰'', ''유미의 "
                                        "세포들'' 등으로 잘 알려진 배우 안보현이 지난 3월 3일부터 "
                                        '교제를 시작했다.',
                                  body2='두 사람의 소속사는 열애 사실을 확인하며 팬들의 응원과 이해를 '
                                        '부탁했습니다. 블랙핑크 멤버가 공개적으로 열애를 인정한 것은 케이팝 '
                                        '스타들이 일반적으로 사생활을 비공개로 유지하는 것과 비교하면 '
                                        '이례적인 일입니다. 이는 아이돌 연애에 대한 업계의 접근 방식에 '
                                        '중대한 변화를 의미합니다.',
                                  qna_list=[QnA(question='블랙핑크의 데이트 상대는 누구인가요?',
                                                answer="블랙핑크의 리드보컬 지수는 ''이태원 "
                                                       "클라쓰'', ''유미의 세포들'' 등으로 "
                                                       '유명한 배우 안보현과 열애 중입니다.'),
                                            QnA(question='지수와 안보현은 언제부터 사귀기 '
                                                         '시작했나요?',
                                                answer='지수와 안보현은 지난 3월 3일부터 '
                                                       '교제를 시작했습니다.'),
                                            QnA(question='블랙핑크의 열애 인정이 의미 있는 '
                                                         '이유는 무엇인가요?',
                                                answer='케이팝 업계는 아이돌에게 사생활을 '
                                                       '비공개로 유지하도록 압력을 가하는 것으로 '
                                                       '유명합니다. 지수가 공개적으로 열애를 '
                                                       '인정한 것은 이례적인 일이며, 아이돌 '
                                                       '연애에 대한 업계의 접근 방식에 변화가 '
                                                       '생겼음을 의미합니다.'),
                                            QnA(question='팬들은 이 소식에 어떤 반응을 '
                                                         '보였나요?',
                                                answer='팬들은 이 소식에 대체로 긍정적인 반응을 '
                                                       '보이며 지수와 안보현에게 응원과 축하를 '
                                                       '보냈습니다.'),
                                            QnA(question='다른 케이팝 아이돌이 공개적으로 '
                                                         '열애를 인정한 적이 있나요?',
                                                answer='최근 몇 년 동안 다른 인기 케이팝 '
                                                       '그룹의 일부 멤버들이 공개적으로 열애를 '
                                                       '인정한 바 있지만, 케이팝 스타가 '
                                                       '사생활에 대해 언급하는 경우는 여전히 '
                                                       '드뭅니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://ichef.bbci.co.uk/news/1024/branded_korean/083d/live/213f4c70-326b-11ee-9edf-f5e2f1f9bf2a.jpg',
                              source='BBC News 코리아'),
                 ArticleImage(url='https://newsimg-hams.hankookilbo.com/2023/08/04/35a04e0d-5e72-444d-8d3b-64784d69ccda.jpg?t=20230804150610',
                              source='한국일보')]),
 Article(category='Sports',
         keywords='PSG,전북 psg,파리생제르망 전북현대',
         contents=[ArticleContent(title="Neymar's Impressive Performance and "
                                        "PSG's Victory in Preseason Friendly "
                                        'Against Jeonbuk Hyundai',
                                  lead='In a preseason friendly match, Paris '
                                       'Saint-Germain (PSG) emerged victorious '
                                       'with a 3-0 win against Jeonbuk '
                                       "Hyundai. Neymar's outstanding "
                                       'performance, which included multiple '
                                       'goals and assists, caught the '
                                       'attention of fans and angered the '
                                       'Japanese team. Despite attempts by PSG '
                                       'to loan Neymar to Barcelona, the offer '
                                       'was rejected by Xavi.',
                                  body1='On Wednesday, PSG faced off against '
                                        'Jeonbuk Hyundai in the Coupang Play '
                                        'Series at the Asiad Stadium in Busan. '
                                        'The match ended with a convincing 3-0 '
                                        'victory for PSG. Neymar stood out '
                                        'during the game, demonstrating his '
                                        'skill and impact on the field. He not '
                                        'only scored multiple goals but also '
                                        'provided crucial assists, showcasing '
                                        'his versatility as an attacking '
                                        "player. However, Neymar's performance "
                                        'did not go unnoticed by the Japanese '
                                        'team. They expressed their '
                                        'frustration and accused PSG-Neymar of '
                                        'ignoring their country during the '
                                        'match.',
                                  body2='This sparked anger among Japanese '
                                        'fans and added an interesting subplot '
                                        'to the friendly encounter. In other '
                                        'news, PSG attempted to loan Neymar to '
                                        'Barcelona. However, their efforts '
                                        'were in vain as Xavi, the Barcelona '
                                        'coach, rejected the offer. This '
                                        "indicates that Neymar's future with "
                                        'PSG remains uncertain, with ongoing '
                                        'speculation about a potential '
                                        "transfer. Overall, PSG's victory "
                                        "against Jeonbuk Hyundai and Neymar's "
                                        'impressive performance in the '
                                        'preseason friendly have generated '
                                        'significant interest. The match not '
                                        "only showcased PSG's dominance on the "
                                        'field but also raised questions about '
                                        "Neymar's future and his relationship "
                                        'with the Japanese team.',
                                  qna_list=[QnA(question='Who won the '
                                                         'preseason friendly '
                                                         'match between PSG '
                                                         'and Jeonbuk Hyundai?',
                                                answer='PSG emerged victorious '
                                                       'with a 3-0 win against '
                                                       'Jeonbuk Hyundai.'),
                                            QnA(question="What did Neymar's "
                                                         'performance in the '
                                                         'match include?',
                                                answer='Neymar scored multiple '
                                                       'goals and provided '
                                                       'crucial assists.'),
                                            QnA(question='How did the Japanese '
                                                         'team react to '
                                                         "Neymar's "
                                                         'performance?',
                                                answer='The Japanese team '
                                                       'expressed their '
                                                       'frustration and '
                                                       'accused PSG-Neymar of '
                                                       'ignoring their country '
                                                       'during the match.'),
                                            QnA(question='Was PSG successful '
                                                         'in loaning Neymar to '
                                                         'Barcelona?',
                                                answer="No, PSG's attempt to "
                                                       'loan Neymar to '
                                                       'Barcelona was rejected '
                                                       'by Xavi, the Barcelona '
                                                       'coach.'),
                                            QnA(question="What does Neymar's "
                                                         'future with PSG look '
                                                         'like?',
                                                answer="Neymar's future with "
                                                       'PSG remains uncertain, '
                                                       'with ongoing '
                                                       'speculation about a '
                                                       'potential transfer.')],
                                  language='EN-US'),
                   ArticleContent(title='内马尔的精彩表现和 PSG 在季前友谊赛中对阵全北现代的胜利',
                                  lead='在一场季前友谊赛中，巴黎圣日耳曼（PSG）以 3-0 '
                                       '的比分战胜了全北现代。内马尔的出色表现，包括多个进球和助攻，引起了球迷的关注，也激怒了日本球队。尽管 '
                                       'PSG 曾试图将内马尔租借给巴塞罗那，但遭到哈维的拒绝。',
                                  body1='本周三，PSG 在釜山亚细亚体育场举行的 Coupang Play '
                                        '系列赛中对阵全北现代。比赛最终以 PSG 3-0 '
                                        '令人信服的胜利结束。内马尔在比赛中表现出色，展示了他的技术和影响力。他不仅打进了多个进球，还送出了关键助攻，展示了他作为一名进攻球员的多面性。然而，日本队并没有忽视内马尔的表现。他们表达了自己的不满，指责 '
                                        'PSG 内马尔在比赛中忽视了他们的国家。',
                                  body2='这引发了日本球迷的愤怒，也为这场友谊赛增添了一个有趣的小插曲。其他新闻方面，PSG '
                                        '试图将内马尔租借给巴塞罗那。然而，由于巴萨主教练哈维拒绝了这一邀请，他们的努力白费了。这表明内马尔在 '
                                        'PSG 的未来仍不明朗，关于潜在转会的猜测仍在继续。总体而言，PSG '
                                        '对阵全北现代的胜利以及内马尔在季前友谊赛中的出色表现引起了人们的极大兴趣。这场比赛不仅展示了 '
                                        'PSG '
                                        '在球场上的统治力，还引发了关于内马尔的未来以及他与日本球队关系的问题。',
                                  qna_list=[QnA(question='PSG '
                                                         '和全北现代之间的季前友谊赛谁赢了？',
                                                answer='PSG 以 3-0 的比分战胜全北现代。'),
                                            QnA(question='内马尔在比赛中的表现包括哪些方面？',
                                                answer='内马尔打入多个进球并送出关键助攻。'),
                                            QnA(question='日本队对内马尔的表现有何反应？',
                                                answer='日本队表达了他们的不满，并指责 '
                                                       'PSG-内马尔在比赛中无视他们的国家。'),
                                            QnA(question='PSG 将内马尔租借给巴塞罗那是否成功？',
                                                answer='不，PSG '
                                                       '将内马尔租借给巴塞罗那的尝试遭到了巴塞罗那主教练哈维的拒绝。'),
                                            QnA(question='内马尔在 PSG 的未来如何？',
                                                answer='内马尔在 PSG '
                                                       '的未来仍不明朗，有关其潜在转会的猜测不断。')],
                                  language='ZH'),
                   ArticleContent(title='네이마르의 인상적인 활약과 전북 현대와의 프리시즌 친선경기에서 '
                                        'PSG의 승리',
                                  lead='프리시즌 친선 경기에서 파리 생제르맹(PSG)이 전북 현대를 상대로 '
                                       '3-0 승리를 거두며 승승장구했습니다. 네이마르의 여러 골과 '
                                       '어시스트를 포함한 뛰어난 활약은 팬들의 관심을 끌었고 일본 팀을 '
                                       '분노하게 만들었습니다. PSG는 네이마르를 바르셀로나로 임대하려는 '
                                       '시도를 했지만, 사비의 제안은 거절당했습니다.',
                                  body1='수요일, 부산 아시아드 경기장에서 열린 쿠팡 플레이 시리즈에서 '
                                        'PSG와 전북 현대가 맞붙었습니다. 경기는 PSG의 3-0 완승으로 '
                                        '끝났습니다. 네이마르는 경기 내내 뛰어난 기량과 경기장에서의 '
                                        '영향력을 보여주며 두각을 나타냈습니다. 여러 골을 넣었을 뿐만 '
                                        '아니라 결정적인 어시스트를 기록하며 공격수로서의 다재다능함을 '
                                        '보여주었습니다. 하지만 네이마르의 활약에 일본 대표팀도 주목하지 '
                                        '않을 수 없었습니다. 그들은 불만을 표출하며 경기 도중 '
                                        'PSG-네이마르가 자국을 무시했다고 비난했습니다.',
                                  body2='이는 일본 팬들의 분노를 불러일으켰고 친선경기에 흥미로운 서브 '
                                        '플롯을 추가했습니다. 다른 소식으로 PSG는 네이마르를 바르셀로나로 '
                                        '임대하려고 시도했습니다. 그러나 바르셀로나의 감독인 사비가 제안을 '
                                        '거절하면서 그들의 노력은 헛수고가 되고 말았습니다. 이는 네이마르의 '
                                        'PSG에서의 미래가 여전히 불확실하다는 것을 나타내며, 이적 '
                                        '가능성에 대한 추측이 계속되고 있습니다. 전반적으로 PSG의 전북 '
                                        '현대전 승리와 네이마르의 프리시즌 친선경기에서의 인상적인 활약은 큰 '
                                        '관심을 불러 일으켰습니다. 이 경기는 PSG의 압도적인 경기력을 '
                                        '보여줬을 뿐만 아니라 네이마르의 미래와 일본 팀과의 관계에 대한 '
                                        '의문도 제기했습니다.',
                                  qna_list=[QnA(question='PSG와 전북 현대의 프리시즌 친선 '
                                                         '경기는 누가 이겼나요?',
                                                answer='PSG가 전북 현대를 상대로 3-0 '
                                                       '승리를 거두며 승승장구했습니다.'),
                                            QnA(question='경기 중 네이마르의 활약은 어땠나요?',
                                                answer='네이마르는 여러 골을 넣었고 결정적인 '
                                                       '어시스트를 제공했습니다.'),
                                            QnA(question='네이마르의 활약에 일본 대표팀은 어떤 '
                                                         '반응을 보였나요?',
                                                answer='일본 대표팀은 경기 도중 '
                                                       'PSG-네이마르가 자국을 무시했다고 '
                                                       '비난하며 불만을 표출했습니다.'),
                                            QnA(question='PSG는 네이마르를 바르셀로나로 '
                                                         '임대하는 데 성공했나요?',
                                                answer='아니요, PSG의 네이마르 임대 시도는 '
                                                       '바르셀로나의 감독인 사비에 의해 '
                                                       '거부되었습니다.'),
                                            QnA(question='네이마르의 PSG에서의 미래는 어떤 '
                                                         '모습일까요?',
                                                answer='네이마르의 PSG에서의 미래는 여전히 '
                                                       '불확실하며, 이적 가능성에 대한 추측이 '
                                                       '계속되고 있습니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://images.chosun.com/resizer/NjE8TdcnZKUnaVQMez997xJ9LQ8=/650x341/filters:focal(326x22:336x32)/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/IP2QLTORFOYOPVHNIRGD7ECB7Q.jpg',
                              source='조선일보'),
                 ArticleImage(url='https://biz.chosun.com/resizer/Mh9kzVU2BBM4y7ocFNdq1nzPHp4=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/57DV7MBQH4KDA2AACVIVDBLSHU.jpg',
                              source='조선비즈')]),
 Article(category='Science',
         keywords='운석',
         contents=[ArticleContent(title='Ancient Tools Made from Meteorites: '
                                        'Pre-Iron Age Wonders',
                                  lead='Even before the Iron Age, tools could '
                                       'be made from iron obtained from '
                                       'meteorites. Scientists are studying '
                                       'ancient tools made from '
                                       'extraterrestrial materials.',
                                  body1='Even before the Iron Age, tools could '
                                        'be made from iron. Smelting '
                                        'technology was immature, but iron '
                                        'could be obtained from meteorites. '
                                        'Rocks from space contain metals like '
                                        'nickel and silicates, and scientists '
                                        'are studying ancient tools made from '
                                        'extraterrestrial materials. The art '
                                        'of working with iron began to emerge '
                                        'during the Late Bronze Age. It is '
                                        'believed to have originated in '
                                        'ancient Anatolia between 1200 and '
                                        '1000 B.C. However, an iron arrowhead '
                                        'held by the Museum of History in '
                                        'Bern, Switzerland, is older than the '
                                        'Iron Age. Scholars believe it is a '
                                        'weapon made from a meteorite. '
                                        'According to the Bern History Museum, '
                                        'there are only 55 archaeological '
                                        'artifacts in the world that are made '
                                        'from meteorites. A recent paper '
                                        'published in the Journal of '
                                        'Archaeological Sciences detailed the '
                                        'arrowhead. The object is 1.5 inches '
                                        'long and weighs 2.9 grams and was '
                                        'excavated in the 19th century. It '
                                        'came from Mörigen, a lake settlement '
                                        'where people were active during the '
                                        'Late Bronze Age. It is five miles '
                                        'from the location where the Meteorite '
                                        'of Twanberg struck the Earth 150,000 '
                                        'years ago. The meteorite was once '
                                        'speculated to be the source of the '
                                        'arrowheads, but research has shown '
                                        'that the mineral could not have been '
                                        'used by ancient people.',
                                  body2='We have yet to detect any Twanberg '
                                        'meteorite components in arrowheads or '
                                        'other artifacts. The arrowhead '
                                        'contains 8.3% nickel, twice as much '
                                        'as the meteorite. According to the '
                                        'researchers, the arrowhead has a low '
                                        'aluminum-26 concentration and a high '
                                        'percentage of geranium. These values '
                                        'raise the possibility that the parent '
                                        'material is an IAB type meteorite. An '
                                        'IAB-type meteorite is one that is '
                                        'composed of metal. It is estimated to '
                                        'have a mass of at least two tons. So '
                                        'far, only three meteorites have '
                                        'fallen in Europe with these '
                                        'characteristics. The authors of the '
                                        'paper claim that the Kaaliyarv '
                                        'meteorite provided the material for '
                                        'the arrowhead. This meteorite created '
                                        'a huge crater on the Estonian island '
                                        'of Saaremaa around 1500 BC. The '
                                        'impact point created a hole through '
                                        'modern-day Poland, Lithuania, and '
                                        'Latvia. As a result, countless pieces '
                                        'of iron meteorite were scattered. The '
                                        'scholars conclude that a trade and '
                                        'transportation system for iron may '
                                        'have existed at the time. They look '
                                        'forward to finding other ancient '
                                        'tools made from space rocks in the '
                                        'future.',
                                  qna_list=[QnA(question='Where did the iron '
                                                         'arrowhead come from?',
                                                answer='The iron arrowhead was '
                                                       'excavated in Mörigen, '
                                                       'a lake settlement '
                                                       'where people were '
                                                       'active during the Late '
                                                       'Bronze Age.'),
                                            QnA(question='What is the '
                                                         'composition of the '
                                                         'arrowhead?',
                                                answer='The arrowhead contains '
                                                       '8.3% nickel, twice as '
                                                       'much as the meteorite, '
                                                       'and has a low '
                                                       'aluminum-26 '
                                                       'concentration and a '
                                                       'high percentage of '
                                                       'geranium.'),
                                            QnA(question='How many meteorite '
                                                         'artifacts are made '
                                                         'from meteorites?',
                                                answer='According to the Bern '
                                                       'History Museum, there '
                                                       'are only 55 '
                                                       'archaeological '
                                                       'artifacts in the world '
                                                       'that are made from '
                                                       'meteorites.'),
                                            QnA(question='What type of '
                                                         'meteorite is the '
                                                         'arrowhead believed '
                                                         'to be made from?',
                                                answer='The arrowhead is '
                                                       'believed to be made '
                                                       'from an IAB type '
                                                       'meteorite, which is '
                                                       'composed of metal.'),
                                            QnA(question='Where did the '
                                                         'material for the '
                                                         'arrowhead come from?',
                                                answer='The authors of the '
                                                       'paper claim that the '
                                                       'material for the '
                                                       'arrowhead came from '
                                                       'the Kaaliyarv '
                                                       'meteorite, which '
                                                       'created a huge crater '
                                                       'on the Estonian island '
                                                       'of Saaremaa around '
                                                       '1500 BC.')],
                                  language='EN-US'),
                   ArticleContent(title='陨石制成的古代工具：铁器时代以前的奇迹',
                                  lead='甚至在铁器时代之前，人们就可以用从陨石中获取的铁制造工具。科学家们正在研究由地外材料制成的古代工具。',
                                  body1='甚至在铁器时代之前，人们就可以用铁制造工具。当时的冶炼技术还不成熟，但可以从陨石中获得铁。来自太空的岩石中含有镍和硅酸盐等金属，科学家们正在研究由地外材料制成的古代工具。青铜时代晚期开始出现用铁加工的艺术。不过，瑞士伯尔尼历史博物馆收藏的一枚铁箭头的历史比铁器时代还要久远。学者们认为它是用陨石制成的武器。据伯尔尼历史博物馆称，世界上仅有 '
                                        '55 '
                                        '件考古文物是由陨石制成的。最近发表在《考古科学杂志》上的一篇论文详细介绍了这个箭头。该物品长 '
                                        '1.5 英寸，重 2.9 克，出土于 19 '
                                        '世纪。它来自莫里根（Mörigen），这里是青铜时代晚期人们活跃的湖边定居点。它距离 '
                                        '15 万年前特旺贝格陨石撞击地球的地点 5 '
                                        '英里。人们曾一度猜测这块陨石是箭头的来源，但研究表明，古人不可能使用这种矿物。',
                                  body2='我们尚未在箭头或其他人工制品中发现任何特旺贝格陨石成分。箭头含有 8.3% '
                                        '的镍，是陨石的两倍。据研究人员称，箭头的铝-26 '
                                        '浓度较低，天竺葵的比例较高。这些数值提高了母体材料是 IAB '
                                        '型陨石的可能性。IAB '
                                        '型陨石是由金属组成的陨石。据估计，它的质量至少有两吨。迄今为止，只有三块陨石坠落在欧洲并具有这些特征。论文作者称，卡利亚里耶夫陨石为箭头提供了材料。这块陨石于公元前 '
                                        '1500 '
                                        '年左右在爱沙尼亚的萨雷马岛上形成了一个巨大的陨石坑。撞击点造成了一个贯穿现代波兰、立陶宛和拉脱维亚的洞。结果，无数铁陨石碎片散落一地。学者们得出结论，当时可能存在铁的贸易和运输系统。他们期待着在未来找到其他由太空岩石制成的古代工具。',
                                  qna_list=[QnA(question='铁箭头从何而来？',
                                                answer='这枚铁箭头是在莫里根（Mörigen）发掘出来的，莫里根是青铜时代晚期的一个湖边定居点，那里的人们非常活跃。'),
                                            QnA(question='箭头的成分是什么？',
                                                answer='箭头的镍含量为 '
                                                       '8.3%，是陨石的两倍，铝-26 '
                                                       '浓度较低，天竺葵含量较高。'),
                                            QnA(question='有多少陨石文物是由陨石制成的？',
                                                answer='据伯尔尼历史博物馆称，世界上仅有 55 '
                                                       '件考古文物是由陨石制成的。'),
                                            QnA(question='据说箭头是用哪种陨石制成的？',
                                                answer='箭头据信是由 IAB '
                                                       '型陨石制成的，这种陨石由金属组成。'),
                                            QnA(question='箭头的材料从何而来？',
                                                answer='论文作者称，箭镞的材料来自 '
                                                       'Kaaliyarv 陨石，该陨石于公元前 '
                                                       '1500 '
                                                       '年左右在爱沙尼亚萨雷马岛上形成了一个巨大的陨石坑。')],
                                  language='ZH'),
                   ArticleContent(title='운석으로 만든 고대 도구: 철기 시대 이전의 불가사의',
                                  lead='철기 시대 이전에도 운석에서 얻은 철로 도구를 만들 수 있었습니다. '
                                       '과학자들은 외계 물질로 만든 고대 도구를 연구하고 있습니다.',
                                  body1='철기 시대 이전에도 철로 도구를 만들 수 있었습니다. 제련 기술은 '
                                        '미숙했지만 운석에서 철을 얻을 수 있었습니다. 우주에서 온 암석에는 '
                                        '니켈과 규산염과 같은 금속이 포함되어 있으며 과학자들은 외계 물질로 '
                                        '만든 고대 도구를 연구하고 있습니다. 철로 작업하는 기술은 청동기 '
                                        '후기 시대에 등장하기 시작했습니다. 기원전 1200년에서 1000년 '
                                        '사이에 고대 아나톨리아에서 시작된 것으로 여겨지지만, 스위스 베른 '
                                        '역사 박물관이 소장하고 있는 철제 화살촉은 철기 시대보다 더 오래된 '
                                        '것입니다. 학자들은 이 화살촉이 운석으로 만들어진 무기라고 '
                                        '믿습니다. 베른 역사 박물관에 따르면 운석으로 만들어진 고고학적 '
                                        '유물은 전 세계에 55개밖에 없다고 합니다. 최근 고고학 과학 '
                                        '저널에 발표된 논문에서 이 화살촉에 대해 자세히 설명했습니다. 이 '
                                        '유물은 길이 1.5인치, 무게 2.9그램으로 19세기에 출토된 '
                                        '것입니다. 이 화살촉은 후기 청동기 시대에 사람들이 활동했던 호수 '
                                        '정착지 뫼리겐에서 나왔어요. 이곳은 15만 년 전 트완베르크 운석이 '
                                        '지구에 떨어진 곳에서 5마일 떨어진 곳입니다. 한때 이 운석이 '
                                        '화살촉의 출처로 추측되기도 했지만, 연구 결과 고대인들이 이 광물을 '
                                        '사용할 수 없었던 것으로 밝혀졌습니다.',
                                  body2='화살촉이나 다른 유물에서 트완버그 운석 성분은 아직 발견되지 '
                                        '않았습니다. 화살촉에는 운석보다 두 배나 많은 8.3%의 니켈이 '
                                        '함유되어 있습니다. 연구진에 따르면 화살촉은 알루미늄-26 농도가 '
                                        '낮고 제라늄의 비율이 높다고 합니다. 이러한 수치는 모물질이 '
                                        'IAB형 운석일 가능성을 높입니다. IAB형 운석은 금속으로 구성된 '
                                        '운석입니다. 최소 2톤 이상의 질량을 가진 것으로 추정됩니다. '
                                        '지금까지 이러한 특성을 가진 운석이 유럽에 떨어진 것은 단 세 '
                                        '개뿐입니다. 논문 저자들은 칼리야르브 운석이 화살촉의 재료를 '
                                        '제공했다고 주장합니다. 이 운석은 기원전 1500년경 에스토니아의 '
                                        '사레마 섬에 거대한 분화구를 만들었습니다. 이 충돌 지점은 오늘날의 '
                                        '폴란드, 리투아니아, 라트비아를 관통하는 구멍을 만들었습니다. 그 '
                                        '결과 수많은 철 운석 조각이 흩어졌습니다. 학자들은 당시 철에 대한 '
                                        '무역 및 운송 시스템이 존재했을 수 있다고 결론지었습니다. 그들은 '
                                        '앞으로 우주 암석으로 만든 다른 고대 도구를 발견할 수 있기를 '
                                        '기대합니다.',
                                  qna_list=[QnA(question='철제 화살촉의 출처는 어디인가요?',
                                                answer='이 철제 화살촉은 후기 청동기 시대에 '
                                                       '사람들이 활동했던 호수 정착지 뫼리겐에서 '
                                                       '출토되었습니다.'),
                                            QnA(question='화살촉의 구성은 어떻게 되나요?',
                                                answer='화살촉에는 운석보다 두 배나 많은 '
                                                       '8.3%의 니켈이 함유되어 있으며, '
                                                       '알루미늄-26 농도가 낮고 제라늄의 '
                                                       '비율이 높습니다.'),
                                            QnA(question='운석으로 만든 운석 유물은 몇 개나 '
                                                         '되나요?',
                                                answer='베른 역사 박물관에 따르면 운석으로 '
                                                       '만들어진 고고학적 유물은 전 세계에 '
                                                       '55개밖에 없다고 해요.'),
                                            QnA(question='화살촉은 어떤 종류의 운석으로 '
                                                         '만들어진 것으로 추정되나요?',
                                                answer='화살촉은 금속으로 구성된 IAB형 '
                                                       '운석으로 만들어진 것으로 추정됩니다.'),
                                            QnA(question='화살촉의 재료는 어디에서 왔나요?',
                                                answer='이 논문의 저자는 화살촉의 재료가 기원전 '
                                                       '1500년경 에스토니아 사레마 섬에 '
                                                       '거대한 분화구를 만든 카알리야르브 '
                                                       '운석에서 나왔다고 주장합니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://cdn.popsci.co.kr/news/thumbnail/202308/21075_11258_547_v150.jpg',
                              source='파퓰러사이언스')]),
 Article(category='Sports',
         keywords='김민재',
         contents=[ArticleContent(title='Kim Min-jae joins Bayern Munich and '
                                        'impresses in preseason friendly',
                                  lead='Kim Min-jae has made a strong start at '
                                       'Bayern Munich, contributing to their '
                                       '4-3 victory over Liverpool in a '
                                       'preseason friendly. The South Korean '
                                       'center-back showcased his attacking '
                                       'prowess with an assist and displayed '
                                       "solid defensive skills. Kim's "
                                       'performance has garnered praise from '
                                       'both his manager, Thomas Tuchel, and '
                                       'Liverpool manager Jurgen Klopp.',
                                  body1='Kim Min-jae has made an immediate '
                                        'impact since joining Bayern Munich. '
                                        'In a preseason friendly against '
                                        'Liverpool, the South Korean '
                                        'center-back played a key role in his '
                                        "team's 4-3 victory. Kim demonstrated "
                                        'his attacking abilities by providing '
                                        "an assist for Serge Gnabry's goal, "
                                        'which helped Munich turn the game '
                                        'around.',
                                  body2='His defensive contributions were also '
                                        'noteworthy, making one tackle, one '
                                        'clearance, and winning two aerial '
                                        "battles. Kim's strong performance "
                                        'earned him a rating of 7.4 from '
                                        'Sofascore, the second-highest among '
                                        'Munich players. His impressive '
                                        'display did not go unnoticed by both '
                                        'his manager, Thomas Tuchel, and '
                                        'Liverpool manager Jurgen Klopp. '
                                        'Tuchel expressed his satisfaction '
                                        "with Kim and the team's center-back "
                                        "depth, while Klopp praised Kim's "
                                        'sharp and unstoppable passes.',
                                  qna_list=[QnA(question='What was Kim '
                                                         "Min-jae's "
                                                         'contribution in '
                                                         "Bayern Munich's "
                                                         'preseason friendly '
                                                         'against Liverpool?',
                                                answer='Kim Min-jae provided '
                                                       'an assist for Serge '
                                                       "Gnabry's goal, helping "
                                                       'Bayern Munich come '
                                                       'from behind to win the '
                                                       'game.'),
                                            QnA(question='How did Kim Min-jae '
                                                         'perform defensively '
                                                         'in the game against '
                                                         'Liverpool?',
                                                answer='Kim Min-jae made one '
                                                       'tackle, one clearance, '
                                                       'and won two aerial '
                                                       'battles, showcasing '
                                                       'his defensive skills.'),
                                            QnA(question='What was Kim '
                                                         "Min-jae's rating in "
                                                         'the game according '
                                                         'to Sofascore?',
                                                answer='Kim Min-jae received a '
                                                       'rating of 7.4 from '
                                                       'Sofascore, the '
                                                       'second-highest among '
                                                       'Bayern Munich players.'),
                                            QnA(question='What did Thomas '
                                                         'Tuchel say about Kim '
                                                         "Min-jae's "
                                                         'performance?',
                                                answer='Thomas Tuchel '
                                                       'expressed his '
                                                       'satisfaction with Kim '
                                                       "Min-jae's performance "
                                                       "and the team's "
                                                       'center-back depth.'),
                                            QnA(question='How did Jurgen Klopp '
                                                         'praise Kim Min-jae?',
                                                answer='Jurgen Klopp described '
                                                       "Kim Min-jae's passes "
                                                       'as sharp and '
                                                       'unstoppable.')],
                                  language='EN-US'),
                   ArticleContent(title='金敏在加盟拜仁慕尼黑并在季前友谊赛中给人留下深刻印象',
                                  lead='金敏在在拜仁慕尼黑的开局表现出色，在季前友谊赛中以 4-3 '
                                       '的比分战胜利物浦。这位韩国中后卫在比赛中助攻一次，展示了自己的进攻能力，并展现了稳健的防守技巧。金明训的表现获得了他的主教练托马斯-图赫尔和利物浦主教练尤尔根-克洛普的一致好评。',
                                  body1='自加盟拜仁慕尼黑以来，金民宰（Kim '
                                        'Min-jae）立竿见影。在对阵利物浦的季前友谊赛中，这位韩国中后卫在球队 '
                                        '4-3 的胜利中发挥了关键作用。金敏在为格纳布里（Serge '
                                        'Gnabry）的进球送上助攻，帮助慕尼黑逆转比赛，展示了自己的进攻能力。',
                                  body2='他在防守方面的贡献也很突出，一次擒抱，一次解围，赢得了两次空中对抗。金的出色表现为他赢得了 '
                                        'Sofascore 7.4 '
                                        '分的高分，在慕尼黑球员中排名第二。他的出色表现也得到了他的主教练托马斯-图赫尔和利物浦主教练尤尔根-克洛普的关注。图赫尔对金和球队的中后卫深度表示满意，而克洛普则称赞金的传球犀利、势不可挡。',
                                  qna_list=[QnA(question='在拜仁慕尼黑对阵利物浦的季前友谊赛中，金敏在做出了怎样的贡献？',
                                                answer='金敏在助攻格纳布里（Serge '
                                                       'Gnabry）进球，帮助拜仁慕尼黑在落后的情况下赢得比赛。'),
                                            QnA(question='在对阵利物浦的比赛中，金敏在的防守表现如何？',
                                                answer='Kim Min-jae '
                                                       '一次擒抱，一次解围，赢得了两次空中对抗，展示了他的防守技巧。'),
                                            QnA(question='根据 Sofascore 的数据，Kim '
                                                         'Min-jae 在比赛中的评分是多少？',
                                                answer='金敏在获得了 Sofascore 7.4 '
                                                       '分的高分，在拜仁慕尼黑球员中排名第二。'),
                                            QnA(question='托马斯-图赫尔如何评价金敏在的表现？',
                                                answer='托马斯-图赫尔对金敏在的表现和球队的中后卫深度表示满意。'),
                                            QnA(question='克洛普是如何称赞金敏在的？',
                                                answer='克洛普（Jurgen '
                                                       'Klopp）形容金敏在的传球非常犀利，势不可挡。')],
                                  language='ZH'),
                   ArticleContent(title='김민재, 바이에른 뮌헨에 입단해 프리시즌 친선경기에서 인상적인 '
                                        '활약을 펼쳤습니다.',
                                  lead='김민재는 바이에른 뮌헨에서 프리시즌 친선 경기에서 리버풀을 상대로 '
                                       '4-3 승리를 거두는 데 기여하며 강렬한 출발을 알렸습니다. 이 한국 '
                                       '센터백은 어시스트를 기록하며 공격력을 뽐냈고, 탄탄한 수비력도 '
                                       '선보였습니다. 김연경의 활약은 토마스 투헬 감독과 리버풀의 위르겐 '
                                       '클롭 감독 모두로부터 찬사를 받았습니다.',
                                  body1='김민재는 바이에른 뮌헨에 입단한 이후 즉각적인 영향력을 '
                                        '발휘했습니다. 리버풀과의 프리시즌 친선 경기에서 이 한국 센터백은 '
                                        '팀의 4-3 승리에 핵심적인 역할을 했습니다. 김민재는 세르주 '
                                        '그나브리의 골을 어시스트하며 자신의 공격 능력을 입증했고, 뮌헨이 '
                                        '경기를 뒤집는 데 큰 역할을 했습니다.',
                                  body2='태클 1건, 클리어링 1건, 공중볼 경합에서 2승을 거두는 등 '
                                        '수비적인 기여도도 주목할 만했습니다. 이러한 활약으로 김연경은 '
                                        '소파스코어에서 뮌헨 선수 중 두 번째로 높은 평점 7.4점을 '
                                        '받았습니다. 그의 인상적인 활약은 토마스 투헬 감독과 리버풀의 '
                                        '위르겐 클롭 감독 모두 주목하지 않을 수 없었습니다. 투헬 감독은 '
                                        '김연경과 팀의 센터백 깊이에 만족감을 드러냈고, 클롭 감독은 '
                                        '김연경의 날카롭고 거침없는 패스에 찬사를 보냈습니다.',
                                  qna_list=[QnA(question='바이에른 뮌헨과 리버풀의 프리시즌 '
                                                         '친선경기에서 김민재의 활약은 '
                                                         '어땠나요?',
                                                answer='김민재는 세르주 그나브리의 골을 '
                                                       '어시스트하며 바이에른 뮌헨이 역전승을 '
                                                       '거두는 데 일조했습니다.'),
                                            QnA(question='김민재는 리버풀과의 경기에서 '
                                                         '수비적으로 어떤 활약을 펼쳤나요?',
                                                answer='김민재는 태클 1개, 클리어링 1개를 '
                                                       '기록했고 공중볼 경합에서 2개를 따내며 '
                                                       '수비력을 뽐냈습니다.'),
                                            QnA(question='소파스코어에 따르면 김민재의 경기 '
                                                         '평점은 어느 정도였나요?',
                                                answer='김민재는 소파스코어에서 7.4점을 받아 '
                                                       '바이에른 뮌헨 선수 중 두 번째로 높은 '
                                                       '평점을 받았습니다.'),
                                            QnA(question='토마스 투헬은 김민재의 연기에 대해 '
                                                         '뭐라고 말했나요?',
                                                answer='토마스 투헬 감독은 김민재의 활약과 팀의 '
                                                       '센터백 깊이에 대해 만족감을 '
                                                       '드러냈습니다.'),
                                            QnA(question='위르겐 클롭 감독은 김민재를 어떻게 '
                                                         '칭찬했을까요?',
                                                answer='위르겐 클롭 감독은 김민재의 패스를 '
                                                       '날카롭고 멈출 수 없는 패스라고 '
                                                       '표현했습니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://thumb.mt.co.kr/21/2023/08/2023080323275287102_1.jpg',
                              source='머니투데이'),
                 ArticleImage(url='https://cdn.fourfourtwo.co.kr/news/thumbnail/202308/38643_87925_4136_v150.jpg',
                              source='포포투')]),
 Article(category='Politics',
         keywords='중국',
         contents=[ArticleContent(title="Southeast Asia's View on US-China "
                                        'Relations and the Importance of '
                                        'Trilateral Cooperation',
                                  lead='The US-China relationship has been a '
                                       'topic of concern in Southeast Asia, '
                                       'with many seeing the US as provocative '
                                       'and demonizing China. Southeast Asian '
                                       'countries emphasize the importance of '
                                       'maintaining a neutral stance and '
                                       'benefiting from both superpowers. '
                                       'Trilateral cooperation between the US, '
                                       'South Korea, and Japan is also seen as '
                                       "crucial in dealing with China's "
                                       'growing aggression.',
                                  body1='The US-China relationship has been a '
                                        'subject of discussion and concern in '
                                        'Southeast Asia. Many countries in the '
                                        'region view the US as provocative and '
                                        'believe that the trend is towards '
                                        'demonizing China. Instead, they '
                                        'emphasize the importance of '
                                        'maintaining a neutral stance and '
                                        'benefiting from both superpowers. '
                                        'Unlike South Korea, which has taken a '
                                        'more activist role against China, '
                                        'Southeast Asian countries, '
                                        'particularly those associated with '
                                        'the Association of Southeast Asian '
                                        'Nations (ASEAN), have shown that the '
                                        "US administration's policy of "
                                        'containment and pressure is not '
                                        'effective in winning their hearts and '
                                        'minds. They see the US strategy of '
                                        'dividing the world into democracies '
                                        'and autocracies and narrowing the '
                                        'circle of public support through the '
                                        'Indo-Pacific strategy as reflecting a '
                                        'new Cold War. The Asia Society, a New '
                                        'York-based nonprofit organization, '
                                        'has published a report titled '
                                        "'Southeast Asia Should Be Prioritized "
                                        "in U.S. Public Policy.' The report "
                                        'highlights the importance of '
                                        'Southeast Asia and its undervalued '
                                        'position in US interests and public '
                                        'rivalries. It recommends policy '
                                        'changes to the US government and '
                                        "calls for a response to China's "
                                        'growing influence in the region. '
                                        'Southeast Asia is the geopolitical '
                                        'heart of the Indo-Pacific region, '
                                        'with vital trade arteries and '
                                        'strategic importance.',
                                  body2='However, the region is wary of being '
                                        'drawn into the US-China rivalry and '
                                        'sees the US as overreacting in its '
                                        'containment efforts. They do not '
                                        "adopt the US-proposed 'free and open' "
                                        'Indo-Pacific strategy as they '
                                        'perceive it as forcing the region '
                                        'into a geopolitical framework. '
                                        'Trilateral cooperation between the '
                                        'US, South Korea, and Japan is seen as '
                                        "critical in dealing with China's "
                                        'increasing aggression. Congressman '
                                        'French Hill emphasized the importance '
                                        'of this cooperation in maintaining '
                                        'economic prosperity and promoting '
                                        'freedom in the Indo-Pacific region. '
                                        'The three countries need to work '
                                        'together to ensure the freedom of '
                                        "trade and navigation, counter China's "
                                        'neocolonial Belt and Road strategy, '
                                        'and uphold peace and prosperity in '
                                        'the region and around the world. The '
                                        'upcoming trilateral summit between '
                                        'the US, South Korea, and Japan '
                                        'demonstrates the commitment to '
                                        'stronger collaboration and marks an '
                                        'important step towards addressing the '
                                        "challenges posed by China's "
                                        'assertiveness. In conclusion, '
                                        "Southeast Asia's view on US-China "
                                        'relations underscores the desire for '
                                        'a neutral stance and the importance '
                                        'of benefiting from both superpowers. '
                                        'Trilateral cooperation between the '
                                        'US, South Korea, and Japan is also '
                                        "seen as crucial in managing China's "
                                        'growing aggression. As the region '
                                        'navigates the complex dynamics '
                                        'between the US and China, maintaining '
                                        'a balanced approach and fostering '
                                        'multilateral partnerships will be key '
                                        'to ensuring peace and prosperity.',
                                  qna_list=[QnA(question='How does Southeast '
                                                         'Asia view the '
                                                         'US-China '
                                                         'relationship?',
                                                answer='Many countries in '
                                                       'Southeast Asia view '
                                                       'the US as provocative '
                                                       'and believe the trend '
                                                       'is towards demonizing '
                                                       'China. They emphasize '
                                                       'neutrality and aim to '
                                                       'benefit from both '
                                                       'superpowers.'),
                                            QnA(question='What do Southeast '
                                                         'Asian countries '
                                                         'think of the US '
                                                         'policy of '
                                                         'containment and '
                                                         'pressure against '
                                                         'China?',
                                                answer='Southeast Asian '
                                                       'countries, especially '
                                                       'ASEAN members, do not '
                                                       'believe that the US '
                                                       'policy of containment '
                                                       'and pressure is '
                                                       'effective. They see it '
                                                       'as reflecting a new '
                                                       'Cold War and are not '
                                                       'swayed by such '
                                                       'efforts.'),
                                            QnA(question='What is the '
                                                         'importance of '
                                                         'Southeast Asia '
                                                         'according to the '
                                                         'Asia Society report?',
                                                answer='The Asia Society '
                                                       'report highlights the '
                                                       'importance of '
                                                       'Southeast Asia, which '
                                                       'is often undervalued '
                                                       'in US interests and '
                                                       'public rivalries. It '
                                                       'recommends policy '
                                                       'changes and calls for '
                                                       "a response to China's "
                                                       'growing influence in '
                                                       'the region.'),
                                            QnA(question='Why does Southeast '
                                                         'Asia not adopt the '
                                                         "US-proposed 'free "
                                                         "and open' "
                                                         'Indo-Pacific '
                                                         'strategy?',
                                                answer='Southeast Asia sees '
                                                       'the US-proposed '
                                                       'strategy as a way to '
                                                       'force the region into '
                                                       'a geopolitical '
                                                       'framework. They '
                                                       'believe it does not '
                                                       'align with their '
                                                       'interests and goals.'),
                                            QnA(question='What is the '
                                                         'significance of '
                                                         'trilateral '
                                                         'cooperation between '
                                                         'the US, South Korea, '
                                                         'and Japan?',
                                                answer='Trilateral cooperation '
                                                       'between the US, South '
                                                       'Korea, and Japan is '
                                                       'seen as critical in '
                                                       "dealing with China's "
                                                       'increasing aggression. '
                                                       'It aims to ensure '
                                                       'freedom of trade and '
                                                       'navigation, counter '
                                                       "China's Belt and Road "
                                                       'strategy, and uphold '
                                                       'peace and prosperity '
                                                       'in the Indo-Pacific.')],
                                  language='EN-US'),
                   ArticleContent(title='东南亚对中美关系的看法及三边合作的重要性',
                                  lead='中美关系一直是东南亚关注的话题，许多人认为美国具有挑衅性，并将中国妖魔化。东南亚国家强调保持中立立场并从两个超级大国中获益的重要性。美国、韩国和日本之间的三边合作也被视为应对中国日益增长的侵略性的关键。',
                                  body1='中美关系一直是东南亚讨论和关注的话题。该地区许多国家认为美国具有挑衅性，并认为将中国妖魔化是大势所趋。相反，他们强调保持中立立场并从两个超级大国中获益的重要性。东南亚国家，尤其是与东南亚国家联盟（ASEAN）有联系的国家，已经表明美国政府的遏制和施压政策并不能有效地赢得他们的民心，这一点与韩国不同，韩国对中国采取了更加积极的态度。他们认为，美国将世界分为民主国家和专制国家，并通过印太战略缩小公众支持圈的战略反映了新冷战。总部位于纽约的非营利组织亚洲协会发表了一份题为《美国公共政策应优先考虑东南亚》的报告。报告强调了东南亚的重要性及其在美国利益和公共竞争中被低估的地位。报告建议美国政府改变政策，并呼吁应对中国在该地区日益增长的影响力。东南亚是印度-太平洋地区的地缘政治核心，拥有重要的贸易动脉和战略重要性。',
                                  body2='然而，该地区对被卷入中美竞争怀有戒心，认为美国的遏制努力反应过度。他们不接受美国提出的 '
                                        "''自由开放 "
                                        "''印太战略，因为他们认为这是将该地区强行纳入一个地缘政治框架。美国、韩国和日本之间的三边合作被认为是应对中国日益加剧的侵略的关键。国会议员弗伦奇-希尔强调了这种合作在维护印太地区经济繁荣和促进自由方面的重要性。三国需要共同努力，确保贸易和航行自由，对抗中国的新殖民主义 "
                                        "''一带一路 "
                                        "''战略，维护本地区乃至全世界的和平与繁荣。即将举行的美国、韩国和日本三边峰会表明了加强合作的承诺，也标志着在应对中国的强硬态度所带来的挑战方面迈出的重要一步。总之，东南亚对中美关系的看法强调了对中立立场的渴望以及从两个超级大国中获益的重要性。美国、韩国和日本之间的三边合作也被视为应对中国日益增长的侵略性的关键。在该地区应对中美之间复杂的动态关系时，保持平衡的态度和促进多边合作关系将是确保和平与繁荣的关键。",
                                  qna_list=[QnA(question='东南亚如何看待中美关系？',
                                                answer='东南亚许多国家认为美国具有挑衅性，并认为妖魔化中国是大势所趋。他们强调中立，旨在从两个超级大国中获益。'),
                                            QnA(question='东南亚国家如何看待美国对中国的遏制和施压政策？',
                                                answer='东南亚国家，尤其是东盟成员国，并不认为美国的遏制和施压政策是有效的。他们认为这反映了一种新的冷战，不会被这种努力所动摇。'),
                                            QnA(question='根据亚洲协会的报告，东南亚的重要性是什么？',
                                                answer='亚洲协会的报告强调了东南亚的重要性，而东南亚在美国的利益和公开竞争中往往被低估。报告建议改变政策，呼吁应对中国在该地区日益增长的影响力。'),
                                            QnA(question="东南亚为何不采纳美国提出的 ''自由开放 "
                                                         "''印太战略？",
                                                answer='东南亚认为美国提出的战略是将该地区强行纳入地缘政治框架的一种方式。他们认为这不符合他们的利益和目标。'),
                                            QnA(question='美国、韩国和日本之间的三边合作有何意义？',
                                                answer='美国、韩国和日本之间的三边合作被视为应对中国日益加剧的侵略的关键。其目的是确保贸易和航行自由，对抗中国的 '
                                                       "''一带一路 "
                                                       "''战略，维护印太地区的和平与繁荣。")],
                                  language='ZH'),
                   ArticleContent(title='미-중 관계에 대한 동남아시아의 시각과 3국 협력의 중요성',
                                  lead='동남아시아에서 미중 관계는 많은 사람들이 미국을 도발적이고 중국을 '
                                       '악마화하는 것으로 간주하는 등 우려의 대상이 되어 왔습니다. '
                                       '동남아시아 국가들은 중립적인 입장을 유지하면서 두 강대국으로부터 '
                                       '혜택을 받는 것이 중요하다고 강조합니다. 미국, 한국, 일본 간의 '
                                       '3국 협력 또한 중국의 침략 증가에 대처하는 데 매우 중요한 것으로 '
                                       '간주됩니다.',
                                  body1='미-중 관계는 동남아시아에서 논의와 우려의 대상이 되어 왔습니다. '
                                        '이 지역의 많은 국가들은 미국을 도발적인 존재로 간주하며 중국을 '
                                        '악마화하는 경향이 있다고 생각합니다. 대신 중립적인 입장을 유지하고 '
                                        '두 강대국으로부터 혜택을 누리는 것이 중요하다고 강조합니다. 중국에 '
                                        '대해 보다 적극적인 역할을 해온 한국과 달리 동남아시아 국가들, '
                                        '특히 동남아시아국가연합(아세안)에 속한 국가들은 미국 행정부의 '
                                        '봉쇄와 압박 정책이 그들의 마음을 얻는 데 효과적이지 않다는 것을 '
                                        '보여주었습니다. 이들은 인도-태평양 전략을 통해 세계를 민주주의 '
                                        '국가와 독재 국가로 나누고 대중의 지지 범위를 좁히려는 미국의 '
                                        '전략이 신냉전을 반영하는 것으로 보고 있습니다. 뉴욕에 본부를 둔 '
                                        "비영리 단체인 아시아 소사이어티는 ''미국 공공 정책에서 "
                                        "동남아시아를 우선시해야 한다''는 제목의 보고서를 발표했습니다. 이 "
                                        '보고서는 동남아시아의 중요성과 미국의 이익과 공공 경쟁에서 '
                                        '동남아시아의 저평가된 위치를 강조합니다. 이 보고서는 미국 정부에 '
                                        '정책 변화를 권고하고 이 지역에서 중국의 영향력 확대에 대한 대응을 '
                                        '촉구합니다. 동남아시아는 인도 태평양 지역의 지정학적 중심지이며, '
                                        '중요한 무역 동맥이자 전략적 중요성을 지니고 있습니다.',
                                  body2='그러나 이 지역은 미중 경쟁에 휘말리는 것을 경계하고 있으며 미국이 '
                                        '봉쇄 노력에 과도하게 반응하고 있다고 보고 있습니다. 이들은 미국이 '
                                        "제안한 ''자유롭고 개방적인'' 인도-태평양 전략이 이 지역을 "
                                        '지정학적 틀에 가두는 것으로 인식하기 때문에 이를 채택하지 '
                                        '않습니다. 미국, 한국, 일본 간의 3국 협력은 중국의 증가하는 '
                                        '침략에 대처하는 데 매우 중요한 것으로 간주됩니다. 프렌치 힐 '
                                        '의원은 인도 태평양 지역의 경제적 번영을 유지하고 자유를 증진하는 '
                                        '데 있어 이러한 협력이 중요하다고 강조했습니다. 3국은 무역과 '
                                        '항해의 자유를 보장하고 중국의 신식민지 일대일로 전략에 대응하며 '
                                        '지역과 전 세계의 평화와 번영을 수호하기 위해 협력해야 합니다. '
                                        '다가오는 미국, 한국, 일본 3국 정상 회담은 협력을 강화하겠다는 '
                                        '의지를 보여주고 중국의 독단적 행보로 인한 도전에 대응하기 위한 '
                                        '중요한 발걸음이 될 것입니다. 결론적으로 미중 관계에 대한 '
                                        '동남아시아의 시각은 중립적 입장에 대한 열망과 두 강대국으로부터 '
                                        '혜택을 받는 것의 중요성을 강조합니다. 미국, 한국, 일본 간의 '
                                        '3국 협력은 또한 중국의 증가하는 침략을 관리하는 데 매우 중요한 '
                                        '것으로 간주됩니다. 미중 간의 복잡한 역학관계를 헤쳐나가는 과정에서 '
                                        '균형 잡힌 접근 방식을 유지하고 다자간 파트너십을 육성하는 것이 '
                                        '평화와 번영을 보장하는 열쇠가 될 것입니다.',
                                  qna_list=[QnA(question='동남아시아는 미-중 관계를 어떻게 '
                                                         '바라볼까요?',
                                                answer='동남아시아의 많은 국가는 미국을 도발적인 '
                                                       '존재로 간주하고 중국을 악마화하는 경향이 '
                                                       '있다고 생각합니다. 이들은 중립을 '
                                                       '강조하며 두 강대국으로부터 이익을 '
                                                       '얻으려고 합니다.'),
                                            QnA(question='동남아시아 국가들은 미국의 대중국 '
                                                         '봉쇄 및 압박 정책에 대해 어떻게 '
                                                         '생각하나요?',
                                                answer='동남아시아 국가들, 특히 아세안 '
                                                       '회원국들은 미국의 봉쇄와 압박 정책이 '
                                                       '효과적이라고 믿지 않습니다. 신냉전을 '
                                                       '반영하는 것으로 보고 있으며 이러한 '
                                                       '노력에 흔들리지 않습니다.'),
                                            QnA(question='아시아 소사이어티 보고서에 따르면 '
                                                         '동남아시아의 중요성은 무엇인가요?',
                                                answer='아시아 소사이어티 보고서는 미국의 '
                                                       '이해관계와 공공 경쟁에서 종종 저평가되는 '
                                                       '동남아시아의 중요성을 강조합니다. 이 '
                                                       '보고서는 정책 변화를 권고하고 이 '
                                                       '지역에서 중국의 영향력 확대에 대한 '
                                                       '대응을 촉구합니다.'),
                                            QnA(question='동남아시아는 왜 미국이 제안한 '
                                                         "''자유롭고 개방적인'' 인도 태평양 "
                                                         '전략을 채택하지 않을까요?',
                                                answer='동남아시아는 미국이 제안한 전략이 이 '
                                                       '지역을 지정학적 틀에 가두려는 의도로 '
                                                       '보고 있습니다. 그들은 이 전략이 '
                                                       '자신들의 이익과 목표에 부합하지 않는다고 '
                                                       '생각합니다.'),
                                            QnA(question='미국, 한국, 일본 3국 협력의 '
                                                         '의미는 무엇인가요?',
                                                answer='미국, 한국, 일본 간의 3국 협력은 '
                                                       '중국의 증가하는 침략에 대응하는 데 매우 '
                                                       '중요한 것으로 간주됩니다. 무역과 항행의 '
                                                       '자유를 보장하고 중국의 일대일로 전략에 '
                                                       '대응하며 인도 태평양의 평화와 번영을 '
                                                       '유지하는 것이 목표입니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://cdn.mindlenews.com/news/thumbnail/202308/4460_11338_1511_v150.jpg',
                              source='시민언론 민들레'),
                 ArticleImage(url='https://gdb.voanews.com/01000000-0aff-0242-b0e3-08db5b043c7a_w1200_r1.jpg',
                              source='VOA Korea')]),
 Article(category='Business/Economy',
         keywords='미국 신용등급 강등',
         contents=[ArticleContent(title='U.S. sovereign credit rating '
                                        'downgraded for first time in 12 '
                                        'years...Asian stocks slammed',
                                  lead='The US sovereign credit rating has '
                                       "been downgraded. It's been 12 years "
                                       "since 2011, and the world's financial "
                                       'markets are nervous. As Korea cannot '
                                       'be safe if there is a turbulence in '
                                       'the U.S. financial market, the changes '
                                       'in the financial market caused by the '
                                       'U.S. sovereign credit rating downgrade '
                                       'will be closely watched.',
                                  body1='Ratings agency Fitch headquarters in '
                                        'New York, U.S. [EPA Yonhap photo] The '
                                        'sovereign credit rating of the United '
                                        'States has been downgraded. It was '
                                        'the first time in 12 years since '
                                        "2011, and the world's financial "
                                        'markets are nervous. As Korea cannot '
                                        'be safe from the turbulence in the '
                                        'U.S. financial market, it will be '
                                        'interesting to see how the U.S. '
                                        'sovereign credit rating downgrade '
                                        'will affect the financial market. '
                                        'Fitch downgrades US sovereign rating '
                                        'after 12 years International credit '
                                        'rating agency Fitch downgraded the '
                                        'sovereign credit rating of the United '
                                        "States from 'AAA' to 'AA+' on January "
                                        '1 (local time). This is the first '
                                        'time in 12 years since 2011 that the '
                                        'three major international credit '
                                        'rating agencies have downgraded the '
                                        'U.S. sovereign credit rating, and the '
                                        'implications for financial markets '
                                        'and the real economy will be closely '
                                        'watched. Fitch today downgraded the '
                                        'U.S. long-term foreign currency '
                                        'issuer rating (IDRs) by one notch to '
                                        'AA+ from AAA and revised the outlook '
                                        "to 'stable' from 'negative watch'. "
                                        "'The downgrade reflects the expected "
                                        'fiscal deterioration in the United '
                                        'States over the next three years, as '
                                        'well as a growing sovereign debt '
                                        "burden and deteriorating governance,' "
                                        'Fitch said in a report. In '
                                        'particular, Fitch noted that '
                                        'governance has deteriorated compared '
                                        'to other countries with AA or AAA '
                                        'ratings, as U.S. politicians have '
                                        'repeatedly stalled over raising the '
                                        'debt limit, only to resolve the issue '
                                        'at the last minute. Trends in U.S. '
                                        "sovereign credit ratings 'The U.S. "
                                        'has seen a steady deterioration in '
                                        'governance standards for more than '
                                        "two decades,' Fitch said, noting that "
                                        "'fiscal and debt problems remain "
                                        'despite a bipartisan agreement in '
                                        'June to suspend the debt limit until '
                                        'January 2025. Meanwhile, Fitch '
                                        'expects the U.S. deficit as a '
                                        'percentage of gross domestic product '
                                        '(GDP) to surge from 3.7% in 2022 to '
                                        '6.3% in 2023, followed by 6.6% in '
                                        '2024 and 6.9% in 2025, as a result of '
                                        'lower tax revenues, higher deficit '
                                        'spending, and a growing interest '
                                        'burden. Fitch also warned about the '
                                        'economic future of the U.S., saying '
                                        "that 'over the next decade, rising "
                                        'interest rates and rising debt will '
                                        'increase interest payments, while an '
                                        'aging population and rising '
                                        'healthcare costs will increase '
                                        'spending on the elderly in the '
                                        "absence of fiscal reform,' and even "
                                        'predicted a recession in the U.S. '
                                        'sooner rather than later, saying that '
                                        "'deteriorating credit conditions, "
                                        'lower investment, and falling '
                                        'consumption will push the U.S. '
                                        'economy into a mild recession in the '
                                        'fourth quarter of this year and the '
                                        'first quarter of next year. Fitch cut '
                                        'the U.S. sovereign rating by one '
                                        "notch to AA+ from AAA, while Moody's "
                                        'maintained its Aaa rating and '
                                        "Standard & Poor's affirmed its AA+ "
                                        'rating. Will there be a repeat of the '
                                        "2011 sovereign downgrade shock? It's "
                                        'been 12 years since the last time a '
                                        'major international credit rating '
                                        'agency downgraded the U.S. sovereign '
                                        "rating, when Standard & Poor's (S&P) "
                                        'lowered it from AAA to AA+ in 2011. '
                                        'At the time, S&P cited political '
                                        'impasse over raising the U.S. debt '
                                        'ceiling as the reason for the '
                                        'downgrade. The move sent shockwaves '
                                        'through international financial '
                                        'markets, with the dollar depreciating '
                                        'and stock prices plummeting. The '
                                        'large-cap S&P500 index dropped 15% in '
                                        'just a few days, and panic spread '
                                        'across European and Asian stock '
                                        'markets. However, the price of US '
                                        'Treasury bonds, which are considered '
                                        'a safe haven asset, rose due to the '
                                        'combination of risk aversion and '
                                        'safe-haven sentiment. The question is '
                                        "whether Fitch's downgrade of the U.S. "
                                        'will follow in the footsteps of '
                                        "Standard & Poor's downgrade of the "
                                        'U.S. in 2011. There is a strong case '
                                        "to be made that the impact of Fitch's "
                                        'downgrade of the U.S. will be '
                                        'limited, given the proximity of the '
                                        '2011 default to the federal debt '
                                        'limit, the proximity of the 2008 '
                                        'global financial crisis, the fact '
                                        'that Fitch had already warned of a '
                                        'downgrade in May when it placed the '
                                        'U.S. sovereign rating outlook on '
                                        "'negative watch,' and the fact that, "
                                        'unlike in 2011, the U.S. economy is '
                                        'on a soft landing. On the other hand, '
                                        'with U.S. equity markets near '
                                        "historic highs, Fitch's downgrade "
                                        'could trigger a correction, and any '
                                        'further downgrades could be '
                                        'devastating to the federal '
                                        "government's fiscal health.",
                                  body2='Is a Stronger Dollar and Lower '
                                        'Treasury Yields Best for the U.S.? '
                                        'According to Bloomberg, the market '
                                        'reaction to the downgrade was '
                                        'relatively subdued. Futures for the '
                                        'S&P 500 and Nasdaq Composite were '
                                        'each down less than 0.5%, while the '
                                        'yield on the 10-year U.S. Treasury '
                                        'note was at 4.03% as of 4:40 p.m. ET, '
                                        'down one basis point (bp=0.01 '
                                        'percentage point) from the previous '
                                        'day. A decline in bond yields implies '
                                        'a rise in bond prices. Meanwhile, '
                                        'U.S. equity futures showed a sharp '
                                        'correction as the market opened. The '
                                        'U.S. sovereign credit rating '
                                        'downgrade continues to strengthen the '
                                        'dollar. In this photo, employees '
                                        'organize dollar bills at the head '
                                        'office of Hana Bank in Euljiro, '
                                        "Jung-gu, Seoul. Oct. 6, 2022 Fitch's "
                                        'downgrade of the U.S. sovereign '
                                        'credit rating is hitting Asian stocks '
                                        'and currencies hard. Asian stocks and '
                                        'currencies weakened in unison on Oct. '
                                        '2. This is because the growing '
                                        'preference for safe assets such as '
                                        'the U.S. dollar and government bonds '
                                        'is causing investors to pull out of '
                                        'Asian markets categorized as risky. '
                                        'According to the Korea Exchange, the '
                                        'Kospi fell 50.60 points, or 1.9%, to '
                                        'close at 2616.47, a day after hitting '
                                        'a yearly high of 2667.07 the day '
                                        'before, while the KOSPI fell 29.91 '
                                        "points, or 3.18%, to 909.76. Japan's "
                                        'Nikkei 225 ended the day down 2.30% '
                                        "at 32,707.69, while Hong Kong's Hang "
                                        "Seng (-2.47%), China's Shanghai "
                                        "Composite (-0.89%) and Taiwan's KMT "
                                        '(-1.85%) were also down. European '
                                        'markets, which open after the Asian '
                                        'close, are also in the red, with the '
                                        'pan-European index, the Euro Stoxx '
                                        '50, down more than 1%. The main focus '
                                        'is on the exchange rate. This is '
                                        'because the stronger dollar is making '
                                        'a comeback after a recent lull. At '
                                        'the Seoul foreign exchange market, '
                                        'the won/dollar exchange rate soared '
                                        'to 1,298.5 won, up 14.7 won from the '
                                        'previous trading day. It was the '
                                        'biggest one-day surge since March 24, '
                                        'when it rose 16.0 won amid financial '
                                        'turmoil in the U.S. banking sector, '
                                        'and the first time in about three '
                                        'weeks that it has touched the '
                                        '1,300-won level since March 10 '
                                        '(1306.5 won). The dollar index, which '
                                        "measures the greenback's value "
                                        'against a basket of six major '
                                        'currencies, stood at 102.21 as of '
                                        '3:30 p.m. KST. A dollar index above '
                                        'the 100 mark indicates that the '
                                        'greenback is stronger against a '
                                        "basket of major currencies. It's "
                                        "unclear how much of a ripple Fitch's "
                                        'downgrade of the U.S. will cause or '
                                        'where it will go. What is clear is '
                                        "that global money's preference for "
                                        'the dollar and U.S. Treasuries is a '
                                        'blessing in disguise for the United '
                                        'States. A strong dollar is a way to '
                                        'export domestic inflation abroad, and '
                                        'greater demand for Treasuries will '
                                        'lead to lower Treasury yields, '
                                        "reducing the government's interest "
                                        'burden.',
                                  qna_list=[QnA(question='What is the impact '
                                                         "of Fitch's downgrade "
                                                         'of the U.S. '
                                                         'sovereign credit '
                                                         'rating?',
                                                answer="Fitch's downgrade "
                                                       'reflects the expected '
                                                       'fiscal deterioration '
                                                       'in the United States '
                                                       'over the next three '
                                                       'years, as well as a '
                                                       'growing sovereign debt '
                                                       'burden and '
                                                       'deteriorating '
                                                       'governance. It is the '
                                                       'first time in 12 years '
                                                       'since 2011 that the '
                                                       'three major '
                                                       'international credit '
                                                       'rating agencies have '
                                                       'downgraded the U.S. '
                                                       'sovereign credit '
                                                       'rating.'),
                                            QnA(question='Will the U.S. '
                                                         'sovereign credit '
                                                         'rating downgrade '
                                                         'have a similar '
                                                         'impact to the 2011 '
                                                         'downgrade?',
                                                answer='There is a strong case '
                                                       'to be made that the '
                                                       "impact of Fitch's "
                                                       'downgrade of the U.S. '
                                                       'will be limited, given '
                                                       'the proximity of the '
                                                       '2011 default to the '
                                                       'federal debt limit, '
                                                       'the proximity of the '
                                                       '2008 global financial '
                                                       'crisis, and the fact '
                                                       'that Fitch had already '
                                                       'warned of a downgrade '
                                                       'in May when it placed '
                                                       'the U.S. sovereign '
                                                       'rating outlook on '
                                                       "'negative watch.' "
                                                       'Additionally, the U.S. '
                                                       'economy is currently '
                                                       'on a soft landing.'),
                                            QnA(question='How did the market '
                                                         'react to the U.S. '
                                                         'sovereign credit '
                                                         'rating downgrade?',
                                                answer='The market reaction to '
                                                       'the downgrade was '
                                                       'relatively subdued. '
                                                       'Futures for the S&P '
                                                       '500 and Nasdaq '
                                                       'Composite were down '
                                                       'less than 0.5%, while '
                                                       'the yield on the '
                                                       '10-year U.S. Treasury '
                                                       'note slightly '
                                                       'decreased. However, '
                                                       'Asian stocks and '
                                                       'currencies were hit '
                                                       'hard, as investors '
                                                       'pulled out of risky '
                                                       'Asian markets due to a '
                                                       'growing preference for '
                                                       'safe assets.'),
                                            QnA(question='What is the main '
                                                         'focus in the '
                                                         'aftermath of the '
                                                         'U.S. sovereign '
                                                         'credit rating '
                                                         'downgrade?',
                                                answer='The main focus is on '
                                                       'the exchange rate, as '
                                                       'the stronger dollar is '
                                                       'making a comeback '
                                                       'after a recent lull. A '
                                                       'stronger dollar can '
                                                       'help export domestic '
                                                       'inflation abroad, and '
                                                       'greater demand for '
                                                       'U.S. Treasuries will '
                                                       'lead to lower Treasury '
                                                       'yields, reducing the '
                                                       "government's interest "
                                                       'burden.')],
                                  language='EN-US'),
                   ArticleContent(title='美国主权信用评级 12 年来首次下调......亚洲股市大跌',
                                  lead='美国主权信用评级被下调。2011 年至今已过去 12 '
                                       '年，世界金融市场紧张不安。如果美国金融市场出现动荡，韩国就不可能安全，因此美国主权信用评级下调所引发的金融市场变化将受到密切关注。',
                                  body1='位于美国纽约的评级机构惠誉总部 [EPA Yonhap photo] '
                                        '美国的主权信用评级被下调。这是自2011年以来的12年中的第一次，世界金融市场为之紧张。韩国无法免受美国金融市场动荡的影响，美国主权信用评级下调将对金融市场产生何种影响值得关注。惠誉时隔12年下调美国主权评级 '
                                        "国际信用评级机构惠誉于当地时间1月1日将美国主权信用评级从 ''AAA "
                                        "''下调至 "
                                        "''AA+''。这是自2011年以来，三大国际信用评级机构时隔12年首次下调美国主权信用评级，其对金融市场和实体经济的影响将受到密切关注。惠誉今天将美国长期外币发行人评级（IDRs）从AAA下调一档至AA+，并将评级展望从 "
                                        "''负面观察 ''调整为 "
                                        "''稳定''。惠誉在一份报告中说：''评级下调反映了美国未来三年财政状况的预期恶化，以及主权债务负担加重和治理恶化。惠誉特别指出，与其他获得AA或AAA评级的国家相比，美国的治理已经恶化，因为美国政界人士在提高债务限额问题上一再拖延，直到最后一刻才解决问题。惠誉称：''20多年来，美国的治理标准持续恶化。''惠誉还指出：''尽管两党在6月份达成了一项协议，将暂停债务限额至2025年1月，但财政和债务问题依然存在。同时，惠誉预计，由于税收收入减少、赤字支出增加以及利息负担加重，美国赤字占国内生产总值（GDP）的比例将从2022年的3.7%激增至2023年的6.3%，随后是2024年的6.6%和2025年的6.9%。惠誉还对美国的经济前景发出了警告，称 "
                                        "''未来十年，利率上升和债务增加将增加利息支出，而人口老龄化和医疗成本上升将在没有财政改革的情况下增加对老年人的支出''，甚至预测美国经济衰退的时间早晚，称 "
                                        "''信贷状况恶化、投资减少和消费下降将推动美国经济在今年第四季度和明年第一季度陷入温和衰退''。惠誉将美国主权评级从 "
                                        'AAA 下调一档至 AA+，穆迪维持其 Aaa 评级，标准普尔确认其 '
                                        'AA+评级。2011 年的主权评级下调冲击会重演吗？自 2011 '
                                        '年标准普尔（S&P）将美国主权评级从 AAA 下调至 '
                                        'AA+，距上一次主要国际信用评级机构下调美国主权评级已有 12 '
                                        '年之久。当时，标普将提高美国债务上限的政治僵局作为下调评级的原因。此举在国际金融市场引起震动，美元贬值，股票价格暴跌。大型股标准普尔500指数在短短几天内下跌了15%，恐慌情绪在欧洲和亚洲股市蔓延。然而，被视为避险资产的美国国债价格却在避险情绪的共同作用下上涨。问题是惠誉下调美国评级是否会步标准普尔 '
                                        '2011 '
                                        '年下调美国评级的后尘。惠誉下调美国评级的影响有限是有充分理由的，因为 '
                                        '2011 年的违约与联邦债务限额相近，与 2008 '
                                        '年全球金融危机相近，而且惠誉在 5 月份将美国主权评级展望定为 '
                                        "''负面观察 ''时就已经发出了下调警告，而且与 2011 "
                                        '年不同的是，美国经济正在软着陆。另一方面，随着美国股市接近历史高点，惠誉的降级可能会引发修正，而任何进一步的降级都可能对联邦政府的财政健康造成破坏。',
                                  body2='美元走强和国债收益率下降对美国最有利吗？据彭博社报道，市场对降级的反应相对平淡。标准普尔500指数和纳斯达克综合指数期货各下跌不到0.5%，而截至美东时间下午4:40，10年期美国国债收益率为4.03%，比前一天下降了一个基点（bp=0.01个百分点）。债券收益率下降意味着债券价格上涨。与此同时，美国股票期货在开市时出现大幅回调。美国主权信用评级下调继续使美元走强。图为员工在位于首尔中区乙支路的花旗银行总部整理美元钞票。2022年10月6日，惠誉下调美国主权信用评级对亚洲股市和货币造成沉重打击。10月2日，亚洲股市和货币齐齐走软，这是因为投资者越来越青睐美元和政府债券等安全资产，导致他们撤出被归类为高风险的亚洲市场。根据韩国交易所的数据，Kospi指数下跌50.60点，或1.9%，收于2616.47点，前一天曾创下2667.07点的年内高点；KOSPI指数下跌29.91点，或3.18%，收于909.76点。日本日经 '
                                        '225 指数收盘下跌 2.30%，报 32707.69 '
                                        '点；香港恒生指数（-2.47%）、中国上证综合指数（-0.89%）和台湾国民党指数（-1.85%）也均下跌。亚洲股市收盘后开盘的欧洲股市也飘红，泛欧斯托克 '
                                        '50 指数跌幅超过 '
                                        '1%。主要焦点是汇率。这是因为强势美元在最近的低迷之后卷土重来。在首尔外汇市场，韩元/美元汇率飙升至 '
                                        '1298.5 韩元，比前一个交易日上涨了 14.7 韩元。这是自 3 月 '
                                        '24 '
                                        '日以来的最大单日涨幅，当时在美国银行业金融动荡的情况下，韩元/美元汇率上涨了 '
                                        '16.0 韩元，这也是自 3 月 10 日（1306.5 '
                                        '韩元）以来，韩元/美元汇率在大约三周内首次触及 1300 '
                                        '韩元的水平。截至韩国时间下午 '
                                        '3:30，衡量美元对一篮子六种主要货币价值的美元指数为 '
                                        '102.21。美元指数超过 100 '
                                        '大关表明美元对一篮子主要货币走强。目前还不清楚惠誉下调美国评级会引起多大的波澜，也不清楚会走向何方。显而易见的是，全球资金对美元和美国国债的青睐对美国来说是一种不幸中的万幸。强势美元是向国外输出国内通胀的一种方式，而对国债的更大需求将导致国债收益率下降，从而减轻政府的利息负担。',
                                  qna_list=[QnA(question='惠誉下调美国主权信用评级有何影响？',
                                                answer='惠誉下调评级反映了美国未来三年财政状况的预期恶化，以及主权债务负担加重和治理恶化。这是自2011年以来，三大国际信用评级机构12年来首次下调美国主权信用评级。'),
                                            QnA(question='美国主权信用评级下调是否会产生与 '
                                                         '2011 年评级下调类似的影响？',
                                                answer='考虑到 2011 '
                                                       '年违约与联邦债务限额的临近、2008 '
                                                       '年全球金融危机的临近，以及惠誉在 5 '
                                                       "月份将美国主权评级展望定为 ''负面观察 "
                                                       "''时就已发出降级警告，有充分理由认为惠誉下调美国评级的影响将是有限的。此外，美国经济目前正处于软着陆阶段。"),
                                            QnA(question='市场对美国主权信用评级下调有何反应？',
                                                answer='市场对评级下调的反应相对平淡。标准普尔 '
                                                       '500 指数和纳斯达克综合指数期货下跌不到 '
                                                       '0.5%，10 '
                                                       '年期美国国债收益率略有下降。不过，亚洲股市和货币受到重创，因为投资者越来越倾向于安全资产，撤出了风险较高的亚洲市场。'),
                                            QnA(question='美国主权信用评级下调后的主要焦点是什么？',
                                                answer='主要焦点是汇率，因为美元在经历了近期的低迷之后正在卷土重来。美元走强有助于向国外输出国内通胀，对美国国债的更大需求将导致国债收益率下降，从而减轻政府的利息负担。')],
                                  language='ZH'),
                   ArticleContent(title='미국 국가신용등급 12년 만에 강등...아시아 증시 폭락',
                                  lead='미국의 국가신용등급이 강등되었습니다. 2011년 이후 12년 만으로 '
                                       '전 세계 금융시장이 긴장하고 있습니다. 미국 금융시장이 요동치면 '
                                       '우리나라도 안심할 수 없는 만큼 미국 국가신용등급 강등에 따른 '
                                       '금융시장 변화를 예의주시하고 있습니다.',
                                  body1='미국 뉴욕에 있는 신용평가사 피치 본사 [EPA 연합뉴스 사진] '
                                        '미국의 국가신용등급이 강등됐다. 2011년 이후 12년 만에 처음 '
                                        '있는 일이라 세계 금융시장이 긴장하고 있다. 한국도 미국 금융시장의 '
                                        '격랑에서 자유로울 수 없는 만큼 미국의 국가신용등급 강등이 '
                                        '금융시장에 어떤 영향을 미칠지 주목됩니다. 피치, 12년 만에 미국 '
                                        '국가신용등급 강등 국제신용평가사 피치가 1일(현지시간) 미국의 '
                                        "국가신용등급을 ''AAA''에서 ''AA+''로 강등했다. 3대 "
                                        '국제 신용평가사가 미국의 국가신용등급을 강등한 것은 2011년 이후 '
                                        '12년 만으로, 금융시장과 실물경제에 미칠 영향이 예의주시되고 '
                                        '있다. 피치는 오늘 미국의 장기 외화 발행자 등급(IDR)을 '
                                        "''AAA''에서 ''AA+''로 한 단계 강등하고 전망을 "
                                        "''부정적 관찰 대상''에서 ''안정적''으로 조정했다. 피치는 "
                                        "보고서에서 ''이번 등급 강등은 향후 3년간 미국의 재정 악화가 "
                                        '예상되고, 국가 부채 부담 증가와 거버넌스 악화를 반영한 '
                                        "것''이라고 밝혔다. 특히 피치는 미국 정치인들이 부채 한도 증액을 "
                                        '놓고 반복적으로 시간을 끌다가 마지막 순간에야 문제를 해결하면서 '
                                        'AA 또는 AAA 등급을 가진 다른 국가에 비해 거버넌스가 '
                                        "악화되었다고 지적했습니다. 미국 국가신용등급 동향 피치는 ''미국은 "
                                        "20년 이상 거버넌스 기준이 꾸준히 악화되어 왔다''며 ''지난 "
                                        '6월 부채한도를 2025년 1월까지 유예하기로 한 초당적 합의에도 '
                                        "불구하고 재정 및 부채 문제는 여전히 남아 있다''고 지적했다. "
                                        '한편, 피치는 세수 감소, 적자 지출 증가, 이자 부담 증가로 인해 '
                                        '미국의 국내총생산(GDP) 대비 재정적자가 2022년 3.7%에서 '
                                        '2023년 6.3%, 2024년 6.6%, 2025년 6.9%로 '
                                        "급증할 것으로 예상했다. 또한 피치는 ''향후 10년간 금리 상승과 "
                                        '부채 증가로 이자 지급이 증가하고, 재정 개혁이 없을 경우 인구 '
                                        "고령화와 의료비 상승으로 노인 지출이 증가할 것''이라며 미국의 "
                                        "경제 미래에 대해 경고했고, ''신용 여건 악화, 투자 감소, 소비 "
                                        '감소로 올해 4분기와 내년 1분기에 미국 경제가 완만한 경기 침체에 '
                                        "빠질 것''이라며 조만간 미국의 경기 침체를 예상하기도 했습니다. "
                                        '피치는 미국의 국가 신용등급을 AAA에서 AA+로 한 단계 낮췄고, '
                                        '무디스는 Aaa 등급을 유지했으며 스탠더드앤드푸어스는 AA+ 등급을 '
                                        '긍정적으로 평가했습니다. 2011년의 국가 신용등급 강등 충격이 '
                                        '반복될까요? 주요 국제 신용 평가 기관이 미국의 국가 신용등급을 '
                                        '강등한 것은 2011년 스탠더드앤드푸어스(S&P)가 미국의 국가 '
                                        '신용등급을 AAA에서 AA+로 강등한 이후 12년 만입니다. 당시 '
                                        'S&P는 미국 부채 한도 증액을 둘러싼 정치적 교착 상태를 신용등급 '
                                        '강등의 이유로 꼽았습니다. 이 결정은 달러 가치가 하락하고 주가가 '
                                        '폭락하는 등 국제 금융 시장에 충격파를 던졌습니다. 대형주 중심의 '
                                        'S&P500 지수는 단 며칠 만에 15% 하락했고, 유럽과 아시아 '
                                        '증시에도 패닉이 확산되었습니다. 그러나 위험 회피 심리와 안전자산 '
                                        '선호 심리가 맞물려 안전자산으로 간주되는 미국 국채 가격은 오히려 '
                                        '상승했습니다. 문제는 피치의 미국 신용등급 강등이 2011년 '
                                        '스탠더드앤드푸어스(S&P)의 미국 신용등급 강등의 전철을 밟을지 '
                                        '여부입니다. 2011년 연방 채무한도 불이행이 2008년 글로벌 '
                                        '금융위기와 근접했다는 점, 피치가 지난 5월 미국 국가 신용등급 '
                                        "전망을 ''부정적 관찰대상''으로 설정하면서 이미 강등을 경고했다는 "
                                        '점, 2011년과 달리 미국 경제가 연착륙하고 있다는 점 등을 '
                                        '고려할 때 피치의 미국 신용등급 강등이 미칠 영향은 제한적일 '
                                        '것이라는 주장이 설득력을 얻고 있다. 반면에 미국 주식 시장이 사상 '
                                        '최고치에 근접한 상황에서 피치의 강등은 조정을 촉발할 수 있으며, '
                                        '추가 강등은 연방 정부의 재정 건전성에 치명적일 수 있습니다.',
                                  body2='달러 강세와 국채 수익률 하락이 미국에 최선일까? 블룸버그에 따르면 '
                                        '신용등급 강등에 대한 시장 반응은 비교적 차분했습니다. S&P '
                                        '500지수와 나스닥 종합지수 선물은 각각 0.5% 미만 하락했고, '
                                        '미국 동부시간 오후 4시 40분 현재 10년 만기 미국 국채 '
                                        '수익률은 4.03%로 전일 대비 '
                                        '1베이시스포인트(bp=0.01%포인트) 하락했습니다. 채권 수익률 '
                                        '하락은 채권 가격 상승을 의미합니다. 한편 미국 주식 선물은 개장과 '
                                        '함께 급격한 조정을 보였습니다. 미국 국가신용등급 강등으로 달러 '
                                        '강세가 지속되고 있다. 사진은 서울 중구 을지로 하나은행 본점에서 '
                                        '직원들이 달러 지폐를 정리하고 있는 모습. 2022년 10월 6일 '
                                        '피치의 미국 국가신용등급 강등으로 아시아 증시와 통화가 큰 타격을 '
                                        '받고 있습니다. 10월 2일 아시아 증시와 통화가 일제히 약세를 '
                                        '보인 것은 미국 달러와 국채 등 안전자산에 대한 선호도가 높아지면서 '
                                        '위험자산으로 분류된 아시아 시장에서 투자자들이 빠져나가고 있기 '
                                        '때문이다. 한국거래소에 따르면 전날 연중 최고치인 2667.07을 '
                                        '기록한 지 하루 만에 코스피는 50.60포인트(1.9%) 하락한 '
                                        '2616.47에 마감했고, 코스닥은 29.91포인트(3.18%) '
                                        '내린 909.76을 기록했다. 일본 닛케이225지수는 2.30% '
                                        '하락한 3만2707.69에 마감했고 홍콩 항셍지수(-2.47%), '
                                        '중국 상하이종합지수(-0.89%), 대만 가권지수(-1.85%)도 '
                                        '하락했다. 아시아 증시 마감 후 개장한 유럽 증시도 범유럽지수인 '
                                        '유로 스톡스 50 지수가 1% 이상 하락하는 등 하락세를 보이고 '
                                        '있습니다. 주요 초점은 환율에 있습니다. 최근 소강상태를 보였던 '
                                        '달러 강세가 다시 살아나고 있기 때문입니다. 서울 외환시장에서 '
                                        '원/달러 환율은 전 거래일보다 14.7원 오른 1,298.5원까지 '
                                        '치솟았다. 이는 미국 은행권 금융 불안으로 16.0원 올랐던 지난 '
                                        '3월 24일 이후 하루 최대 상승폭이자, 지난 3월 '
                                        '10일(1306.5원) 이후 약 3주 만에 1300원대를 터치한 '
                                        '것이다. 주요 6개국 통화 바스켓에 대한 달러화 가치를 측정하는 '
                                        '달러 인덱스는 오후 3시 30분(한국시간) 현재 102.21을 '
                                        '기록했다. 달러 인덱스가 100을 넘으면 주요 통화 바스켓에 비해 '
                                        '달러가 강세라는 뜻입니다. 피치의 미국 신용등급 강등이 얼마나 큰 '
                                        '파장을 일으킬지, 그 파장이 어디까지 갈지는 불분명합니다. 분명한 '
                                        '것은 달러와 미국 국채에 대한 글로벌 자금의 선호가 미국에게는 '
                                        '축복이라는 것입니다. 달러 강세는 국내 인플레이션을 해외로 수출할 '
                                        '수 있는 수단이며, 국채에 대한 수요가 증가하면 국채 수익률이 '
                                        '낮아져 정부의 이자 부담이 줄어듭니다.',
                                  qna_list=[QnA(question='Fitch의 미국 국가신용등급 강등이 '
                                                         '미치는 영향은 무엇인가요?',
                                                answer='피치의 신용등급 강등은 향후 3년간 '
                                                       '미국의 재정 악화가 예상되고, 국가 부채 '
                                                       '부담 증가와 거버넌스 악화를 반영한 '
                                                       '것입니다. 3대 국제 신용평가사가 미국의 '
                                                       '국가신용등급을 강등한 것은 2011년 '
                                                       '이후 12년 만에 처음입니다.'),
                                            QnA(question='미국 국가신용등급 강등은 2011년 '
                                                         '강등과 비슷한 영향을 미칠까요?',
                                                answer='2011년 연방 부채 한도 채무 불이행과 '
                                                       '2008년 글로벌 금융 위기의 근접성, '
                                                       '그리고 지난 5월 미국의 국가 신용등급 '
                                                       "전망을 ''부정적 관찰 대상''으로 "
                                                       '지정하면서 이미 신용등급 강등을 경고한 '
                                                       '바 있다는 점을 고려할 때 피치의 미국 '
                                                       '신용등급 강등에 따른 영향은 제한적일 '
                                                       '것이라는 주장이 설득력을 얻고 있습니다. '
                                                       '또한 미국 경제는 현재 연착륙하고 '
                                                       '있습니다.'),
                                            QnA(question='미국 국가신용등급 강등에 대한 시장의 '
                                                         '반응은 어땠나요?',
                                                answer='신용등급 강등에 대한 시장 반응은 비교적 '
                                                       '차분했습니다. S&P 500 및 나스닥 '
                                                       '종합지수 선물은 0.5% 미만 하락했고, '
                                                       '미국 국채 10년물 수익률은 소폭 '
                                                       '하락했습니다. 그러나 투자자들이 안전자산 '
                                                       '선호 현상으로 인해 위험한 아시아 '
                                                       '시장에서 자금을 회수하면서 아시아 주식과 '
                                                       '통화는 큰 타격을 받았습니다.'),
                                            QnA(question='미국 국가신용등급 강등 이후 주요 '
                                                         '관심사는 무엇인가요?',
                                                answer='최근 소강상태를 보였던 달러 강세가 다시 '
                                                       '회복되고 있기 때문에 주요 초점은 환율에 '
                                                       '맞춰져 있습니다. 달러 강세는 국내 '
                                                       '인플레이션을 해외로 수출하는 데 도움이 '
                                                       '될 수 있으며, 미국 국채에 대한 수요가 '
                                                       '증가하면 국채 금리가 낮아져 정부의 이자 '
                                                       '부담이 줄어듭니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://cdn.mindlenews.com/news/thumbnail/202308/4446_11292_2019_v150.jpg',
                              source='시민언론 민들레'),
                 ArticleImage(url='https://image.imnews.imbc.com/replay/2023/nw930/article/__icsFiles/afieldfile/2023/08/03/0930_20230803_093536_1_4_Large.jpg',
                              source='MBC뉴스')]),
 Article(category='Entertainment',
         keywords='고딩엄빠 인플루언서',
         contents=[ArticleContent(title="'GoDaddy4' influencer's ex-husband "
                                        "'Assaulted his full-term wife? I got "
                                        "beaten up'",
                                  lead="Ryu Hye-lin 'Ex-husband, habitual "
                                       'drunkenness, assault, and verbal '
                                       "abuse'...'Give child support to "
                                       "yourself' Ex-husband A 'No evidence "
                                       "that I didn't hit him', 'I deposit "
                                       'child support every month, pay '
                                       "everything I owe'",
                                  body1='',
                                  body2="Ryu Hye-lin appeared on 'Going Dad 4' "
                                        "and exposed her ex-husband, a '1.6 "
                                        "million influencer', while ex-husband "
                                        'A refuted the broadcast content and '
                                        'said...',
                                  qna_list=[QnA(question='What is the '
                                                         'controversy '
                                                         'surrounding Ryu '
                                                         'Hye-lin and her '
                                                         'ex-husband?',
                                                answer='The controversy '
                                                       'revolves around '
                                                       'accusations of '
                                                       'assault, habitual '
                                                       'drunkenness, and '
                                                       'verbal abuse made by '
                                                       'Ryu Hye-lin against '
                                                       'her ex-husband, who is '
                                                       'a popular influencer. '
                                                       'Her ex-husband denies '
                                                       'these allegations.'),
                                            QnA(question='What did Ryu Hye-lin '
                                                         "reveal on 'Going Dad "
                                                         "4'?",
                                                answer='On the show, Ryu '
                                                       'Hye-lin shared details '
                                                       'of the alleged abuse '
                                                       'she experienced during '
                                                       'her marriage and '
                                                       'explained the reasons '
                                                       'for their divorce. She '
                                                       'also discussed the '
                                                       'challenges of being a '
                                                       'young mother.'),
                                            QnA(question='How did her '
                                                         'ex-husband respond '
                                                         'to the allegations?',
                                                answer='Her ex-husband '
                                                       'countered the claims, '
                                                       'saying that he was '
                                                       'also a victim of '
                                                       'physical violence and '
                                                       'that the broadcast '
                                                       'misrepresented the '
                                                       'facts. He maintains '
                                                       'that he has paid child '
                                                       'support regularly.')],
                                  language='EN-US'),
                   ArticleContent(title="GoDaddy4 ''影响者的前夫 ''殴打了他已满月的妻子？我被打了",
                                  lead="Ryu Hye-lin ''前夫，习惯性酗酒、殴打和辱骂''...... "
                                       "''把孩子的抚养费给你自己''，前夫A "
                                       "''没有证据证明我没有打他''，''我每个月都存孩子的抚养费，欠的都还了''。",
                                  body1='',
                                  body2="柳惠琳在《加油！爸爸4》节目中曝光了 ''160万影响力 "
                                        "''的前夫，而前夫A则对节目内容进行了反驳，并表示...",
                                  qna_list=[QnA(question='围绕 Ryu Hye-lin '
                                                         '和她前夫的争议是什么？',
                                                answer='争议的焦点是 Ryu Hye-lin '
                                                       '对其前夫的指控，她的前夫是一位很有影响力的人物，被指控殴打、习惯性酗酒和辱骂。她的前夫否认了这些指控。'),
                                            QnA(question='柳惠麟在《加油！爸爸 4》中透露了什么？',
                                                answer='在节目中，Ryu Hye-lin '
                                                       '分享了她在婚姻中遭受虐待的细节，并解释了他们离婚的原因。她还谈到了作为年轻母亲所面临的挑战。'),
                                            QnA(question='她的前夫是如何回应这些指控的？',
                                                answer='她的前夫反驳说，他也是身体暴力的受害者，广播歪曲了事实。他坚称自己定期支付子女抚养费。')],
                                  language='ZH'),
                   ArticleContent(title="''고대디4'' 인플루언서 전남편 ''만삭 아내 폭행? 맞았다''",
                                  lead="류혜린 ''전남편, 상습적 음주-폭행-언어폭력''...''양육비 직접 "
                                       "내놔'' 전남편 A씨 ''때리지 않았다는 증거 없다'', ''매달 "
                                       "양육비 입금, 빚진 것 다 갚고 있다''",
                                  body1='',
                                  body2="류혜린이 ''아빠 어디가4''에 출연해 ''160만 인플루언서''인 "
                                        '전남편에 대해 폭로한 가운데, 전남편 A씨는 방송 내용을 반박하며 '
                                        '이렇게 말했습니다.',
                                  qna_list=[QnA(question='류혜린과 전남편을 둘러싼 논란은 '
                                                         '무엇인가요?',
                                                answer='이번 논란은 류혜린이 유명 인플루언서인 '
                                                       '전남편에게 폭행, 상습적인 음주, 폭언을 '
                                                       '했다는 의혹을 둘러싸고 불거졌습니다. '
                                                       '류혜린의 전남편은 이러한 의혹을 부인하고 '
                                                       '있습니다.'),
                                            QnA(question="류혜린은 ''아빠 어디가4''에서 "
                                                         '어떤 사연을 공개했나요?',
                                                answer='이날 방송에서 류혜린은 결혼 생활 중 '
                                                       '겪은 학대 의혹에 대해 상세히 밝히고 '
                                                       '이혼 사유에 대해 설명했습니다. 또한 '
                                                       '젊은 엄마로서 겪는 어려움에 대해서도 '
                                                       '이야기했습니다.'),
                                            QnA(question='전남편은 이 혐의에 대해 어떻게 '
                                                         '대응했나요?',
                                                answer='그녀의 전남편은 자신도 신체적 폭력의 '
                                                       '피해자이며 방송이 사실을 잘못 전달했다고 '
                                                       '주장하며 반박했습니다. 그는 자신이 '
                                                       '정기적으로 양육비를 지급했다고 '
                                                       '주장합니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://thumb.mt.co.kr/21/2023/08/2023080315281096391_1.jpg',
                              source='머니투데이'),
                 ArticleImage(url='https://biz.chosun.com/resizer/05acUJnyE3jGHLJS_ZOJlEIGW24=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/NSVL4RQTYM6BQS3RFXHG5QEFDI.jpg',
                              source='조선비즈')])]

########################## STEP 6 ##########################
step6 = [Folder(today=datetime.date(2023, 8, 5),
        folder_name='Knife-Attack-at-Daej',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: 'Knife Attack at Daejeon High School: Suspect "
                         "Arrested'\n"
                         "description: 'A man in his 20s brandished a knife at "
                         'a teacher in his 40s at a high school in Daejeon. '
                         'The suspect was caught within two hours, and police '
                         'investigations revealed intriguing details about the '
                         "suspect's past.'\n"
                         "category: 'Crime'\n"
                         "keywords: '대전 칼부림,대전 고등학교 칼부림,대전,대전 대덕구 칼부림'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/replay/2023/nwtoday/article/__icsFiles/afieldfile/2023/08/05/today_20230805_071028_1_6_Large.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'A man in his 20s brandished a knife at a teacher in '
                         'his 40s at a high school in Daejeon. The suspect was '
                         'caught within two hours, and police investigations '
                         "revealed intriguing details about the suspect's "
                         'past.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. What happened at the high school '
                         'in Daejeon?</b></summary>\n'
                         '    A man in his 20s brandished a knife at a teacher '
                         'in his 40s.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. Was the suspect '
                         'caught?</b></summary>\n'
                         '    Yes, the police caught the suspect within two '
                         'hours.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. What did the suspect reveal about '
                         'his past?</b></summary>\n'
                         '    The suspect told police that he had been a '
                         'priest.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. How did the suspect enter the '
                         'school without being stopped?</b></summary>\n'
                         '    The suspect entered the school without being '
                         'stopped by the learning guard at the main gate.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. What happened to the victim '
                         'teacher?</b></summary>\n'
                         '    The victim teacher was taken to a hospital and '
                         'underwent emergency surgery.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>5. Where was the suspect '
                         'caught?</b></summary>\n'
                         '    The suspect was caught on a nearby road two '
                         'hours after the crime.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>6. What is the next step in the '
                         'investigation?</b></summary>\n'
                         '    Police plan to further investigate the motive '
                         'and circumstances of the crime.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## Knife Attack at Daejeon High School: Suspect '
                         'Arrested\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'At a high school in Daejeon, a man in his 20s '
                         'brandished a weapon at a teacher in his 40s. The '
                         'suspect was caught within two hours and told police '
                         'he had been a priest in the past. According to the '
                         'police, the suspect entered the school without being '
                         'stopped by the learning guard at the main gate. He '
                         'then sought out a teacher in the staff room and '
                         'attacked the teacher with the weapon.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://www.goodmorningcc.com/news/thumbnail/202308/293936_325538_1955_v150.jpg" '
                         'alt="굿모닝충청" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 굿모닝충청</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'The victim teacher was taken to a hospital and '
                         'underwent emergency surgery. Police caught the '
                         'suspect on a nearby road two hours after the crime. '
                         'When questioned about the motive for the crime, the '
                         'suspect remained silent. Police plan to further '
                         'investigate the motive and circumstances of the '
                         'crime.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '大田高中发生持刀袭击事件：嫌犯被捕'\n"
                         "description: '一名 20 多岁的男子在大田一所高中向一名 40 "
                         "多岁的教师挥刀。嫌犯在两小时内被抓获，警方调查发现了嫌犯过去的一些耐人寻味的细节。'\n"
                         "category: 'Crime'\n"
                         "keywords: '대전 칼부림,대전 고등학교 칼부림,대전,대전 대덕구 칼부림'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/replay/2023/nwtoday/article/__icsFiles/afieldfile/2023/08/05/today_20230805_071028_1_6_Large.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '一名 20 多岁的男子在大田一所高中向一名 40 '
                         '多岁的教师挥刀。嫌犯在两小时内被抓获，警方调查发现了嫌犯过去的一些耐人寻味的细节。\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 大田高中发生了什么事？</b></summary>\n'
                         '    一名 20 多岁的男子向一名 40 多岁的教师挥刀。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 嫌犯抓到了吗？</b></summary>\n'
                         '    是的，警方在两小时内就抓住了嫌疑人。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 嫌疑人透露了他的哪些过去？</b></summary>\n'
                         '    嫌疑人告诉警方，他曾是一名牧师。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 嫌疑人是如何进入学校而未被拦截的？</b></summary>\n'
                         '    嫌疑人进入学校时没有被大门口的学习卫兵拦住。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 受害教师怎么了？</b></summary>\n'
                         '    受害教师被送往医院，接受了紧急手术。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>5. 嫌犯在哪里落网？</b></summary>\n'
                         '    案发两小时后，嫌疑人在附近公路上落网。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>6. 调查的下一步是什么？</b></summary>\n'
                         '    警方计划进一步调查犯罪动机和犯罪情节。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 大田高中发生持刀袭击事件：嫌犯被捕\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '在大田的一所高中，一名 20 多岁的男子向一名 40 '
                         '多岁的教师挥舞武器。嫌犯在两小时内落网，他告诉警方自己过去曾是一名牧师。据警方称，嫌疑人进入学校时没有被大门口的保安拦住。随后，他在教员室找到一名教师，并用武器袭击了这名教师。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://www.goodmorningcc.com/news/thumbnail/202308/293936_325538_1955_v150.jpg" '
                         'alt="굿모닝충청" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 굿모닝충청</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '受害教师被送往医院，接受了紧急手术。案发两小时后，警方在附近公路上抓获了嫌疑人。当被问及犯罪动机时，嫌疑人保持沉默。警方计划进一步调查犯罪动机和犯罪情节。\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '대전 고등학교에서 칼부림 사건 발생: 용의자 검거'\n"
                         "description: '대전의 한 고등학교에서 20대 남성이 40대 교사에게 칼을 휘두른 "
                         '사건이 발생했습니다. 용의자는 2시간 만에 붙잡혔고, 경찰 조사 결과 용의자의 과거에 대한 '
                         "흥미로운 내용이 밝혀졌습니다.'\n"
                         "category: 'Crime'\n"
                         "keywords: '대전 칼부림,대전 고등학교 칼부림,대전,대전 대덕구 칼부림'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/replay/2023/nwtoday/article/__icsFiles/afieldfile/2023/08/05/today_20230805_071028_1_6_Large.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '대전의 한 고등학교에서 20대 남성이 40대 교사에게 칼을 휘두른 사건이 발생했습니다. '
                         '용의자는 2시간 만에 붙잡혔고, 경찰 조사 결과 용의자의 과거에 대한 흥미로운 내용이 '
                         '밝혀졌습니다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 대전의 한 고등학교에서 무슨 일이 '
                         '있었나요?</b></summary>\n'
                         '    20대 남성이 40대 교사에게 칼을 휘두른 사건이 발생했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 용의자가 잡혔나요?</b></summary>\n'
                         '    네, 경찰은 2시간 만에 용의자를 체포했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 용의자가 자신의 과거에 대해 밝힌 내용은 '
                         '무엇인가요?</b></summary>\n'
                         '    용의자는 경찰에 자신이 성직자였다고 진술했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 용의자는 어떻게 제지당하지 않고 학교에 들어갈 수 '
                         '있었나요?</b></summary>\n'
                         '    용의자는 정문에서 학습 경비원의 제지를 받지 않고 학교로 들어갔습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 피해 교사는 어떻게 되었나요?</b></summary>\n'
                         '    피해 교사는 병원으로 이송되어 응급 수술을 받았습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>5. 용의자는 어디에서 잡혔나요?</b></summary>\n'
                         '    용의자는 범행 2시간 후 인근 도로에서 붙잡혔습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>6. 조사의 다음 단계는 무엇인가요?</b></summary>\n'
                         '    경찰은 범행 동기와 경위 등을 추가로 조사할 계획입니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 대전 고등학교에서 칼부림 사건 발생: 용의자 검거\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '대전의 한 고등학교에서 20대 남성이 40대 교사에게 흉기를 휘두른 사건이 발생했습니다. '
                         '용의자는 2시간 만에 붙잡혔고, 과거에 성직자였다고 경찰에 진술했습니다. 경찰에 따르면 '
                         '용의자는 정문에서 배움터 지킴이에게 제지당하지 않고 학교로 들어갔다고 합니다. 그런 다음 '
                         '교무실에 있는 교사를 찾아 흉기로 교사를 공격했습니다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://www.goodmorningcc.com/news/thumbnail/202308/293936_325538_1955_v150.jpg" '
                         'alt="굿모닝충청" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 굿모닝충청</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '피해 교사는 병원으로 이송되어 응급 수술을 받았습니다. 경찰은 범행 2시간 후 인근 도로에서 '
                         '용의자를 붙잡았습니다. 범행 동기에 대한 질문에 용의자는 묵묵부답으로 일관했습니다. 경찰은 '
                         '범행 동기와 경위 등을 추가로 조사할 계획입니다.\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='Arrests-Made-at-Gang',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: 'Arrests Made at Gangnam High-Speed Terminal "
                         "with Weapons'\n"
                         "description: 'A man in his 20s was apprehended at "
                         'Gangnam Express Bus Terminal in Seoul for carrying '
                         'weapons, raising concerns about a potential crime '
                         "spree.'\n"
                         "category: 'Crime'\n"
                         "keywords: '고속터미널,고속터미널 흉기'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://news.kbs.co.kr/data/news/2023/08/04/20230804_vxxJFM.jpg" '
                         'alt="KBS뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from KBS뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'A man in his 20s was apprehended at Gangnam Express '
                         'Bus Terminal in Seoul for carrying weapons, raising '
                         'concerns about a potential crime spree.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. Who was arrested at Gangnam '
                         'Express Bus Terminal?</b></summary>\n'
                         '    A man in his 20s, known as Mr. A, was '
                         'apprehended at the terminal.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. What weapons did the arrested man '
                         'have?</b></summary>\n'
                         '    The man was found in possession of a knife and a '
                         'toy gun.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. Were there any casualties or '
                         'injuries?</b></summary>\n'
                         '    Fortunately, there were no casualties or '
                         'injuries reported in this incident.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. What is the current status of the '
                         'investigation?</b></summary>\n'
                         '    The police are currently investigating the '
                         'incident and the motive behind it.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## Arrests Made at Gangnam High-Speed Terminal with '
                         'Weapons\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'The Seocho Police Station in Seoul reported that '
                         'they arrested a man, identified as Mr. A, in his 20s '
                         'at the Gangnam Express Bus Terminal. The arrest was '
                         'made after a security guard alerted the police about '
                         'a man carrying a weapon near the terminal. Within '
                         'six minutes of receiving the report, the police were '
                         'able to apprehend the suspect.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/society/article/__icsFiles/afieldfile/2023/08/04/R230804-24.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'It was discovered that the man had a knife and a toy '
                         'gun in his bag. Fortunately, he did not use the '
                         'weapons to harm anyone. The police are currently '
                         'investigating the incident and the motive behind '
                         'it.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '江南高速客运站逮捕携带武器者'\n"
                         "description: '一名 20 "
                         "多岁的男子因携带武器在首尔江南高速巴士客运站被捕，引发了人们对潜在犯罪狂潮的担忧。'\n"
                         "category: 'Crime'\n"
                         "keywords: '고속터미널,고속터미널 흉기'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://news.kbs.co.kr/data/news/2023/08/04/20230804_vxxJFM.jpg" '
                         'alt="KBS뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from KBS뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '一名 20 多岁的男子因携带武器在首尔江南高速巴士客运站被捕，引发了人们对潜在犯罪狂潮的担忧。\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 谁在江南长途汽车客运站被捕？</b></summary>\n'
                         '    一名 20 多岁的男子（被称为 A 先生）在终点站被捕。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 被捕者携带了什么武器？</b></summary>\n'
                         '    该男子被发现持有一把刀和一把玩具枪。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 有人员伤亡吗？</b></summary>\n'
                         '    幸运的是，此次事件中没有人员伤亡报告。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 调查的现状如何？</b></summary>\n'
                         '    警方目前正在调查这起事件及其背后的动机。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 江南高速客运站逮捕携带武器者\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '首尔瑞草警察局报告称，他们在江南高速汽车客运站逮捕了一名 20 多岁的男子，此人名叫 A '
                         '先生。警方是在一名保安员向警方报告有一名男子在终点站附近携带武器后实施逮捕的。警方在接到报告后 6 '
                         '分钟内就逮捕了嫌疑人。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/society/article/__icsFiles/afieldfile/2023/08/04/R230804-24.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '人们发现，这名男子的包里有一把刀和一把玩具枪。幸运的是，他没有使用这些武器伤害任何人。警方目前正在调查这起事件及其背后的动机。\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '강남 고속터미널에서 흉기 소지 피의자 검거'\n"
                         "description: '서울 강남고속버스터미널에서 20대 남성이 흉기를 소지한 혐의로 "
                         "검거되어 잠재적 범죄 행위에 대한 우려가 커지고 있습니다.'\n"
                         "category: 'Crime'\n"
                         "keywords: '고속터미널,고속터미널 흉기'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://news.kbs.co.kr/data/news/2023/08/04/20230804_vxxJFM.jpg" '
                         'alt="KBS뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from KBS뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '서울 강남고속버스터미널에서 20대 남성이 흉기를 소지한 혐의로 검거되어 잠재적 범죄 행위에 '
                         '대한 우려가 커지고 있습니다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 강남고속버스터미널에서 체포된 사람은 '
                         '누구인가요?</b></summary>\n'
                         '    A씨로 알려진 20대 남성이 터미널에서 체포되었습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 체포된 남성은 어떤 무기를 소지하고 '
                         '있었나요?</b></summary>\n'
                         '    이 남성은 칼과 장난감 총을 소지한 채 발견되었습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 사상자나 부상자가 있었나요?</b></summary>\n'
                         '    다행히 이번 사건으로 인한 사상자나 부상자는 보고되지 않았습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 현재 조사 진행 상황은 어떻게 '
                         '되나요?</b></summary>\n'
                         '    경찰은 현재 사건의 경위와 범행 동기를 조사하고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 강남 고속터미널에서 흉기 소지 피의자 검거\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '서울 서초경찰서는 강남고속버스터미널에서 20대 남성 A씨를 검거했다고 밝혔습니다. 이번 검거는 '
                         '터미널 근처에 흉기를 든 남성이 있다는 경비원의 신고를 받고 출동한 경찰에 의해 '
                         '이루어졌습니다. 신고를 받은 경찰은 6분 만에 용의자를 검거할 수 있었습니다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/society/article/__icsFiles/afieldfile/2023/08/04/R230804-24.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '이 남성은 가방에 칼과 장난감 총을 가지고 있었던 것으로 밝혀졌습니다. 다행히도 그는 무기를 '
                         '사용하여 사람을 해치지는 않았습니다. 경찰은 현재 사건 경위와 범행 동기를 조사하고 '
                         '있습니다.\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='A-Hair-on-the-Wheel-',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: ''A Hair on the Wheel' - Rolls-Royce Accident "
                         "at Apgujeong Station'\n"
                         "description: 'A Rolls-Royce SUV worth 600 million "
                         'won crashed into a sidewalk near Apgujeong Station '
                         'in Seoul, severely injuring a woman in her 20s. The '
                         'incident was covered by the YouTube channel '
                         "'Caracula Detective Agency' which released photos of "
                         'the scene and the driver involved. The victim '
                         "suffered a broken leg in the accident.'\n"
                         "category: 'Accidents'\n"
                         "keywords: '롤스로이스 사고'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://res.heraldm.com/content/image/2023/08/03/20230803000139_p.jpg" '
                         'alt="헤럴드경제" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 헤럴드경제</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'A Rolls-Royce SUV worth 600 million won crashed into '
                         'a sidewalk near Apgujeong Station in Seoul, severely '
                         'injuring a woman in her 20s. The incident was '
                         "covered by the YouTube channel 'Caracula Detective "
                         "Agency' which released photos of the scene and the "
                         'driver involved. The victim suffered a broken leg in '
                         'the accident.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. What happened at Apgujeong '
                         'Station?</b></summary>\n'
                         '    A Rolls-Royce SUV crashed into a sidewalk near '
                         'Apgujeong Station, severely injuring a woman in her '
                         '20s.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. Who covered the '
                         'accident?</b></summary>\n'
                         "    The YouTube channel 'Caracula Detective Agency' "
                         'provided coverage of the accident.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. What evidence was found at the '
                         'scene?</b></summary>\n'
                         '    Debris from the crash included strands of hair '
                         'believed to belong to the victim.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>3. What was the driver's behavior "
                         'after the accident?</b></summary>\n'
                         '    The driver, who had full-body tattoos, acted '
                         'threateningly towards the police officers and seemed '
                         'unconcerned about the injured victim.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. What were the injuries sustained '
                         'by the victim?</b></summary>\n'
                         '    The victim suffered a broken leg and head and '
                         'stomach injuries.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## 'A Hair on the Wheel' - Rolls-Royce Accident at "
                         'Apgujeong Station\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'A Rolls-Royce SUV collided with a sidewalk near '
                         'Apgujeong Station in Gangnam-gu, Seoul, causing '
                         'serious injuries to a woman in her 20s. The incident '
                         'took place at around 8:10 p.m. on April 2. The '
                         "YouTube channel 'Caracula Detective Agency' provided "
                         'coverage of the accident and shared photos showing '
                         'the driver, a 28-year-old individual named A, '
                         'exiting the vehicle and the woman trapped beneath '
                         'the car. The debris from the crash displayed a few '
                         'strands of hair believed to belong to the victim.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://news.imaeil.com/photos/2023/08/05/2023080507281692897_l.jpg" '
                         'alt="매일신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 매일신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'The driver, who had full-body tattoos, reportedly '
                         'acted threateningly towards the police officers at '
                         "the scene. Despite bystanders' warnings, the driver "
                         'accelerated, leaving the victim in a critical '
                         'condition. The victim underwent surgery for a broken '
                         'leg and head and stomach injuries. The driver tested '
                         'positive for ketamine in a drug test and is '
                         'currently under investigation.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '车轮上的一根头发''--劳斯莱斯在狎鸥亭站发生事故'\n"
                         "description: '一辆价值 6 亿韩元的劳斯莱斯 SUV "
                         '在首尔狎鸥亭站附近撞上人行道，造成一名 20 多岁的妇女严重受伤。YouTube 频道 '
                         "''Caracula Detective Agency "
                         "''报道了这一事件，并发布了现场照片和肇事司机的照片。受害者在事故中腿部骨折。'\n"
                         "category: 'Accidents'\n"
                         "keywords: '롤스로이스 사고'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://res.heraldm.com/content/image/2023/08/03/20230803000139_p.jpg" '
                         'alt="헤럴드경제" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 헤럴드경제</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '一辆价值 6 亿韩元的劳斯莱斯 SUV 在首尔狎鸥亭站附近撞上人行道，造成一名 20 '
                         "多岁的妇女严重受伤。YouTube 频道 ''Caracula Detective Agency "
                         "''报道了这一事件，并发布了现场照片和肇事司机的照片。受害者在事故中腿部骨折。\n"
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 狎鸥亭站发生了什么事？</b></summary>\n'
                         '    一辆劳斯莱斯越野车在狎鸥亭站附近撞上人行道，造成一名 20 多岁的妇女严重受伤。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 谁负责事故赔偿？</b></summary>\n'
                         "    YouTube 频道 'Caracula Detective Agency "
                         "'对事故进行了报道。\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 现场发现了哪些证据？</b></summary>\n'
                         '    坠机碎片中包括据信属于受害者的几缕头发。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 事故发生后，司机的行为如何？</b></summary>\n'
                         '    这名全身刺青的司机对警察进行威胁，似乎并不关心受伤的受害者。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 受害者受了什么伤？</b></summary>\n'
                         '    受害者腿部骨折，头部和腹部受伤。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## 车轮上的一根头发''--劳斯莱斯在狎鸥亭站发生事故\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '一辆劳斯莱斯 SUV 在首尔江南区狎鸥亭站附近与人行道相撞，造成一名 20 '
                         '多岁的妇女严重受伤。事故发生在 4 月 2 日晚上 8 点 10 分左右。YouTube 频道 '
                         "'Caracula Detective Agency '对事故进行了报道，并分享了驾驶员（28 岁，名叫 "
                         'A）下车和被困在车下的女子的照片。车祸中的碎片显示了几缕据信属于受害者的头发。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://news.imaeil.com/photos/2023/08/05/2023080507281692897_l.jpg" '
                         'alt="매일신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 매일신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '据报道，这名全身刺青的司机对现场的警察进行了威胁。尽管旁观者发出了警告，但司机还是加速行驶，导致受害者生命垂危。受害者因腿部骨折、头部和胃部受伤接受了手术。该司机在毒品测试中氯胺酮检测呈阳性，目前正在接受调查。\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '''바퀴에 머리카락'' - 압구정역 롤스로이스 사고'\n"
                         "description: '서울 압구정역 인근 인도에서 6억 원 상당의 롤스로이스 SUV 차량이 "
                         '인도로 추락해 20대 여성이 중상을 입는 사고가 발생했습니다. 이 사건은 유튜브 채널 '
                         "''카라큘라 탐정단''이 현장 사진과 가해 운전자의 모습을 공개하면서 알려졌습니다. 피해자는 "
                         "이 사고로 다리가 부러지는 부상을 입었습니다.'\n"
                         "category: 'Accidents'\n"
                         "keywords: '롤스로이스 사고'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://res.heraldm.com/content/image/2023/08/03/20230803000139_p.jpg" '
                         'alt="헤럴드경제" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 헤럴드경제</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '서울 압구정역 인근 인도에서 6억 원 상당의 롤스로이스 SUV 차량이 인도로 추락해 20대 '
                         "여성이 중상을 입는 사고가 발생했습니다. 이 사건은 유튜브 채널 ''카라큘라 탐정단''이 현장 "
                         '사진과 가해 운전자의 모습을 공개하면서 알려졌습니다. 피해자는 이 사고로 다리가 부러지는 '
                         '부상을 입었습니다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 압구정역에서는 무슨 일이 '
                         '있었나요?</b></summary>\n'
                         '    압구정역 인근 인도에서 롤스로이스 SUV 차량이 인도를 들이받아 20대 여성이 중상을 '
                         '입는 사고가 발생했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 사고는 누가 보상하나요?</b></summary>\n'
                         "    유튜브 채널 '카라큘라 탐정 에이전시'에서 사고 현장을 취재했습니다.\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 현장에서 어떤 증거가 '
                         '발견되었나요?</b></summary>\n'
                         '    사고 잔해에는 희생자의 것으로 추정되는 머리카락이 포함되어 있었습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 사고 후 운전자의 행동은 '
                         '어땠나요?</b></summary>\n'
                         '    전신에 문신을 한 운전자는 경찰관에게 위협적인 행동을 보였고 다친 피해자에 대해서는 '
                         '전혀 신경 쓰지 않는 것처럼 보였습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 피해자가 입은 부상은 무엇인가요?</b></summary>\n'
                         '    피해자는 다리 골절과 머리 및 복부 부상을 입었습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## ''바퀴에 머리카락'' - 압구정역 롤스로이스 사고\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '서울 강남구 압구정역 인근에서 롤스로이스 SUV 차량이 인도와 충돌해 20대 여성이 중상을 '
                         '입는 사고가 발생했습니다. 사건은 4월 2일 오후 8시 10분경에 발생했습니다. 유튜브 채널 '
                         "'카라큘라 탐정단'은 사고 현장을 취재하며 운전자인 28세 A씨와 차에서 내리는 모습, 차 "
                         '밑에 갇힌 여성의 모습을 담은 사진을 공개했습니다. 사고 잔해에서 피해자의 것으로 추정되는 '
                         '머리카락 몇 가닥이 발견되었습니다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://news.imaeil.com/photos/2023/08/05/2023080507281692897_l.jpg" '
                         'alt="매일신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 매일신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '전신에 문신을 한 운전자는 현장에 출동한 경찰관에게 위협적인 행동을 한 것으로 알려졌습니다. '
                         '목격자들의 경고에도 불구하고 운전자는 속도를 높여 피해자를 위독한 상태에 빠뜨렸습니다. '
                         '피해자는 다리 골절과 머리 및 복부 부상으로 수술을 받았습니다. 운전자는 약물 검사에서 케타민 '
                         '양성 반응을 보였으며 현재 조사를 받고 있습니다.\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='Police-Station-and-B',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: ''Police Station and Bureau of Investigation "
                         "Next to Fire Station' Returns for Season 2'\n"
                         "description: 'SBS's 'The Police Station Next to the "
                         "Fire Station and Guk Gua Soo' will premiere on April "
                         "4 at 10 p.m. as a follow-up to 'Demon'.'\n"
                         "category: 'Entertainment'\n"
                         "keywords: '소방서 옆 경찰서 그리고 국과수'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://biz.chosun.com/resizer/T7PaBYXeO7JRRekZISLb1oOCsSE=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/2THYHQXKAZ4LLS2VCZLTKF47UA.jpg" '
                         'alt="조선비즈" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 조선비즈</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "SBS's 'The Police Station Next to the Fire Station "
                         "and Guk Gua Soo' will premiere on April 4 at 10 p.m. "
                         "as a follow-up to 'Demon'.\n"
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>0. When will 'The Police Station "
                         "Next to the Fire Station and Guk Gua Soo' "
                         'premiere?</b></summary>\n'
                         "    'The Police Station Next to the Fire Station and "
                         "Guk Gua Soo' will premiere on April 4 at 10 p.m.\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. How many episodes will Season 2 '
                         'have?</b></summary>\n'
                         '    Season 2 will be broadcast in 12 episodes.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. What will be the main focus of '
                         'Season 2?</b></summary>\n'
                         '    Season 2 will depict the upgraded cooperation of '
                         'firefighting, crime-fighting, and evidence-gathering '
                         'police officers.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. What happened at the end of '
                         'Season 1?</b></summary>\n'
                         "    Season 1 ended with a 'parking tower burial' and "
                         "the subsequent 'fight against a serial arsonist.'\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. What can viewers expect from '
                         'Season 2?</b></summary>\n'
                         '    Viewers can expect a series of near-disastrous '
                         'events and accidents in Season 2.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## 'Police Station and Bureau of Investigation Next "
                         "to Fire Station' Returns for Season 2\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "Season 2 of 'The Police Station Next to the Fire "
                         "Station and Guk Gua Soo' is a drama that depicts the "
                         'upgraded cooperation of firefighting, '
                         'crime-fighting, and evidence-gathering police '
                         'officers who face unprecedented and unprecedented '
                         'cases, and will be broadcast in 12 episodes.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558910_683707_2921_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Season 2 picks up where Season 1 left off with the '
                         "'parking tower burial' ending and the subsequent "
                         "'fight against a serial arsonist,' with a series of "
                         'near-disastrous events and accidents.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '消防局旁的警察局和调查局》第二季回归'\n"
                         "description: 'SBS《消防局隔壁的警察局和Guk Gua "
                         "Soo》将于4月4日晚10点首播，作为《恶魔》的后续节目。'\n"
                         "category: 'Entertainment'\n"
                         "keywords: '소방서 옆 경찰서 그리고 국과수'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://biz.chosun.com/resizer/T7PaBYXeO7JRRekZISLb1oOCsSE=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/2THYHQXKAZ4LLS2VCZLTKF47UA.jpg" '
                         'alt="조선비즈" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 조선비즈</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'SBS《消防局隔壁的警察局和Guk Gua Soo》将于4月4日晚10点首播，作为《恶魔》的后续节目。\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 消防局旁边的警察局和 Guk Gua '
                         'Soo》将于何时首播？</b></summary>\n'
                         '    消防局旁边的警察局和 Guk Gua Soo》将于 4 月 4 日晚 10 点首播。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 第二季有多少集？</b></summary>\n'
                         '    第二季将分 12 集播出。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 第二季的重点是什么？</b></summary>\n'
                         '    第二季将描述消防、打击犯罪和收集证据警察之间的升级合作。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 第一季结尾发生了什么？</b></summary>\n'
                         "    第一季以 '埋葬停车塔 '和随后的 '打击连环纵火犯 '结束。\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 观众对第二季有什么期待？</b></summary>\n'
                         '    观众可以期待在第二季中发生一系列近乎灾难性的事件和事故。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 消防局旁的警察局和调查局》第二季回归\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '消防局隔壁的派出所和郭瓜秀》第二季是一部描述消防、打击犯罪和收集证据的警察在面对前所未有的案件时升级合作的电视剧，将分 '
                         '12 集播出。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558910_683707_2921_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "第二季承接了第一季 '埋葬停车塔 '的结局和随后的 "
                         "'打击连环纵火犯'，发生了一系列险些酿成大祸的事件和事故。\n"),
             Markdown(language='KO',
                      md='---\n'
                         "title: '''소방서 옆 경찰서, 수사국''이 시즌2로 돌아옵니다.'\n"
                         "description: 'SBS ''소방서 옆 경찰서, 국과수''는 ''악마'' 후속으로 오는 "
                         "4월 4일 밤 10시에 첫 방송될 예정이다.'\n"
                         "category: 'Entertainment'\n"
                         "keywords: '소방서 옆 경찰서 그리고 국과수'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://biz.chosun.com/resizer/T7PaBYXeO7JRRekZISLb1oOCsSE=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/2THYHQXKAZ4LLS2VCZLTKF47UA.jpg" '
                         'alt="조선비즈" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 조선비즈</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "SBS ''소방서 옆 경찰서, 국과수''는 ''악마'' 후속으로 오는 4월 4일 밤 10시에 "
                         '첫 방송될 예정이다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>0. '소방서 옆 경찰서, 국과수'는 언제 "
                         '개봉하나요?</b></summary>\n'
                         "    '소방서 옆 경찰서, 국과수'는 오는 4월 4일 밤 10시에 첫 방송된다.\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 시즌 2는 몇 개의 에피소드로 '
                         '구성되나요?</b></summary>\n'
                         '    시즌 2는 12개의 에피소드로 방송될 예정입니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 시즌 2의 주요 초점은 '
                         '무엇인가요?</b></summary>\n'
                         '    시즌 2에서는 소방, 범죄 진압, 증거 수집 경찰관의 업그레이드된 협력이 그려질 '
                         '예정입니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 시즌 1이 끝났을 때 무슨 일이 '
                         '있었나요?</b></summary>\n'
                         "    시즌 1은 '주차 타워 매몰 사건'과 이어진 '연쇄 방화범과의 싸움'으로 끝났습니다.\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 시즌 2에서 시청자는 무엇을 기대할 수 '
                         '있나요?</b></summary>\n'
                         '    시즌 2에서는 재앙에 가까운 사건과 사고가 연이어 발생할 것으로 예상됩니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## ''소방서 옆 경찰서, 수사국''이 시즌2로 돌아옵니다.\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "'소방서 옆 경찰서, 국과수' 시즌2는 전대미문의 초유의 사건에 맞닥뜨린 소방, 강력, "
                         '증거수집 경찰관들의 업그레이드된 공조 수사를 그린 드라마로, 총 12부작으로 방송될 '
                         '예정이다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558910_683707_2921_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "시즌 2는 '주차 타워 매몰 사건'의 결말과 그 이후의 '연쇄 방화범과의 싸움'으로 시즌 "
                         '1에서 시작하여 재앙에 가까운 사건과 사고의 연속으로 이어집니다.\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='Intensive-Rainfall-L',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: 'Intensive Rainfall Leaves Gyeongsangbuk-do "
                         'Region in Urgent Need of Precautions and Port '
                         "Restoration'\n"
                         "description: 'Almost three weeks after heavy rains "
                         'caused significant damage to the northern '
                         'Gyeongsangbuk-do region, authorities are emphasizing '
                         'the importance of taking preventive measures and '
                         'restoring ports to address the increasing frequency '
                         "of such disasters.'\n"
                         "category: 'World/International'\n"
                         "keywords: '뉴스'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://news.kbs.co.kr/data/news/title_image/newsmp4/daegu/news9/2023/08/04/50_7741234.jpg" '
                         'alt="KBS뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from KBS뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Almost three weeks after heavy rains caused '
                         'significant damage to the northern Gyeongsangbuk-do '
                         'region, authorities are emphasizing the importance '
                         'of taking preventive measures and restoring ports to '
                         'address the increasing frequency of such disasters.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. What caused the major damage in '
                         'the northern Gyeongsangbuk-do region?</b></summary>\n'
                         '    The major damage in the northern '
                         'Gyeongsangbuk-do region was caused by torrential '
                         'rains.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. What is Gyeongsangbuk-do doing to '
                         'address the increasing frequency of '
                         'disasters?</b></summary>\n'
                         '    Gyeongsangbuk-do is taking preventive measures '
                         'and restoring ports to address the increasing '
                         'frequency of disasters.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. What is the emergency restoration '
                         'rate for the intensive rainfall?</b></summary>\n'
                         '    The emergency restoration rate for the intensive '
                         'rainfall is 89.8% overall, including 98.2% for roads '
                         'and bridges.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. What action is Gyeongsangbuk-do '
                         'taking through the Landslide Response System '
                         'Innovation Task Force?</b></summary>\n'
                         '    Gyeongsangbuk-do is planning to build disaster '
                         'prevention villages, conduct a large-scale safety '
                         'diagnosis, and improve warning, evacuation, and '
                         'rescue systems through the Landslide Response System '
                         'Innovation Task Force.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. What is the importance of '
                         'permanent recovery plans and disaster '
                         'preparedness?</b></summary>\n'
                         '    The extent of the damage caused by extreme '
                         'weather events depends on how well permanent '
                         'recovery plans and disaster preparedness are '
                         'established.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## Intensive Rainfall Leaves Gyeongsangbuk-do Region '
                         'in Urgent Need of Precautions and Port Restoration\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "It's been almost three weeks since torrential rains "
                         'caused major damage in northern Gyeongsangbuk-do. '
                         'Gyeongsangbuk-do believes that disasters that may or '
                         'may not come once in 50 or 100 years will become '
                         'more frequent in the future, and is taking this '
                         'opportunity to prepare a solid alternative. The '
                         'emergency restoration rate for this intensive '
                         'rainfall is 89.8% overall, including 98.2% for roads '
                         'and bridges. Now that emergency restoration is in '
                         'its final stages, attention is shifting to port '
                         'restoration and preventive measures.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://yonhapnewstv-prod.s3.ap-northeast-2.amazonaws.com/article/MYH/20230804/MYH20230804026100641_P1.jpg" '
                         'alt="연합뉴스TV" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 연합뉴스TV</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Gyeongsangbuk-do is taking action through the '
                         'Landslide Response System Innovation Task Force, '
                         'saying the heavy rains have shown that there are no '
                         'safe zones. It plans to build disaster prevention '
                         'villages that can prevent landslides, and will begin '
                         'a large-scale safety diagnosis of risk factors such '
                         'as artificial objects in the mountains. In addition, '
                         'we will improve the warning, evacuation, and rescue '
                         'and relief systems so that rapid dissemination and '
                         'evacuation can be carried out in actual situations. '
                         'With extreme weather events such as extreme '
                         'downpours becoming an everyday occurrence, the '
                         'extent of the damage will depend on how well we '
                         'establish permanent recovery plans and disaster '
                         'preparedness.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '强降雨导致庆尚北道地区急需采取预防措施和恢复港口'\n"
                         'description: '
                         "'在暴雨给庆尚北道北部地区造成重大损失近三周后，当局强调了采取预防措施和恢复港口的重要性，以应对日益频繁的此类灾害。'\n"
                         "category: 'World/International'\n"
                         "keywords: '뉴스'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://news.kbs.co.kr/data/news/title_image/newsmp4/daegu/news9/2023/08/04/50_7741234.jpg" '
                         'alt="KBS뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from KBS뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '在暴雨给庆尚北道北部地区造成重大损失近三周后，当局强调了采取预防措施和恢复港口的重要性，以应对日益频繁的此类灾害。\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. '
                         '是什么造成了庆尚北道北部地区的重大损失？</b></summary>\n'
                         '    庆尚北道北部地区的主要损失是由暴雨造成的。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 庆尚北道如何应对日益频繁的灾害？</b></summary>\n'
                         '    庆尚北道正在采取预防措施并恢复港口，以应对日益频繁的灾害。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 强降雨的紧急恢复率是多少？</b></summary>\n'
                         '    强降雨的紧急恢复率总体为 89.8%，其中道路和桥梁的紧急恢复率为 98.2%。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. '
                         '庆尚北道通过滑坡应对系统创新工作组采取了哪些行动？</b></summary>\n'
                         '    '
                         '庆尚北道正计划建设防灾村，进行大规模安全诊断，并通过滑坡应对系统创新工作组完善预警、疏散和救援系统。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. '
                         '永久恢复计划和灾难准备的重要性是什么？</b></summary>\n'
                         '    极端天气事件造成的破坏程度取决于永久性恢复计划和备灾工作做得如何。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 强降雨导致庆尚北道地区急需采取预防措施和恢复港口\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '自暴雨在庆尚北道北部造成重大损失以来，已经过去了近三个星期。庆尚北道认为，50 年或 100 '
                         '年不一定会发生一次的灾害今后会越来越频繁，并借此机会准备了坚实的替代措施。此次强降雨的紧急恢复率总体为 '
                         '89.8%，其中道路和桥梁的紧急恢复率为 '
                         '98.2%。目前，紧急修复工作已进入最后阶段，注意力正转向港口修复和预防措施。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://yonhapnewstv-prod.s3.ap-northeast-2.amazonaws.com/article/MYH/20230804/MYH20230804026100641_P1.jpg" '
                         'alt="연합뉴스TV" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 연합뉴스TV</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '庆尚北道正在通过山体滑坡应对系统革新工作组采取行动，称暴雨表明没有安全区。庆尚北道计划建设能够预防山体滑坡的防灾村，并开始对山体中的人工物体等危险因素进行大规模安全诊断。此外，我们还将完善预警、避难和抢险救灾系统，以便在实际情况下进行快速传播和避难。随着特大暴雨等极端天气事件的日常化，损失程度将取决于我们如何建立永久性的恢复计划和防灾准备。\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '집중호우로 경상북도 지역, 예방 조치와 항구 복구가 시급하다'\n"
                         "description: '폭우로 경북 북부 지역에 큰 피해가 발생한 지 약 3주가 지난 지금, "
                         '당국은 이러한 재해의 빈도가 높아짐에 따라 예방 조치와 항구 복구의 중요성을 강조하고 '
                         "있습니다.'\n"
                         "category: 'World/International'\n"
                         "keywords: '뉴스'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="http://news.kbs.co.kr/data/news/title_image/newsmp4/daegu/news9/2023/08/04/50_7741234.jpg" '
                         'alt="KBS뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from KBS뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '폭우로 경북 북부 지역에 큰 피해가 발생한 지 약 3주가 지난 지금, 당국은 이러한 재해의 '
                         '빈도가 높아짐에 따라 예방 조치와 항구 복구의 중요성을 강조하고 있습니다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 경북 북부 지역에 큰 피해가 발생한 원인은 '
                         '무엇인가요?</b></summary>\n'
                         '    경북 북부 지역의 주요 피해는 집중호우로 인해 발생했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 경상북도는 재난 발생 빈도 증가에 대응하기 위해 어떤 노력을 '
                         '하고 있나요?</b></summary>\n'
                         '    경상북도는 재해 발생 빈도가 높아짐에 따라 예방 대책과 항구 복구에 나서고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 집중호우로 인한 긴급 복구율은 '
                         '얼마인가요?</b></summary>\n'
                         '    집중호우로 인한 긴급 복구율은 도로 및 교량 98.2%를 포함하여 전체적으로 '
                         '89.8%입니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 경상북도는 산사태 대응체계 혁신 태스크포스를 통해 어떤 '
                         '조치를 취하고 있나요?</b></summary>\n'
                         '    경상북도는 산사태 대응체계 혁신 태스크포스를 통해 방재마을 조성, 대대적인 안전진단 '
                         '실시, 경보-대피-구조체계 개선 등을 추진할 계획입니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 영구 복구 계획과 재해 대비의 중요성은 '
                         '무엇인가요?</b></summary>\n'
                         '    기상이변으로 인한 피해의 정도는 영구적인 복구 계획과 재난 대비가 얼마나 잘 수립되어 '
                         '있는지에 따라 달라집니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 집중호우로 경상북도 지역, 예방 조치와 항구 복구가 시급하다\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '집중호우로 경북 북부지역에 큰 피해가 발생한 지 3주 가까이 지났습니다. 경상북도는 50년, '
                         '100년에 한 번 올지 모르는 재난이 앞으로 더 빈번해질 것으로 보고 이번 기회에 확실한 '
                         '대안을 마련하고 있습니다. 이번 집중호우로 인한 응급복구율은 도로-교량 98.2%를 포함해 '
                         '전체 89.8%입니다. 응급 복구가 마무리 단계에 접어들면서 이제는 항만 복구와 예방 대책으로 '
                         '관심이 옮겨가고 있습니다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://yonhapnewstv-prod.s3.ap-northeast-2.amazonaws.com/article/MYH/20230804/MYH20230804026100641_P1.jpg" '
                         'alt="연합뉴스TV" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 연합뉴스TV</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '경상북도는 이번 집중호우로 산사태 안전지대가 없다는 것이 드러났다며 산사태 대응체계 혁신 '
                         '태스크포스를 통해 대응에 나서고 있습니다. 산사태를 예방할 수 있는 방재마을을 조성하고, 산지 '
                         '내 인공물 등 위험요인에 대한 대대적인 안전진단에 나설 계획이다. 아울러 실제 상황에서 신속한 '
                         '상황전파와 대피가 이뤄질 수 있도록 경보-대피-구조-구호 체계를 개선한다. 집중호우와 같은 '
                         '기상이변이 일상화되고 있는 상황에서 항구적인 복구계획과 재난 대비책을 얼마나 잘 수립하느냐에 '
                         '따라 피해 규모가 달라질 것입니다.\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='I-hope-I-never-have-',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: ''I hope I never have to use "
                         "it'...self-defense firearms in spate of violent "
                         "crimes'\n"
                         "description: 'Delays and out-of-stock notices amid "
                         "surge in sales 'I must protect my body' anxiety "
                         "spreads'\n"
                         "category: 'Technology'\n"
                         "keywords: '호신용품'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/640/307/imgdb/original/2023/0804/20230804502176.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Delays and out-of-stock notices amid surge in sales '
                         "'I must protect my body' anxiety spreads\n"
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. What is causing the surge in '
                         'sales of self-defense products?</b></summary>\n'
                         '    The surge in sales of self-defense products is '
                         'being caused by ongoing serious incidents and the '
                         'anxiety of individuals wanting to protect '
                         'themselves.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. Which online store posted a '
                         'message about the delay in delivery?</b></summary>\n'
                         '    NAVER Smart Store, which sells self-defense '
                         'products, posted a message about the delay in '
                         'delivery.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. How much did sales of '
                         'self-defense products increase on '
                         'G-market?</b></summary>\n'
                         '    Sales of self-defense products on G-market '
                         'increased by 243 percent from March 22 to March 3 '
                         'compared to the same period last year.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. Why are people buying '
                         'self-defense products?</b></summary>\n'
                         '    People are buying self-defense products due to '
                         'the anxiety of potential harm and the need to '
                         'protect themselves.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. What self-defense products are '
                         'popular among women?</b></summary>\n'
                         '    Kubotan, a keychain with a pointed end, is '
                         'popular among women for self-defense.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## 'I hope I never have to use it'...self-defense "
                         'firearms in spate of violent crimes\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'Delayed deliveries and out-of-stock notices amid a '
                         "sales surge 'Protect your body' anxiety spreads An "
                         'online store is out of tridents. Shopping Mall '
                         "Nurijip Galmuri 'Sales of self-defense products have "
                         'been surging recently due to the ongoing serious '
                         'incidents...We will do our best to deliver them as '
                         'quickly as possible and hope that you will never '
                         "have to use them, as our company motto says.' On the "
                         '4th, NAVER Smart Store, which sells self-defense '
                         'products, posted a message about the delay in '
                         'delivery. The three-piece baton, which costs 15,900 '
                         "won, has over 8,100 reviews. 'I bought it for "
                         'self-defense after seeing a vicious post about a '
                         "murder in broad daylight,' most of them said. On "
                         'March 3, 13 days after the stabbing in Shinlim-dong, '
                         'Gwanak-gu, Seoul, another indiscriminate crime '
                         'occurred at a department store near Seohyeon Station '
                         'in Bundang-gu, Seongnam-si, Gyeonggi-do, and the '
                         'number of consumers seeking self-defense products '
                         'has surged. The news that the police have launched '
                         'an investigation into the crime, with a series of '
                         'warning posts on large communities, is also '
                         "amplifying consumers' anxiety. Some products are "
                         'even selling out. A sign for a company selling '
                         'self-defense products.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://img.biz.sbs.co.kr/upload/2023/08/04/ixf1691116949643.jpg" '
                         'alt="SBS Biz" />\n'
                         '    <figcaption>\n'
                         '        <h4> from SBS Biz</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Nurijip Galmuri According to G-market, sales of '
                         'self-defense products increased by 243 percent from '
                         'March 22 to March 3 compared to the same period last '
                         'year. Sales of truncheons for self-defense increased '
                         'by 303%. On 11th Avenue, sales of self-defense '
                         'products and self-defense sprays increased by 109% '
                         'and 171%, respectively, compared to the same period '
                         "last year. 'After the stabbing in Shinlim-dong on "
                         'the 21st of last month, people who were overwhelmed '
                         "by the anxiety of 'what could happen to me' were "
                         'buying a lot of related products to protect '
                         "themselves,' said an industry insider. 'In addition, "
                         'the Seohyun Station incident every three days is '
                         'expected to cause a further surge in self-defense '
                         "product sales.' In fact, on the fourth day after the "
                         "Seohyun Station incident, 'self-defense products' "
                         'ranked at the top of the Naver Shopping search '
                         'chart. Kubotan is popular among women. There were '
                         "over 1,300 reviews. Nurijip Galmuri 'When I go to "
                         'the bathroom, take the train, or walk down the '
                         'street, I find myself constantly looking around, and '
                         "I'm sensitive to the slightest sound,' said Yoo "
                         'Ah-moo-gae, a woman in her 40s who lives in '
                         "Seongbuk-gu, Seoul. 'In a chat room with my family, "
                         'we discussed whether we should all buy self-defense '
                         "products.' Another man in his 30s, Yoon Ah-moo-gae, "
                         "said, 'The stabbing incident made me realize that "
                         'women who are relatively weak are not the only ones '
                         "who become victims.' 'I'm thinking of buying a "
                         'lightweight spray, a trident, or a kubotan (a '
                         "keychain with a pointed end) for self-defense,' he "
                         'said. By Yoo Yoon-hee Lee duck@hani.co.kr\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '我希望永远不用它''......暴力犯罪中的自卫火器'\n"
                         "description: '我必须保护我的身体 ''的焦虑情绪在蔓延'\n"
                         "category: 'Technology'\n"
                         "keywords: '호신용품'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/640/307/imgdb/original/2023/0804/20230804502176.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "我必须保护我的身体 ''的焦虑情绪在蔓延\n"
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 是什么原因导致自卫产品销量激增？</b></summary>\n'
                         '    自卫产品销量激增的原因是不断发生的严重事件和个人希望保护自己的焦虑。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 哪家网店发布了延迟发货的消息？</b></summary>\n'
                         '    销售自卫产品的 NAVER Smart Store 发布了一条关于延迟交货的消息。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. G-market '
                         '上的自卫产品销量增长了多少？</b></summary>\n'
                         '    从 3 月 22 日到 3 月 3 日，G-market 上的自卫产品销售额与去年同期相比增长了 '
                         '243%。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 人们为什么购买自卫产品？</b></summary>\n'
                         '    人们购买自卫产品，是因为对潜在伤害的焦虑和保护自己的需要。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 哪些自卫产品受女性欢迎？</b></summary>\n'
                         '    Kubotan 是一种末端带尖的钥匙扣，深受女性喜爱，用于自卫。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## 我希望永远不用它''......暴力犯罪中的自卫火器\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "在 '保护您的身体 '的焦虑情绪蔓延的情况下，延迟交货和缺货通知在销售激增的情况下蔓延 "
                         '一家网店的三叉戟缺货。购物中心 Nurijip Galmuri '
                         "'由于严重事件不断发生，自卫产品的销量最近急剧上升......我们将尽最大努力尽快发货，并希望您永远不必使用它们，正如我们公司的座右铭所说的那样。4 "
                         '日，销售自卫产品的 NAVER 智能商店发布了关于延迟交货的消息。价格为 15900 韩元的三件套警棍有 '
                         '8100 '
                         "多条评论。我是在看到光天化日之下发生凶杀案的恶性帖子后买来自卫的，'大多数人都这样说。3月3日，首尔冠岳区新林洞刺杀事件发生13天后，京畿道城南市盆唐区瑞岘（Seohyeon）车站附近的一家百货店又发生了一起滥杀案件，寻求自卫产品的消费者人数激增。警方已对这起犯罪展开调查，并在大型社区发布了一系列警告帖，这一消息也加剧了消费者的焦虑。一些产品甚至卖断货。一家销售自卫产品的公司的招牌。\n"
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://img.biz.sbs.co.kr/upload/2023/08/04/ixf1691116949643.jpg" '
                         'alt="SBS Biz" />\n'
                         '    <figcaption>\n'
                         '        <h4> from SBS Biz</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Nurijip Galmuri 据 G-market 统计，从 3 月 22 日到 3 月 3 '
                         '日，自卫产品的销售额与去年同期相比增长了 243%。自卫用警棍的销售额增长了 303%。在第 11 '
                         "大街，自卫产品和自卫喷雾器的销售额分别比去年同期增长了 109% 和 171%。一位业内人士说：'上个月 "
                         '21 '
                         "日新林洞发生持刀伤人事件后，被'我可能会发生什么事'的焦虑压垮的人们购买了大量相关产品来保护自己。'此外，每三天发生一次的徐贤站事件预计也会引起自卫产品销售的进一步激增。事实上，在徐贤站事件发生后的第四天，'自卫产品'就在 "
                         'Naver 购物搜索排行榜上名列前茅。Kubotan 在女性中很受欢迎。共有 1 300 '
                         '多条评论。Nurijip Galmuri 住在首尔城北区的 40 多岁女性 Yoo Ah-moo-gae '
                         "说：'上厕所、坐火车或走在街上时，我发现自己总是东张西望，对最轻微的声音都很敏感。在与家人的聊天室里，我们讨论是否应该购买自卫产品。'另一位 "
                         '30 多岁的男子 Yoon Ah-moo-gae '
                         "说，'刺伤事件让我意识到，并不是只有相对弱小的女性才会成为受害者。'他说，'我正在考虑买一个轻型喷雾器、三叉戟或kubotan（一种末端尖尖的钥匙扣）用于自卫。作者：Yoo "
                         'Yoon-hee Lee duck@hani.co.kr\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '''절대 쓸 일이 없었으면 좋겠다''...강력 범죄가 잇따르는 호신용 총기'\n"
                         "description: '판매 급증에 따른 배송 지연 및 품절 안내에 ''내 몸은 내가 지켜야 "
                         "한다''는 불안감 확산'\n"
                         "category: 'Technology'\n"
                         "keywords: '호신용품'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/640/307/imgdb/original/2023/0804/20230804502176.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "판매 급증에 따른 배송 지연 및 품절 안내에 ''내 몸은 내가 지켜야 한다''는 불안감 확산\n"
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 호신용품의 판매량이 급증하는 이유는 '
                         '무엇인가요?</b></summary>\n'
                         '    호신용품의 판매 급증은 계속되는 심각한 사건 사고와 스스로를 보호하고자 하는 개인의 '
                         '불안감으로 인해 발생하고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 어느 온라인 스토어에서 배송 지연에 대한 메시지를 '
                         '게시했나요?</b></summary>\n'
                         '    호신용품을 판매하는 네이버 스마트스토어는 배송 지연에 대한 안내 메시지를 '
                         '게시했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. G마켓에서 호신용품 판매량이 얼마나 '
                         '증가했나요?</b></summary>\n'
                         '    3월 22일부터 3월 3일까지 G마켓에서 호신용품 판매량은 전년 동기 대비 243% '
                         '증가했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 사람들이 호신용품을 구매하는 이유는 '
                         '무엇인가요?</b></summary>\n'
                         '    사람들은 잠재적 위험에 대한 불안감과 스스로를 보호해야 한다는 필요성 때문에 호신용 '
                         '제품을 구매하고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 여성들에게 인기 있는 호신용품에는 어떤 것이 '
                         '있나요?</b></summary>\n'
                         '    끝이 뾰족한 열쇠고리인 쿠보탄은 호신용으로 여성들 사이에서 인기가 높습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## ''절대 쓸 일이 없었으면 좋겠다''...강력 범죄가 잇따르는 호신용 총기\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "판매 급증에 배송 지연-품절 안내 '호신용품' 불안감 확산 온라인 쇼핑몰에서 삼지창 품절 "
                         "사태가 벌어졌습니다. 쇼핑몰 누리집 갈무리 '최근 계속되는 심각한 사건사고로 호신용품 판매가 "
                         '급증하고 있습니다...최대한 빠른 배송을 위해 최선을 다하겠으며, 회사 사훈처럼 절대 사용하지 '
                         "않으시길 바랍니다'. 호신용품을 판매하는 네이버 스마트스토어는 4일 배송 지연에 대한 안내문을 "
                         '게재했다. 15,900원짜리 호신봉 3종 세트는 8,100개가 넘는 리뷰가 올라와 있습니다. '
                         "대부분 '대낮에 살인사건이 발생했다는 악의적인 게시물을 보고 호신용으로 구입했다'는 "
                         '내용이었다. 서울 관악구 신림동 칼부림 사건이 발생한 지 13일 만인 지난 3일, 경기도 '
                         '성남시 분당구 서현역 인근 백화점에서 또다시 무차별 범죄가 발생하면서 호신용품을 찾는 '
                         '소비자들이 급증하고 있다. 경찰이 수사에 착수했다는 소식과 함께 대형 커뮤니티에 경고성 글이 '
                         '잇따라 올라오면서 소비자들의 불안감이 증폭되고 있습니다. 일부 제품은 품절 사태까지 벌어지고 '
                         '있습니다. 호신용품을 판매하는 한 회사의 간판.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://img.biz.sbs.co.kr/upload/2023/08/04/ixf1691116949643.jpg" '
                         'alt="SBS Biz" />\n'
                         '    <figcaption>\n'
                         '        <h4> from SBS Biz</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '누리집 갈무리 G마켓에 따르면 지난 3월 22일부터 3월 3일까지 호신용품 판매량은 지난해 '
                         '같은 기간보다 243% 증가했다. 호신용 곤봉 판매량은 303% 증가했습니다. 11번가에서는 '
                         '호신용품과 호신용 스프레이 판매량이 지난해 같은 기간에 비해 각각 109%, 171% '
                         "증가했습니다. 업계 관계자는 '지난달 21일 신림동 칼부림 사건 이후 '나도 당할 수 있다'는 "
                         "불안감에 휩싸인 사람들이 자신을 보호하기 위해 관련 제품을 많이 구매하고 있다'고 말했다. "
                         "이어 '여기에 사흘마다 서현역 사건이 터지면서 호신용품 판매는 더욱 급증할 것으로 예상된다'고 "
                         "덧붙였다. 실제로 서현역 사건 발생 4일째 되는 날 네이버 쇼핑 검색 차트에는 '호신용품'이 "
                         '상위권에 올랐다. 쿠보탄은 여성들에게 인기가 많았습니다. 1,300개가 넘는 리뷰가 '
                         "있었습니다. 서울 성북구에 사는 40대 여성 유 아무개 씨는 누리집 갈무리에서 '화장실을 갈 "
                         "때나 전철을 탈 때, 길을 걸을 때 자꾸 주위를 둘러보게 되고 작은 소리에도 예민해진다'며 "
                         "'쿠보탄을 구매하게 됐다'고 말했다. '가족들과 채팅방에서 호신용품을 사면 어떨까 하는 "
                         "이야기를 나눴어요.' 또 다른 30대 남성 윤 아무개 씨는 '칼부림 사건으로 상대적으로 약자인 "
                         "여성만 피해자가 되는 것이 아니라는 것을 깨달았다'고 말했습니다. 그는 '호신용 스프레이나 "
                         "삼지창, 쿠보탄(끝이 뾰족한 열쇠고리) 등을 구입해 호신용으로 사용할까 생각 중'이라고 "
                         '말했다. 이윤희 duck@hani.co.kr\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='Hanmyeong-Butcher-Sh',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: 'Hanmyeong Butcher Shop and Gastron Support "
                         "Production of SBS Drama 'Police Station and "
                         "Gukgwasoo Next to Fire Station''\n"
                         "description: 'Hanmyeong Butcher Shop and Gastron are "
                         "both supporting the production of SBS's new Friday "
                         "drama 'Police Station and Gukgwasoo Next to Fire "
                         "Station'. The drama tells the story of a fire "
                         'department, a police department, and a gukgwasoo '
                         "working together to solve unprecedented cases.'\n"
                         "category: 'Entertainment'\n"
                         "keywords: '소방서 옆 경찰서'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558808_683527_413_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Hanmyeong Butcher Shop and Gastron are both '
                         "supporting the production of SBS's new Friday drama "
                         "'Police Station and Gukgwasoo Next to Fire Station'. "
                         'The drama tells the story of a fire department, a '
                         'police department, and a gukgwasoo working together '
                         'to solve unprecedented cases.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>0. What is the Friday drama 'Police "
                         "Station and Gukgwasoo Next to Fire Station' "
                         'about?</b></summary>\n'
                         "    'Police Station and Gukgwasoo Next to Fire "
                         "Station' is a drama that follows the collaboration "
                         'between a fire department, a police department, and '
                         'a gukgwasoo to solve complex and unprecedented '
                         'cases.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. Who are some of the actors in the '
                         'drama?</b></summary>\n'
                         '    The drama stars actors such as Kim Rae Won, Son '
                         'Ho Joon, and Gong Seung Yeon.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>2. When does the drama 'Police "
                         "Station and Gukgwasoo Next to Fire Station' "
                         'air?</b></summary>\n'
                         '    The drama airs every Friday at 10 pm on SBS.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. What is Hanmyeong Butcher Shop '
                         'known for?</b></summary>\n'
                         '    Hanmyeong Butcher Shop is a renowned franchise '
                         'brand specializing in aged raw meat.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. How does Hanmyeong Butcher Shop '
                         'support its franchisees?</b></summary>\n'
                         '    Hanmyeong Butcher Shop supports its franchisees '
                         'through multifaceted brand promotion strategies and '
                         'by supplying all ingredients, including meat and '
                         'sauces, to franchisees in one pack.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>5. What does Gastron specialize '
                         'in?</b></summary>\n'
                         '    Gastron specializes in industrial gas '
                         'detectors.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>6. What product of Gastron is '
                         'featured as PPL in the drama?</b></summary>\n'
                         "    The drama's PPL includes Gastron's portable gas "
                         'detectors.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>7. What gases can Gastron's gas "
                         'detectors detect?</b></summary>\n'
                         "    Gastron's gas detectors can simultaneously "
                         'detect oxygen, carbon monoxide, hydrogen sulfide, '
                         'and combustible gases.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## Hanmyeong Butcher Shop and Gastron Support '
                         "Production of SBS Drama 'Police Station and "
                         "Gukgwasoo Next to Fire Station'\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'Hanmyeong Butcher Shop and Gastron are actively '
                         "involved in the production of SBS's new Friday drama "
                         "'Police Station and Gukgwasoo Next to Fire Station'. "
                         'This drama revolves around the collaboration between '
                         'a fire department, a police department, and a '
                         'gukgwasoo to solve complex and unprecedented cases. '
                         'Starring actors such as Kim Rae Won, Son Ho Joon, '
                         'and Gong Seung Yeon, the drama has gained attention '
                         'since its premiere. It airs every Friday at 10 pm on '
                         'SBS. Hanmyeong Butcher Shop is a renowned franchise '
                         'brand specializing in aged raw meat. It provides '
                         'franchisees with multifaceted brand promotion '
                         'strategies to boost sales. The headquarters ensures '
                         'the smooth operation of stores by supplying all '
                         'ingredients, including meat and sauces, in one '
                         'pack.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558806_683525_3934_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Additionally, logistics and distribution are handled '
                         'by the headquarters, reducing supply costs and '
                         'increasing franchisee margins. Gastron, on the other '
                         'hand, is a company specializing in industrial gas '
                         'detectors. Founded in 1992, Gastron has achieved '
                         'localization and globalization of gas detectors, '
                         "becoming a leader in the industry. The drama's PPL "
                         "(Product Placement) includes Gastron's portable gas "
                         'detectors, which are frequently used by firefighters '
                         'in the field. These detectors can simultaneously '
                         'detect oxygen, carbon monoxide, hydrogen sulfide, '
                         'and combustible gases. As disaster sites often '
                         'involve various gas-related risks, wearing a gas '
                         'detector is essential for the safety of '
                         'firefighters. Gastron aims to promote its products '
                         'effectively through its support for the drama '
                         'production and PPL promotion.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         'title: '
                         "'汉明肉店和Gastron支持SBS电视剧《警察局和消防局旁边的Gukgwasoo》的制作'\n"
                         "description: 'Hanmyeong 肉铺和 Gastron 都支持 SBS "
                         "新周五剧《消防局旁边的警察局和古国水》的制作。该剧讲述了消防队、警察局和Gukgwasoo一起解决前所未有的案件的故事。'\n"
                         "category: 'Entertainment'\n"
                         "keywords: '소방서 옆 경찰서'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558808_683527_413_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Hanmyeong 肉铺和 Gastron 都支持 SBS '
                         '新周五剧《消防局旁边的警察局和古国水》的制作。该剧讲述了消防队、警察局和Gukgwasoo一起解决前所未有的案件的故事。\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. '
                         '周五电视剧《警察局和消防局旁边的古格瓦苏》讲述的是什么内容？</b></summary>\n'
                         '    '
                         '消防局旁的警察局和古格水》是一部讲述消防局、警察局和古格水合作解决复杂而前所未有的案件的电视剧。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 剧中有哪些演员？</b></summary>\n'
                         '    该剧由金来沅、孙浩俊和龚承妍等演员主演。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. '
                         '警察局和消防局旁边的古格瓦苏》何时播出？</b></summary>\n'
                         '    该剧每周五晚 10 点在 SBS 播出。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. Hanmyeong Butcher Shop '
                         '以什么而闻名？</b></summary>\n'
                         '    Hanmyeong Butcher Shop 是一家专门经营老生肉的知名特许经营品牌。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. Hanmyeong Butcher Shop '
                         '如何支持加盟商？</b></summary>\n'
                         '    Hanmyeong Butcher Shop '
                         '通过多方面的品牌推广战略，以及向加盟商统一供应肉类和酱料等所有配料，为加盟商提供支持。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>5. Gastron 擅长什么？</b></summary>\n'
                         '    Gastron 专门生产工业气体检测仪。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>6. Gastron 的什么产品在剧中扮演 '
                         'PPL？</b></summary>\n'
                         '    该剧的 PPL 包括 Gastron 的便携式气体检测仪。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>7. Gastron '
                         '气体检测仪可以检测哪些气体？</b></summary>\n'
                         '    Gastron 气体检测仪可同时检测氧气、一氧化碳、硫化氢和可燃气体。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 汉明肉店和Gastron支持SBS电视剧《警察局和消防局旁边的Gukgwasoo》的制作\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'Hanmyeong 肉铺和 Gastron 积极参与了 SBS '
                         '新周五剧《消防局旁的警察局和古国水》的制作。该剧围绕消防队、警察局和Gukgwasoo之间的合作展开，以解决前所未有的复杂案件。该剧由金来沅、孙浩俊、龚承妍等演员主演，自首播以来就备受关注。该剧每周五晚 '
                         '10 点在 SBS 播出。Hanmyeong Butcher Shop '
                         '是一家著名的老生肉特许经营品牌。它为加盟商提供多方面的品牌推广策略，以促进销售。总部通过一包式供应肉类和酱料等所有配料，确保店铺顺利运营。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558806_683525_3934_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '此外，总部还负责物流和配送，从而降低了供应成本，增加了加盟商的利润。Gastron '
                         '则是一家专业生产工业气体检测仪的公司。Gastron 公司成立于 1992 '
                         '年，实现了气体检测仪的本地化和全球化，成为行业的领导者。该剧的 PPL（产品植入）包括 Gastron '
                         '的便携式气体检测仪，这是消防员在现场经常使用的产品。这些探测器可以同时检测氧气、一氧化碳、硫化氢和可燃气体。由于灾害现场往往存在各种与气体有关的风险，因此佩戴气体检测仪对消防员的安全至关重要。Gastron '
                         '希望通过支持电视剧制作和 PPL 推广，有效推广其产品。\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '한명정육점과 가스트론, SBS 드라마 ''경찰서와 소방서 옆 국과수'' 제작 "
                         "지원'\n"
                         "description: '한명정육점과 가스트론이 SBS 새 금토드라마 ''소방서 옆 "
                         "국밥집''의 제작을 지원합니다. 이 드라마는 소방서, 경찰서, 국과수가 힘을 합쳐 전대미문의 "
                         "사건을 해결해 나가는 이야기를 담고 있습니다.'\n"
                         "category: 'Entertainment'\n"
                         "keywords: '소방서 옆 경찰서'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558808_683527_413_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "한명정육점과 가스트론이 SBS 새 금토드라마 ''소방서 옆 국밥집''의 제작을 지원합니다. 이 "
                         '드라마는 소방서, 경찰서, 국과수가 힘을 합쳐 전대미문의 사건을 해결해 나가는 이야기를 담고 '
                         '있습니다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>0. 금요드라마 '소방서 옆 경찰서, 국과수'는 어떤 "
                         '내용인가요?</b></summary>\n'
                         "    '소방서 옆집에 국과수'는 소방서, 경찰서, 국과수의 협업을 통해 복잡하고 전대미문의 "
                         '사건을 해결해나가는 과정을 담은 드라마다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 드라마에 출연하는 배우들은 '
                         '누구인가요?</b></summary>\n'
                         '    이 드라마에는 김래원, 손호준, 공승연 등의 배우가 출연합니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>2. 드라마 '소방서 옆집에 경찰서와 국과수'는 언제 "
                         '방영되나요?</b></summary>\n'
                         '    드라마는 매주 금요일 오후 10시 SBS에서 방영됩니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 한명정육점은 무엇으로 유명하나요?</b></summary>\n'
                         '    한명정육점은 숙성 생고기 전문 프랜차이즈 브랜드로 유명합니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 한명정육점은 가맹점을 어떻게 '
                         '지원하나요?</b></summary>\n'
                         '    한명정육점은 다각적인 브랜드 홍보 전략과 고기, 소스 등 모든 식재료를 원팩으로 '
                         '가맹점에 공급하는 등 가맹점을 지원하고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>5. 가스트론의 전문 분야는 '
                         '무엇인가요?</b></summary>\n'
                         '    가스트론은 산업용 가스 감지기 전문 기업입니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>6. 드라마에 PPL로 등장하는 가스트론의 제품은 '
                         '무엇인가요?</b></summary>\n'
                         '    드라마의 PPL에는 가스트론의 휴대용 가스 감지기가 포함되어 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>7. 가스트론의 가스 감지기는 어떤 가스를 감지할 수 '
                         '있나요?</b></summary>\n'
                         '    가스트론의 가스 감지기는 산소, 일산화탄소, 황화수소 및 가연성 가스를 동시에 감지할 '
                         '수 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## 한명정육점과 가스트론, SBS 드라마 ''경찰서와 소방서 옆 국과수'' 제작 지원\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "한명정육점과 가스트론이 SBS 새 금토드라마 '소방서 옆 국과수' 제작에 적극 참여합니다. 이 "
                         '드라마는 소방서, 경찰서, 국과수의 협업을 통해 복잡하고 전대미문의 사건을 해결해나가는 내용을 '
                         '담고 있습니다. 김래원, 손호준, 공승연 등 배우들이 출연하며 첫 방송부터 화제를 모은 '
                         '드라마입니다. 매주 금요일 오후 10시 SBS에서 방영됩니다. 한명정육점은 숙성 생고기 전문 '
                         '프랜차이즈 브랜드로 유명합니다. 가맹점 매출 증대를 위해 다각적인 브랜드 홍보 전략을 가맹점에 '
                         '제공하고 있습니다. 본사는 고기와 소스 등 모든 식재료를 원팩으로 공급해 매장의 원활한 운영을 '
                         '보장합니다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.mhns.co.kr/news/thumbnail/202308/558806_683525_3934_v150.jpg" '
                         'alt="문화뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 문화뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '또한 물류와 유통을 본사에서 처리하기 때문에 공급 비용을 절감하고 가맹점 마진을 높일 수 '
                         '있습니다. 반면 가스트론은 산업용 가스 검지기 전문 기업입니다. 1992년 설립된 가스트론은 '
                         '가스 검지기의 국산화와 세계화를 이뤄내며 업계 선두주자로 자리매김했다. 드라마의 PPL(제품 '
                         '광고)에는 소방관들이 현장에서 자주 사용하는 가스트론의 휴대용 가스 감지기가 등장합니다. 이 '
                         '감지기는 산소, 일산화탄소, 황화수소, 가연성 가스를 동시에 감지할 수 있습니다. 재난 '
                         '현장에는 다양한 가스 관련 위험이 수반되는 경우가 많기 때문에 소방관의 안전을 위해 가스 '
                         '감지기 착용은 필수입니다. 가스트론은 드라마 제작 지원과 PPL 홍보를 통해 제품을 효과적으로 '
                         '알린다는 목표입니다.\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='Governor-Kim-Kwan-yo',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: 'Governor Kim Kwan-young Highlights Positive "
                         "Aspects of World Scout Jamboree'\n"
                         "description: 'North Jeolla Province Governor Kim "
                         'Kwan-young has expressed optimism about the ongoing '
                         'World Scout Jamboree, emphasizing the enjoyable '
                         'experiences of participants. Despite concerns over '
                         'the recent fever outbreak and extreme weather '
                         'conditions, Governor Kim remains committed to '
                         "ensuring the event's success.'\n"
                         "category: 'Politics'\n"
                         "keywords: '김관영'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.eroun.net/news/thumbnail/202308/35826_64573_3536_v150.jpg" '
                         'alt="이로운넷" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 이로운넷</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'North Jeolla Province Governor Kim Kwan-young has '
                         'expressed optimism about the ongoing World Scout '
                         'Jamboree, emphasizing the enjoyable experiences of '
                         'participants. Despite concerns over the recent fever '
                         'outbreak and extreme weather conditions, Governor '
                         "Kim remains committed to ensuring the event's "
                         'success.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. What has Governor Kim '
                         "Kwan-young's role been at the World Scout "
                         'Jamboree?</b></summary>\n'
                         '    Governor Kim Kwan-young has been overseeing the '
                         'World Scout Jamboree and has chosen to stay at the '
                         'campsite for the past two days to ensure safety and '
                         'address any concerns.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. How have the participants been '
                         'enjoying the jamboree?</b></summary>\n'
                         '    According to Governor Kim, the participants have '
                         'been having a lot of fun, particularly during the '
                         'evening as they engage in cultural activities.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. What factors contributed to the '
                         'recent fever outbreak?</b></summary>\n'
                         '    Governor Kim attributed the fever outbreak to '
                         'jet lag and exhaustion experienced by athletes '
                         'traveling long distances to participate in the '
                         'jamboree.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. How are the organizers addressing '
                         'the heatwave?</b></summary>\n'
                         '    The organizers have implemented measures such as '
                         'moving indoor activities, experience centers, and '
                         'exhibits indoors, and canceling certain outdoor '
                         'activities to prioritize participant safety during '
                         'the heatwave.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>4. What is the governor's stance "
                         "regarding the event's success?</b></summary>\n"
                         '    Governor Kim remains optimistic about the '
                         "event's success and emphasized the indomitable "
                         'spirit of the jamboree.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## Governor Kim Kwan-young Highlights Positive '
                         'Aspects of World Scout Jamboree\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'Governor Kim Kwan-young of North Jeolla Province has '
                         'been actively involved in overseeing the World Scout '
                         'Jamboree. He has even chosen to stay at the campsite '
                         'for the past two days, closely observing the '
                         'activities and engaging with the participants. '
                         'According to Governor Kim, the participants have '
                         'been having a great time, particularly during the '
                         'evening when they immerse themselves in their '
                         "respective cultures. The governor's presence at the "
                         'campsite serves to address safety concerns and '
                         'ensure the smooth functioning of the jamboree. He '
                         'has visited the key sites, inspected the facilities, '
                         'and interacted with the scouts. Despite the '
                         'challenges faced, Governor Kim remains optimistic '
                         "about the event's success.\n"
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.pressian.com/_resources/10/2023/08/04/2023080410440197244_l.png" '
                         'alt="프레시안" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 프레시안</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Addressing the recent fever outbreak, he attributed '
                         'it to factors such as jet lag and exhaustion '
                         'experienced by athletes traveling long distances to '
                         "participate. He noted that the scouts' condition has "
                         'been improving over the course of the jamboree. In '
                         'response to the heatwave, the organizers have '
                         'implemented necessary measures to prioritize the '
                         'safety of all participants. Governor Kim emphasized '
                         'the indomitable spirit of the jamboree, highlighting '
                         'the determination to persevere regardless of the '
                         'weather conditions. Indoor activities, experience '
                         'centers, and exhibits have been planned to provide a '
                         'respite from the heat, while certain outdoor '
                         'activities have been canceled. The governor stated '
                         'that further decisions regarding large gatherings, '
                         'such as K-pop concerts, will be made after a '
                         'comprehensive assessment in an upcoming meeting. '
                         'With his unwavering dedication to ensuring '
                         'participant safety and a memorable jamboree '
                         'experience, Governor Kim Kwan-young personifies the '
                         'spirit of a responsible leader and an attentive '
                         'father.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '金宽永州长强调世界童子军大会的积极意义'\n"
                         "description: '全罗北道知事金宽永（Kim "
                         "Kwan-young）对正在举行的世界童子军大露营表示乐观，并强调了参与者的愉快经历。尽管最近爆发的高烧和极端天气状况令人担忧，但金省长仍致力于确保活动取得成功。'\n"
                         "category: 'Politics'\n"
                         "keywords: '김관영'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.eroun.net/news/thumbnail/202308/35826_64573_3536_v150.jpg" '
                         'alt="이로운넷" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 이로운넷</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '全罗北道知事金宽永（Kim '
                         'Kwan-young）对正在举行的世界童子军大露营表示乐观，并强调了参与者的愉快经历。尽管最近爆发的高烧和极端天气状况令人担忧，但金省长仍致力于确保活动取得成功。\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. Kim Kwan-young '
                         '总督在世界童子军大会上发挥了什么作用？</b></summary>\n'
                         '    金宽永省长一直在监督世界童子军大露营活动，并选择在过去两天留在营地，以确保安全并解决任何问题。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 参加者对这次盛会有何感想？</b></summary>\n'
                         '    据金省长说，参加者们玩得很开心，尤其是晚上的文化活动。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 哪些因素导致了最近的发烧疫情？</b></summary>\n'
                         '    金州长将发烧的原因归结为运动员长途跋涉参加大运会造成的时差和疲惫。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 主办方如何应对热浪？</b></summary>\n'
                         '    '
                         '主办方采取了一些措施，如将室内活动、体验中心和展品移至室内，取消某些室外活动，以便在热浪中优先保证参与者的安全。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 对于活动的成功举办，州长的态度如何？</b></summary>\n'
                         '    金州长对此次活动的成功保持乐观，并强调了该活动不屈不挠的精神。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 金宽永州长强调世界童子军大会的积极意义\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '全罗北道省长金宽永一直积极参与监督世界童子军大会。在过去的两天里，他甚至选择留在营地，仔细观察各项活动，并与参与者进行交流。据金省长说，参加者们都玩得很开心，尤其是晚上，他们都沉浸在各自的文化氛围中。州长在营地的存在是为了解决安全问题，确保大会顺利进行。他视察了主要地点，检查了设施，并与童子军进行了互动。尽管面临种种挑战，金州长仍对活动的成功持乐观态度。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.pressian.com/_resources/10/2023/08/04/2023080410440197244_l.png" '
                         'alt="프레시안" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 프레시안</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '在谈到最近的发烧疫情时，他将其归因于运动员长途跋涉参加比赛所经历的时差和疲惫等因素。他指出，童子军的状况在大会期间有所改善。为应对热浪，组织者采取了必要措施，优先保证所有参与者的安全。金省长强调了童子军不屈不挠的精神，强调了无论天气状况如何都要坚持到底的决心。在取消某些室外活动的同时，还计划举办室内活动、体验中心和展览，以缓解炎热的天气。州长表示，有关 '
                         'K-pop '
                         '演唱会等大型集会的进一步决定将在即将召开的会议上进行全面评估后做出。金宽永州长坚定不移地致力于确保参与者的安全和难忘的庆典体验，他是一位负责任的领导者和细心的父亲。\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '김관영 도지사, 세계스카우트잼버리의 긍정적 측면 강조'\n"
                         "description: '김관영 전북도지사는 현재 진행 중인 세계스카우트잼버리에 대해 낙관적인 "
                         '전망을 내놓으며 참가자들의 즐거운 경험을 강조했습니다. 김 지사는 최근 발생한 신종플루와 '
                         "기상이변에 대한 우려에도 불구하고 잼버리 성공 개최를 위해 최선을 다하고 있습니다.'\n"
                         "category: 'Politics'\n"
                         "keywords: '김관영'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.eroun.net/news/thumbnail/202308/35826_64573_3536_v150.jpg" '
                         'alt="이로운넷" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 이로운넷</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '김관영 전북도지사는 현재 진행 중인 세계스카우트잼버리에 대해 낙관적인 전망을 내놓으며 '
                         '참가자들의 즐거운 경험을 강조했습니다. 김 지사는 최근 발생한 신종플루와 기상이변에 대한 '
                         '우려에도 불구하고 잼버리 성공 개최를 위해 최선을 다하고 있습니다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 세계스카우트잼버리에서 김관영 도지사의 역할은 '
                         '무엇이었나요?</b></summary>\n'
                         '    세계스카우트잼버리를 총괄하고 있는 김관영 도지사는 안전 확보와 우려사항 해결을 위해 '
                         '지난 이틀간 야영장에 머물며 현장을 직접 챙겼습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 참가자들은 잼버리를 어떻게 즐기고 '
                         '있나요?</b></summary>\n'
                         '    김 지사에 따르면 참가자들은 특히 저녁 시간에 문화 활동을 하며 즐거운 시간을 보내고 '
                         '있다고 합니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 최근 발열이 발생한 원인은 '
                         '무엇인가요?</b></summary>\n'
                         '    김 지사는 잼버리 참가를 위해 장거리 이동을 하는 선수들이 시차적응과 피로로 인해 '
                         '발열이 발생한 것으로 추정했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 주최측은 폭염에 어떻게 대처하고 '
                         '있나요?</b></summary>\n'
                         '    주최 측은 폭염 기간 동안 참가자 안전을 최우선으로 고려해 실내 활동, 체험관 및 '
                         '전시를 실내로 옮기고 일부 야외 활동을 취소하는 등의 조치를 시행하고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 행사의 성공에 대한 주지사의 입장은 '
                         '무엇인가요?</b></summary>\n'
                         '    김 지사는 대회 성공 개최를 낙관하며 불굴의 잼버리 정신을 강조했다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 김관영 도지사, 세계스카우트잼버리의 긍정적 측면 강조\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '김관영 전북도지사가 세계스카우트잼버리를 진두지휘하며 적극적으로 참여하고 있다. 김 지사는 지난 '
                         '이틀간 야영장에 머물며 참가자들의 활동을 면밀히 관찰하고 참가자들과 소통하는 시간을 갖기도 '
                         '했다. 김 지사에 따르면 참가자들은 특히 저녁시간에 각국의 문화에 흠뻑 빠져들며 즐거운 시간을 '
                         '보내고 있다고 합니다. 김 지사가 캠프장에 상주하는 것은 안전 문제를 해결하고 잼버리가 '
                         '원활하게 운영될 수 있도록 하기 위해서다. 그는 주요 장소를 방문하고 시설을 점검하며 스카우트 '
                         '대원들과 교류했습니다. 김 지사는 여러 가지 어려움에도 불구하고 잼버리 성공 개최를 낙관하고 '
                         '있다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://cdn.pressian.com/_resources/10/2023/08/04/2023080410440197244_l.png" '
                         'alt="프레시안" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 프레시안</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '그는 최근 발생한 열병에 대해 참가를 위해 장거리 이동을 하는 선수들이 겪는 시차적응과 피로 '
                         '등의 요인 때문이라고 설명했습니다. 그는 잼버리가 진행되는 동안 스카우트 대원들의 컨디션이 '
                         '개선되고 있다고 언급했습니다. 조직위는 폭염에 대비해 모든 참가자의 안전을 최우선으로 고려한 '
                         '대책을 시행하고 있다. 김 지사는 잼버리의 불굴의 정신을 강조하며 날씨와 상관없이 꿋꿋이 '
                         '이겨내자는 의지를 다졌다. 더위를 피할 수 있는 실내 활동, 체험관, 전시관 등이 계획되어 '
                         '있으며, 일부 야외 활동은 취소되었습니다. 주지사는 케이팝 콘서트와 같은 대규모 모임에 대한 '
                         '추가 결정은 다음 회의에서 종합적으로 평가한 후 결정할 것이라고 말했습니다. 참가자들의 안전과 '
                         '기억에 남는 잼버리 경험을 위해 한결같이 헌신하는 김관영 도지사는 책임감 있는 지도자이자 '
                         '자상한 아버지의 모습을 보여주고 있습니다.\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='50-billion-club-Park',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: ''50 billion club' Park Young-soo "
                         "arrested...What's the difference from when he was "
                         "dismissed a month ago?'\n"
                         "description: 'The arrest warrant for former special "
                         'prosecutor Park Young-soo, which the court dismissed '
                         'once, was issued on March 3. Park was lobbied by a '
                         "private businessman in Daejeon-dong...'\n"
                         "category: 'Politics'\n"
                         "keywords: '박영수 구속'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/647/imgdb/original/2023/0804/20230804501508.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'The arrest warrant for former special prosecutor '
                         'Park Young-soo, which the court dismissed once, was '
                         'issued on March 3. Park was lobbied by a private '
                         'businessman in Daejeon-dong...\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. Why was an arrest warrant issued '
                         'for Park Young-soo?</b></summary>\n'
                         '    An arrest warrant was issued for Park Young-soo '
                         'due to the risk of evidence being destroyed. The '
                         'prosecution believes that new charges filed during '
                         'the reinforcement investigation, including a '
                         'violation of the anti-graft law, helped reverse the '
                         'outcome.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>1. What is the '5 billion "
                         "club'?</b></summary>\n"
                         "    The '5 billion club' refers to a group of "
                         'individuals who allegedly received money in exchange '
                         'for assisting private developers in Daejeon-dong.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. Who else is being investigated in '
                         "relation to the '5 billion club'?</b></summary>\n"
                         '    Former Nationalist Party of Korea lawmaker Kwak '
                         'Sang-do and former Supreme Court Justice Kwon '
                         'Soon-il are also being investigated in connection '
                         "with the '5 billion club' case.\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. What is the significance of Park '
                         "Young-soo's arrest in the '5 billion club' "
                         'investigation?</b></summary>\n'
                         "    Park Young-soo's arrest is expected to "
                         "accelerate the rest of the '5 billion club' "
                         'investigation. It may also lead to a further '
                         'investigation into other members of the group.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## '50 billion club' Park Young-soo "
                         "arrested...What's the difference from when he was "
                         'dismissed a month ago?\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'Former special prosecutor Park Young-soo, who is '
                         "under suspicion of the so-called '5 billion club' "
                         'for receiving money in exchange for helping private '
                         'developers in Daejeon-dong, heads to court to appear '
                         'for his second pre-arrest interrogation (warrant '
                         'examination) at the Seoul Central District Court in '
                         'Seocho-gu, Seoul, on Wednesday morning. Yonhap An '
                         'arrest warrant for former special prosecutor Park '
                         'Young-soo, which the court had dismissed once, was '
                         'issued on Wednesday. Park is considered one of the '
                         "members of the '5 billion club' that allegedly "
                         'received lobbying from a private businessman in '
                         'Daegu-dong. Additional charges filed by prosecutors '
                         'in the course of the reinforcement investigation are '
                         'believed to have made the difference. Yoon Jae-nam, '
                         'deputy chief judge of the Seoul Central District '
                         "Court's warrant division, announced the reason for "
                         'issuing an arrest warrant for Park on the night of '
                         "March 3, saying that 'there is a risk of evidence "
                         "being destroyed.' Normally, an arrest warrant is "
                         'issued on the premise that the charges have been '
                         'partially proven and for reasons such as evidence '
                         'destruction and fear of escape. Previously, in June, '
                         'Chief Warrant Officer Yoo Chang-hoon dismissed the '
                         'arrest warrant, saying that the charges were '
                         "'disputed in factual and legal terms' and did not "
                         'recognize the charges themselves. The prosecution '
                         'believes the new charges, which were filed in a '
                         'reinforced investigation, helped reverse the '
                         'outcome. Prosecutors added the charge of violating '
                         'the anti-graft law, alleging that 1.1 billion won of '
                         'the money Park was supposed to receive went to her '
                         'daughter, Park Ah-moo-gae, in the form of loans '
                         'while she was a special prosecutor. The prosecution '
                         'claimed that private businesses in Daejeon-dong '
                         'promised to pay Park, and that the promise was '
                         "realized in the 1.1 billion won that went to Park's "
                         'daughter, which the court accepted.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://dimg.donga.com/a/800/0/95/5/wps/NEWS/IMAGE/2023/08/04/120570314.1.jpg" '
                         'alt="동아일보" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 동아일보</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "Park's destruction of her cell phone earlier this "
                         'year is also believed to have contributed to the '
                         "court's determination of 'evidence destruction "
                         "concerns.' New evidence obtained during the "
                         'reinforcement investigation also played a role. '
                         'During the reinforcement investigation, the '
                         'prosecution obtained a loan agreement stating that '
                         'Kim Man-bae, the majority shareholder of Hwacheon '
                         'Daewoo Asset Management, borrowed 500 million won '
                         'from Park, and that Park was to receive the money '
                         'back in shares. The document served to support the '
                         'allegation that Park had agreed to receive money. '
                         "'After carefully analyzing the reasons for "
                         'dismissing the warrant, we reinforced the evidence '
                         'with solid evidence and explained it in detail to '
                         "the court,' said an official from the Seoul Central "
                         "District Prosecutors' Office. Park has previously "
                         "stated that she 'did not receive or promise anything "
                         'in exchange for participating in the Daejeon-dong '
                         "development project or arranging financing.' The "
                         'detention of Park is expected to speed up the rest '
                         "of the '5 billion club' investigation. In "
                         'particular, the investigation of former Nationalist '
                         'Party of Korea lawmaker Kwak Sang-do, whose case is '
                         'similarly structured in that he realized the money '
                         'he was to receive through his children, is likely to '
                         "gain momentum. Prosecutors called Kwak's son, Kwak "
                         'Sang-do, who received 5 billion won in severance pay '
                         '(2.5 billion won in error) from Hwacheon Daewoo, for '
                         'questioning on the 27th of last month and again '
                         'earlier this week. A prosecution official said on '
                         "March 3, 'We plan to investigate the alleged '5 "
                         "billion club' in a sequential manner.' Former "
                         'Supreme Court Justice Kwon Soon-il, who is suspected '
                         "of 'trial transactions,' is also being investigated. "
                         'By Kwang-joon Jeon light@hani.co.kr\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '500亿俱乐部 ''朴永洙被捕......他与一个月前被解雇时有什么不同？'\n"
                         "description: '对前特别检察官朴永洙的逮捕令于 3 月 3 "
                         "日签发，法院曾一度驳回该逮捕令。朴英洙是在大田洞一位私人商人的游说下...'\n"
                         "category: 'Politics'\n"
                         "keywords: '박영수 구속'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/647/imgdb/original/2023/0804/20230804501508.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '对前特别检察官朴永洙的逮捕令于 3 月 3 '
                         '日签发，法院曾一度驳回该逮捕令。朴英洙是在大田洞一位私人商人的游说下...\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 为什么会对朴永洙发出逮捕令？</b></summary>\n'
                         '    '
                         '由于存在证据被销毁的风险，对朴永洙发出了逮捕令。检方认为，在强化调查期间提出的新指控，包括违反反贪污法，有助于扭转结果。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>1. 什么是 '50 亿俱乐部'？</b></summary>\n"
                         "    50 亿俱乐部 '指的是一群人，据称他们通过协助大田洞的私人开发商而获得了金钱。\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>2. 还有谁正在接受与 '50 亿俱乐部 "
                         "'有关的调查？</b></summary>\n"
                         "    前国民之党立法委员郭尚道和前最高法院大法官权顺一也因与 '50 亿俱乐部 '案有关而受到调查。\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>3. 朴永洙被捕对 '50 亿俱乐部 "
                         "'调查有何意义？</b></summary>\n"
                         "    预计朴永洙的被捕将加速 '50 亿俱乐部 "
                         "'调查的后续工作。这也可能导致对该集团其他成员的进一步调查。\n"
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## 500亿俱乐部 ''朴永洙被捕......他与一个月前被解雇时有什么不同？\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "因帮助大田洞私人开发商收受钱财而涉嫌所谓 '50 亿俱乐部 "
                         "'的前特别检察官朴永洙周三上午前往首尔瑞草区首尔中央地方法院接受第二次逮捕前审讯（逮捕令审查）。韩联社 "
                         "本周三，法院签发了对前特别检察官朴永洙（Park Young-soo）的逮捕令。朴英洙被认为是 '50 "
                         '亿俱乐部 '
                         "'成员之一，据称该俱乐部接受了大邱洞一名私人商人的游说。检方在强化调查过程中提出的额外指控被认为起到了决定性作用。首尔中央地方法院搜查令庭副庭长尹在男 "
                         '3 月 3 日晚宣布了对朴槿惠签发逮捕令的理由，称 '
                         "'有证据被破坏的风险'。通常情况下，签发逮捕令的前提是指控已部分成立，原因包括证据被破坏和担心逃跑等。在此之前的 "
                         '6 月，一级准尉柳昌勋（Yoo Chang-hoon）驳回了逮捕令，称指控 '
                         "'在事实和法律方面存在争议'，并不承认指控本身。检方认为，在强化调查中提出的新指控有助于扭转结果。检方增加了违反反贪污法的指控，称朴槿惠在担任特别检察官期间，将本应得到的 "
                         '11 '
                         '亿韩元以贷款的形式交给了女儿朴雅睦。检方称，大田洞的私营企业承诺向朴槿惠支付款项，而朴槿惠女儿获得的 '
                         '11 亿韩元也实现了这一承诺，法院接受了这一说法。\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://dimg.donga.com/a/800/0/95/5/wps/NEWS/IMAGE/2023/08/04/120570314.1.jpg" '
                         'alt="동아일보" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 동아일보</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "朴槿惠在今年早些时候销毁了自己的手机，据信这也是法院认定'证据销毁问题'的原因之一。强化调查期间获得的新证据也发挥了作用。在强化调查期间，检方获得了一份借款协议，其中指出华川大宇资产管理公司的大股东金万裴向朴槿惠借款 "
                         '5 亿韩元，朴槿惠将以股份的形式收回这笔钱。该文件为 Park '
                         "同意收钱的指控提供了支持。首尔中央地方检察厅的一位官员说：'在仔细分析了驳回搜查令的理由后，我们用确凿的证据加强了证据，并向法庭做了详细解释。朴槿惠此前曾表示，她 "
                         "'没有接受或承诺任何参与大田洞开发项目或安排融资的交换条件'。朴槿惠被拘留预计将加速 '50 亿俱乐部 "
                         "'调查的其余部分。尤其是对前国民之党议员郭尚道的调查，其案件结构类似，郭尚道通过其子女了解到自己将获得这笔钱，因此调查可能会加速。上个月 "
                         '27 日和本周早些时候，检察官分别传唤了郭尚道的儿子郭尚道（从华川大宇领取了 50 '
                         '亿韩元的遣散费（错误为 25 亿韩元））接受讯问。一位检方官员在 3 月 3 '
                         "日表示：'我们计划对所谓的'50 "
                         "亿俱乐部'依次进行调查。涉嫌'审判交易'的前最高法院大法官权顺一也正在接受调查。作者：Kwang-joon "
                         'Jeon light@hani.co.kr\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '''500억 클럽'' 박영수 구속...한 달 전 해임 당시와 달라진 점은?'\n"
                         "description: '법원이 한 차례 기각했던 박영수 전 특별검사에 대한 구속영장이 3일 "
                         "발부됐다. 박 전 특검은 대전동의 한 민간 사업가로부터 로비를 받았다...'\n"
                         "category: 'Politics'\n"
                         "keywords: '박영수 구속'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/647/imgdb/original/2023/0804/20230804501508.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '법원이 한 차례 기각했던 박영수 전 특별검사에 대한 구속영장이 3일 발부됐다. 박 전 특검은 '
                         '대전동의 한 민간 사업가로부터 로비를 받았다...\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 박영수 특별검사팀에 대한 구속영장이 발부된 이유는 '
                         '무엇인가요?</b></summary>\n'
                         '    박영수 특별검사팀은 증거인멸의 우려가 있다는 이유로 박영수 특별검사팀에 대해 구속영장을 '
                         '청구했습니다. 검찰은 보강 수사 과정에서 청탁금지법 위반 등 새로운 혐의가 추가되면서 결과가 '
                         '뒤집힌 것으로 보고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>1. '50억 클럽'이란 무엇인가요?</b></summary>\n"
                         "    '50억 클럽'은 대전동 일대 민간 개발업자를 도와주는 대가로 돈을 받았다는 의혹을 "
                         '받는 개인들을 일컫는 말이다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>2. '50억 클럽'과 관련하여 또 누가 조사를 받고 "
                         '있나요?</b></summary>\n'
                         "    곽상도 전 국민의당 의원과 권순일 전 대법관도 '50억 클럽' 사건과 관련해 수사를 "
                         '받고 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>3. '50억 클럽' 수사에서 박영수 특검의 구속이 갖는 의미는 "
                         '무엇인가요?</b></summary>\n'
                         "    박영수 특검의 구속으로 나머지 '50억 클럽' 수사에 속도가 붙을 것으로 전망됩니다. "
                         '또한 그룹 내 다른 멤버들에 대한 추가 수사로 이어질 가능성도 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         "## ''500억 클럽'' 박영수 구속...한 달 전 해임 당시와 달라진 점은?\n"
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "대전동 민간 개발업자를 도와주는 대가로 금품을 받은 이른바 '50억 클럽' 의혹을 받고 있는 "
                         '박영수 전 특별검사가 2일 오전 서울 서초구 서울중앙지방법원에서 두 번째 구속 전 피의자 '
                         '심문(영장실질심사)에 출석하기 위해 법정으로 향하고 있다. 연합뉴스 법원이 한 차례 기각했던 '
                         '박영수 특별검사팀의 박영수 전 특별검사에 대한 구속영장이 2일 발부됐다. 박 전 특검은 대구의 '
                         "한 민간 사업가로부터 로비를 받은 혐의를 받는 '50억 클럽' 멤버 중 한 명으로 꼽힌다. "
                         '검찰이 보강 수사 과정에서 추가 혐의를 적용한 것이 영향을 미친 것으로 보인다. 윤재남 '
                         "서울중앙지법 영장전담 부장판사는 3일 밤 '증거인멸의 우려가 있다'며 박 전 대통령에 대한 "
                         '구속영장 발부 사유를 밝혔다. 통상 구속영장은 혐의가 일부 소명됐다는 전제 하에 증거인멸, '
                         "도주 우려 등의 사유를 들어 발부된다. 앞서 지난 6월 유창훈 영장전담 부장판사는 '사실관계 "
                         "및 법리상 다툼의 여지가 있다'며 혐의 자체를 인정하지 않고 구속영장을 기각한 바 있다. "
                         '검찰은 보강 수사를 통해 새롭게 제기된 혐의가 결과를 뒤집는 데 도움이 됐다고 보고 있습니다. '
                         '검찰은 박 전 대통령이 받아야 할 돈 중 11억 원이 특검 재직 당시 딸 박 아무개 씨에게 '
                         '대여금 명목으로 전달됐다며 청탁금지법 위반 혐의를 추가했다. 검찰은 대전동 소재 개인 '
                         '사업자들이 박 전 대통령에게 돈을 주기로 약속했고, 박 전 대통령의 딸에게 간 11억 원은 그 '
                         '약속이 실현된 것이라고 주장했고, 법원은 이를 받아들였다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://dimg.donga.com/a/800/0/95/5/wps/NEWS/IMAGE/2023/08/04/120570314.1.jpg" '
                         'alt="동아일보" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 동아일보</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         "박 씨가 올해 초 휴대전화를 파기한 것도 법원이 '증거인멸 우려'를 판단하는 데 영향을 미친 "
                         '것으로 추정됩니다. 보강 수사를 통해 확보한 새로운 증거도 한몫했다. 검찰은 보강 수사 '
                         '과정에서 화천대우자산운용의 대주주인 김만배 씨가 박 씨로부터 5억 원을 빌리고, 박 씨가 이 '
                         '돈을 주식으로 돌려받기로 한 차용증을 확보했다. 이 문건은 박 전 대통령이 돈을 받기로 했다는 '
                         "의혹을 뒷받침하는 근거가 됐다. 서울중앙지검 관계자는 '영장 기각 사유를 면밀히 분석한 뒤 "
                         "확실한 증거로 보강해 법원에 상세히 설명했다'고 말했다. 앞서 박 전 대통령은 '대장동 개발 "
                         "사업에 참여하거나 자금 조달을 알선하는 대가로 금품을 받거나 약속한 사실이 없다'고 진술한 바 "
                         "있다. 박 전 대통령의 구속으로 나머지 '50억 클럽' 수사에 속도가 붙을 것으로 전망된다. "
                         '특히 자녀를 통해 금품을 수수했다는 점에서 사건 구조가 비슷한 곽상도 전 국민의당 의원에 대한 '
                         '수사도 탄력을 받을 것으로 보인다. 검찰은 화천대우로부터 퇴직금 50억 원(착오 25억 원)을 '
                         '받은 곽 의원의 아들 곽상도 의원을 지난달 27일에 이어 이번 주 초에 다시 불러 조사했다. '
                         "검찰 관계자는 3일 ''50억 클럽' 의혹에 대해 순차적으로 조사할 계획'이라고 밝혔다. "
                         "'재판 거래' 의혹을 받고 있는 권순일 전 대법관도 조사를 받고 있다. 전광준 기자 "
                         'light@hani.co.kr\n')]),
 Folder(today=datetime.date(2023, 8, 5),
        folder_name='Arrest-Made-in-Daegu',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: 'Arrest Made in Daegu University Threatening "
                         "Post Case'\n"
                         "description: 'A 20-year-old individual who posted a "
                         'threatening message on the Daegu University bulletin '
                         'board has been apprehended by the Gyeongsan Police '
                         'Department. The post, which mentioned stabbings, '
                         'triggered concerns among students and prompted an '
                         "investigation.'\n"
                         "category: 'Crime'\n"
                         "keywords: '칼부림예고'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'EN-US'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://newsimg.sedaily.com/2023/08/04/29TA0FROJB_1.jpg" '
                         'alt="서울경제신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 서울경제신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'A 20-year-old individual who posted a threatening '
                         'message on the Daegu University bulletin board has '
                         'been apprehended by the Gyeongsan Police Department. '
                         'The post, which mentioned stabbings, triggered '
                         'concerns among students and prompted an '
                         'investigation.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. Who has been arrested by the '
                         'Gyeongsan Police Department?</b></summary>\n'
                         '    A 20-year-old individual has been arrested by '
                         'the Gyeongsan Police Department.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. What was the content of the '
                         'threatening post?</b></summary>\n'
                         "    The post mentioned 'Daegu University Rollo Noir "
                         "Zoro 3 degrees of stabbings.'\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. How did the police trace the '
                         'individual?</b></summary>\n'
                         '    The police traced the individual through their '
                         'internet address (IP).\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. What charges will the police file '
                         'against the arrested individual?</b></summary>\n'
                         '    The police will file threatening charges against '
                         'the arrested individual.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. What is the punishment for the '
                         'crime of threatening?</b></summary>\n'
                         '    The crime of threatening is punishable by up to '
                         'three years in prison and a fine of up to 5 million '
                         'won.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## Arrest Made in Daegu University Threatening Post '
                         'Case\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         'The Gyeongsan Police Department in Gyeongsangbuk-do, '
                         'Gyeongsangbuk-do, announced on the afternoon of the '
                         '4th that it arrested A, in his 20s, for writing a '
                         'post satirizing stabbings on the Everytime Daegu '
                         'University bulletin board (threats).A wrote a post '
                         "at 2:38 p.m. on the same day, saying, 'Daegu "
                         "University Rollo Noir Zoro 3 degrees of stabbings.' "
                         "He posted a post titled, 'Daegu University Rolloa "
                         'Zoro. The post was deleted at 3:10 p.m., but '
                         "students who saw it reported it as a 'warning of a "
                         "weapon rampage,' prompting police to launch an "
                         'investigation. Police traced his internet address '
                         '(IP) and arrested him five hours later near a study '
                         'cafe in Gyeongsan, North Gyeongsang Province.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://newsimg.sedaily.com/2023/08/04/29TA11XCJD_1.jpg" '
                         'alt="서울경제신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 서울경제신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         'Police plan to file threatening charges against him. '
                         'In the wake of the recent stabbing rampage, police '
                         'have been applying threatening charges to posters of '
                         'death threats on online communities and social media '
                         'services (SNS). The crime of threatening is '
                         'punishable by up to three years in prison and a fine '
                         'of up to 5 million won.\n'),
             Markdown(language='ZH',
                      md='---\n'
                         "title: '大邱大学恐吓帖案被捕'\n"
                         "description: '庆山警察局逮捕了一名在大邱大学公告栏上发布恐吓信息的 20 "
                         "岁男子。该帖子提到了刺杀事件，引发了学生们的担忧，并引发了调查。'\n"
                         "category: 'Crime'\n"
                         "keywords: '칼부림예고'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'ZH'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://newsimg.sedaily.com/2023/08/04/29TA0FROJB_1.jpg" '
                         'alt="서울경제신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 서울경제신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '庆山警察局逮捕了一名在大邱大学公告栏上发布恐吓信息的 20 '
                         '岁男子。该帖子提到了刺杀事件，引发了学生们的担忧，并引发了调查。\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 庆山警察局逮捕了谁？</b></summary>\n'
                         '    庆山警察局逮捕了一名 20 岁的男子。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 威胁帖子的内容是什么？</b></summary>\n'
                         "    帖子中提到 '大邱大学罗洛-诺伊尔-佐罗3度刺杀'。\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 警方是如何追踪到此人的？</b></summary>\n'
                         '    警方通过该人的互联网地址（IP）对其进行了追踪。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 警方将对被捕者提出哪些指控？</b></summary>\n'
                         '    警方将对被捕者提出威胁性指控。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 威胁罪的惩罚是什么？</b></summary>\n'
                         '    威胁罪最高可判处三年监禁和 500 万韩元罚款。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 大邱大学恐吓帖案被捕\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         "庆尚北道庆尚警察厅4日下午宣布，逮捕了在大邱大学Everytime公告栏（威胁）上发帖讽刺刺杀事件的20多岁的A某。A某于当天下午2点38分发帖称：'大邱大学Rollo "
                         "Noir Zoro 3度刺杀。他还发布了一个名为 '大邱大学 Rolloa Zoro "
                         "'的帖子。该帖子于下午 3 点 10 分被删除，但看到帖子的学生将其举报为 "
                         "'武器暴行警告'，促使警方展开调查。警方追踪到了他的互联网地址（IP），并于五小时后在庆尚北道庆山市一家学习咖啡馆附近将其逮捕。\n"
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://newsimg.sedaily.com/2023/08/04/29TA11XCJD_1.jpg" '
                         'alt="서울경제신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 서울경제신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '警方计划对他提出威胁指控。在最近发生的刺杀事件之后，警方一直在对在网络社区和社交媒体服务（SNS）上发布死亡威胁的人提出威胁指控。威胁罪最高可判处三年监禁和 '
                         '500 万韩元罚款。\n'),
             Markdown(language='KO',
                      md='---\n'
                         "title: '대구대학교 협박 게시물 사건 피의자 검거'\n"
                         "description: '대구대학교 게시판에 협박성 글을 게시한 20대가 경산경찰서에 "
                         '붙잡혔습니다. 칼부림을 언급한 이 게시물은 학생들의 우려를 불러일으키며 수사를 '
                         "촉발했습니다.'\n"
                         "category: 'Crime'\n"
                         "keywords: '칼부림예고'\n"
                         "date: '2023-08-05'\n"
                         "author: 'wikitoday.io'\n"
                         "language: 'KO'\n"
                         '---\n'
                         '\n'
                         '## Summary\n'
                         '\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://newsimg.sedaily.com/2023/08/04/29TA0FROJB_1.jpg" '
                         'alt="서울경제신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 서울경제신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '대구대학교 게시판에 협박성 글을 게시한 20대가 경산경찰서에 붙잡혔습니다. 칼부림을 언급한 이 '
                         '게시물은 학생들의 우려를 불러일으키며 수사를 촉발했습니다.\n'
                         '\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 경산경찰서에 체포된 사람은 '
                         '누구인가요?</b></summary>\n'
                         '    경북 경산경찰서에 20대 남성이 검거됐습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 협박성 게시물의 내용은 '
                         '무엇인가요?</b></summary>\n'
                         "    해당 게시물에는 '대구대 롤로누아 조로 3도 칼부림'이라는 제목의 글이 올라왔습니다.\n"
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 경찰은 이 개인을 어떻게 '
                         '추적했나요?</b></summary>\n'
                         '    경찰은 인터넷 주소(IP)를 통해 해당 개인을 추적했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 체포된 사람에게는 경찰이 어떤 혐의를 '
                         '적용하나요?</b></summary>\n'
                         '    경찰은 체포된 개인에 대해 협박 혐의를 적용할 것입니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 협박죄의 처벌은 어떻게 되나요?</b></summary>\n'
                         '    협박죄는 3년 이하의 징역 또는 500만 원 이하의 벌금에 처해질 수 있습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '\n'
                         '## 대구대학교 협박 게시물 사건 피의자 검거\n'
                         '\n'
                         '_2023-08-05 - wikitoday_\n'
                         '\n'
                         '경북 경산경찰서는 에브리타임 대구대 게시판에 칼부림을 풍자하는 글을 쓴 혐의(협박)로 20대 '
                         "A씨를 검거했다고 4일 오후 밝혔다.A씨는 이날 오후 2시 38분께 '대구대 롤로아 조로 3도 "
                         "칼부림'이라는 게시물을 작성했다. 그는 '대구대 롤로아 조로'라는 제목의 글을 올렸다. 이 "
                         "게시물은 오후 3시 10분께 삭제됐지만, 이를 본 학생들이 '흉기 난동 경고'라며 신고해 "
                         '경찰이 수사에 착수했다. 경찰은 그의 인터넷 주소(IP)를 추적해 5시간 뒤 경북 경산의 한 '
                         '스터디카페 근처에서 그를 체포했습니다.\n'
                         '\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://newsimg.sedaily.com/2023/08/04/29TA11XCJD_1.jpg" '
                         'alt="서울경제신문" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 서울경제신문</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '\n'
                         '경찰은 그를 협박 혐의로 기소할 계획입니다. 최근 칼부림 난동 사건 이후 경찰은 온라인 '
                         '커뮤니티와 소셜 미디어 서비스(SNS)에 살해 협박을 게시하는 게시자에게 협박 혐의를 적용하고 '
                         '있습니다. 협박죄는 3년 이하의 징역 또는 500만 원 이하의 벌금에 처해질 수 '
                         '있습니다.\n')])]