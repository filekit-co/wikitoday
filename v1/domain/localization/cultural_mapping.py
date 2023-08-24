from datetime import time
from functools import lru_cache

from domain.entities import Language

# Mapping of country IDs to languages that are culturally relevant to that country
_cultural_language_mapping = {
    "AR": [Language.ES, Language.PT_BR], # 아르헨티나는 스페인어를 공용어로 사용하며, 이웃하는 브라질과의 경제 및 문화적 연결을 고려하여 포르투갈어도 포함됩니다.
    "AU": [Language.EN_US, Language.ZH], # 호주는 영어를 사용하며, 중국과의 경제적 연결을 고려하여 중국어도 포함됩니다.
    "AT": [Language.DE, Language.FR, Language.IT], # 오스트리아는 독일어를 사용하며, 주변 유럽 국가와의 연결을 반영하여 프랑스어와 이탈리아어도 포함됩니다.
    "BE": [Language.NL, Language.FR, Language.DE],  # 벨기에는 네덜란드어, 프랑스어, 독일어를 공용어로 사용하며, 이 세 언어가 포함되었습니다.
    "BR": [Language.PT_BR, Language.ES, Language.FR, Language.DE], # 브라질은 포르투갈어를 사용하며, 이웃 국가와의 연결을 고려하여 스페인어도 포함되었습니다. 축구 관련된 뉴스에 의해 프랑스어와 독일어를 추가합니다.
    "CA": [Language.EN_US, Language.FR], # 캐나다는 영어와 프랑스어를 공용어로 사용합니다.
    "CL": [Language.ES, Language.PT_BR],
    "CO": [Language.ES, Language.PT_BR],
    "CZ": [Language.CS, Language.DE, Language.PL],
    "DK": [Language.DA, Language.SV, ],
    "EG": [Language.FR], # 이집트는 아랍어를 공용어로 사용하며, 프랑스어는 역사적인 연결을 반영합니다.
    "FI": [Language.FI, Language.SV, Language.RU],
    "FR": [Language.FR, Language.DE, Language.IT, Language.ES], # 프랑스는 프랑스어를 사용하며, 주요 이웃 국가들과의 연결을 반영하여 추가 언어가 포함되었습니다.
    "DE": [Language.DE, Language.FR, Language.IT],
    "GR": [Language.EL, Language.IT],
    "HK": [Language.ZH, Language.EN_US, Language.JA], # 홍콩은 중국어와 영어를 공용어로 사용하며, 일본과의 거래량을 고려하여 일본어도 포함됩니다.
    "HU": [Language.HU, Language.DE],
    "IN": [Language.EN_US], # 인도는 힌디어와 영어를 주요 언어로 사용하며, 다양한 언어가 혼용되는 나라입니다.
    "ID": [Language.ID, Language.EN_US, Language.ZH],
    "IE": [Language.EN_GB],
    # "IL": [Language.HE, ], # 이스라엘은 히브리어와 아랍어를 공용어로 사용합니다
    "IT": [Language.IT, Language.FR, Language.DE],
    "JP": [Language.JA, ], 
    "KE": [Language.FR],
    "MY": [Language.EN_US, Language.ZH],
    "MX": [Language.ES, Language.EN_US],
    "NL": [Language.NL, Language.DE, Language.FR],
    "NZ": [Language.EN_US, ],
    "NG": [Language.EN_US, Language.FR],
    "NO": [Language.NB, Language.SV, Language.DA],
    "PE": [Language.ES, Language.PT_BR],
    "PH": [Language.ZH, Language.EN_US,Language.JA],
    "PL": [Language.PL, Language.DE, Language.RU],
    "PT": [Language.PT_PT, Language.ES],
    "RO": [Language.RO, Language.HU],
    "RU": [Language.RU, Language.UK, Language.DE],
    "SA": [Language.EN_US],
    "SG": [Language.EN_US, Language.ZH, ],
    "ZA": [Language.EN_US],
    "KR": [Language.KO, Language.EN_US, ], # 대한민국은 한국어를 사용하며, 일본과 중국과의 거리가 가까운 연결을 반영합니다.
    "ES": [Language.ES, Language.PT_PT, Language.FR],
    "SE": [Language.SV, Language.DA],
    "CH": [Language.DE, Language.FR, Language.IT], #  스위스는 독일어, 프랑스어, 이탈리아어를 공용어로 사용하여 이 세 언어를 포함시킵니다.
    "TW": [Language.ZH, Language.EN_US],
    "TH": [Language.ZH, Language.EN_US],
    "TR": [Language.TR, ],
    "UA": [Language.UK, Language.RU],
    "GB": [Language.EN_GB, Language.FR, Language.DE],
    "VN": [Language.EN_US, Language.ZH],
}


# 6am and 6pm by Korean time
countries_time_at_kr_6 = {
    time(10, 0): ["MX"],
    time(11, 0): ["US", "CA", "CO", "PE"],
    time(12, 0): ["CL", "KR", "JP"],
    time(13, 0): ["BR", "AR"],
    time(16, 0): ["GB", "PT", "IE"],
    time(17, 0): ["DE", "FR", "IT", "ES", "NL", "CH", "SE", "BE", "PL", "AT", "DK", "CZ", "HU", "NO", "NG"],
    time(18, 0): ["ZA", "UA", "IL", "FI", "GR", "RO"],
    time(19, 0): ["RU", "TR", "SA", "KE"],
    time(21, 30): ["IN"],
    time(22, 0): ["MX"],
    time(23, 0): ["US", "CA", "CO", "PE"],
    time(0, 0): ["SG", "TW", "MY", "HK", "PH", "KR", "JP"],
    time(1, 0): ["BR", "AR"],
    time(2, 0): ["AU"],
    time(4, 0): ["NZ"],
    time(7, 0): ["RU", "TR", "SA", "KE"],
    time(9, 30): ["IN"],
    time(11, 0): ["ID", "VN", "TH"],
    time(12, 0): ["SG", "TW", "MY", "HK", "PH"],
    time(14, 0): ["AU"],
    time(16, 0): ["NZ"]
}

@lru_cache()
def get_culturally_relevant_languages(country_id, include_english=True):
    """
    Returns a list of languages that are likely to be of interest based on cultural,
    historical, and economic connections to the given country.

    :param country_id: Two-letter country ID (e.g., "KR")
    :param include_english: Whether to include English as a target language
    :return: List of target languages as Language Enum
    """

    # Retrieve the culturally relevant languages for the given country
    culturally_relevant_languages = _cultural_language_mapping.get(country_id, [])

    # Include English if requested and if it's not already in the list
    if include_english and Language.EN_US not in culturally_relevant_languages:
        culturally_relevant_languages.append(Language.EN_US)

    return culturally_relevant_languages


