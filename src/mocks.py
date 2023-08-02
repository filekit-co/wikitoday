from domain.entities import (Article, ArticleContent, ArticleImage,
                             CrawledTrend, GoogleTrend, QnA,
                             TranslatedCrawledTrend, TrendArticleMeta)

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
step_3 = [TranslatedCrawledTrend(keywords=['류현진'],
                        articles=["# Title: Ryu's 146 mph fastball wasn't "
                                  "enough to stop AL's winningest team\n"
                                  '\n'
                                  '# Lead: 2 starts against Baltimore...5 '
                                  'innings, 9 hits, 4 runs.\n'
                                  '\n'
                                  '# Body: Game 2 start against Baltimore...5 '
                                  'innings, 9 hits, 4 runs.\n'
                                  "Toronto Blue Jays' Hyun-jin Ryu delivers a "
                                  'pitch in the first inning of a baseball '
                                  'game against the Baltimore Orioles at '
                                  'Rogers Centre in Toronto, Ontario, Canada, '
                                  'Tuesday, Feb. 2, 2018. Toronto/AP\n'
                                  'His first big league start in 426 days. It '
                                  'was a shaky start. But he gradually '
                                  'regained the stability of the "Korean '
                                  'Monster. Ryu Hyun-jin, 36, who lost 13 '
                                  'kilograms during his rehabilitation, is '
                                  'back and healthy.\n'
                                  'Ryu started the 2023 Major League Baseball '
                                  '(MLB) World Series against the Baltimore '
                                  'Orioles at Rogers Centre in Toronto, '
                                  'Ontario, Canada, on Feb. 2 (KST) and gave '
                                  'up four runs on nine hits (one home run) in '
                                  'five innings with one walk and three '
                                  'strikeouts. Threw 80 pitches (54 for '
                                  "strikes). It wasn't a bad performance for "
                                  'his first start in 14 months after '
                                  'undergoing ligament splicing surgery on his '
                                  'left elbow. It had been 426 days since '
                                  "Ryu's last big league start, on June 2 last "
                                  'year against the Chicago White Sox at '
                                  'Rogers Centre. On that day, 46,691 fans '
                                  'were in attendance at Rogers Centre to '
                                  "witness Ryu's return.\n"
                                  'Against Baltimore, the team with the best '
                                  'record in the American League, he got off '
                                  'to a very bad start. In the top of the '
                                  'first inning, Ryu threw an 88.2 mph (142 '
                                  "km/h) fastball to Baltimore's first batter, "
                                  'catcher Adley Rutzman, for a double. Ryan '
                                  'Mountcastle, the No. 2 hitter, was hit by '
                                  'an 84.7 mph (136 km/h) cutter on the third '
                                  'pitch of the at-bat for a double. He then '
                                  'allowed Anthony Santander to hit a fastball '
                                  'to left for his third straight hit. The big '
                                  'league mound, his first in 14 months, '
                                  'seemed overwhelming for Ryu. But he settled '
                                  'down and got Austin Hayes to fly out to '
                                  'center with runners on first and third. '
                                  "Gunner Henderson's infield single allowed a "
                                  'second run to score, but that was it for '
                                  'the first inning.\n'
                                  'Ryu gave up a run in the top of the second '
                                  'on a bases-loaded double, but his curveball '
                                  'was working well in the third through fifth '
                                  'innings. But in the top of the sixth, with '
                                  'the score 3-3, a 77.4-mile-per-hour (124.6 '
                                  'km/h) changeup to leadoff hitter Henderson '
                                  'sailed into center field for a solo shot. '
                                  'Ryu promptly turned the mound over to '
                                  'Trevor Richards.\n'
                                  "Ryu's four-seam fastball touched 91 miles "
                                  'per hour (146.5 km/h) on the day. His '
                                  'average velocity was 89 miles per hour '
                                  '(143.3 km/h). His changeup was so jagged '
                                  "that even he couldn't believe it, but he "
                                  'still managed to get out of trouble in the '
                                  'third and fifth innings by inducing a pair '
                                  'of bases-loaded singles. "It\'s very '
                                  'encouraging to see him back in the big '
                                  "leagues, and it'll be interesting to see "
                                  'what he does next," MLB.com Toronto '
                                  'reporter Keegan Matheson wrote on Twitter '
                                  'after the game, "especially with his '
                                  'stuff."\n'
                                  'Toronto was outscored 3-13 as its bullpen '
                                  'was unable to withstand the Baltimore '
                                  'firepower. Santander went 3-for-4 with a '
                                  'grand slam and four RBIs, while Henderson '
                                  'went 3-for-5 with a home run and four RBIs '
                                  'off Ryu Hyun-jin. Ryu was the losing '
                                  'pitcher in his comeback as Toronto failed '
                                  'to complete the comeback. Toronto has lost '
                                  'three straight. With the team running a '
                                  "six-man starting rotation, Ryu's next start "
                                  'will be on Aug. 8 against the Cleveland '
                                  'Cavaliers.\n'
                                  'Reporter Yanghee Kim whizzer4@hani.co.kr',
                                  '# Title: Ryu takes 4-run loss in 5 innings '
                                  'in comeback start; top velocity 146 mph\n'
                                  '\n'
                                  "# Lead: Major League Baseball's Ryu "
                                  'Hyun-jin of Toronto gave up four runs in '
                                  'five innings in his first start since '
                                  'undergoing elbow ligament reconstruction '
                                  'surgery last June. Ryu started a home game '
                                  'against the Baltimore...\n'
                                  '\n'
                                  '# Body: Full Play\n'
                                  "Major League Baseball's Hyun-jin Ryu gave "
                                  'up four runs in five innings in his first '
                                  'start since undergoing elbow ligament '
                                  'reconstruction surgery in June of last '
                                  'year.Ryu started the game against Baltimore '
                                  'and gave up two runs on three hits in the '
                                  'first inning and another in the second, but '
                                  'induced two groundouts and settled down to '
                                  'work through the fifth inning without '
                                  'allowing another run.6Ryu, who was also on '
                                  'the mound in the inning, gave up a solo '
                                  'home run to Henderson, the first batter he '
                                  'faced, and was removed with the score 3 to '
                                  '4.After five innings and nine hits and four '
                                  'runs, Ryu struck out three while walking '
                                  'one and reached 80 mph on his fastball.With '
                                  "Toronto's 13-3 blowout loss, Ryu was handed "
                                  'his first loss of the season and raised his '
                                  'ERA to 7.20.'],
                        images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg',
                                             source='한겨레'),
                                ArticleImage(url='https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg',
                                             source='MBC뉴스')])]


