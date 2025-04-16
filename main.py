from parser.flight_parser import parse_flights
from filtering.filter_by_status import filter_by_status
from filtering.status_choice import get_status_choice

if __name__ == '__main__':
    try:
        flights = parse_flights("Dział testów automatycznych zadanie (dane) - Lot Summer Internship.xml")

        selected_status = get_status_choice()
        scheduled_flights = filter_by_status(flights, selected_status)

        for f in scheduled_flights:
            print(f)
    except ValueError as e:
        print(f"Validation error: {e}")
