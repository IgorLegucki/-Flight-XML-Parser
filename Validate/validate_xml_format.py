import xml.etree.ElementTree as ET
from logger.app_logger import logger


def load_xml(xml_path: str):
    try:
        tree = ET.parse(xml_path)
        return tree.getroot()
    except ET.ParseError as e:
        error_msg = f"XML syntax error: {e}"
        logger.error(error_msg)
        raise ValueError(error_msg)
