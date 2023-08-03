import datetime

from domain.entities import (Article, ArticleContent, ArticleImage,
                             CrawledTrend, Folder, GoogleTrend, Language,
                             Markdown, QnA, TranslatedCrawledTrend,
                             TrendArticleMeta)

######################### STEP 1 ##########################
step_1 = [GoogleTrend(query='류현진',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://www.hani.co.kr/arti/sports/baseball/1102657.html',
                                        source='한겨레'),
                       TrendArticleMeta(url='https://imnews.imbc.com/news/2023/sports/article/6510102_36154.html',
                                        source='MBC뉴스')]),
 GoogleTrend(query='참교육 유튜버',
             related_quries=[],
             articles=[TrendArticleMeta(url='https://www.donga.com/news/Society/article/all/20230802/120527436/1',
                                        source='동아일보'),
                       TrendArticleMeta(url='https://news.mt.co.kr/mtview.php?no=2023080206005192911',
                                        source='머니투데이')])]


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
step_4 = [
    Article(
        category='Entertainment',
         keywords='안보현,지수 안보현,안보현 지수,블랙핑크 지수',
         contents=[ArticleContent(title="[Official] BLACKPINK's Jisoo and "
                                        'Actor Bo Bo Hyun Confirmed to be '
                                        'Dating',
                                  lead='Jisoo (28) of the group BLACKPINK and '
                                       'actor Bo Bo Hyun (35) are in a '
                                       "relationship. On the 3rd, Jisoo's "
                                       "agency, YG Entertainment, said, 'They "
                                       'are getting to know each other little '
                                       "by little with good feelings.'",
                                  body1='Jisoo (28) of the group Blackpink and '
                                        'actor Bo Bo Hyun (35) are in a '
                                        "relationship. On March 3, Jisoo's "
                                        "agency YG Entertainment said, 'They "
                                        'are getting to know each other little '
                                        'by little with good feelings.',
                                  body2='We would appreciate it if you could '
                                        "watch them with a warm gaze.' Anbo "
                                        "Hyun's agency, FN Entertainment, also "
                                        "said, 'They are in the stage of "
                                        'getting to know each other carefully '
                                        'with good feelings. We would '
                                        'appreciate it if you could watch them '
                                        "with a warm gaze.' Earlier in the "
                                        'day, media outlet Dispatch reported '
                                        'that Jisoo and Anbo Hyun were spotted '
                                        "dating at Jisoo's home in Seoul. "
                                        "'They have a lot of common "
                                        'denominators, from acting to singing '
                                        "to fashion,' a source close to the "
                                        'pair told the Dispatch.',
                                  qna_list=[QnA(question='Who is Jisoo?',
                                                answer='Jisoo is a member of '
                                                       'the popular girl group '
                                                       'BLACKPINK.'),
                                            QnA(question='Who is Bo Bo Hyun?',
                                                answer='Bo Bo Hyun is an actor '
                                                       'known for his roles in '
                                                       'dramas such as '
                                                       "'Itaewon Class' and "
                                                       "'Yumi's Cells.'"),
                                            QnA(question='How did the news of '
                                                         'Jisoo and Bo Bo Hyun '
                                                         'dating come out?',
                                                answer='The news was first '
                                                       'reported by media '
                                                       'outlet Dispatch, which '
                                                       'revealed that the two '
                                                       'were spotted dating at '
                                                       "Jisoo's home in Seoul."),
                                            QnA(question="What did Jisoo's "
                                                         'agency say about '
                                                         'their relationship?',
                                                answer="Jisoo's agency, YG "
                                                       'Entertainment, stated '
                                                       'that Jisoo and Bo Bo '
                                                       'Hyun are getting to '
                                                       'know each other little '
                                                       'by little with good '
                                                       'feelings.'),
                                            QnA(question='What did Bo Bo '
                                                         "Hyun's agency say "
                                                         'about their '
                                                         'relationship?',
                                                answer="Bo Bo Hyun's agency, "
                                                       'FN Entertainment, also '
                                                       'mentioned that they '
                                                       'are in the stage of '
                                                       'getting to know each '
                                                       'other carefully with '
                                                       'good feelings.')],
                                  language=Language.EN_US)],
         images=[ArticleImage(url='https://newsimg.sedaily.com/2023/08/03/29T9HS4184_1.jpg',
                              source='서울경제신문'),
                 ArticleImage(url='https://www.allurekorea.com/wp_data/allure/2023/08/style_64cb5029288c0-700x500-1691046194.jpg',
                              source='얼루어 코리아 (Allure Korea)')]),
    Article(category='Sports',
         keywords='류현진',
         contents=[ArticleContent(
             language="EN-US",
             title="Ryu's Return to the Mound Ends in a "
                                      'Loss Against the Baltimore Orioles',
                                lead="Toronto Blue Jays' pitcher, Hyun-jin "
                                     'Ryu, made his first start in over a year '
                                     "but couldn't prevent the AL's leading "
                                     'team from winning.',
                                body1='In his comeback game, Hyun-jin Ryu '
                                      'pitched for the Toronto Blue Jays '
                                      'against the Baltimore Orioles in the '
                                      'Major League Baseball (MLB) World '
                                      "Series. Despite Ryu's efforts, the "
                                      'Orioles emerged victorious, scoring '
                                      'four runs on nine hits in five innings. '
                                      'Ryu showcased his talents by throwing a '
                                      'fastball at an impressive speed of 146 '
                                      'mph.',
                                body2='However, his performance was unable to '
                                      'secure a win for his team. This loss '
                                      "marked Ryu's first in the 2023 season "
                                      'after undergoing ligament splicing '
                                      'surgery in his left elbow. Despite the '
                                      'setback, fans and experts are '
                                      "optimistic about Ryu's future "
                                      'performance.',
                                qna_list=[QnA(question='Who did Hyun-jin Ryu '
                                                       'pitch against in his '
                                                       'comeback game?',
                                              answer='Hyun-jin Ryu pitched '
                                                     'against the Baltimore '
                                                     'Orioles.'),
                                          QnA(question='How many runs did the '
                                                       'Baltimore Orioles '
                                                       'score against Ryu?',
                                              answer='The Baltimore Orioles '
                                                     'scored four runs against '
                                                     'Ryu.'),
                                          QnA(question="What was Ryu's "
                                                       'fastball speed during '
                                                       'the game?',
                                              answer="Ryu's fastball reached "
                                                     'an impressive speed of '
                                                     '146 mph.'),
                                          QnA(question="What was Ryu's "
                                                       'previous performance '
                                                       'before his comeback '
                                                       'game?',
                                              answer='Ryu had been out of '
                                                     'action for over a year '
                                                     'due to ligament splicing '
                                                     'surgery on his left '
                                                     'elbow.'),
                                          QnA(question='What is the outlook '
                                                       "for Ryu's future "
                                                       'performances?',
                                              answer='Despite the loss, fans '
                                                     'and experts are '
                                                     "optimistic about Ryu's "
                                                     'future performance.')])],
         images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg',
                              source='한겨레'),
                 ArticleImage(url='https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg',
                              source='MBC뉴스')]),
      Article(category='Sports',
         keywords='류현진2',
         contents=[ArticleContent(
             language="EN-US",
             title="Ryu's Return to the Mound Ends in a "
                                      'Loss Against the Baltimore Orioles',
                                lead="Toronto Blue Jays' pitcher, Hyun-jin "
                                     'Ryu, made his first start in over a year '
                                     "but couldn't prevent the AL's leading "
                                     'team from winning.',
                                body1='In his comeback game, Hyun-jin Ryu '
                                      'pitched for the Toronto Blue Jays '
                                      'against the Baltimore Orioles in the '
                                      'Major League Baseball (MLB) World '
                                      "Series. Despite Ryu's efforts, the "
                                      'Orioles emerged victorious, scoring '
                                      'four runs on nine hits in five innings. '
                                      'Ryu showcased his talents by throwing a '
                                      'fastball at an impressive speed of 146 '
                                      'mph.',
                                body2='However, his performance was unable to '
                                      'secure a win for his team. This loss '
                                      "marked Ryu's first in the 2023 season "
                                      'after undergoing ligament splicing '
                                      'surgery in his left elbow. Despite the '
                                      'setback, fans and experts are '
                                      "optimistic about Ryu's future "
                                      'performance.',
                                qna_list=[QnA(question='Who did Hyun-jin Ryu '
                                                       'pitch against in his '
                                                       'comeback game?',
                                              answer='Hyun-jin Ryu pitched '
                                                     'against the Baltimore '
                                                     'Orioles.'),
                                          QnA(question='How many runs did the '
                                                       'Baltimore Orioles '
                                                       'score against Ryu?',
                                              answer='The Baltimore Orioles '
                                                     'scored four runs against '
                                                     'Ryu.'),
                                          QnA(question="What was Ryu's "
                                                       'fastball speed during '
                                                       'the game?',
                                              answer="Ryu's fastball reached "
                                                     'an impressive speed of '
                                                     '146 mph.'),
                                          QnA(question="What was Ryu's "
                                                       'previous performance '
                                                       'before his comeback '
                                                       'game?',
                                              answer='Ryu had been out of '
                                                     'action for over a year '
                                                     'due to ligament splicing '
                                                     'surgery on his left '
                                                     'elbow.'),
                                          QnA(question='What is the outlook '
                                                       "for Ryu's future "
                                                       'performances?',
                                              answer='Despite the loss, fans '
                                                     'and experts are '
                                                     "optimistic about Ryu's "
                                                     'future performance.')])],
         images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg',
                              source='한겨레'),
                 ArticleImage(url='https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg',
                              source='MBC뉴스')])                              
                              ]


