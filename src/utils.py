from dataclasses import fields
from typing import Dict, Type, TypeVar

T = TypeVar('T')

def generate_dataclass(dc: Type[T], data: Dict) -> T:
    """ignore fields not explicitly written"""
    
    keys = {f.name for f in fields(dc)}
    filtered_data = {k: v for k, v in data.items() if k in keys}
    return dc(**filtered_data)