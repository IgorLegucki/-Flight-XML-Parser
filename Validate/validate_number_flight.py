import re
from logger.app_logger import logger


def validate_number_flight(code: str):
    if not re.fullmatch(r"^[A-Z]{2,3}\d{1,4}$", code):
        error_msg = f"Invalid flight code: {code}"
        logger.error(error_msg)
        raise ValueError(error_msg)
