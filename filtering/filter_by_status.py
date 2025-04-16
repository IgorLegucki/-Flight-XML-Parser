from typing import List
from model.flight_model import Flight

def filter_by_status(flights: List[Flight], status: str) -> List[Flight]:
    return [flight for flight in flights if flight.status.lower() == status.lower()]