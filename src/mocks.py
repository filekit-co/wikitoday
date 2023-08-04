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
step_6 = [
  {
    "today": "2023-08-03",
    "folder_name": "-Women-s-World-Cup-S",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: [Women's World Cup] South Korea Draws 1-1 with Germany...No Miracles\ndescription: Women's World Cup South Korea draws 1-1 with Germany...no miracle Jo So-hyun scores first and concedes a header Group H eliminated after 1-0 loss No miracle for South Korea, Germany. South Korea's women's soccer team was held to a 1-1 draw by Germany at the World Cup, ending their run to the round of 16 for the first time in eight years. Coach Colin Bell62\ncategory: Sports\nkeywords: 월드컵,여자월드컵,fifa 여자 월드컵,여자 월드컵\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://images.chosun.com/resizer/wx6X9TvnT8W5TzPGSyjoPQTS0WY=/1200x630/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/I22EQMSWFZMAPKLTDEFGVSVQMU.jpg\" alt=\"조선일보\" />\n    <figcaption>\n        <h4> from 조선일보</h4>\n    </figcaption>\n</figure>\n\nWomen's World Cup South Korea draws 1-1 with Germany...no miracle Jo So-hyun scores first and concedes a header Group H eliminated after 1-0 loss No miracle for South Korea, Germany. South Korea's women's soccer team was held to a 1-1 draw by Germany at the World Cup, ending their run to the round of 16 for the first time in eight years. Coach Colin Bell62\n\n## QnA\n\n\n<details>\n    <summary><b>0. What was the result of the match between South Korea and Germany at the Women's World Cup?</b></summary>\n    The match between South Korea and Germany ended in a 1-1 draw.\n</details>\n\n<details>\n    <summary><b>1. What does this result mean for South Korea's women's soccer team?</b></summary>\n    This result ended South Korea's run to the round of 16 at the Women's World Cup after eight years.\n</details>\n\n<details>\n    <summary><b>2. Who scored the first goal for South Korea in the match?</b></summary>\n    Jo So-hyun scored the first goal for South Korea.\n</details>\n\n<details>\n    <summary><b>3. How did South Korea concede the equalizing goal?</b></summary>\n    South Korea conceded a header for Germany's equalizing goal.\n</details>\n\n<details>\n    <summary><b>4. Who is the coach of South Korea's women's soccer team?</b></summary>\n    Colin Bell is the coach of South Korea's women's soccer team.\n</details>\n\n\n## [Women's World Cup] South Korea Draws 1-1 with Germany...No Miracles\n\n_2023-08-03 - wikitoday_\n\n\n\n<figure>\n    <img src=\"https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/ns/2023/08/03/NISI20230803_0000392999_web.jpg\" alt=\"네이트 뉴스\" />\n    <figcaption>\n        <h4> from 네이트 뉴스</h4>\n    </figcaption>\n</figure>\n\n\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: [女子世界杯]韩国 1-1 战平德国......没有奇迹\ndescription: 女足世界杯 韩国队 1-1 战平德国队......没有奇迹 赵素贤先入一球，头球破门 H 组 1-0 落败后被淘汰 韩国队没有奇迹，德国队也没有奇迹。韩国女足在世界杯上以 1-1 被德国队逼平，八年来首次止步十六强。教练科林-贝尔62\ncategory: Sports\nkeywords: 월드컵,여자월드컵,fifa 여자 월드컵,여자 월드컵\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://images.chosun.com/resizer/wx6X9TvnT8W5TzPGSyjoPQTS0WY=/1200x630/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/I22EQMSWFZMAPKLTDEFGVSVQMU.jpg\" alt=\"조선일보\" />\n    <figcaption>\n        <h4> from 조선일보</h4>\n    </figcaption>\n</figure>\n\n女足世界杯 韩国队 1-1 战平德国队......没有奇迹 赵素贤先入一球，头球破门 H 组 1-0 落败后被淘汰 韩国队没有奇迹，德国队也没有奇迹。韩国女足在世界杯上以 1-1 被德国队逼平，八年来首次止步十六强。教练科林-贝尔62\n\n## QnA\n\n\n<details>\n    <summary><b>0. 韩国队和德国队在女足世界杯上的比赛结果如何？</b></summary>\n    韩国队与德国队的比赛以 1-1 战平告终。\n</details>\n\n<details>\n    <summary><b>1. 这一结果对韩国女子足球队意味着什么？</b></summary>\n    这一结果结束了韩国队时隔八年再次闯入女足世界杯 16 强的历史。\n</details>\n\n<details>\n    <summary><b>2. 谁为韩国队攻入了本场比赛的第一个进球？</b></summary>\n    赵素贤为韩国队攻入第一球。\n</details>\n\n<details>\n    <summary><b>3. 韩国队是如何失球扳平比分的？</b></summary>\n    韩国队头球破门，为德国队扳平比分。\n</details>\n\n<details>\n    <summary><b>4. 谁是韩国女子足球队的教练？</b></summary>\n    科林-贝尔是韩国女子足球队的教练。\n</details>\n\n\n## [女子世界杯]韩国 1-1 战平德国......没有奇迹\n\n_2023-08-03 - wikitoday_\n\n\n\n<figure>\n    <img src=\"https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/ns/2023/08/03/NISI20230803_0000392999_web.jpg\" alt=\"네이트 뉴스\" />\n    <figcaption>\n        <h4> from 네이트 뉴스</h4>\n    </figcaption>\n</figure>\n\n\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: [여자 월드컵] 한국, 독일과 1-1 무승부...기적은 없었다\ndescription: 여자월드컵 한국, 독일과 1-1 무승부...기적은 없었다 조소현 선제골 넣었다가 헤딩 실점 1-0 패배로 H조 탈락 한국, 독일에 기적은 없었다. 한국 여자 축구 대표팀이 월드컵에서 독일과 1-1 무승부를 기록하며 8년 만에 16강 진출에 실패했습니다. 콜린 벨 감독62\ncategory: Sports\nkeywords: 월드컵,여자월드컵,fifa 여자 월드컵,여자 월드컵\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://images.chosun.com/resizer/wx6X9TvnT8W5TzPGSyjoPQTS0WY=/1200x630/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/I22EQMSWFZMAPKLTDEFGVSVQMU.jpg\" alt=\"조선일보\" />\n    <figcaption>\n        <h4> from 조선일보</h4>\n    </figcaption>\n</figure>\n\n여자월드컵 한국, 독일과 1-1 무승부...기적은 없었다 조소현 선제골 넣었다가 헤딩 실점 1-0 패배로 H조 탈락 한국, 독일에 기적은 없었다. 한국 여자 축구 대표팀이 월드컵에서 독일과 1-1 무승부를 기록하며 8년 만에 16강 진출에 실패했습니다. 콜린 벨 감독62\n\n## QnA\n\n\n<details>\n    <summary><b>0. 여자 월드컵에서 한국과 독일의 경기 결과는 어떻게 되었나요?</b></summary>\n    한국과 독일의 경기는 1-1 무승부로 끝났습니다.\n</details>\n\n<details>\n    <summary><b>1. 이번 결과는 한국 여자 축구 대표팀에게 어떤 의미가 있을까요?</b></summary>\n    이 결과로 한국은 8년 만에 여자 월드컵 16강 진출에 성공했습니다.\n</details>\n\n<details>\n    <summary><b>2. 이 경기에서 한국의 첫 골은 누가 넣었나요?</b></summary>\n    조소현이 한국의 첫 골을 넣었습니다.\n</details>\n\n<details>\n    <summary><b>3. 한국은 어떻게 동점골을 허용했을까요?</b></summary>\n    한국은 독일의 동점골을 헤딩으로 허용했습니다.\n</details>\n\n<details>\n    <summary><b>4. 한국 여자 축구 대표팀의 감독은 누구인가요?</b></summary>\n    콜린 벨은 한국 여자 축구 대표팀의 감독입니다.\n</details>\n\n\n## [여자 월드컵] 한국, 독일과 1-1 무승부...기적은 없었다\n\n_2023-08-03 - wikitoday_\n\n\n\n<figure>\n    <img src=\"https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/ns/2023/08/03/NISI20230803_0000392999_web.jpg\" alt=\"네이트 뉴스\" />\n    <figcaption>\n        <h4> from 네이트 뉴스</h4>\n    </figcaption>\n</figure>\n\n\n\n_end_\n"
      }
    ]
  },
  {
    "today": "2023-08-03",
    "folder_name": "-Seo-Hyun-rok-stabbi",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: 'Seo Hyun-rok stabbing' incident at Seohyeon Station: Eyewitness accounts and video footage\ndescription: Eyewitnesses of the 'Seo Hyun-rok stabbing' incident near Seohyeon Station on the Suinbundang Line in Seongnam-si, Gyeonggi-do, share their accounts of the horrifying attack. Additionally, video footage of the incident showing the assailant running and wielding a weapon has been circulating online.\ncategory: Crime\nkeywords: 서현역 칼부림,서현역,분당 칼부림,칼부림,서현역 흉기난동,서현역 칼부림 영상,서현역 흉기,분당 서현역,성남 칼부림,서현역칼부림,분당 서현역 칼부림\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://images.chosun.com/resizer/mIOGGxHGoKGFPL9sEqwLTcVHIno=/668x350/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/PSZIV47GC5GLPNFUN5RSNTK42E.jpg\" alt=\"조선일보\" />\n    <figcaption>\n        <h4> from 조선일보</h4>\n    </figcaption>\n</figure>\n\nEyewitnesses of the 'Seo Hyun-rok stabbing' incident near Seohyeon Station on the Suinbundang Line in Seongnam-si, Gyeonggi-do, share their accounts of the horrifying attack. Additionally, video footage of the incident showing the assailant running and wielding a weapon has been circulating online.\n\n## QnA\n\n\n<details>\n    <summary><b>0. What happened near Seohyeon Station?</b></summary>\n    A stabbing incident occurred near Seohyeon Station on the Suinbundang Line in Bundang-gu, Seongnam-si, Gyeonggi-do.\n</details>\n\n<details>\n    <summary><b>1. When did the incident take place?</b></summary>\n    The incident took place on the afternoon of the 3rd.\n</details>\n\n<details>\n    <summary><b>2. Were there any eyewitnesses?</b></summary>\n    Yes, there were eyewitnesses who witnessed the Seo Hyun-rok stabbing incident near Seohyeon Station.\n</details>\n\n<details>\n    <summary><b>3. What can be seen in the video footage of the incident?</b></summary>\n    The video footage shows the suspect running towards citizens and indiscriminately swinging a weapon. There are also moments of the suspect rescuing victims.\n</details>\n\n<details>\n    <summary><b>4. How many victims were injured in the incident?</b></summary>\n    A total of 14 victims were injured in the incident.\n</details>\n\n<details>\n    <summary><b>5. Has the primary suspect been arrested?</b></summary>\n    Yes, the primary suspect has been arrested.\n</details>\n\n<details>\n    <summary><b>6. Are the authorities investigating the incident?</b></summary>\n    Yes, the authorities are actively investigating the incident and looking into the involvement of any additional individuals.\n</details>\n\n\n## 'Seo Hyun-rok stabbing' incident at Seohyeon Station: Eyewitness accounts and video footage\n\n_2023-08-03 - wikitoday_\n\nOn the afternoon of the 3rd, a stabbing incident took place near Seohyeon Station on the Suinbundang Line in Bundang-gu, Seongnam-si, Gyeonggi-do. The police received a report of a weapon-wielding rampage at approximately 5:59 p.m. that day and were able to apprehend the suspect by 6:09 p.m. Eyewitnesses at the scene describe their harrowing experiences during the attack. Meanwhile, photos and videos of the incident, including CCTV footage of the suspect, have been widely shared on various online platforms. These videos show the assailant swiftly approaching innocent citizens and indiscriminately swinging the weapon.\n\n<figure>\n    <img src=\"https://thumb.mt.co.kr/21/2023/08/2023080319425980965_1.jpg\" alt=\"머니투데이\" />\n    <figcaption>\n        <h4> from 머니투데이</h4>\n    </figcaption>\n</figure>\n\nThe footage also captures moments of bravery as the suspect rescues victims. According to the authorities, the suspect drove a car onto the sidewalk, striking five people before entering a department store building in AK Plaza and continuing the attack. A total of 14 victims were injured and have been transported to nearby hospitals. While the police have already arrested the primary suspect, they are actively investigating to determine if there are any additional individuals involved in the incident.\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: 西岘站 '徐贤路刺伤 '事件：目击者陈述和视频录像\ndescription: 京畿道城南市水云塘线锡玄站附近发生的 '徐贤路刺杀事件 '的目击者讲述了这起骇人听闻的袭击事件。此外，网上还流传着袭击者边跑边挥舞武器的视频片段。\ncategory: Crime\nkeywords: 서현역 칼부림,서현역,분당 칼부림,칼부림,서현역 흉기난동,서현역 칼부림 영상,서현역 흉기,분당 서현역,성남 칼부림,서현역칼부림,분당 서현역 칼부림\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://images.chosun.com/resizer/mIOGGxHGoKGFPL9sEqwLTcVHIno=/668x350/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/PSZIV47GC5GLPNFUN5RSNTK42E.jpg\" alt=\"조선일보\" />\n    <figcaption>\n        <h4> from 조선일보</h4>\n    </figcaption>\n</figure>\n\n京畿道城南市水云塘线锡玄站附近发生的 '徐贤路刺杀事件 '的目击者讲述了这起骇人听闻的袭击事件。此外，网上还流传着袭击者边跑边挥舞武器的视频片段。\n\n## QnA\n\n\n<details>\n    <summary><b>0. 西贤站附近发生了什么事？</b></summary>\n    京畿道城南市盆唐区水云塘线锡玄站附近发生一起刺伤事件。\n</details>\n\n<details>\n    <summary><b>1. 事件发生在何时？</b></summary>\n    事件发生在 3 日下午。\n</details>\n\n<details>\n    <summary><b>2. 有目击证人吗？</b></summary>\n    是的，有目击者在西岘站附近目睹了徐贤路被刺事件。\n</details>\n\n<details>\n    <summary><b>3. 从事件的视频录像中可以看到什么？</b></summary>\n    录像显示，嫌疑人冲向市民，肆意挥舞武器。视频中还有嫌犯解救受害者的瞬间。\n</details>\n\n<details>\n    <summary><b>4. 事件中有多少人受伤？</b></summary>\n    共有 14 人在事件中受伤。\n</details>\n\n<details>\n    <summary><b>5. 主要嫌疑人是否已被逮捕？</b></summary>\n    是的，主要嫌疑人已经被捕。\n</details>\n\n<details>\n    <summary><b>6. 当局是否正在调查这一事件？</b></summary>\n    是的，当局正在积极调查这起事件，并调查是否有其他人参与其中。\n</details>\n\n\n## 西岘站 '徐贤路刺伤 '事件：目击者陈述和视频录像\n\n_2023-08-03 - wikitoday_\n\n3 日下午，京畿道城南市盆唐区水云塘线锡玄站附近发生一起持刀伤人事件。警方于当天下午 5 时 59 分左右接到持械行凶的报警，并于下午 6 时 09 分将嫌疑人抓获。与此同时，事件的照片和视频，包括嫌疑人的闭路电视录像，也在各种网络平台上被广泛分享。这些视频显示，袭击者迅速接近无辜市民，肆意挥舞武器。\n\n<figure>\n    <img src=\"https://thumb.mt.co.kr/21/2023/08/2023080319425980965_1.jpg\" alt=\"머니투데이\" />\n    <figcaption>\n        <h4> from 머니투데이</h4>\n    </figcaption>\n</figure>\n\n录像还记录了嫌犯营救受害者的英勇瞬间。据当局称，嫌犯驾驶一辆汽车冲上人行道，撞伤 5 人，然后进入 AK 广场的一栋百货大楼继续实施袭击。共有 14 名受害者受伤，已被送往附近的医院。虽然警方已经逮捕了主要嫌疑人，但他们仍在积极调查，以确定是否有其他人员参与了此次事件。\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: 서현역 '서현록 칼부림' 사건: 목격자 진술 및 영상\ndescription: 경기도 성남시 수인분당선 서현역 인근에서 발생한 '서현록 칼부림' 사건의 목격자들이 끔찍한 사건에 대해 증언하고 있습니다. 또한 가해자가 달려가 흉기를 휘두르는 장면이 담긴 사건 영상이 온라인에 유포되고 있습니다.\ncategory: Crime\nkeywords: 서현역 칼부림,서현역,분당 칼부림,칼부림,서현역 흉기난동,서현역 칼부림 영상,서현역 흉기,분당 서현역,성남 칼부림,서현역칼부림,분당 서현역 칼부림\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://images.chosun.com/resizer/mIOGGxHGoKGFPL9sEqwLTcVHIno=/668x350/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/PSZIV47GC5GLPNFUN5RSNTK42E.jpg\" alt=\"조선일보\" />\n    <figcaption>\n        <h4> from 조선일보</h4>\n    </figcaption>\n</figure>\n\n경기도 성남시 수인분당선 서현역 인근에서 발생한 '서현록 칼부림' 사건의 목격자들이 끔찍한 사건에 대해 증언하고 있습니다. 또한 가해자가 달려가 흉기를 휘두르는 장면이 담긴 사건 영상이 온라인에 유포되고 있습니다.\n\n## QnA\n\n\n<details>\n    <summary><b>0. 서현역 근처에서 무슨 일이 있었나요?</b></summary>\n    경기도 성남시 분당구 수인분당선 서현역 인근에서 칼부림 사건이 발생했습니다.\n</details>\n\n<details>\n    <summary><b>1. 언제 사건이 발생했나요?</b></summary>\n    이 사건은 3일 오후에 발생했습니다.\n</details>\n\n<details>\n    <summary><b>2. 목격자가 있었나요?</b></summary>\n    네, 서현역 인근에서 서현록 칼부림 사건을 목격한 목격자가 있었습니다.\n</details>\n\n<details>\n    <summary><b>3. 사건의 비디오 영상에서 무엇을 볼 수 있나요?</b></summary>\n    영상에는 용의자가 시민들을 향해 달려가 무차별적으로 흉기를 휘두르는 모습이 담겨 있습니다. 용의자가 피해자를 구하는 장면도 있습니다.\n</details>\n\n<details>\n    <summary><b>4. 이번 사건으로 몇 명의 피해자가 부상을 입었나요?</b></summary>\n    이 사건으로 총 14명의 피해자가 부상을 입었습니다.\n</details>\n\n<details>\n    <summary><b>5. 주요 용의자가 체포되었나요?</b></summary>\n    예, 주요 용의자가 체포되었습니다.\n</details>\n\n<details>\n    <summary><b>6. 당국에서 사건을 조사하고 있나요?</b></summary>\n    예, 당국은 이 사건을 적극적으로 조사하고 있으며 추가 연루자가 있는지 조사하고 있습니다.\n</details>\n\n\n## 서현역 '서현록 칼부림' 사건: 목격자 진술 및 영상\n\n_2023-08-03 - wikitoday_\n\n3일 오후 경기도 성남시 분당구 수인분당선 서현역 인근에서 칼부림 사건이 발생했습니다. 경찰은 이날 오후 5시 59분경 흉기를 휘두르는 난동 신고를 접수하고 오후 6시 9분경 용의자를 검거할 수 있었으며, 현장에 있던 목격자들은 사건 당시의 끔찍한 상황을 설명했습니다. 한편, 용의자가 찍힌 CCTV 영상을 포함한 사건 관련 사진과 동영상이 다양한 온라인 플랫폼에서 널리 공유되고 있습니다. 이 영상에는 가해자가 무고한 시민들에게 재빨리 다가가 무차별적으로 흉기를 휘두르는 모습이 담겨 있습니다.\n\n<figure>\n    <img src=\"https://thumb.mt.co.kr/21/2023/08/2023080319425980965_1.jpg\" alt=\"머니투데이\" />\n    <figcaption>\n        <h4> from 머니투데이</h4>\n    </figcaption>\n</figure>\n\n영상에는 용의자가 피해자를 구출하는 용감한 순간도 담겨 있습니다. 당국에 따르면 용의자는 인도로 차를 몰고 가 5명을 치고 AK플라자 백화점 건물로 진입해 공격을 계속했습니다. 총 14명의 피해자가 부상을 입고 인근 병원으로 이송되었습니다. 경찰은 이미 주 용의자를 체포했으며, 사건에 연루된 추가 인물이 있는지 확인하기 위해 적극적으로 수사를 진행하고 있습니다.\n\n_end_\n"
      }
    ]
  },
  {
    "today": "2023-08-03",
    "folder_name": "BLACKPINK-Jisoo-and-",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: BLACKPINK Jisoo and Bo Bo Hyun Confirmed to be Dating\ndescription: BLACKPINK's Jisoo (28) and actor Bo Bo Hyun (35) have officially confirmed that they are dating.\ncategory: Entertainment\nkeywords: 지수 안보현,지수,안보현 지수\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://dimg.donga.com/a/800/0/95/5/wps/NEWS/IMAGE/2023/08/03/120541903.5.jpg\" alt=\"동아일보\" />\n    <figcaption>\n        <h4> from 동아일보</h4>\n    </figcaption>\n</figure>\n\nBLACKPINK's Jisoo (28) and actor Bo Bo Hyun (35) have officially confirmed that they are dating.\n\n## QnA\n\n\n<details>\n    <summary><b>0. Who is BLACKPINK Jisoo dating?</b></summary>\n    BLACKPINK's Jisoo is dating actor Bo Bo Hyun.\n</details>\n\n<details>\n    <summary><b>1. What did YG Entertainment say about their relationship?</b></summary>\n    YG Entertainment stated that Jisoo and Bo Bo Hyun are getting to know each other little by little with good feelings.\n</details>\n\n<details>\n    <summary><b>2. Are Jisoo and Bo Bo Hyun's agencies supportive of their relationship?</b></summary>\n    Yes, both YG Entertainment and FN Entertainment expressed their hopes that fans would support Jisoo and Boo Hyun's relationship.\n</details>\n\n<details>\n    <summary><b>3. How old is Jisoo?</b></summary>\n    Jisoo was born in 1995, making her 28 years old.\n</details>\n\n<details>\n    <summary><b>4. What is Jisoo's recent acting debut?</b></summary>\n    Jisoo made her acting debut in the JTBC drama 'Snowdrop.'\n</details>\n\n\n## BLACKPINK Jisoo and Bo Bo Hyun Confirmed to be Dating\n\n_2023-08-03 - wikitoday_\n\nBlackpink's Jisoo (28) and actor Boo Hyun (35) are in a relationship. On the 3rd, Jisoo's agency, YG Entertainment, stated that Jisoo and Boo Hyun are getting to know each other little by little with good feelings. Both agencies expressed their hopes that fans would support their relationship.\n\n<figure>\n    <img src=\"https://newsimg.sedaily.com/2023/08/03/29T9IVKXFN_3.jpg\" alt=\"서울경제신문\" />\n    <figcaption>\n        <h4> from 서울경제신문</h4>\n    </figcaption>\n</figure>\n\nDespite the seven-year age gap between them, Jisoo and Boo Hyun are said to be nurturing their love with consideration for each other. Jisoo, who was born in 1995, recently made her acting debut in the JTBC drama 'Snowdrop' and is actively pursuing her career. Boo Hyun, on the other hand, has built up his filmography with roles in various dramas and gained popularity through his recent role in tvN's 'This Cadet Please.'\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: BLACKPINK Jisoo 和 Bo Bo Hyun 被证实正在交往\ndescription: BLACKPINK 的 Jisoo（28 岁）和演员 Bo Bo Hyun（35 岁）正式确认正在交往。\ncategory: Entertainment\nkeywords: 지수 안보현,지수,안보현 지수\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://dimg.donga.com/a/800/0/95/5/wps/NEWS/IMAGE/2023/08/03/120541903.5.jpg\" alt=\"동아일보\" />\n    <figcaption>\n        <h4> from 동아일보</h4>\n    </figcaption>\n</figure>\n\nBLACKPINK 的 Jisoo（28 岁）和演员 Bo Bo Hyun（35 岁）正式确认正在交往。\n\n## QnA\n\n\n<details>\n    <summary><b>0. BLACKPINK Jisoo 在和谁约会？</b></summary>\n    BLACKPINK 的 Jisoo 正在与演员 Bo Bo Hyun 约会。\n</details>\n\n<details>\n    <summary><b>1. YG Entertainment 对他们的关系有何评论？</b></summary>\n    YG Entertainment 表示，Jisoo 和 Bo Bo Hyun 正在逐渐了解对方，感情很好。\n</details>\n\n<details>\n    <summary><b>2. Jisoo 和 Bo Bo Hyun 的经纪公司支持他们的恋情吗？</b></summary>\n    是的，YG Entertainment 和 FN Entertainment 都表示希望粉丝们支持 Jisoo 和 Boo Hyun 的恋情。\n</details>\n\n<details>\n    <summary><b>3. Jisoo 多大了？</b></summary>\n    Jisoo 出生于 1995 年，今年 28 岁。\n</details>\n\n<details>\n    <summary><b>4. Jisoo 最近的演艺首秀是什么？</b></summary>\n    Jisoo 在 JTBC 电视剧《Snowdrop》中首次担任演员。\n</details>\n\n\n## BLACKPINK Jisoo 和 Bo Bo Hyun 被证实正在交往\n\n_2023-08-03 - wikitoday_\n\nBlackpink 的 Jisoo（28 岁）和演员 Boo Hyun（35 岁）正在热恋中。3 日，Jisoo 的经纪公司 YG Entertainment 表示，Jisoo 和 Boo Hyun 正在慢慢了解对方，感情很好。双方经纪公司都表示希望粉丝们能够支持他们的恋情。\n\n<figure>\n    <img src=\"https://newsimg.sedaily.com/2023/08/03/29T9IVKXFN_3.jpg\" alt=\"서울경제신문\" />\n    <figcaption>\n        <h4> from 서울경제신문</h4>\n    </figcaption>\n</figure>\n\n据说，尽管 Jisoo 和 Boo Hyun 的年龄相差 7 岁，但他们仍在相互体贴的基础上培养爱情。1995 年出生的 Jisoo 最近首次出演了 JTBC 电视剧《Snowdrop》，目前正在积极地发展自己的事业。另一方面，Boo Hyun 通过出演各种电视剧积累了自己的电影作品，并通过最近出演 tvN 的《拜托了，士官生》获得了人气。\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: 블랙핑크 지수-보보경심 려, 열애 사실 확인\ndescription: 블랙핑크 지수(28)와 배우 안보현(35)이 열애를 공식 확인했습니다.\ncategory: Entertainment\nkeywords: 지수 안보현,지수,안보현 지수\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://dimg.donga.com/a/800/0/95/5/wps/NEWS/IMAGE/2023/08/03/120541903.5.jpg\" alt=\"동아일보\" />\n    <figcaption>\n        <h4> from 동아일보</h4>\n    </figcaption>\n</figure>\n\n블랙핑크 지수(28)와 배우 안보현(35)이 열애를 공식 확인했습니다.\n\n## QnA\n\n\n<details>\n    <summary><b>0. 블랙핑크 지수는 누구와 사귀나요?</b></summary>\n    블랙핑크 지수가 배우 안보현과 열애 중입니다.\n</details>\n\n<details>\n    <summary><b>1. YG엔터테인먼트는 두 사람의 관계에 대해 뭐라고 말했나요?</b></summary>\n    YG엔터테인먼트는 지수와 안보현이 좋은 감정을 가지고 조금씩 서로를 알아가고 있다고 밝혔다.\n</details>\n\n<details>\n    <summary><b>2. 지수와 안보현의 소속사는 두 사람의 관계를 지지하나요?</b></summary>\n    네, YG엔터테인먼트와 FN엔터테인먼트 모두 팬들이 지수와 부현의 연애를 응원해 주길 바란다고 밝혔습니다.\n</details>\n\n<details>\n    <summary><b>3. 지수는 몇 살인가요?</b></summary>\n    지수는 1995년생으로 올해 나이 28세입니다.\n</details>\n\n<details>\n    <summary><b>4. 지수의 최근 연기 데뷔작은 무엇인가요?</b></summary>\n    지수는 JTBC 드라마 '스노우 드롭'으로 연기 데뷔를 했습니다.\n</details>\n\n\n## 블랙핑크 지수-보보경심 려, 열애 사실 확인\n\n_2023-08-03 - wikitoday_\n\n블랙핑크 지수(28)와 배우 부현(35)이 열애 중인 것으로 확인됐다. 3일 지수의 소속사 YG엔터테인먼트는 지수와 부현이 좋은 감정을 가지고 조금씩 서로를 알아가고 있다고 밝혔다. 두 소속사 모두 팬들이 두 사람의 만남을 응원해줬으면 좋겠다는 바람을 전했다.\n\n<figure>\n    <img src=\"https://newsimg.sedaily.com/2023/08/03/29T9IVKXFN_3.jpg\" alt=\"서울경제신문\" />\n    <figcaption>\n        <h4> from 서울경제신문</h4>\n    </figcaption>\n</figure>\n\n지수와 부현은 7살의 나이 차이에도 불구하고 서로에 대한 배려로 사랑을 키워가고 있는 것으로 전해졌습니다. 1995년생인 지수는 최근 JTBC 드라마 '눈이 부시게'로 연기에 데뷔해 활발한 활동을 펼치고 있다. 한편, 부현은 다양한 드라마에 출연하며 필모그래피를 쌓아왔으며, 최근 tvN '이번 생은 처음이라'에 출연하며 인기를 얻고 있습니다.\n\n_end_\n"
      }
    ]
  },
  {
    "today": "2023-08-03",
    "folder_name": "Neymar-s-Stellar-Per",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: Neymar's Stellar Performance in PSG Victory\ndescription: Paris Saint-Germain (PSG) defeats Jeonbuk Hyundai 3-0 in a friendly match, thanks to Neymar's impressive performance.\ncategory: Sports\nkeywords: PSG,파리생제르망,네이마르,파리생제르망 전북현대\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://flexible.img.hani.co.kr/flexible/normal/900/658/imgdb/original/2023/0803/20230803503133.jpg\" alt=\"한겨레\" />\n    <figcaption>\n        <h4> from 한겨레</h4>\n    </figcaption>\n</figure>\n\nParis Saint-Germain (PSG) defeats Jeonbuk Hyundai 3-0 in a friendly match, thanks to Neymar's impressive performance.\n\n## QnA\n\n\n<details>\n    <summary><b>0. Who was the standout player in the match?</b></summary>\n    Neymar delivered a standout performance, scoring two goals and providing one assist for PSG.\n</details>\n\n<details>\n    <summary><b>1. What was the final score of the match?</b></summary>\n    PSG secured a 3-0 victory against Jeonbuk Hyundai.\n</details>\n\n<details>\n    <summary><b>2. How did Neymar perform after returning from his injury?</b></summary>\n    Neymar showed no signs of injury as he displayed his exceptional skills and contributed significantly to PSG's victory.\n</details>\n\n<details>\n    <summary><b>3. How did the fans react to the match?</b></summary>\n    The fans showed their appreciation for the players with lavish cheers and support throughout the match.\n</details>\n\n<details>\n    <summary><b>4. What was the significance of this victory for PSG?</b></summary>\n    The victory in this friendly match served as a welcome boost for PSG after a somewhat disappointing preseason.\n</details>\n\n\n## Neymar's Stellar Performance in PSG Victory\n\n_2023-08-03 - wikitoday_\n\nParis Saint-Germain (PSG) emerged victorious in their friendly match against Jeonbuk Hyundai, securing a 3-0 win in the Coupang Play Series. Neymar, who returned to the starting lineup after recovering from an ankle injury, showcased his exceptional skills, scoring two goals and providing one assist.\n\n<figure>\n    <img src=\"http://news.kbs.co.kr/data/news/2023/08/03/20230803_rlKbuP.jpg\" alt=\"KBS뉴스\" />\n    <figcaption>\n        <h4> from KBS뉴스</h4>\n    </figcaption>\n</figure>\n\nThe victory comes as a welcome boost for PSG, following a less-than-ideal preseason performance in Japan. The match, held at the Asiad Stadium in Busan, attracted a crowd of over 43,000 fans who showed their appreciation for the players with enthusiastic cheers.\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: 内马尔在 PSG 胜利中的精彩表现\ndescription: 在一场友谊赛中，巴黎圣日耳曼（PSG）凭借内马尔的出色发挥，以 3-0 的比分击败全北现代。\ncategory: Sports\nkeywords: PSG,파리생제르망,네이마르,파리생제르망 전북현대\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://flexible.img.hani.co.kr/flexible/normal/900/658/imgdb/original/2023/0803/20230803503133.jpg\" alt=\"한겨레\" />\n    <figcaption>\n        <h4> from 한겨레</h4>\n    </figcaption>\n</figure>\n\n在一场友谊赛中，巴黎圣日耳曼（PSG）凭借内马尔的出色发挥，以 3-0 的比分击败全北现代。\n\n## QnA\n\n\n<details>\n    <summary><b>0. 谁是本场比赛的佼佼者？</b></summary>\n    内马尔表现出色，为 PSG 打进两球并送出一次助攻。\n</details>\n\n<details>\n    <summary><b>1. 比赛的最终比分是多少？</b></summary>\n    PSG 3-0 战胜全北现代。\n</details>\n\n<details>\n    <summary><b>2. 内马尔伤愈复出后表现如何？</b></summary>\n    内马尔没有受伤的迹象，他展示了自己出众的技能，为 PSG 的胜利做出了巨大贡献。\n</details>\n\n<details>\n    <summary><b>3. 球迷们对比赛的反应如何？</b></summary>\n    整场比赛，球迷们用热烈的欢呼和支持表达了对球员们的感谢。\n</details>\n\n<details>\n    <summary><b>4. 这场胜利对 PSG 意义何在？</b></summary>\n    在经历了令人失望的季前赛之后，这场友谊赛的胜利为 PSG 打了一支强心针。\n</details>\n\n\n## 内马尔在 PSG 胜利中的精彩表现\n\n_2023-08-03 - wikitoday_\n\n巴黎圣日耳曼队（PSG）在与全北现代队的友谊赛中以 3-0 的比分获胜。从脚踝伤势中恢复后重返首发阵容的内马尔展示了他非凡的球技，打进两球并送出一次助攻。\n\n<figure>\n    <img src=\"http://news.kbs.co.kr/data/news/2023/08/03/20230803_rlKbuP.jpg\" alt=\"KBS뉴스\" />\n    <figcaption>\n        <h4> from KBS뉴스</h4>\n    </figcaption>\n</figure>\n\nPSG 在日本的季前赛表现不尽如人意，本场比赛的胜利为 PSG 打了一支强心针。本场比赛在釜山亚细亚体育场举行，吸引了超过 43,000 名球迷到场观战，他们用热情的欢呼声表达了对球员的赞赏。\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: PSG 승리를 이끈 네이마르의 눈부신 활약\ndescription: 파리 생제르맹(PSG)이 네이마르의 인상적인 활약에 힘입어 친선경기에서 전북 현대를 3-0으로 물리쳤습니다.\ncategory: Sports\nkeywords: PSG,파리생제르망,네이마르,파리생제르망 전북현대\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://flexible.img.hani.co.kr/flexible/normal/900/658/imgdb/original/2023/0803/20230803503133.jpg\" alt=\"한겨레\" />\n    <figcaption>\n        <h4> from 한겨레</h4>\n    </figcaption>\n</figure>\n\n파리 생제르맹(PSG)이 네이마르의 인상적인 활약에 힘입어 친선경기에서 전북 현대를 3-0으로 물리쳤습니다.\n\n## QnA\n\n\n<details>\n    <summary><b>0. 이번 경기에서 눈에 띄는 선수는 누구였나요?</b></summary>\n    네이마르는 PSG에서 2골을 넣고 1도움을 기록하며 뛰어난 활약을 펼쳤습니다.\n</details>\n\n<details>\n    <summary><b>1. 경기의 최종 스코어는 어떻게 되나요?</b></summary>\n    PSG가 전북 현대를 상대로 3-0 승리를 거뒀습니다.\n</details>\n\n<details>\n    <summary><b>2. 부상에서 돌아온 네이마르는 어떤 활약을 펼쳤나요?</b></summary>\n    네이마르는 부상 흔적도 없이 뛰어난 기량을 선보이며 PSG의 승리에 크게 기여했습니다.\n</details>\n\n<details>\n    <summary><b>3. 팬들의 경기 반응은 어땠나요?</b></summary>\n    팬들은 경기 내내 아낌없는 환호와 응원으로 선수들에게 감사의 마음을 전했습니다.\n</details>\n\n<details>\n    <summary><b>4. 이번 승리가 PSG에게 어떤 의미가 있나요?</b></summary>\n    이 친선 경기의 승리는 다소 실망스러운 프리시즌을 보낸 PSG에게 반가운 활력소가 되었습니다.\n</details>\n\n\n## PSG 승리를 이끈 네이마르의 눈부신 활약\n\n_2023-08-03 - wikitoday_\n\n파리 생제르맹(PSG)이 전북 현대와의 친선경기에서 3-0 승리를 거두며 쿠팡 플레이 시리즈에서 승승장구했습니다. 발목 부상에서 회복해 선발 라인업에 복귀한 네이마르는 2골 1도움을 기록하며 뛰어난 기량을 뽐냈습니다.\n\n<figure>\n    <img src=\"http://news.kbs.co.kr/data/news/2023/08/03/20230803_rlKbuP.jpg\" alt=\"KBS뉴스\" />\n    <figcaption>\n        <h4> from KBS뉴스</h4>\n    </figcaption>\n</figure>\n\n프리시즌 일본에서 기대에 못 미치는 성적을 거둔 PSG에게 이번 승리는 반가운 소식이 아닐 수 없습니다. 부산 아시아드 스타디움에서 열린 이 경기에는 4만 3천여 명의 팬들이 운집해 열광적인 환호로 선수들에게 감사를 표했습니다.\n\n_end_\n"
      }
    ]
  },
  {
    "today": "2023-08-03",
    "folder_name": "Cass-Becomes-Officia",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: Cass Becomes Official Sponsor of LCK Summer 2023\ndescription: Cass (OB Beer) has announced its official sponsorship of the 'League of Legends Champions Korea (LCK) Summer' tournament. The LCK is the largest League of Legends competition in Korea, known for its high level of competitiveness and scale. Cass aims to target Gen Z consumers through this sponsorship and expand its presence in the esports community.\ncategory: Sports\nkeywords: LCK\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://cdn.newsquest.co.kr/news/thumbnail/202308/209346_101708_377_v150.jpg\" alt=\"뉴스퀘스트\" />\n    <figcaption>\n        <h4> from 뉴스퀘스트</h4>\n    </figcaption>\n</figure>\n\nCass (OB Beer) has announced its official sponsorship of the 'League of Legends Champions Korea (LCK) Summer' tournament. The LCK is the largest League of Legends competition in Korea, known for its high level of competitiveness and scale. Cass aims to target Gen Z consumers through this sponsorship and expand its presence in the esports community.\n\n## QnA\n\n\n<details>\n    <summary><b>0. What is LCK Summer 2023?</b></summary>\n    LCK Summer 2023 is the upcoming League of Legends Champions Korea tournament, which is the largest League of Legends competition in Korea. It will determine the top teams who will qualify for the League of Legends World Championship.\n</details>\n\n<details>\n    <summary><b>1. Why is Cass sponsoring LCK Summer 2023?</b></summary>\n    Cass is targeting Gen Z consumers, who are passionate about esports, by sponsoring the LCK Summer 2023 tournament. It is an opportunity for the brand to expand its presence in the esports community and connect with its main target audience.\n</details>\n\n<details>\n    <summary><b>2. What activities will Cass offer at the tournament?</b></summary>\n    Cass will set up a booth at the tournament venue, offering its limited-edition Cass Lemon Squeeze and custom beer pouches. Fans can also participate in the 'Cass Cheerful' zone, where they can write down their cheers on Cass Lemon Squeeze Cheer Pool sheets.\n</details>\n\n<details>\n    <summary><b>3. What benefits will supporters of 'CASS X LCK' receive?</b></summary>\n    Supporters of 'CASS X LCK' will receive exclusive benefits, including a front-row view of the LCK Summer Finals, a welcome kit with support items, and a shuttle bus service to and from the event.\n</details>\n\n<details>\n    <summary><b>4. Where will Cass have a booth besides the LCK Summer tournament?</b></summary>\n    Cass will also have a booth at the LCK Summer Finals and Fan Festa, which will be held at the DCC Daejeon Convention Center in Daejeon, South Korea.\n</details>\n\n\n## Cass Becomes Official Sponsor of LCK Summer 2023\n\n_2023-08-03 - wikitoday_\n\nCass (OB Beer) has officially partnered with the 'League of Legends Champions Korea (LCK) Summer' tournament, set to take place this month. LCK, which has been held since 2012, is the biggest League of Legends gaming competition in Korea. With its intense gameplay and massive following, League of Legends has become increasingly popular among esports fans. The upcoming LCK Summer tournament will mark the first time in five years that the finals will be held in South Korea. It will determine the top teams from each country's league who will qualify for the League of Legends World Championship.\n\n<figure>\n    <img src=\"http://www.consumernews.co.kr/news/thumbnail/202308/684779_261211_1843_v150.jpg\" alt=\"소비자가 만드는 신문\" />\n    <figcaption>\n        <h4> from 소비자가 만드는 신문</h4>\n    </figcaption>\n</figure>\n\nAs an official sponsor, Cass aims to connect with its main target audience, Gen Z consumers, who are avid esports enthusiasts. The brand plans to set up a booth at the tournament venue, offering its limited-edition Cass Lemon Squeeze and custom beer pouches. Fans will also have the opportunity to participate in the 'Cass Cheerful' zone, where they can write down their cheers on Cass Lemon Squeeze Cheer Pool sheets. Selected supporters will receive exclusive benefits, including a front-row view of the LCK Summer Finals, a welcome kit, and a shuttle bus service to and from the event. Additionally, Cass will have a booth at the LCK Summer Finals and Fan Festa, showcasing a high-angle photo booth and limited-edition merchandise featuring the logos of the finalist teams. With this sponsorship, Cass aims to bring the lively energy of Cass to the esports community and create an engaging experience for the younger generation.\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: 卡斯成为 LCK Summer 2023 的官方赞助商\ndescription: 卡斯（OB Beer）宣布正式赞助 '英雄联盟韩国冠军赛（LCK）夏季赛'。LCK 是韩国最大的英雄联盟比赛，以其高水平的竞争力和规模而闻名。卡斯旨在通过此次赞助锁定 Z 世代消费者，并扩大其在电竞界的影响力。\ncategory: Sports\nkeywords: LCK\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://cdn.newsquest.co.kr/news/thumbnail/202308/209346_101708_377_v150.jpg\" alt=\"뉴스퀘스트\" />\n    <figcaption>\n        <h4> from 뉴스퀘스트</h4>\n    </figcaption>\n</figure>\n\n卡斯（OB Beer）宣布正式赞助 '英雄联盟韩国冠军赛（LCK）夏季赛'。LCK 是韩国最大的英雄联盟比赛，以其高水平的竞争力和规模而闻名。卡斯旨在通过此次赞助锁定 Z 世代消费者，并扩大其在电竞界的影响力。\n\n## QnA\n\n\n<details>\n    <summary><b>0. LCK 2023 夏季赛是什么？</b></summary>\n    LCK 2023 夏季赛是即将在韩国举行的英雄联盟冠军赛，也是韩国最大的英雄联盟比赛。它将决出有资格参加英雄联盟世界锦标赛的顶级战队。\n</details>\n\n<details>\n    <summary><b>1. 卡斯为什么赞助 LCK Summer 2023？</b></summary>\n    卡斯通过赞助 LCK 2023 夏季赛，瞄准了热衷于电子竞技的 Z 世代消费者。这是该品牌扩大其在电竞社区的影响力并与其主要目标受众建立联系的一次机会。\n</details>\n\n<details>\n    <summary><b>2. 卡斯将在比赛中提供哪些活动？</b></summary>\n    卡斯将在比赛场地设立展台，提供限量版卡斯柠檬汽水和定制啤酒袋。球迷们还可以参加 '卡斯欢呼 '区，在卡斯柠檬水欢呼纸上写下自己的欢呼。\n</details>\n\n<details>\n    <summary><b>3. CASS X LCK '的支持者将获得哪些好处？</b></summary>\n    CASS X LCK '的支持者将获得独家优惠，包括在前排观看 LCK 夏季总决赛，获得包含支持物品的欢迎包，以及往返赛事的班车服务。\n</details>\n\n<details>\n    <summary><b>4. 除了 LCK 夏季锦标赛，卡斯还将在哪里设摊？</b></summary>\n    卡斯还将在韩国大田 DCC 大田会展中心举行的 LCK 夏季总决赛和粉丝节上设立展台。\n</details>\n\n\n## 卡斯成为 LCK Summer 2023 的官方赞助商\n\n_2023-08-03 - wikitoday_\n\n卡斯（OB Beer）已正式与将于本月举行的 '英雄联盟韩国冠军赛（LCK）夏季赛 '合作。LCK 自 2012 年开始举办，是韩国最大的英雄联盟游戏比赛。凭借其激烈的游戏性和大量的追随者，《英雄联盟》在电竞爱好者中越来越受欢迎。即将举行的 LCK 夏季赛将是五年来首次在韩国举行总决赛。它将决出每个国家联赛中的顶级队伍，这些队伍将获得参加英雄联盟世界锦标赛的资格。\n\n<figure>\n    <img src=\"http://www.consumernews.co.kr/news/thumbnail/202308/684779_261211_1843_v150.jpg\" alt=\"소비자가 만드는 신문\" />\n    <figcaption>\n        <h4> from 소비자가 만드는 신문</h4>\n    </figcaption>\n</figure>\n\n作为官方赞助商，卡斯旨在与其主要目标受众--狂热的电竞爱好者 Z 世代消费者建立联系。该品牌计划在比赛场地设立一个展位，提供限量版 Cass Lemon Squeeze 和定制啤酒袋。粉丝们还将有机会参与 'Cass Cheerful '专区，在 'Cass Lemon Squeeze Cheer Pool '纸上写下自己的欢呼。被选中的支持者将获得独家优惠，包括在前排观看 LCK 夏季总决赛、欢迎礼包和往返赛事的班车服务。此外，卡斯还将在 LCK 夏季总决赛和球迷嘉年华上设立展台，展示高角度照相亭和印有决赛队伍标志的限量版商品。通过此次赞助，卡斯旨在将卡斯的活力带入电竞社区，为年轻一代创造有吸引力的体验。\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: 카스, 2023 LCK 서머 공식 후원사로 선정되다\ndescription: 카스(OB맥주)가 '리그 오브 레전드 챔피언스 코리아(이하 LCK) 서머' 대회를 공식 후원한다고 밝혔습니다. LCK는 국내 최대 규모의 리그 오브 레전드 대회로, 높은 수준의 경쟁력과 규모를 자랑하는 것으로 유명합니다. 카스는 이번 후원을 통해 Z세대 소비자를 공략하고 e스포츠 커뮤니티에서 입지를 넓힌다는 목표입니다.\ncategory: Sports\nkeywords: LCK\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://cdn.newsquest.co.kr/news/thumbnail/202308/209346_101708_377_v150.jpg\" alt=\"뉴스퀘스트\" />\n    <figcaption>\n        <h4> from 뉴스퀘스트</h4>\n    </figcaption>\n</figure>\n\n카스(OB맥주)가 '리그 오브 레전드 챔피언스 코리아(이하 LCK) 서머' 대회를 공식 후원한다고 밝혔습니다. LCK는 국내 최대 규모의 리그 오브 레전드 대회로, 높은 수준의 경쟁력과 규모를 자랑하는 것으로 유명합니다. 카스는 이번 후원을 통해 Z세대 소비자를 공략하고 e스포츠 커뮤니티에서 입지를 넓힌다는 목표입니다.\n\n## QnA\n\n\n<details>\n    <summary><b>0. LCK 서머 2023이란 무엇인가요?</b></summary>\n    LCK 서머 2023은 다가오는 국내 최대 규모의 리그 오브 레전드 대회인 리그 오브 레전드 챔피언스 코리아 토너먼트입니다. 이 대회를 통해 리그 오브 레전드 월드 챔피언십에 출전할 상위 팀이 결정됩니다.\n</details>\n\n<details>\n    <summary><b>1. 카스가 LCK 서머 2023을 후원하는 이유는 무엇인가요?</b></summary>\n    카스는 LCK 서머 2023 토너먼트 후원을 통해 e스포츠에 열정을 가진 Z세대 소비자를 타깃으로 삼고 있습니다. 이 대회는 카스가 e스포츠 커뮤니티에서 입지를 넓히고 주요 타겟층과 소통할 수 있는 기회입니다.\n</details>\n\n<details>\n    <summary><b>2. 카스는 토너먼트에서 어떤 활동을 제공하나요?</b></summary>\n    카스는 대회장에 부스를 설치해 한정판 카스 레몬 스퀴즈와 커스텀 맥주 파우치를 제공할 예정입니다. 팬들은 '카스 치어풀' 존에서 카스 레몬 스퀴즈 응원지에 응원을 적을 수 있는 이벤트에도 참여할 수 있습니다.\n</details>\n\n<details>\n    <summary><b>3. 'CASS X LCK' 서포터즈에게는 어떤 혜택이 있나요?</b></summary>\n    '캐스 X LCK' 서포터즈에게는 LCK 서머 결승전 관람권, 응원 물품이 담긴 웰컴 키트, 행사장 왕복 셔틀버스 운행 등 특별한 혜택이 제공됩니다.\n</details>\n\n<details>\n    <summary><b>4. 카스는 LCK 서머 토너먼트 외에 어디에서 부스를 운영하나요?</b></summary>\n    카스는 대전 DCC 대전 컨벤션 센터에서 열리는 LCK 서머 결승전 및 팬 페스타에도 부스를 운영할 예정입니다.\n</details>\n\n\n## 카스, 2023 LCK 서머 공식 후원사로 선정되다\n\n_2023-08-03 - wikitoday_\n\n카스(OB맥주)가 이달 열리는 '리그 오브 레전드 챔피언스 코리아(이하 LCK) 서머' 대회에 공식 후원사로 참여합니다. 2012년부터 개최되고 있는 LCK는 국내 최대 규모의 리그 오브 레전드 게임 대회입니다. 리그 오브 레전드는 박진감 넘치는 게임 플레이와 수많은 팬으로 인해 e스포츠 팬들 사이에서 점점 더 인기를 얻고 있습니다. 다가오는 LCK 서머 토너먼트에서는 5년 만에 한국에서 결승전이 열릴 예정입니다. 이 대회를 통해 리그 오브 레전드 월드 챔피언십에 출전할 각국 리그의 상위 팀이 결정됩니다.\n\n<figure>\n    <img src=\"http://www.consumernews.co.kr/news/thumbnail/202308/684779_261211_1843_v150.jpg\" alt=\"소비자가 만드는 신문\" />\n    <figcaption>\n        <h4> from 소비자가 만드는 신문</h4>\n    </figcaption>\n</figure>\n\n공식 후원사인 카스는 e스포츠에 열광하는 주요 타겟층인 Z세대 소비자들과 소통하는 것을 목표로 하고 있습니다. 카스는 토너먼트 현장에 부스를 설치해 한정판 카스 레몬 스퀴즈와 맞춤형 맥주 파우치를 제공할 계획입니다. 팬들은 '카스 치어풀' 존에서 카스 레몬 스퀴즈 응원지에 응원 문구를 적을 수 있는 '카스 치어풀' 이벤트에도 참여할 수 있다. 선발된 서포터즈에게는 LCK 서머 결승전 맨 앞줄 관람, 웰컴 키트, 행사장 왕복 셔틀 버스 서비스 등 특별한 혜택이 제공됩니다. 또한, 카스는 LCK 서머 결승전과 팬 페스타에 부스를 마련해 하이앵글 포토 부스와 결승 진출 팀의 로고가 새겨진 한정판 굿즈를 선보일 예정입니다. 카스는 이번 후원을 통해 카스의 활기찬 에너지를 e스포츠 커뮤니티에 전달하고 젊은 세대에게 매력적인 경험을 선사하고자 합니다.\n\n_end_\n"
      }
    ]
  },
  {
    "today": "2023-08-03",
    "folder_name": "China-s-Economy-Faci",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: China's Economy Facing Crisis: Implications of 279.7% and 46.5% Indicators\ndescription: The Chinese economy is heading towards a crisis, with indicators such as government debt reaching alarming levels. Additionally, the high youth unemployment rate raises concerns about social unrest. These factors have implications not only for China but also for the global economy.\ncategory: Politics\nkeywords: 중국\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"http://www.lec.co.kr/news/thumbnail/202308/743858_78889_4346_v150.jpg\" alt=\"법률저널\" />\n    <figcaption>\n        <h4> from 법률저널</h4>\n    </figcaption>\n</figure>\n\nThe Chinese economy is heading towards a crisis, with indicators such as government debt reaching alarming levels. Additionally, the high youth unemployment rate raises concerns about social unrest. These factors have implications not only for China but also for the global economy.\n\n## QnA\n\n\n<details>\n    <summary><b>0. What are the indicators suggesting a crisis in China's economy?</b></summary>\n    The indicators suggesting a crisis in China's economy include the alarmingly high government debt, estimated to be around 279% to 297% of the national debt. The youth unemployment rate, which stands at 46.5%, is another worrisome indicator.\n</details>\n\n<details>\n    <summary><b>1. How are local governments in China affected by the real estate market?</b></summary>\n    Local governments in China have been heavily reliant on real estate development for revenue. However, with the recent decline in the real estate market, these governments have struggled to service their debt, leading to financial challenges.\n</details>\n\n<details>\n    <summary><b>2. Why is the youth unemployment rate concerning in China?</b></summary>\n    The youth unemployment rate in China is concerning because it stands at 46.5%, significantly higher than the government's official urban youth unemployment rate of 21.3%. This high rate of unemployment among the youth population could lead to social unrest and protests.\n</details>\n\n<details>\n    <summary><b>3. What external challenges does China's economy face?</b></summary>\n    China's economy is facing challenges in terms of declining exports and foreign investment. Countries like Vietnam are attracting foreign investment that would have previously gone to China. Additionally, the dominance of the United States in semiconductors and advanced technologies poses a challenge for China's ambitions in high-tech industries.\n</details>\n\n<details>\n    <summary><b>4. What is the potential for China's economy despite the challenges?</b></summary>\n    China, with its large population and strong manufacturing capabilities, has the potential to drive economic development through domestic demand if incomes rise and consumption is supported. However, realizing this potential requires effective political leadership that can address the current economic challenges.\n</details>\n\n\n## China's Economy Facing Crisis: Implications of 279.7% and 46.5% Indicators\n\n_2023-08-03 - wikitoday_\n\nThere is growing concern about China's economy, with predictions of a crisis and deflation. The severity of the situation is reflected in the indicators, particularly the Chinese government's debt. Various estimates suggest that the national debt stands at around 279% to 297%, significantly higher than the government's official data. This alarming level of debt has been driven by the government's desperate efforts to stimulate economic growth. Prior to the 2008 financial crisis, China's government debt was only around 60%. One major issue is that nearly 100% of China's government debt is held by local governments, which have been heavily reliant on real estate development for revenue. However, with the recent decline in the real estate market, local governments have struggled to service their debt. In 2022, real estate revenue accounted for 21% of local government revenue in China, with provinces like Tianjin and Jilin experiencing significant declines of 62% and 61% respectively. The impact of the real estate market extends beyond revenue. It constitutes a quarter of China's GDP and its stagnation has resulted in decreased consumption. While the rest of the world is grappling with inflation, China has managed to maintain a 0% inflation rate, as its citizens are not spending enough to drive inflation. Another alarming indicator is the youth unemployment rate, which stands at 46.5% according to Professor Zhang Dandan of Peking University. While the Chinese government reports an official urban youth unemployment rate of 21.3%, the actual figure is much higher. Furthermore, the job market for recent college graduates is extremely competitive, with only about 50% of them able to find employment.\n\n<figure>\n    <img src=\"http://news.kbs.co.kr/data/news/2023/08/03/20230803_mOOJ4M.jpg\" alt=\"KBS뉴스\" />\n    <figcaption>\n        <h4> from KBS뉴스</h4>\n    </figcaption>\n</figure>\n\nThese economic challenges have the potential to lead to a youth bulge, where a large number of young people face limited job prospects, fueling social discontent and possible protests. However, it is difficult to predict whether this will escalate into a second Tiananmen Square incident. Many Chinese youth, despite their discontent and bleak prospects, exhibit a social phenomenon characterized by fear of social interaction and a rejection of societal expectations. They prioritize personal satisfaction over financial success, often spending their time engrossed in their smartphones and leading a leisurely lifestyle. Externally, China is also facing obstacles. Its traditional strengths, such as exports and foreign investment, are declining. Countries like Vietnam are attracting foreign investment that would previously have gone to China. Additionally, the dominance of the United States in semiconductors and advanced technologies presents a challenge for China's ambitions in high-tech industries beyond manufacturing. Despite these challenges, China's potential cannot be disregarded, given its large population and strong manufacturing capabilities. If domestic incomes rise and consumption is supported, China has the potential to drive economic development through domestic demand. However, achieving this potential is contingent on appropriate political leadership. China's Communist Party, with its immense membershipbase, must acknowledge the current economic situation and devise strategies to address it. China needs leaders like Deng Xiaoping, who facilitated its economic transformation in the past. While the concerns for China's economy are valid, the potential impact on South Korea, given their economic interdependence, is also a cause for concern.\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: 中国经济面临危机：279.7%和46.5%指标的影响\ndescription: 中国经济正走向危机，政府债务等指标已达到惊人的水平。此外，居高不下的青年失业率也引发了对社会动荡的担忧。这些因素不仅对中国有影响，对全球经济也有影响。\ncategory: Politics\nkeywords: 중국\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"http://www.lec.co.kr/news/thumbnail/202308/743858_78889_4346_v150.jpg\" alt=\"법률저널\" />\n    <figcaption>\n        <h4> from 법률저널</h4>\n    </figcaption>\n</figure>\n\n中国经济正走向危机，政府债务等指标已达到惊人的水平。此外，居高不下的青年失业率也引发了对社会动荡的担忧。这些因素不仅对中国有影响，对全球经济也有影响。\n\n## QnA\n\n\n<details>\n    <summary><b>0. 哪些指标表明中国经济出现了危机？</b></summary>\n    表明中国经济出现危机的指标包括高得惊人的政府债务，估计约占国债的 279% 至 297%。青年失业率高达 46.5%，是另一个令人担忧的指标。\n</details>\n\n<details>\n    <summary><b>1. 房地产市场对中国地方政府有何影响？</b></summary>\n    中国地方政府的财政收入一直严重依赖房地产开发。然而，随着近期房地产市场的下滑，这些政府已难以偿还债务，从而面临财政挑战。\n</details>\n\n<details>\n    <summary><b>2. 为什么中国的青年失业率令人担忧？</b></summary>\n    中国的青年失业率令人担忧，因为它高达 46.5%，大大高于政府官方公布的 21.3% 的城镇青年失业率。青年人口的高失业率可能会引发社会动荡和抗议活动。\n</details>\n\n<details>\n    <summary><b>3. 中国经济面临哪些外部挑战？</b></summary>\n    中国经济正面临出口和外国投资下降的挑战。越南等国正在吸引以前会流向中国的外资。此外，美国在半导体和先进技术领域的主导地位也对中国在高科技产业的雄心壮志构成了挑战。\n</details>\n\n<details>\n    <summary><b>4. 尽管面临挑战，中国经济的潜力何在？</b></summary>\n    中国人口众多，制造业实力雄厚，如果收入增加，消费得到支持，中国有潜力通过内需推动经济发展。然而，实现这一潜力需要有效的政治领导，以应对当前的经济挑战。\n</details>\n\n\n## 中国经济面临危机：279.7%和46.5%指标的影响\n\n_2023-08-03 - wikitoday_\n\n人们对中国经济的担忧与日俱增，预测中国将面临危机和通货紧缩。形势的严重性反映在各项指标上，尤其是中国政府的债务。各种估计表明，中国的国债约为 279% 至 297%，大大高于政府的官方数据。这一惊人的债务水平是由政府拼命刺激经济增长所造成的。在 2008 年金融危机之前，中国的政府债务仅为 60% 左右。一个主要问题是，中国近 100% 的政府债务由地方政府持有，而这些地方政府的财政收入严重依赖于房地产开发。然而，随着近期房地产市场的下滑，地方政府已难以偿还债务。2022 年，房地产收入占中国地方政府收入的 21%，其中天津和吉林等省分别大幅下降 62% 和 61%。房地产市场的影响不仅限于财政收入。房地产占中国 GDP 的四分之一，房地产市场的停滞导致消费减少。当世界其他国家都在努力应对通胀时，中国却成功地保持了 0% 的通胀率，因为国民的消费不足以推动通胀。另一个令人担忧的指标是青年失业率，根据北京大学张丹丹教授的研究，青年失业率高达 46.5%。虽然中国政府官方公布的城镇青年失业率为 21.3%，但实际数字要高得多。此外，应届大学毕业生的就业市场竞争异常激烈，只有约 50%的人能够找到工作。\n\n<figure>\n    <img src=\"http://news.kbs.co.kr/data/news/2023/08/03/20230803_mOOJ4M.jpg\" alt=\"KBS뉴스\" />\n    <figcaption>\n        <h4> from KBS뉴스</h4>\n    </figcaption>\n</figure>\n\n这些经济挑战有可能导致青年人口暴增，大量年轻人面临有限的就业前景，从而引发社会不满和可能的抗议活动。然而，很难预测这是否会升级为第二次天安门事件。许多中国青年尽管心怀不满、前景暗淡，但却表现出一种社会现象，其特点是害怕社会交往、拒绝社会期望。他们将个人满足感置于经济成功之上，经常沉迷于智能手机，过着悠闲的生活。在外部，中国也面临着障碍。中国的传统优势，如出口和外国投资，正在下降。越南等国正在吸引以前会流向中国的外国投资。此外，美国在半导体和先进技术领域的主导地位也对中国在制造业以外的高科技产业的雄心壮志构成了挑战。尽管存在这些挑战，但鉴于中国人口众多、制造能力强大，其潜力不容忽视。如果国内收入增加，消费得到支持，中国就有潜力通过内需推动经济发展。然而，实现这一潜力取决于适当的政治领导。拥有庞大党员基础的中国共产党必须承认当前的经济形势，并制定应对策略。中国需要像邓小平这样的领导人，他在过去推动了中国的经济转型。虽然对中国经济的担忧是合理的，但由于两国经济相互依存，对韩国的潜在影响也令人担忧。\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: 위기에 직면한 중국 경제: 279.7% 및 46.5% 지표의 시사점\ndescription: 중국 경제는 정부 부채와 같은 지표가 우려할 만한 수준에 도달하는 등 위기를 향해 나아가고 있습니다. 또한 높은 청년 실업률로 인해 사회 불안에 대한 우려도 커지고 있습니다. 이러한 요인들은 중국뿐만 아니라 글로벌 경제에도 영향을 미칩니다.\ncategory: Politics\nkeywords: 중국\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"http://www.lec.co.kr/news/thumbnail/202308/743858_78889_4346_v150.jpg\" alt=\"법률저널\" />\n    <figcaption>\n        <h4> from 법률저널</h4>\n    </figcaption>\n</figure>\n\n중국 경제는 정부 부채와 같은 지표가 우려할 만한 수준에 도달하는 등 위기를 향해 나아가고 있습니다. 또한 높은 청년 실업률로 인해 사회 불안에 대한 우려도 커지고 있습니다. 이러한 요인들은 중국뿐만 아니라 글로벌 경제에도 영향을 미칩니다.\n\n## QnA\n\n\n<details>\n    <summary><b>0. 중국 경제의 위기를 시사하는 지표에는 어떤 것이 있나요?</b></summary>\n    중국 경제의 위기를 시사하는 지표로는 국가 부채의 약 279%에서 297%로 추정되는 놀라울 정도로 높은 정부 부채가 있습니다. 46.5%에 달하는 청년 실업률도 우려스러운 지표입니다.\n</details>\n\n<details>\n    <summary><b>1. 중국 지방 정부는 부동산 시장의 영향을 어떻게 받고 있나요?</b></summary>\n    중국의 지방 정부는 부동산 개발에 크게 의존해 수익을 창출해 왔습니다. 하지만 최근 부동산 시장이 침체되면서 이들 지방 정부는 부채 상환에 어려움을 겪고 있으며, 이는 재정적 어려움으로 이어지고 있습니다.\n</details>\n\n<details>\n    <summary><b>2. 중국의 청년 실업률이 우려되는 이유는 무엇인가요?</b></summary>\n    중국의 청년 실업률은 46.5%로 정부의 공식 도시 청년 실업률인 21.3%보다 훨씬 높기 때문에 우려스러운 수준입니다. 청년층의 높은 실업률은 사회 불안과 시위로 이어질 수 있습니다.\n</details>\n\n<details>\n    <summary><b>3. 중국 경제는 어떤 외부 도전에 직면해 있나요?</b></summary>\n    중국 경제는 수출과 외국인 투자 감소라는 도전에 직면해 있습니다. 베트남과 같은 국가들은 이전에는 중국으로 향했던 외국인 투자를 유치하고 있습니다. 또한 반도체 및 첨단 기술 분야에서 미국의 우위는 첨단 기술 산업에 대한 중국의 야망에 도전이 되고 있습니다.\n</details>\n\n<details>\n    <summary><b>4. 이러한 어려움에도 불구하고 중국 경제의 잠재력은 무엇일까요?</b></summary>\n    많은 인구와 강력한 제조업 역량을 갖춘 중국은 소득이 증가하고 소비가 뒷받침된다면 내수를 통해 경제 발전을 견인할 잠재력을 가지고 있습니다. 하지만 이러한 잠재력을 실현하기 위해서는 현재 당면한 경제 문제를 해결할 수 있는 효과적인 정치적 리더십이 필요합니다.\n</details>\n\n\n## 위기에 직면한 중국 경제: 279.7% 및 46.5% 지표의 시사점\n\n_2023-08-03 - wikitoday_\n\n중국 경제에 대한 위기와 디플레이션에 대한 예측이 나오면서 중국 경제에 대한 우려가 커지고 있습니다. 상황의 심각성은 지표, 특히 중국 정부의 부채에 반영되어 있습니다. 다양한 추정치에 따르면 국가 부채는 약 279%에서 297%로 정부의 공식 데이터보다 훨씬 높습니다. 이러한 놀라운 수준의 부채는 경제 성장을 촉진하려는 정부의 필사적인 노력으로 인해 발생했습니다. 2008년 금융 위기 이전에는 중국의 정부 부채가 60% 정도에 불과했습니다. 한 가지 주요 문제는 중국 정부 부채의 거의 100%를 부동산 개발에 크게 의존해 온 지방 정부가 보유하고 있다는 점입니다. 그러나 최근 부동산 시장이 하락하면서 지방 정부는 부채 상환에 어려움을 겪고 있습니다. 2022년 중국 지방정부 수입에서 부동산 수입이 차지하는 비중은 21%였으며, 톈진과 지린성은 각각 62%와 61%로 크게 감소했습니다. 부동산 시장의 영향은 세입을 넘어선 것입니다. 부동산 시장은 중국 GDP의 4분의 1을 차지하며, 부동산 시장의 침체는 소비 감소로 이어졌습니다. 전 세계가 인플레이션과 씨름하는 동안 중국은 0%의 인플레이션율을 유지하고 있는데, 이는 중국 국민들이 인플레이션을 유발할 만큼 충분히 소비하지 않기 때문입니다. 베이징대학교의 장단단 교수에 따르면 청년 실업률은 46.5%에 달해 또 다른 우려스러운 지표입니다. 중국 정부가 공식적으로 발표하는 도시 청년 실업률은 21.3%이지만, 실제 수치는 훨씬 더 높습니다. 또한 최근 대학 졸업생의 취업 시장은 경쟁이 매우 치열하여 약 50%만이 취업에 성공할 수 있습니다.\n\n<figure>\n    <img src=\"http://news.kbs.co.kr/data/news/2023/08/03/20230803_mOOJ4M.jpg\" alt=\"KBS뉴스\" />\n    <figcaption>\n        <h4> from KBS뉴스</h4>\n    </figcaption>\n</figure>\n\n이러한 경제적 어려움은 많은 젊은이들이 제한된 일자리 전망에 직면하여 사회적 불만과 시위 가능성을 불러일으키는 청년 폭증으로 이어질 수 있습니다. 그러나 이것이 제2의 천안문 사태로 확대될지 여부는 예측하기 어렵습니다. 많은 중국 청년들은 불만과 암울한 전망에도 불구하고 사회적 상호작용에 대한 두려움과 사회적 기대에 대한 거부를 특징으로 하는 사회 현상을 보이고 있습니다. 이들은 경제적 성공보다 개인적인 만족을 우선시하며, 스마트폰에 몰두하며 여유로운 라이프스타일을 즐기는 경우가 많습니다. 외부적으로도 중국은 장애물에 직면해 있습니다. 수출과 외국인 투자와 같은 전통적인 강점이 감소하고 있습니다. 베트남과 같은 국가들이 과거 중국으로 향하던 외국인 투자를 유치하고 있습니다. 또한 반도체 및 첨단 기술 분야에서 미국의 우위는 제조업을 넘어 첨단 기술 산업에 대한 중국의 야망에 도전이 되고 있습니다. 이러한 도전에도 불구하고 많은 인구와 강력한 제조업 역량을 고려할 때 중국의 잠재력을 무시할 수 없습니다. 국내 소득이 증가하고 소비가 뒷받침된다면 중국은 내수를 통해 경제 발전을 견인할 수 있는 잠재력을 가지고 있습니다. 그러나 이러한 잠재력을 실현하기 위해서는 적절한 정치적 리더십이 필요합니다. 막대한 당원 기반을 가진 중국 공산당은 현재의 경제 상황을 인정하고 이를 해결하기 위한 전략을 수립해야 합니다. 중국에는 과거 경제 변혁을 촉진한 덩샤오핑과 같은 지도자가 필요합니다. 중국 경제에 대한 우려는 타당하지만, 양국의 경제적 상호의존성을 고려할 때 한국에 미칠 잠재적 영향도 우려할 만한 사안입니다.\n\n_end_\n"
      }
    ]
  },
  {
    "today": "2023-08-03",
    "folder_name": "U-S-Credit-Rating-Do",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: U.S. Credit Rating Downgrade Sends Shockwaves Through Global Markets\ndescription: Financial markets around the world are reeling after the sovereign credit rating of the United States was downgraded, causing declines in stock markets and raising concerns about the future of the economy.\ncategory: World/International\nkeywords: 미국 신용등급 강등\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://image.imnews.imbc.com/replay/2023/nw930/article/__icsFiles/afieldfile/2023/08/03/0930_20230803_093536_1_4_Large.jpg\" alt=\"MBC뉴스\" />\n    <figcaption>\n        <h4> from MBC뉴스</h4>\n    </figcaption>\n</figure>\n\nFinancial markets around the world are reeling after the sovereign credit rating of the United States was downgraded, causing declines in stock markets and raising concerns about the future of the economy.\n\n## QnA\n\n\n<details>\n    <summary><b>0. What led to the downgrading of the U.S. credit rating?</b></summary>\n    Fitch cited the expected deterioration of the U.S. fiscal position over the next three years and the rising national debt burden as the reasons for the downgrade.\n</details>\n\n<details>\n    <summary><b>1. How are financial markets reacting to the downgrade?</b></summary>\n    Financial markets around the world are showing signs of unease, with Asian and European stocks falling. However, experts believe that the impact may not be as severe as in 2011 due to the robust growth of the U.S. economy.\n</details>\n\n<details>\n    <summary><b>2. What is the response from the White House and U.S. Treasury Secretary Janet Yellen?</b></summary>\n    Both the White House and U.S. Treasury Secretary Janet Yellen have expressed their disagreement with Fitch's decision, calling it arbitrary and based on outdated metrics.\n</details>\n\n\n## U.S. Credit Rating Downgrade Sends Shockwaves Through Global Markets\n\n_2023-08-03 - wikitoday_\n\nGlobal financial markets are in turmoil following the downgrading of the sovereign credit rating of the United States by Fitch Ratings. This comes after a day of losses in European and Asian markets, and stocks in New York have also taken a hit. The impact of the downgrade is significant, as it is the first time in 12 years that a major international rating agency has downgraded the U.S. sovereign rating.\n\n<figure>\n    <img src=\"https://cdn.mindlenews.com/news/thumbnail/202308/4446_11292_2019_v150.jpg\" alt=\"시민언론 민들레\" />\n    <figcaption>\n        <h4> from 시민언론 민들레</h4>\n    </figcaption>\n</figure>\n\nFitch cited the expected deterioration of the U.S. fiscal position and the rising national debt burden as reasons for the downgrade. Both the White House and U.S. Treasury Secretary Janet Yellen have expressed their disagreement with Fitch's decision, calling it arbitrary and based on outdated metrics. The downgrade has caused unease in financial markets worldwide, with Asian and European stocks falling. However, experts believe that the impact of the downgrade may not be as severe as in 2011, due to the robust growth of the U.S. economy.\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: 美国信用评级下调引发全球市场震动\ndescription: 美国的主权信用评级被下调后，全球金融市场一片混乱，导致股市下跌，并引发了对未来经济的担忧。\ncategory: World/International\nkeywords: 미국 신용등급 강등\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://image.imnews.imbc.com/replay/2023/nw930/article/__icsFiles/afieldfile/2023/08/03/0930_20230803_093536_1_4_Large.jpg\" alt=\"MBC뉴스\" />\n    <figcaption>\n        <h4> from MBC뉴스</h4>\n    </figcaption>\n</figure>\n\n美国的主权信用评级被下调后，全球金融市场一片混乱，导致股市下跌，并引发了对未来经济的担忧。\n\n## QnA\n\n\n<details>\n    <summary><b>0. 是什么导致了美国信用评级的下调？</b></summary>\n    惠誉认为，未来三年美国财政状况的预期恶化和国债负担的上升是下调评级的原因。\n</details>\n\n<details>\n    <summary><b>1. 金融市场对降级有何反应？</b></summary>\n    全球金融市场出现了不安的迹象，亚洲和欧洲股市纷纷下跌。不过，专家认为，由于美国经济增长强劲，其影响可能不会像 2011 年那样严重。\n</details>\n\n<details>\n    <summary><b>2. 白宫和美国财政部长珍妮特-耶伦对此有何回应？</b></summary>\n    白宫和美国财政部长珍妮特-耶伦（Janet Yellen）都表示不同意惠誉的决定，称其武断且基于过时的衡量标准。\n</details>\n\n\n## 美国信用评级下调引发全球市场震动\n\n_2023-08-03 - wikitoday_\n\n惠誉国际评级公司（Fitch Ratings）下调美国主权信用评级后，全球金融市场陷入动荡。在此之前，欧洲和亚洲市场连日亏损，纽约股市也受到冲击。此次评级下调影响重大，因为这是 12 年来首次有大型国际评级机构下调美国主权评级。\n\n<figure>\n    <img src=\"https://cdn.mindlenews.com/news/thumbnail/202308/4446_11292_2019_v150.jpg\" alt=\"시민언론 민들레\" />\n    <figcaption>\n        <h4> from 시민언론 민들레</h4>\n    </figcaption>\n</figure>\n\n惠誉将美国财政状况的预期恶化和国债负担的上升作为降级的原因。白宫和美国财政部长珍妮特-耶伦都表示不同意惠誉的决定，称其武断且基于过时的衡量标准。评级下调引起了全球金融市场的不安，亚洲和欧洲股市纷纷下跌。不过，专家认为，由于美国经济增长强劲，降级的影响可能不会像2011年那么严重。\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: 미국 신용등급 강등, 글로벌 시장에 충격파를 던지다\ndescription: 미국의 국가신용등급이 강등된 후 전 세계 금융시장이 요동치고 있으며, 이로 인해 주식시장이 하락하고 경제의 미래에 대한 우려가 커지고 있습니다.\ncategory: World/International\nkeywords: 미국 신용등급 강등\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://image.imnews.imbc.com/replay/2023/nw930/article/__icsFiles/afieldfile/2023/08/03/0930_20230803_093536_1_4_Large.jpg\" alt=\"MBC뉴스\" />\n    <figcaption>\n        <h4> from MBC뉴스</h4>\n    </figcaption>\n</figure>\n\n미국의 국가신용등급이 강등된 후 전 세계 금융시장이 요동치고 있으며, 이로 인해 주식시장이 하락하고 경제의 미래에 대한 우려가 커지고 있습니다.\n\n## QnA\n\n\n<details>\n    <summary><b>0. 미국 신용 등급이 강등된 이유는 무엇인가요?</b></summary>\n    피치는 향후 3년간 미국의 재정 상태가 악화될 것으로 예상되는 점과 국가 부채 부담 증가를 신용등급 강등의 원인으로 꼽았습니다.\n</details>\n\n<details>\n    <summary><b>1. 금융 시장은 신용등급 강등에 어떻게 반응하고 있나요?</b></summary>\n    아시아 및 유럽 증시가 하락하는 등 전 세계 금융 시장이 불안한 조짐을 보이고 있습니다. 하지만 전문가들은 미국 경제의 견조한 성장으로 인해 2011년만큼의 충격은 없을 것으로 보고 있습니다.\n</details>\n\n<details>\n    <summary><b>2. 백악관과 재닛 옐런 미국 재무장관의 반응은 어떤가요?</b></summary>\n    백악관과 재닛 옐런 미국 재무장관은 피치의 결정이 자의적이고 시대에 뒤떨어진 지표에 근거한 것이라며 이에 동의하지 않는다는 입장을 표명했습니다.\n</details>\n\n\n## 미국 신용등급 강등, 글로벌 시장에 충격파를 던지다\n\n_2023-08-03 - wikitoday_\n\n국제 신용평가사 피치 레이팅스가 미국의 국가 신용등급을 강등하면서 글로벌 금융 시장이 혼란에 빠졌습니다. 유럽과 아시아 증시가 하루 만에 하락한 데 이어 뉴욕 증시도 타격을 입었습니다. 주요 국제 신용평가 기관이 미국의 국가 신용등급을 강등한 것은 12년 만에 처음 있는 일이기 때문에 이번 신용등급 강등의 영향은 상당합니다.\n\n<figure>\n    <img src=\"https://cdn.mindlenews.com/news/thumbnail/202308/4446_11292_2019_v150.jpg\" alt=\"시민언론 민들레\" />\n    <figcaption>\n        <h4> from 시민언론 민들레</h4>\n    </figcaption>\n</figure>\n\n피치는 미국 재정 상태의 예상되는 악화와 국가 부채 부담 증가를 신용등급 강등의 이유로 꼽았습니다. 백악관과 재닛 옐런 미국 재무장관은 피치의 결정이 자의적이고 시대에 뒤떨어진 지표를 근거로 한 것이라며 동의하지 않는다는 입장을 표명했습니다. 이번 신용등급 강등으로 아시아 및 유럽 증시가 하락하는 등 전 세계 금융 시장에 불안감이 확산되고 있습니다. 그러나 전문가들은 미국 경제의 견조한 성장으로 인해 이번 신용등급 강등의 영향이 2011년만큼 심각하지는 않을 것으로 보고 있습니다.\n\n_end_\n"
      }
    ]
  },
  {
    "today": "2023-08-03",
    "folder_name": "-GoDaddy4-influencer",
    "mds": [
      {
        "language": "EN-US",
        "md": "---\ntitle: 'GoDaddy4' influencer's ex-husband denies assault allegations\ndescription: The ex-husband of a popular social media influencer featured on the show 'GoDaddy4' has denied allegations of assault and abuse made by his ex-wife. In a video posted on his YouTube channel, he refuted the claims and stated his side of the story. The couple's divorce and ongoing custody battle have been highly publicized, leading to a heated online debate.\ncategory: Entertainment\nkeywords: 고딩엄빠 인플루언서\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: EN-US\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://thumb.mt.co.kr/21/2023/08/2023080315281096391_1.jpg\" alt=\"머니투데이\" />\n    <figcaption>\n        <h4> from 머니투데이</h4>\n    </figcaption>\n</figure>\n\nThe ex-husband of a popular social media influencer featured on the show 'GoDaddy4' has denied allegations of assault and abuse made by his ex-wife. In a video posted on his YouTube channel, he refuted the claims and stated his side of the story. The couple's divorce and ongoing custody battle have been highly publicized, leading to a heated online debate.\n\n## QnA\n\n\n<details>\n    <summary><b>0. What were the allegations made by Ryu Hye-lin?</b></summary>\n    Ryu Hye-lin alleged that she was a victim of habitual drunkenness, assault, and verbal abuse by her ex-husband during their marriage.\n</details>\n\n<details>\n    <summary><b>1. What did Mr. A say in response to the allegations?</b></summary>\n    Mr. A denied the allegations and claimed that the broadcast was more interested in ratings than verifying the truth. He also stated that he was a victim of physical abuse himself.\n</details>\n\n<details>\n    <summary><b>2. What was the controversy surrounding their divorce?</b></summary>\n    The controversy involved issues of child support and accusations of infidelity. Ryu Hye-lin faced legal action from Mr. A after sharing details of their child support arrangement on social media.\n</details>\n\n<details>\n    <summary><b>3. What has been the reaction on social media?</b></summary>\n    The controversy has sparked intense debate, with supporters of both parties expressing their opinions online. Fans of Ryu Hye-lin have been targeting Mr. A with malicious comments.\n</details>\n\n\n## 'GoDaddy4' influencer's ex-husband denies assault allegations\n\n_2023-08-03 - wikitoday_\n\nThe ex-husband, referred to as Mr. A, responded to the accusations made by his ex-wife, Ryu Hye-lin, during her appearance on the show 'GoDaddy4'. Ryu Hye-lin alleged that she was a victim of habitual drunkenness, assault, and verbal abuse during their marriage, leading to their divorce. However, Mr. A claimed that the broadcast was more interested in ratings than verifying the truth. In his video, Mr. A stated that he was also a victim of physical abuse and provided details of the incidents. He described an instance where he threw a pillow at Ryu Hye-lin during an argument, resulting in a bruise on her knee. Mr. A also denied the allegations of habitual drinking and abusive behavior, stating that he hardly consumed alcohol after getting married.\n\n<figure>\n    <img src=\"https://biz.chosun.com/resizer/OzWm5zbHZgPosTTDyJbsKxtO7Vk=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/3DGCCITC2SDZVH2H2HEZUAHUWI.jpg\" alt=\"조선비즈\" />\n    <figcaption>\n        <h4> from 조선비즈</h4>\n    </figcaption>\n</figure>\n\nRegarding their divorce, Mr. A mentioned that it was a mutual decision and questioned why he was labeled as unfaithful. He also addressed the issue of child support, stating that he has been making regular monthly payments. The controversy surrounding the couple's divorce and custody battle has sparked intense discussion on social media. Fans of Ryu Hye-lin, who has a large following as a social media influencer, have been bombarding Mr. A with malicious comments. Ryu Hye-lin, on the other hand, faced legal action from Mr. A after she shared details of their child support arrangement on social media. The conflicting accounts of both parties have further fueled the debate, with supporters taking sides and expressing their opinions online. The allegations of assault and abuse have raised important discussions about domestic violence and the challenges faced by victims.\n\n_end_\n"
      },
      {
        "language": "ZH",
        "md": "---\ntitle: GoDaddy4 '影响者的前夫否认袭击指控\ndescription: 在节目《GoDaddy4》中大受欢迎的社交媒体影响者的前夫否认了前妻对他的攻击和虐待指控。他在自己的 YouTube 频道上发布了一段视频，驳斥了这些指控，并陈述了自己的观点。这对夫妇的离婚和正在进行的监护权争夺战一直备受关注，引发了激烈的网络讨论。\ncategory: Entertainment\nkeywords: 고딩엄빠 인플루언서\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: ZH\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://thumb.mt.co.kr/21/2023/08/2023080315281096391_1.jpg\" alt=\"머니투데이\" />\n    <figcaption>\n        <h4> from 머니투데이</h4>\n    </figcaption>\n</figure>\n\n在节目《GoDaddy4》中大受欢迎的社交媒体影响者的前夫否认了前妻对他的攻击和虐待指控。他在自己的 YouTube 频道上发布了一段视频，驳斥了这些指控，并陈述了自己的观点。这对夫妇的离婚和正在进行的监护权争夺战一直备受关注，引发了激烈的网络讨论。\n\n## QnA\n\n\n<details>\n    <summary><b>0. 柳惠琳的指控是什么？</b></summary>\n    Ryu Hye-lin 声称，她是其前夫在婚姻存续期间习惯性酗酒、殴打和辱骂的受害者。\n</details>\n\n<details>\n    <summary><b>1. A 先生是如何回应这些指控的？</b></summary>\n    A 先生否认了这些指控，并声称广播公司更关心的是收视率，而不是核实真相。他还表示，他本人也是身体虐待的受害者。\n</details>\n\n<details>\n    <summary><b>2. 围绕他们离婚的争议是什么？</b></summary>\n    争议涉及子女抚养费问题和出轨指控。Ryu Hye-lin 在社交媒体上分享了他们的子女抚养费安排细节后，面临 A 先生的法律诉讼。\n</details>\n\n<details>\n    <summary><b>3. 社交媒体上的反应如何？</b></summary>\n    这一争议引发了激烈的讨论，双方的支持者都在网上表达了自己的观点。Ryu Hye-lin 的粉丝针对 A 先生发表了恶意评论。\n</details>\n\n\n## GoDaddy4 '影响者的前夫否认袭击指控\n\n_2023-08-03 - wikitoday_\n\n被称为 A 先生的前夫对前妻 Ryu Hye-lin 在参加节目《GoDaddy4》时提出的指控做出了回应。Ryu Hye-lin 声称，她在婚姻存续期间是习惯性酗酒、殴打和辱骂的受害者，导致他们离婚。然而，A 先生声称，广播公司更关心的是收视率，而不是核实真相。在视频中，A 先生说他也是身体虐待的受害者，并提供了事件的细节。他描述了自己在一次争吵中向柳惠琳扔枕头，导致她膝盖瘀伤的事件。A 先生还否认了习惯性饮酒和虐待行为的指控，称他在结婚后几乎不饮酒。\n\n<figure>\n    <img src=\"https://biz.chosun.com/resizer/OzWm5zbHZgPosTTDyJbsKxtO7Vk=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/3DGCCITC2SDZVH2H2HEZUAHUWI.jpg\" alt=\"조선비즈\" />\n    <figcaption>\n        <h4> from 조선비즈</h4>\n    </figcaption>\n</figure>\n\n关于他们的离婚，A 先生提到这是双方共同的决定，并质疑为什么他被贴上了不忠的标签。他还谈到了孩子的抚养费问题，并表示自己一直按月定期支付抚养费。围绕这对夫妇离婚和抚养权争夺的争议在社交媒体上引发了激烈的讨论。在社交媒体上拥有众多粉丝的柳惠琳的粉丝们对 A 先生进行了恶意评论。另一方面，Ryu Hye-lin 在社交媒体上分享了他们的子女抚养安排细节后，面临着 A 先生的法律诉讼。双方相互矛盾的说法进一步加剧了争论，支持者们纷纷在网上站队并表达自己的观点。关于攻击和虐待的指控引发了关于家庭暴力和受害者所面临挑战的重要讨论。\n\n_end_\n"
      },
      {
        "language": "KO",
        "md": "---\ntitle: '고대디4' 인플루언서의 전남편이 폭행 혐의를 부인했습니다.\ndescription: 쇼 '고대디4'에 출연한 인기 소셜 미디어 인플루언서의 전남편이 전처의 폭행 및 학대 혐의를 부인했습니다. 그는 자신의 유튜브 채널에 올린 동영상에서 이러한 주장을 반박하고 자신의 입장을 밝혔습니다. 이 부부의 이혼과 현재 진행 중인 양육권 싸움이 크게 알려지면서 온라인에서 열띤 논쟁이 벌어지고 있습니다.\ncategory: Entertainment\nkeywords: 고딩엄빠 인플루언서\ndate: \"2023-08-03\"\nauthor: wikitoday.io\nlanguage: KO\n---\n\n# Summary\n\n<figure>\n    <img src=\"https://thumb.mt.co.kr/21/2023/08/2023080315281096391_1.jpg\" alt=\"머니투데이\" />\n    <figcaption>\n        <h4> from 머니투데이</h4>\n    </figcaption>\n</figure>\n\n쇼 '고대디4'에 출연한 인기 소셜 미디어 인플루언서의 전남편이 전처의 폭행 및 학대 혐의를 부인했습니다. 그는 자신의 유튜브 채널에 올린 동영상에서 이러한 주장을 반박하고 자신의 입장을 밝혔습니다. 이 부부의 이혼과 현재 진행 중인 양육권 싸움이 크게 알려지면서 온라인에서 열띤 논쟁이 벌어지고 있습니다.\n\n## QnA\n\n\n<details>\n    <summary><b>0. 류혜린 씨가 제기한 의혹은 무엇인가요?</b></summary>\n    류혜린은 결혼 생활 중 전남편으로부터 상습적인 음주와 폭행, 폭언의 피해를 입었다고 주장했습니다.\n</details>\n\n<details>\n    <summary><b>1. A씨는 이 혐의에 대해 어떤 입장을 밝혔나요?</b></summary>\n    A씨는 혐의를 부인하며 방송이 진실 확인보다 시청률에 더 관심이 있다고 주장했습니다. 또한 자신도 신체적 학대의 피해자였다고 진술했습니다.\n</details>\n\n<details>\n    <summary><b>2. 두 사람의 이혼을 둘러싼 논란은 무엇이었나요?</b></summary>\n    이 논란에는 양육비 문제와 외도 의혹이 얽혀 있었습니다. 류혜린은 양육비 합의 내용을 SNS에 공개한 후 A씨로부터 법적 조치를 당했습니다.\n</details>\n\n<details>\n    <summary><b>3. 소셜 미디어의 반응은 어땠나요?</b></summary>\n    이 논란은 양측 지지자들이 온라인에서 각자의 의견을 표출하며 격렬한 논쟁을 불러일으켰습니다. 류혜린의 팬들은 악성 댓글로 A씨를 공격하고 있습니다.\n</details>\n\n\n## '고대디4' 인플루언서의 전남편이 폭행 혐의를 부인했습니다.\n\n_2023-08-03 - wikitoday_\n\nA씨로 지목된 전남편은 전처 류혜린이 '고대디4' 출연 당시 제기한 의혹에 대해 반박했습니다. 류혜린은 결혼 생활 중 상습적인 음주와 폭행, 폭언의 피해자였고, 이로 인해 이혼에 이르렀다고 주장했습니다. 하지만 A씨는 방송이 진실 확인보다 시청률에 더 관심이 있다고 주장했습니다. A씨는 영상에서 자신도 신체적 폭력의 피해자라고 밝히며 사건의 구체적인 정황을 제시했습니다. 그는 말다툼 중 류혜린에게 베개를 던져 무릎에 멍이 들게 한 사례를 설명했습니다. 또한 A씨는 결혼 후 술을 거의 마시지 않는다며 상습 음주 및 폭력 혐의를 부인했다.\n\n<figure>\n    <img src=\"https://biz.chosun.com/resizer/OzWm5zbHZgPosTTDyJbsKxtO7Vk=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/3DGCCITC2SDZVH2H2HEZUAHUWI.jpg\" alt=\"조선비즈\" />\n    <figcaption>\n        <h4> from 조선비즈</h4>\n    </figcaption>\n</figure>\n\n이혼에 대해 A씨는 서로의 결정이었다고 말하며 왜 자신이 불성실한 사람으로 분류되는지 의문을 제기했습니다. 또한 양육비 문제도 언급하며 매달 정기적으로 지급하고 있다고 말했습니다. 두 사람의 이혼과 양육권 분쟁을 둘러싼 논란은 소셜 미디어에서 격렬한 논쟁을 불러일으켰습니다. 소셜 미디어 인플루언서로 많은 팔로워를 보유한 류혜린의 팬들은 A씨에게 악성 댓글을 쏟아내고 있다. 반면 류혜린은 양육비 합의 내용을 SNS에 공유한 후 A씨로부터 법적 조치를 당했습니다. 양측의 상반된 주장에 지지자들은 온라인을 통해 어느 한쪽 편을 들며 의견을 표출하는 등 논쟁은 더욱 가열되고 있습니다. 폭행 및 학대 혐의는 가정 폭력과 피해자가 직면한 어려움에 대한 중요한 논의를 불러일으켰습니다.\n\n_end_\n"
      }
    ]
  }
]