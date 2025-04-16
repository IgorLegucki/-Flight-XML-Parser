import re
from logger.app_logger import logger


def validate_airport_code(code: str, label: str):
    if not re.fullmatch(r"^[A-Z]{4}$", code):
        error_msg = f"Invalid {label} airport code: {code}"
        logger.error(error_msg)
        raise ValueError(error_msg)