########################## STEP 5 ##########################
step_5 = [Article(category='Entertainment',
         keywords='안보현,지수 안보현,안보현 지수,블랙핑크 지수',
         contents=[ArticleContent(title="BLACKPINK's Jisoo and Actor Ahn Bo "
                                        'Hyun Confirm Relationship',
                                  lead="Girl group BLACKPINK's Jisoo and actor "
                                       'Ahn Bo Hyun have confirmed their '
                                       'relationship very quickly.',
                                  body1="Jisoo's agency, YG Entertainment, "
                                        'said that they are getting to know '
                                        'each other little by little with good '
                                        'feelings and urged people to watch '
                                        "them with a warm gaze. Ahn Bo Hyun's "
                                        'agency, FN Entertainment, echoed the '
                                        'sentiment and asked people to watch '
                                        'them with a warm gaze. Despite their '
                                        'busy schedules, the couple is '
                                        'continuing to see each other.',
                                  body2='They have many common denominators, '
                                        'including acting, singing, and '
                                        'fashion. Jisoo, a member of '
                                        'BLACKPINK, debuted in 2016 and '
                                        'recently completed her acting debut. '
                                        'Ahn Bo Hyun, who made his debut as a '
                                        'model in 2007, has appeared in '
                                        'various dramas and gained popularity '
                                        'for his roles. The couple has a '
                                        'seven-year age difference.',
                                  qna_list=[QnA(question='Who confirmed their '
                                                         'relationship?',
                                                answer="BLACKPINK's Jisoo and "
                                                       'actor Ahn Bo Hyun.'),
                                            QnA(question="What did Jisoo's "
                                                         'agency say about '
                                                         'their relationship?',
                                                answer='They are getting to '
                                                       'know each other little '
                                                       'by little with good '
                                                       'feelings and urged '
                                                       'people to watch them '
                                                       'with a warm gaze.'),
                                            QnA(question='What did Ahn Bo '
                                                         "Hyun's agency say "
                                                         'about their '
                                                         'relationship?',
                                                answer='They are in the stage '
                                                       'of getting to know '
                                                       'each other with good '
                                                       'feelings and asked '
                                                       'people to watch them '
                                                       'with a warm gaze.'),
                                            QnA(question='What are some common '
                                                         'denominators between '
                                                         'Jisoo and Ahn Bo '
                                                         'Hyun?',
                                                answer='They have common '
                                                       'denominators including '
                                                       'acting, singing, and '
                                                       'fashion.'),
                                            QnA(question='When did Jisoo debut '
                                                         'and what is her '
                                                         'recent achievement?',
                                                answer='Jisoo debuted in 2016 '
                                                       'as a member of '
                                                       'BLACKPINK and recently '
                                                       'completed her acting '
                                                       'debut.'),
                                            QnA(question='When did Ahn Bo Hyun '
                                                         'debut and what are '
                                                         'some of his popular '
                                                         'roles?',
                                                answer='Ahn Bo Hyun made his '
                                                       'debut as a model in '
                                                       '2007 and gained '
                                                       'popularity for his '
                                                       'roles in various '
                                                       'dramas.'),
                                            QnA(question='How old is the '
                                                         'couple?',
                                                answer='There is a seven-year '
                                                       'age difference between '
                                                       'the two.')],
                                  language=Language.EN_US),
                   ArticleContent(title='BLACKPINK 的 Jisoo 和演员安宝贤确认恋情',
                                  lead='女子组合 BLACKPINK 的 Jisoo 和演员安宝贤迅速确认了恋情。',
                                  body1='Jisoo 的经纪公司 YG Entertainment '
                                        '表示，他们正怀着美好的感情一点一点地了解对方，并呼吁大家用温暖的目光注视他们。安宝贤的经纪公司 '
                                        'FN Entertainment '
                                        '也表示了同样的看法，并希望大家用温暖的目光注视着他们。尽管工作繁忙，但这对情侣仍在继续交往。',
                                  body2='她们有许多共同点，包括演戏、唱歌和时尚。BLACKPINK 成员 '
                                        'Jisoo 于 2016 年出道，最近完成了她的演艺首秀。2007 '
                                        '年以模特身份出道的安宝贤出演了多部电视剧，并凭借角色获得了很高的人气。这对情侣年龄相差 '
                                        '7 岁。',
                                  qna_list=[QnA(question='谁确认了他们的关系？',
                                                answer='BLACKPINK 的 Jisoo '
                                                       '和演员安宝贤。'),
                                            QnA(question='Jisoo '
                                                         '的经纪公司如何看待他们的关系？',
                                                answer='他们带着美好的感情一点一点地了解彼此，并催促人们用温暖的目光注视着他们。'),
                                            QnA(question='安宝贤的经纪公司如何评价他们的关系？',
                                                answer='他们正处于相互了解的阶段，感情很好，请大家用温暖的目光注视着他们。'),
                                            QnA(question='Jisoo 和安宝贤之间有哪些共同点？',
                                                answer='他们的共同点包括表演、唱歌和时尚。'),
                                            QnA(question='Jisoo '
                                                         '何时出道，最近取得了哪些成就？',
                                                answer='Jisoo 于 2016 年作为 '
                                                       'BLACKPINK '
                                                       '成员出道，最近完成了她的演艺首秀。'),
                                            QnA(question='安宝贤何时出道，他出演过哪些受欢迎的角色？',
                                                answer='2007 '
                                                       '年，安宝贤以模特身份出道，并因出演多部电视剧而广受欢迎。'),
                                            QnA(question='这对夫妇多大年纪？',
                                                answer='两人的年龄相差 7 岁。')],
                                  language=Language.ZH),
                   ArticleContent(title='블랙핑크 지수와 배우 안보현, 열애 사실 확인',
                                  lead='걸그룹 블랙핑크의 지수와 배우 안보현이 열애를 빠르게 확인했습니다.',
                                  body1='지수의 소속사 YG엔터테인먼트는 두 사람이 좋은 감정으로 조금씩 '
                                        '서로를 알아가고 있다며 따뜻한 시선으로 지켜봐 달라고 당부했습니다. '
                                        '안보현의 소속사 FN엔터테인먼트 역시 이에 공감하며 따뜻한 시선으로 '
                                        '두 사람을 지켜봐 달라고 당부했다. 두 사람은 바쁜 스케줄에도 '
                                        '불구하고 만남을 이어가고 있습니다.',
                                  body2='연기, 노래, 패션 등 많은 공통분모를 가지고 있습니다. 블랙핑크의 '
                                        '멤버 지수는 2016년에 데뷔해 최근 연기 데뷔를 마쳤다. '
                                        '2007년 모델로 데뷔한 안보현은 다양한 드라마에 출연하며 연기력을 '
                                        '인정받았고, 다양한 역할로 인기를 얻었습니다. 두 사람은 7살 나이 '
                                        '차이가 난다.',
                                  qna_list=[QnA(question='누가 두 사람의 관계를 확인했나요?',
                                                answer='블랙핑크의 지수와 배우 안보현.'),
                                            QnA(question='지수의 소속사는 두 사람의 관계에 '
                                                         '대해 뭐라고 말했나요?',
                                                answer='두 사람은 좋은 감정으로 조금씩 서로를 '
                                                       '알아가고 있다며 따뜻한 시선으로 지켜봐 '
                                                       '달라고 당부했다.'),
                                            QnA(question='안보현의 소속사는 두 사람의 관계에 '
                                                         '대해 뭐라고 말했나요?',
                                                answer='두 사람은 좋은 감정으로 서로를 알아가는 '
                                                       '단계라며 따뜻한 시선으로 지켜봐 달라고 '
                                                       '당부했다.'),
                                            QnA(question='지수와 안보현의 공통분모는 '
                                                         '무엇인가요?',
                                                answer='이들은 연기, 노래, 패션 등 공통 '
                                                       '분모를 가지고 있습니다.'),
                                            QnA(question='지수는 언제 데뷔했고 최근 성과는 '
                                                         '무엇인가요?',
                                                answer='2016년 블랙핑크 멤버로 데뷔한 지수는 '
                                                       '최근 연기자로 데뷔했습니다.'),
                                            QnA(question='안보현은 언제 데뷔했고 어떤 역할을 '
                                                         '주로 맡았나요?',
                                                answer='안보현은 2007년 모델로 데뷔해 다양한 '
                                                       '드라마에 출연하며 인기를 얻었습니다.'),
                                            QnA(question='부부의 나이는 몇 살인가요?',
                                                answer='두 사람 사이에는 7살의 나이 차이가 '
                                                       '있습니다.')],
                                  language=Language.KO)],
         images=[ArticleImage(url='https://image.ytn.co.kr/general/jpg/2023/0803/202308031050039701_t.jpg',
                              source='YTN'),
                 ArticleImage(url='https://newsimg.sedaily.com/2023/08/03/29T9HS4184_1.jpg',
                              source='서울경제신문')])]

