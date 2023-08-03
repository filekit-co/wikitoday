# https://trends.google.com/trends/trendingsearches/daily?geo=KR&hl=en-GB
import os
from enum import StrEnum

NUM_MAX_ARTICLE = 2
GOOGLE_BASE_TRENDS_API='https://trends.google.com/trends/trendingsearches/daily/rss?geo='

# 미국, 인도, 일본, 싱가포르, 호주, 홍콩, 타이완, 브라질, 캐나다, 독일, 네덜란드, 인도네시아, 대한민국, 러시아, 터키, 베트남, 필리핀
class TargetCountryCode(StrEnum):
    US = "US"  # United States
    IN = "IN"  # India
    JP = "JP"  # Japan
    SG = "SG"  # Singapore
    AU = "AU"  # Australia
    HK = "HK"  # Hong Kong
    TW = "TW"  # Taiwan
    BR = "BR"  # Brazil
    CA = "CA"  # Canada
    DE = "DE"  # Germany
    NL = "NL"  # Netherlands
    ID = "ID"  # Indonesia
    KR = "KR"  # South Korea
    RU = "RU"  # Russia
    TR = "TR"  # Türkiye
    VN = "VN"  # Vietnam
    PH = "PH"  # Philippines

_GOOGLE_GEO_PICKER = [
    {"id": "AR", "name": "Argentina"},
    {"id": "AU", "name": "Australia"},
    {"id": "AT", "name": "Austria"},
    {"id": "BE", "name": "Belgium"},
    {"id": "BR", "name": "Brazil"},
    {"id": "CA", "name": "Canada"},
    {"id": "CL", "name": "Chile"},
    {"id": "CO", "name": "Colombia"},
    {"id": "CZ", "name": "Czechia"},
    {"id": "DK", "name": "Denmark"},
    {"id": "EG", "name": "Egypt"},
    {"id": "FI", "name": "Finland"},
    {"id": "FR", "name": "France"},
    {"id": "DE", "name": "Germany"},
    {"id": "GR", "name": "Greece"},
    {"id": "HK", "name": "Hong Kong"},
    {"id": "HU", "name": "Hungary"},
    {"id": "IN", "name": "India"},
    {"id": "ID", "name": "Indonesia"},
    {"id": "IE", "name": "Ireland"},
    {"id": "IL", "name": "Israel"},
    {"id": "IT", "name": "Italy"},
    {"id": "JP", "name": "Japan"},
    {"id": "KE", "name": "Kenya"},
    {"id": "MY", "name": "Malaysia"},
    {"id": "MX", "name": "Mexico"},
    {"id": "NL", "name": "Netherlands"},
    {"id": "NZ", "name": "New Zealand"},
    {"id": "NG", "name": "Nigeria"},
    {"id": "NO", "name": "Norway"},
    {"id": "PE", "name": "Peru"},
    {"id": "PH", "name": "Philippines"},
    {"id": "PL", "name": "Poland"},
    {"id": "PT", "name": "Portugal"},
    {"id": "RO", "name": "Romania"},
    {"id": "RU", "name": "Russia"},
    {"id": "SA", "name": "Saudi Arabia"},
    {"id": "SG", "name": "Singapore"},
    {"id": "ZA", "name": "South Africa"},
    {"id": "KR", "name": "South Korea"},
    {"id": "ES", "name": "Spain"},
    {"id": "SE", "name": "Sweden"},
    {"id": "CH", "name": "Switzerland"},
    {"id": "TW", "name": "Taiwan"},
    {"id": "TH", "name": "Thailand"},
    {"id": "TR", "name": "Türkiye"},
    {"id": "UA", "name": "Ukraine"},
    {"id": "GB", "name": "United Kingdom"},    
    {"id": "VN", "name": "Vietnam"},
]


GPT_MODEL = "gpt-3.5-turbo-16k-0613"
