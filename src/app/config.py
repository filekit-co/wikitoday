from functools import lru_cache

from dotenv import dotenv_values, load_dotenv  # noqa

load_dotenv()

@lru_cache
def get_env():
    return dotenv_values()

