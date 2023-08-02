from dataclasses import fields
from typing import Dict, List, Type, TypeVar

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
