import logging


def setup_logger(logger, log_level=logging.INFO, log_file=None):
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    handler = logging.StreamHandler() if not log_file else logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(handler)
    logger.setLevel(log_level)