########################## STEP 4 ##########################
step_4 = [
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
step_5 = [
    Article(
    category='Sports',
      keywords='류현진',
         contents=[ArticleContent(title="Ryu's Return to the Mound Ends in a "
                                        'Loss Against the Baltimore Orioles',
                                  lead="Toronto Blue Jays' pitcher, Hyun-jin "
                                       'Ryu, made his first start in over a '
                                       "year but couldn't prevent the AL's "
                                       'leading team from winning.',
                                  body1='In his comeback game, Hyun-jin Ryu '
                                        'pitched for the Toronto Blue Jays '
                                        'against the Baltimore Orioles in the '
                                        'Major League Baseball (MLB) World '
                                        "Series. Despite Ryu's efforts, the "
                                        'Orioles emerged victorious, scoring '
                                        'four runs on nine hits in five '
                                        'innings. Ryu showcased his talents by '
                                        'throwing a fastball at an impressive '
                                        'speed of 146 mph.',
                                  body2='However, his performance was unable '
                                        'to secure a win for his team. This '
                                        "loss marked Ryu's first in the 2023 "
                                        'season after undergoing ligament '
                                        'splicing surgery in his left elbow. '
                                        'Despite the setback, fans and experts '
                                        "are optimistic about Ryu's future "
                                        'performance.',
                                  qna_list=[QnA(question='Who did Hyun-jin Ryu '
                                                         'pitch against in his '
                                                         'comeback game?',
                                                answer='Hyun-jin Ryu pitched '
                                                       'against the Baltimore '
                                                       'Orioles.'),
                                            QnA(question='How many runs did '
                                                         'the Baltimore '
                                                         'Orioles score '
                                                         'against Ryu?',
                                                answer='The Baltimore Orioles '
                                                       'scored four runs '
                                                       'against Ryu.'),
                                            QnA(question="What was Ryu's "
                                                         'fastball speed '
                                                         'during the game?',
                                                answer="Ryu's fastball reached "
                                                       'an impressive speed of '
                                                       '146 mph.'),
                                            QnA(question="What was Ryu's "
                                                         'previous performance '
                                                         'before his comeback '
                                                         'game?',
                                                answer='Ryu had been out of '
                                                       'action for over a year '
                                                       'due to ligament '
                                                       'splicing surgery on '
                                                       'his left elbow.'),
                                            QnA(question='What is the outlook '
                                                         "for Ryu's future "
                                                         'performances?',
                                                answer='Despite the loss, fans '
                                                       'and experts are '
                                                       "optimistic about Ryu's "
                                                       'future performance.')],
                                  language='EN-US'),
                   ArticleContent(title='柳箫然重返投手丘，最终不敌巴尔的摩金莺队',
                                  lead='多伦多蓝鸟队的投手柳贤振一年多来首次先发，但未能阻止美联领先的球队获胜。',
                                  body1='在美国职业棒球大联盟（MLB）世界系列赛中，柳贤振代表多伦多蓝鸟队对阵巴尔的摩金莺队，这是他的复出之战。尽管柳贤振做出了努力，但金莺队还是取得了胜利，在五局比赛中被击出九支安打，得到四分。隆以令人印象深刻的 '
                                        '146 英里/小时的速度投出快速球，展示了自己的天赋。',
                                  body2='然而，他的表现未能为球队赢得一场胜利。这场失利是柳箫然接受左肘韧带接合手术后在 '
                                        '2023 '
                                        '赛季的首场失利。尽管遭遇挫折，但球迷和专家对柳箫然未来的表现持乐观态度。',
                                  qna_list=[QnA(question='柳贤振在复出赛中的对手是谁？',
                                                answer='柳贤振在与巴尔的摩金莺队的比赛中投球。'),
                                            QnA(question='巴尔的摩金莺队对柳箫然的得分是多少？',
                                                answer='巴尔的摩金莺队对柳箫然打出四次安打。'),
                                            QnA(question='比赛中隆的快速球速是多少？',
                                                answer='柳箫然的快速球达到了令人印象深刻的 146 '
                                                       '英里/小时。'),
                                            QnA(question='柳忠秧在复出前的表现如何？',
                                                answer='由于左肘接受了韧带接合手术，柳忠秧已经休战了一年多。'),
                                            QnA(question='柳忠秧未来的表现前景如何？',
                                                answer='尽管输掉了比赛，但球迷和专家们对柳箫然未来的表现还是持乐观态度。')],
                                  language='ZH'),
                   ArticleContent(title='류현진의 마운드 복귀, 볼티모어 오리올스전 패배로 끝나다',
                                  lead='토론토 블루제이스의 류현진 투수가 1년여 만에 선발 등판했지만, AL '
                                       '선두 팀의 승리를 막지는 못했습니다.',
                                  body1='류현진은 메이저리그 야구(MLB) 월드시리즈에서 토론토 블루제이스와 '
                                        '볼티모어 오리올스를 상대로 복귀전에서 선발 투수로 등판했습니다. '
                                        '류현진의 호투에도 불구하고 오리올스는 5이닝 동안 9안타에 '
                                        '4실점하며 승리를 거뒀습니다. 류현진은 시속 146마일이라는 놀라운 '
                                        '속도의 직구를 던지며 자신의 재능을 뽐냈습니다.',
                                  body2='그러나 그의 활약은 팀의 승리를 보장하지 못했습니다. 이번 패배는 '
                                        '왼쪽 팔꿈치 인대 접합 수술을 받은 류현진의 2023시즌 첫 '
                                        '패배였습니다. 아쉬움에도 불구하고 팬들과 전문가들은 류현진의 향후 '
                                        '활약에 대해 낙관적인 전망을 내놓고 있습니다.',
                                  qna_list=[QnA(question='류현진 선수의 복귀전에서 상대 투수는 '
                                                         '누구였나요?',
                                                answer='류현진이 볼티모어 오리올스를 상대로 '
                                                       '투구했습니다.'),
                                            QnA(question='볼티모어 오리올스가 류현진을 상대로 '
                                                         '얼마나 많은 득점을 올렸나요?',
                                                answer='볼티모어 오리올스는 류현진을 상대로 '
                                                       '4득점을 올렸습니다.'),
                                            QnA(question='경기 중 류현진의 직구 속도는 어느 '
                                                         '정도였나요?',
                                                answer='류현진의 직구는 최고 시속 '
                                                       '146마일이라는 놀라운 속도를 '
                                                       '기록했습니다.'),
                                            QnA(question='복귀전 경기 전 류제국의 이전 성적은 '
                                                         '어땠나요?',
                                                answer='류 선수는 왼쪽 팔꿈치 인대 접합 수술로 '
                                                       '1년 넘게 경기에 나서지 못했습니다.'),
                                            QnA(question='류 선수의 향후 활약에 대한 전망은 '
                                                         '어떻게 되나요?',
                                                answer='패배에도 불구하고 팬들과 전문가들은 '
                                                       '류제국의 향후 활약에 대해 낙관적인 '
                                                       '전망을 내놓고 있습니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg',
                              source='한겨레'),
                 ArticleImage(url='https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg',
                              source='MBC뉴스')]),
 Article(category='Sports',
         keywords='류현진2',
         contents=[ArticleContent(title="Ryu's Return to the Mound Ends in a "
                                        'Loss Against the Baltimore Orioles',
                                  lead="Toronto Blue Jays' pitcher, Hyun-jin "
                                       'Ryu, made his first start in over a '
                                       "year but couldn't prevent the AL's "
                                       'leading team from winning.',
                                  body1='In his comeback game, Hyun-jin Ryu '
                                        'pitched for the Toronto Blue Jays '
                                        'against the Baltimore Orioles in the '
                                        'Major League Baseball (MLB) World '
                                        "Series. Despite Ryu's efforts, the "
                                        'Orioles emerged victorious, scoring '
                                        'four runs on nine hits in five '
                                        'innings. Ryu showcased his talents by '
                                        'throwing a fastball at an impressive '
                                        'speed of 146 mph.',
                                  body2='However, his performance was unable '
                                        'to secure a win for his team. This '
                                        "loss marked Ryu's first in the 2023 "
                                        'season after undergoing ligament '
                                        'splicing surgery in his left elbow. '
                                        'Despite the setback, fans and experts '
                                        "are optimistic about Ryu's future "
                                        'performance.',
                                  qna_list=[QnA(question='Who did Hyun-jin Ryu '
                                                         'pitch against in his '
                                                         'comeback game?',
                                                answer='Hyun-jin Ryu pitched '
                                                       'against the Baltimore '
                                                       'Orioles.'),
                                            QnA(question='How many runs did '
                                                         'the Baltimore '
                                                         'Orioles score '
                                                         'against Ryu?',
                                                answer='The Baltimore Orioles '
                                                       'scored four runs '
                                                       'against Ryu.'),
                                            QnA(question="What was Ryu's "
                                                         'fastball speed '
                                                         'during the game?',
                                                answer="Ryu's fastball reached "
                                                       'an impressive speed of '
                                                       '146 mph.'),
                                            QnA(question="What was Ryu's "
                                                         'previous performance '
                                                         'before his comeback '
                                                         'game?',
                                                answer='Ryu had been out of '
                                                       'action for over a year '
                                                       'due to ligament '
                                                       'splicing surgery on '
                                                       'his left elbow.'),
                                            QnA(question='What is the outlook '
                                                         "for Ryu's future "
                                                         'performances?',
                                                answer='Despite the loss, fans '
                                                       'and experts are '
                                                       "optimistic about Ryu's "
                                                       'future performance.')],
                                  language='EN-US'),
                   ArticleContent(title='柳箫然重返投手丘，最终不敌巴尔的摩金莺队',
                                  lead='多伦多蓝鸟队的投手柳贤振一年多来首次先发，但未能阻止美联领先的球队获胜。',
                                  body1='在美国职业棒球大联盟（MLB）世界系列赛中，柳贤振代表多伦多蓝鸟队对阵巴尔的摩金莺队，这是他的复出之战。尽管柳贤振做出了努力，但金莺队还是取得了胜利，在五局比赛中被击出九支安打，得到四分。隆以 '
                                        '146 英里/小时的惊人速度投出快速球，展示了自己的天赋。',
                                  body2='然而，他的表现未能为球队赢得一场胜利。这场失利是柳箫然接受左肘韧带接合手术后在 '
                                        '2023 '
                                        '赛季的首场失利。尽管遭遇挫折，但球迷和专家对柳箫然未来的表现持乐观态度。',
                                  qna_list=[QnA(question='柳贤振在复出赛中的对手是谁？',
                                                answer='柳贤振在与巴尔的摩金莺队的比赛中投球。'),
                                            QnA(question='巴尔的摩金莺队对柳箫然的得分是多少？',
                                                answer='巴尔的摩金莺队在与柳箫然的比赛中得到 4 '
                                                       '分。'),
                                            QnA(question='比赛中隆的快速球速是多少？',
                                                answer='柳箫然的快速球达到了令人印象深刻的 146 '
                                                       '英里/小时。'),
                                            QnA(question='柳忠秧在复出前的表现如何？',
                                                answer='由于左肘接受了韧带接合手术，柳忠秧已经休战了一年多。'),
                                            QnA(question='柳忠秧未来的表现前景如何？',
                                                answer='尽管输掉了比赛，但球迷和专家们对柳箫然未来的表现还是很乐观。')],
                                  language='ZH'),
                   ArticleContent(title='류현진의 마운드 복귀, 볼티모어 오리올스전 패배로 끝나다',
                                  lead='토론토 블루제이스의 류현진 투수가 1년여 만에 선발 등판했지만, AL '
                                       '선두 팀의 승리를 막지는 못했습니다.',
                                  body1='류현진은 메이저리그 야구(MLB) 월드시리즈에서 토론토 블루제이스와 '
                                        '볼티모어 오리올스를 상대로 복귀전에서 선발 투수로 등판했습니다. '
                                        '류현진의 호투에도 불구하고 오리올스는 5이닝 동안 9안타에 '
                                        '4실점하며 승리를 거뒀습니다. 류현진은 시속 146마일이라는 놀라운 '
                                        '속도의 직구를 던지며 자신의 재능을 뽐냈습니다.',
                                  body2='그러나 그의 활약은 팀의 승리를 보장하지 못했습니다. 이번 패배는 '
                                        '왼쪽 팔꿈치 인대 접합 수술을 받은 류현진의 2023시즌 첫 '
                                        '패배였습니다. 아쉬움에도 불구하고 팬들과 전문가들은 류현진의 향후 '
                                        '활약에 대해 낙관적인 전망을 내놓고 있습니다.',
                                  qna_list=[QnA(question='류현진 선수의 복귀전에서 상대 투수는 '
                                                         '누구였나요?',
                                                answer='류현진이 볼티모어 오리올스를 상대로 '
                                                       '투구했습니다.'),
                                            QnA(question='볼티모어 오리올스가 류현진을 상대로 '
                                                         '얼마나 많은 득점을 올렸나요?',
                                                answer='볼티모어 오리올스는 류현진을 상대로 '
                                                       '4득점을 올렸습니다.'),
                                            QnA(question='경기 중 류현진의 직구 속도는 어느 '
                                                         '정도였나요?',
                                                answer='류현진의 직구는 최고 시속 '
                                                       '146마일이라는 놀라운 속도를 '
                                                       '기록했습니다.'),
                                            QnA(question='복귀전 경기 전 류제국의 이전 성적은 '
                                                         '어땠나요?',
                                                answer='류 선수는 왼쪽 팔꿈치 인대 접합 수술로 '
                                                       '1년 넘게 경기에 나서지 못했습니다.'),
                                            QnA(question='류 선수의 향후 활약에 대한 전망은 '
                                                         '어떻게 되나요?',
                                                answer='패배에도 불구하고 팬들과 전문가들은 '
                                                       '류제국의 향후 활약에 대해 낙관적인 '
                                                       '전망을 내놓고 있습니다.')],
                                  language='KO')],
         images=[ArticleImage(url='https://flexible.img.hani.co.kr/flexible/normal/970/652/imgdb/original/2023/0802/20230802501164.jpg',
                              source='한겨레'),
                 ArticleImage(url='https://image.imnews.imbc.com/news/2023/sports/article/__icsFiles/afieldfile/2023/08/02/y230802-3.jpg',
                              source='MBC뉴스')])]
