from datetime import datetime
from logger.app_logger import logger


def validate_iso8601(time_str: str, label: str):
    try:
        datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        error_msg = f"Invalid {label} time format: {time_str}"
        logger.error(error_msg)
        raise ValueError(error_msg)
