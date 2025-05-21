from model.flight_model import Flight
from parser.flight_parser import parse_flights
import os


def test_parse_valid_flight():
    xml_file = os.path.join(os.path.dirname(__file__), '..',
                            'Rozkład_lotów.xml')

    flights = parse_flights(xml_file)

    assert isinstance(flights, list), "parse_flights should return a list"

    assert len(flights) > 0, "There should be at least one flight"

    assert isinstance(flights[0], Flight), "The first element should be a Flight object"
