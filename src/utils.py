import re
from dataclasses import fields
from enum import StrEnum
from pprint import pprint
from typing import Dict, List, Type, TypeVar
from urllib.parse import quote

import regex

T = TypeVar('T')
SENTENCE_PATTERN = regex.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!\:)\s+|\p{Cc}+|\p{Cf}+")

def generate_dataclass(dc: Type[T], data: Dict) -> T:
    """ignore fields not explicitly written"""
    
    keys = {f.name for f in fields(dc)}
    filtered_data = {k: v for k, v in data.items() if k in keys}
    return dc(**filtered_data)


def split_sentences(text: str) -> List[str]:
    sentences = SENTENCE_PATTERN.split(text)
    return [sentence for sentence in sentences if sentence]


def create_url_path(title: str, max_length: int = 20) -> str:
    # 알파벳과 숫자만 남기고 모두 제거합니다. 공백은 하이픈('-')으로 변경합니다.
    
    cleaned_title = re.sub(
        pattern = r'\W+',
        repl = ' ', 
        string = title.strip()
    ).replace(' ', '-')
    
    # 최대 길이를 초과하는 경우 문자열을 잘라냅니다.
    if len(cleaned_title) > max_length:
        cleaned_title = cleaned_title[:max_length]
    # URL-safe 문자열로 변환합니다.
    url_path = quote(cleaned_title)
    return url_path

class TermColors(StrEnum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def color_print(text: str, color = TermColors.OKGREEN):
    print(color + text + TermColors.ENDC)


# to use single quote string
# https://yaml.org/spec/1.2.2/#732-single-quoted-style
def reformat_yaml(text: str) -> str:
    # i.g Minwook's -> Minwook''s
    return text.replace("'", "''")
