# https://trends.google.com/trends/trendingsearches/daily?geo=KR&hl=en-GB
import os
from enum import StrEnum

NUM_MAX_ARTICLE = 2
GOOGLE_BASE_TRENDS_API='https://trends.google.com/trends/trendingsearches/daily/rss?geo='

# 
class TargetCountryCode(StrEnum):
    # The ranking is based on a combination of factors such as population, 
    # global influence, and national income levels.
    
    US = "US"  # United States
    JP = "JP"  # Japan
    DE = "DE"  # Germany
    GB = "GB"  # United Kingdom
    FR = "FR"  # France
    IN = "IN"  # India
    BR = "BR"  # Brazil
    RU = "RU"  # Russia
    IT = "IT"  # Italy
    CA = "CA"  # Canada
    KR = "KR"  # South Korea
    AU = "AU"  # Australia
    ES = "ES"  # Spain
    MX = "MX"  # Mexico
    NL = "NL"  # Netherlands
    CH = "CH"  # Switzerland
    TR = "TR"  # Türkiye
    SA = "SA"  # Saudi Arabia
    SE = "SE"  # Sweden
    ID = "ID"  # Indonesia
    BE = "BE"  # Belgium
    AR = "AR"  # Argentina
    ZA = "ZA"  # South Africa
    PL = "PL"  # Poland
    AT = "AT"  # Austria
    SG = "SG"  # Singapore
    UA = "UA"  # Ukraine
    TW = "TW"  # Taiwan
    NO = "NO"  # Norway
    IL = "IL"  # Israel
    MY = "MY"  # Malaysia
    VN = "VN"  # Vietnam
    HK = "HK"  # Hong Kong
    TH = "TH"  # Thailand
    DK = "DK"  # Denmark
    CL = "CL"  # Chile
    PH = "PH"  # Philippines
    CZ = "CZ"  # Czechia
    FI = "FI"  # Finland
    GR = "GR"  # Greece
    PT = "PT"  # Portugal
    IE = "IE"  # Ireland
    CO = "CO"  # Colombia
    RO = "RO"  # Romania
    NZ = "NZ"  # New Zealand
    HU = "HU"  # Hungary
    PE = "PE"  # Peru
    KE = "KE"  # Kenya
    NG = "NG"  # Nigeria

GPT_MODEL = "gpt-3.5-turbo-16k-0613"