########################## STEP 6 ##########################
step_6 = [Folder(today=datetime.date(2023, 8, 2),
        folder_name='Ryu-s-Return-to-the-Mound-Ends-in-a-Loss',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: Ryu's Return to the Mound Ends in a Loss "
                         'Against the Baltimore Orioles\n'
                         "description: Toronto Blue Jays' pitcher, Hyun-jin "
                         'Ryu, made his first start in over a year but '
                         "couldn't prevent the AL's leading team from "
                         'winning.\n'
                         'category: Sports\n'
                         'keywords: 류현진\n'
                         'date: 2023-08-02\n'
                         'author: wikitoday.io\n'
                         'language: EN-US\n'
                         '---\n'
                         '\n'
                         '# Summary\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         "Toronto Blue Jays' pitcher, Hyun-jin Ryu, made his "
                         "first start in over a year but couldn't prevent the "
                         "AL's leading team from winning.\n"
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. Who did Hyun-jin Ryu pitch '
                         'against in his comeback game?</b></summary>\n'
                         '    Hyun-jin Ryu pitched against the Baltimore '
                         'Orioles.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. How many runs did the Baltimore '
                         'Orioles score against Ryu?</b></summary>\n'
                         '    The Baltimore Orioles scored four runs against '
                         'Ryu.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>2. What was Ryu's fastball speed "
                         'during the game?</b></summary>\n'
                         "    Ryu's fastball reached an impressive speed of "
                         '146 mph.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>3. What was Ryu's previous "
                         'performance before his comeback game?</b></summary>\n'
                         '    Ryu had been out of action for over a year due '
                         'to ligament splicing surgery on his left elbow.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>4. What is the outlook for Ryu's "
                         'future performances?</b></summary>\n'
                         '    Despite the loss, fans and experts are '
                         "optimistic about Ryu's future performance.\n"
                         '</details>\n'
                         '\n'
                         '\n'
                         "## Ryu's Return to the Mound Ends in a Loss Against "
                         'the Baltimore Orioles\n'
                         '\n'
                         '_2023-08-02 - wikitoday_\n'
                         '\n'
                         'In his comeback game, Hyun-jin Ryu pitched for the '
                         'Toronto Blue Jays against the Baltimore Orioles in '
                         'the Major League Baseball (MLB) World Series. '
                         "Despite Ryu's efforts, the Orioles emerged "
                         'victorious, scoring four runs on nine hits in five '
                         'innings. Ryu showcased his talents by throwing a '
                         'fastball at an impressive speed of 146 mph.\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         'However, his performance was unable to secure a win '
                         "for his team. This loss marked Ryu's first in the "
                         '2023 season after undergoing ligament splicing '
                         'surgery in his left elbow. Despite the setback, fans '
                         "and experts are optimistic about Ryu's future "
                         'performance.\n'
                         '\n'
                         '_end_\n'),
             Markdown(language='ZH',
                      md='---\n'
                         'title: 柳箫然重返投手丘，最终不敌巴尔的摩金莺队\n'
                         'description: 多伦多蓝鸟队的投手柳贤振一年多来首次先发，但未能阻止美联领先的球队获胜。\n'
                         'category: Sports\n'
                         'keywords: 류현진\n'
                         'date: 2023-08-02\n'
                         'author: wikitoday.io\n'
                         'language: ZH\n'
                         '---\n'
                         '\n'
                         '# Summary\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '多伦多蓝鸟队的投手柳贤振一年多来首次先发，但未能阻止美联领先的球队获胜。\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 柳贤振在复出赛中的对手是谁？</b></summary>\n'
                         '    柳贤振在与巴尔的摩金莺队的比赛中投球。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 巴尔的摩金莺队对柳箫然的得分是多少？</b></summary>\n'
                         '    巴尔的摩金莺队对柳箫然打出四次安打。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 比赛中隆的快速球速是多少？</b></summary>\n'
                         '    柳箫然的快速球达到了令人印象深刻的 146 英里/小时。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 柳忠秧在复出前的表现如何？</b></summary>\n'
                         '    由于左肘接受了韧带接合手术，柳忠秧已经休战了一年多。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 柳忠秧未来的表现前景如何？</b></summary>\n'
                         '    尽管输掉了比赛，但球迷和专家们对柳箫然未来的表现还是持乐观态度。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '## 柳箫然重返投手丘，最终不敌巴尔的摩金莺队\n'
                         '\n'
                         '_2023-08-02 - wikitoday_\n'
                         '\n'
                         '在美国职业棒球大联盟（MLB）世界系列赛中，柳贤振代表多伦多蓝鸟队对阵巴尔的摩金莺队，这是他的复出之战。尽管柳贤振做出了努力，但金莺队还是取得了胜利，在五局比赛中被击出九支安打，得到四分。隆以令人印象深刻的 '
                         '146 英里/小时的速度投出快速球，展示了自己的天赋。\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '然而，他的表现未能为球队赢得一场胜利。这场失利是柳箫然接受左肘韧带接合手术后在 2023 '
                         '赛季的首场失利。尽管遭遇挫折，但球迷和专家对柳箫然未来的表现持乐观态度。\n'
                         '\n'
                         '_end_\n'),
             Markdown(language='KO',
                      md='---\n'
                         'title: 류현진의 마운드 복귀, 볼티모어 오리올스전 패배로 끝나다\n'
                         'description: 토론토 블루제이스의 류현진 투수가 1년여 만에 선발 등판했지만, AL '
                         '선두 팀의 승리를 막지는 못했습니다.\n'
                         'category: Sports\n'
                         'keywords: 류현진\n'
                         'date: 2023-08-02\n'
                         'author: wikitoday.io\n'
                         'language: KO\n'
                         '---\n'
                         '\n'
                         '# Summary\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '토론토 블루제이스의 류현진 투수가 1년여 만에 선발 등판했지만, AL 선두 팀의 승리를 막지는 '
                         '못했습니다.\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 류현진 선수의 복귀전에서 상대 투수는 '
                         '누구였나요?</b></summary>\n'
                         '    류현진이 볼티모어 오리올스를 상대로 투구했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 볼티모어 오리올스가 류현진을 상대로 얼마나 많은 득점을 '
                         '올렸나요?</b></summary>\n'
                         '    볼티모어 오리올스는 류현진을 상대로 4득점을 올렸습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 경기 중 류현진의 직구 속도는 어느 '
                         '정도였나요?</b></summary>\n'
                         '    류현진의 직구는 최고 시속 146마일이라는 놀라운 속도를 기록했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 복귀전 경기 전 류제국의 이전 성적은 '
                         '어땠나요?</b></summary>\n'
                         '    류 선수는 왼쪽 팔꿈치 인대 접합 수술로 1년 넘게 경기에 나서지 못했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 류 선수의 향후 활약에 대한 전망은 어떻게 '
                         '되나요?</b></summary>\n'
                         '    패배에도 불구하고 팬들과 전문가들은 류제국의 향후 활약에 대해 낙관적인 전망을 내놓고 '
                         '있습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '## 류현진의 마운드 복귀, 볼티모어 오리올스전 패배로 끝나다\n'
                         '\n'
                         '_2023-08-02 - wikitoday_\n'
                         '\n'
                         '류현진은 메이저리그 야구(MLB) 월드시리즈에서 토론토 블루제이스와 볼티모어 오리올스를 상대로 '
                         '복귀전에서 선발 투수로 등판했습니다. 류현진의 호투에도 불구하고 오리올스는 5이닝 동안 '
                         '9안타에 4실점하며 승리를 거뒀습니다. 류현진은 시속 146마일이라는 놀라운 속도의 직구를 '
                         '던지며 자신의 재능을 뽐냈습니다.\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '그러나 그의 활약은 팀의 승리를 보장하지 못했습니다. 이번 패배는 왼쪽 팔꿈치 인대 접합 '
                         '수술을 받은 류현진의 2023시즌 첫 패배였습니다. 아쉬움에도 불구하고 팬들과 전문가들은 '
                         '류현진의 향후 활약에 대해 낙관적인 전망을 내놓고 있습니다.\n'
                         '\n'
                         '_end_\n')]),
 Folder(today=datetime.date(2023, 8, 2),
        folder_name='Ryu-s-Return-to-the-Mound-Ends-in-a-Loss',
        mds=[Markdown(language='EN-US',
                      md='---\n'
                         "title: Ryu's Return to the Mound Ends in a Loss "
                         'Against the Baltimore Orioles\n'
                         "description: Toronto Blue Jays' pitcher, Hyun-jin "
                         'Ryu, made his first start in over a year but '
                         "couldn't prevent the AL's leading team from "
                         'winning.\n'
                         'category: Sports\n'
                         'keywords: 류현진2\n'
                         'date: 2023-08-02\n'
                         'author: wikitoday.io\n'
                         'language: EN-US\n'
                         '---\n'
                         '\n'
                         '# Summary\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         "Toronto Blue Jays' pitcher, Hyun-jin Ryu, made his "
                         "first start in over a year but couldn't prevent the "
                         "AL's leading team from winning.\n"
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. Who did Hyun-jin Ryu pitch '
                         'against in his comeback game?</b></summary>\n'
                         '    Hyun-jin Ryu pitched against the Baltimore '
                         'Orioles.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. How many runs did the Baltimore '
                         'Orioles score against Ryu?</b></summary>\n'
                         '    The Baltimore Orioles scored four runs against '
                         'Ryu.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>2. What was Ryu's fastball speed "
                         'during the game?</b></summary>\n'
                         "    Ryu's fastball reached an impressive speed of "
                         '146 mph.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>3. What was Ryu's previous "
                         'performance before his comeback game?</b></summary>\n'
                         '    Ryu had been out of action for over a year due '
                         'to ligament splicing surgery on his left elbow.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         "    <summary><b>4. What is the outlook for Ryu's "
                         'future performances?</b></summary>\n'
                         '    Despite the loss, fans and experts are '
                         "optimistic about Ryu's future performance.\n"
                         '</details>\n'
                         '\n'
                         '\n'
                         "## Ryu's Return to the Mound Ends in a Loss Against "
                         'the Baltimore Orioles\n'
                         '\n'
                         '_2023-08-02 - wikitoday_\n'
                         '\n'
                         'In his comeback game, Hyun-jin Ryu pitched for the '
                         'Toronto Blue Jays against the Baltimore Orioles in '
                         'the Major League Baseball (MLB) World Series. '
                         "Despite Ryu's efforts, the Orioles emerged "
                         'victorious, scoring four runs on nine hits in five '
                         'innings. Ryu showcased his talents by throwing a '
                         'fastball at an impressive speed of 146 mph.\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         'However, his performance was unable to secure a win '
                         "for his team. This loss marked Ryu's first in the "
                         '2023 season after undergoing ligament splicing '
                         'surgery in his left elbow. Despite the setback, fans '
                         "and experts are optimistic about Ryu's future "
                         'performance.\n'
                         '\n'
                         '_end_\n'),
             Markdown(language='ZH',
                      md='---\n'
                         'title: 柳箫然重返投手丘，最终不敌巴尔的摩金莺队\n'
                         'description: 多伦多蓝鸟队的投手柳贤振一年多来首次先发，但未能阻止美联领先的球队获胜。\n'
                         'category: Sports\n'
                         'keywords: 류현진2\n'
                         'date: 2023-08-02\n'
                         'author: wikitoday.io\n'
                         'language: ZH\n'
                         '---\n'
                         '\n'
                         '# Summary\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '多伦多蓝鸟队的投手柳贤振一年多来首次先发，但未能阻止美联领先的球队获胜。\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 柳贤振在复出赛中的对手是谁？</b></summary>\n'
                         '    柳贤振在与巴尔的摩金莺队的比赛中投球。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 巴尔的摩金莺队对柳箫然的得分是多少？</b></summary>\n'
                         '    巴尔的摩金莺队在与柳箫然的比赛中得到 4 分。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 比赛中隆的快速球速是多少？</b></summary>\n'
                         '    柳箫然的快速球达到了令人印象深刻的 146 英里/小时。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 柳忠秧在复出前的表现如何？</b></summary>\n'
                         '    由于左肘接受了韧带接合手术，柳忠秧已经休战了一年多。\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 柳忠秧未来的表现前景如何？</b></summary>\n'
                         '    尽管输掉了比赛，但球迷和专家们对柳箫然未来的表现还是很乐观。\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '## 柳箫然重返投手丘，最终不敌巴尔的摩金莺队\n'
                         '\n'
                         '_2023-08-02 - wikitoday_\n'
                         '\n'
                         '在美国职业棒球大联盟（MLB）世界系列赛中，柳贤振代表多伦多蓝鸟队对阵巴尔的摩金莺队，这是他的复出之战。尽管柳贤振做出了努力，但金莺队还是取得了胜利，在五局比赛中被击出九支安打，得到四分。隆以 '
                         '146 英里/小时的惊人速度投出快速球，展示了自己的天赋。\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '然而，他的表现未能为球队赢得一场胜利。这场失利是柳箫然接受左肘韧带接合手术后在 2023 '
                         '赛季的首场失利。尽管遭遇挫折，但球迷和专家对柳箫然未来的表现持乐观态度。\n'
                         '\n'
                         '_end_\n'),
             Markdown(language='KO',
                      md='---\n'
                         'title: 류현진의 마운드 복귀, 볼티모어 오리올스전 패배로 끝나다\n'
                         'description: 토론토 블루제이스의 류현진 투수가 1년여 만에 선발 등판했지만, AL '
                         '선두 팀의 승리를 막지는 못했습니다.\n'
                         'category: Sports\n'
                         'keywords: 류현진2\n'
                         'date: 2023-08-02\n'
                         'author: wikitoday.io\n'
                         'language: KO\n'
                         '---\n'
                         '\n'
                         '# Summary\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg" '
                         'alt="한겨레" />\n'
                         '    <figcaption>\n'
                         '        <h4> from 한겨레</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '토론토 블루제이스의 류현진 투수가 1년여 만에 선발 등판했지만, AL 선두 팀의 승리를 막지는 '
                         '못했습니다.\n'
                         '\n'
                         '## QnA\n'
                         '\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>0. 류현진 선수의 복귀전에서 상대 투수는 '
                         '누구였나요?</b></summary>\n'
                         '    류현진이 볼티모어 오리올스를 상대로 투구했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>1. 볼티모어 오리올스가 류현진을 상대로 얼마나 많은 득점을 '
                         '올렸나요?</b></summary>\n'
                         '    볼티모어 오리올스는 류현진을 상대로 4득점을 올렸습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>2. 경기 중 류현진의 직구 속도는 어느 '
                         '정도였나요?</b></summary>\n'
                         '    류현진의 직구는 최고 시속 146마일이라는 놀라운 속도를 기록했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>3. 복귀전 경기 전 류제국의 이전 성적은 '
                         '어땠나요?</b></summary>\n'
                         '    류 선수는 왼쪽 팔꿈치 인대 접합 수술로 1년 넘게 경기에 나서지 못했습니다.\n'
                         '</details>\n'
                         '\n'
                         '<details>\n'
                         '    <summary><b>4. 류 선수의 향후 활약에 대한 전망은 어떻게 '
                         '되나요?</b></summary>\n'
                         '    패배에도 불구하고 팬들과 전문가들은 류제국의 향후 활약에 대해 낙관적인 전망을 내놓고 '
                         '있습니다.\n'
                         '</details>\n'
                         '\n'
                         '\n'
                         '## 류현진의 마운드 복귀, 볼티모어 오리올스전 패배로 끝나다\n'
                         '\n'
                         '_2023-08-02 - wikitoday_\n'
                         '\n'
                         '류현진은 메이저리그 야구(MLB) 월드시리즈에서 토론토 블루제이스와 볼티모어 오리올스를 상대로 '
                         '복귀전에서 선발 투수로 등판했습니다. 류현진의 호투에도 불구하고 오리올스는 5이닝 동안 '
                         '9안타에 4실점하며 승리를 거뒀습니다. 류현진은 시속 146마일이라는 놀라운 속도의 직구를 '
                         '던지며 자신의 재능을 뽐냈습니다.\n'
                         '\n'
                         '<figure>\n'
                         '    <img '
                         'src="https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg" '
                         'alt="MBC뉴스" />\n'
                         '    <figcaption>\n'
                         '        <h4> from MBC뉴스</h4>\n'
                         '    </figcaption>\n'
                         '</figure>\n'
                         '\n'
                         '그러나 그의 활약은 팀의 승리를 보장하지 못했습니다. 이번 패배는 왼쪽 팔꿈치 인대 접합 '
                         '수술을 받은 류현진의 2023시즌 첫 패배였습니다. 아쉬움에도 불구하고 팬들과 전문가들은 '
                         '류현진의 향후 활약에 대해 낙관적인 전망을 내놓고 있습니다.\n'
                         '\n'
                         '_end_\n')])]