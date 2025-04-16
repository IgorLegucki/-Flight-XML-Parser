import logging

logger = logging.getLogger("flight_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("flight_errors.log")
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)