from logger.app_logger import logger


def validate_require_element(value: str, label: str):
    if (value == "" or value is None):
        error_msg = f"Missing required element: {label}"
        logger.error(error_msg)
        raise ValueError(error_msg)
