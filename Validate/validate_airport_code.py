import re


def validate_airport_code(code: str, label: str):
    if not re.fullmatch(r"^[A-Z]{4}$", code):
        raise ValueError(f"Invalid {label} airport code: {code}")