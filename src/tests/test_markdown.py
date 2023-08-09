from domain.entities import ArticleContent, ArticleImage, QnA
from infra.markdown import Article, to_folders
from mocks import step_5


def test_to_folders():
    article_date = '20220807'
    result = to_folders(step_5, article_date)
    assert len(result) == 9


def _break_html(body) -> str:
    return body + '<p><html>'

def test_to_folder_template_html_escape():
    article = Article(category='Sports',
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
                                  language='EN-US')],
         images=[ArticleImage(url='https://img.olympicchannel.com/images/image/private/t_social_share_thumb/f_auto/primary/an8hsyg0rlbuy0cvbi32',
                              source='Olympics'),
                 ArticleImage(url='https://biz.chosun.com/resizer/LwAJb26bxlCQqjko_uBVir_Q5SM=/650x341/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/FJ2ZH42M2DYNMXRDD7JKH4KRGA.png',
                              source='조선비즈')])
    breaked = _break_html(article.contents[0].body1)
    article.contents[0].body1 = breaked
    result = to_folders([article, ], '20220807')

    # print(result[0].mds[0].md)
    # assert False
