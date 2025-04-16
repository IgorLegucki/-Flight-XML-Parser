from dataclasses import dataclass
from typing import Optional


@dataclass
class Flight:
    number: str
    aircraft: str
    departure_airport: str
    departure_time: str
    arrival_airport: str
    arrival_time: str
    status: Optional[str] = None
