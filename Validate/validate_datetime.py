from datetime import datetime


def validate_iso8601(time_str: str, label: str):
    try:
        datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        raise ValueError(f"Invalid {label} time format: {time_str}")
