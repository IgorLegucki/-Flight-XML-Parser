from typing import List
from model.flight_model import Flight
from Validate.validate_xml_format import load_xml
from Validate.validate_datetime import validate_iso8601
from Validate.validate_airport_code import validate_airport_code
from Validate.validate_number_flight import validate_number_flight
from Validate.validate_require_element import validate_require_element


def parse_flights(xml_path: str) -> List[Flight]:
    root = load_xml(xml_path)
    if root is None:
        return []

    flights = []
    for flight_elem in root.findall('flight'):
        number = flight_elem.findtext('number')
        validate_require_element(number, "number")
        validate_number_flight(number)

        aircraft = flight_elem.findtext('aircraft')
        validate_require_element(aircraft, "aircraft")

        departure = flight_elem.find('departure')
        dep_airport = departure.findtext('airport')
        validate_require_element(dep_airport, "departure airport")
        validate_airport_code(dep_airport, "departure")

        dep_time = departure.findtext('time')
        validate_require_element(dep_time, "departure time")
        validate_iso8601(dep_time, "departure")

        arrival = flight_elem.find('arrival')
        arr_airport = arrival.findtext('airport')
        validate_require_element(arr_airport, "arrival airport")
        validate_airport_code(arr_airport, "arrival")

        arr_time = arrival.findtext('time')
        validate_require_element(arr_time, "arrival time")
        validate_iso8601(arr_time, "arrival")

        status = flight_elem.findtext('status')
        validate_require_element(status, "status")

        flight = Flight(
            number=number,
            aircraft=aircraft,
            departure_airport=dep_airport,
            departure_time=dep_time,
            arrival_airport=arr_airport,
            arrival_time=arr_time,
            status=status
        )
        flights.append(flight)

    return flights
