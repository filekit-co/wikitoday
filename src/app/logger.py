import logging
from enum import Enum
from functools import lru_cache
from logging.config import dictConfig

from utils import EnumContainsMeta


class LogLevel(Enum, metaclass=EnumContainsMeta):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    @staticmethod
    def get_log_level(env_level: str):
        if env_level.lower() == 'dev':
            return LogLevel.DEBUG
        else:
            return LogLevel.INFO

class TermColors(str, Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColoredFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: TermColors.OKBLUE.value + "[%(asctime)s] %(levelname)s in %(module)s: %(message)s" + TermColors.ENDC.value,
        logging.INFO: TermColors.OKGREEN.value + "[%(asctime)s] %(levelname)s in %(module)s: %(message)s" + TermColors.ENDC.value,
        logging.WARNING: TermColors.WARNING.value + "[%(asctime)s] %(levelname)s in %(module)s: %(message)s" + TermColors.ENDC.value,
        logging.ERROR: TermColors.FAIL.value + "[%(asctime)s] %(levelname)s in %(module)s: %(message)s" + TermColors.ENDC.value,
        logging.CRITICAL: TermColors.FAIL.value + "[%(asctime)s] %(levelname)s in %(module)s: %(message)s" + TermColors.ENDC.value,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger(app_level: str):
    log_level = LogLevel.get_log_level(app_level)
    
    if log_level not in LogLevel:
        raise ValueError(f"Invalid log level: {log_level}")

    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                '()': logging.StreamHandler,
                'formatter': 'default',
            },
        },
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'root': {
            'level': log_level.value,
            'handlers': ['console'],
        },
    }

    dictConfig(LOGGING_CONFIG)

@lru_cache(maxsize=None)
def get_colored_logger(name) -> logging.Logger:
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter())
    logger.addHandler(handler)
    return logger