import tempfile
from parser.flight_parser import parse_flights

sample_xml = """
  <flights>
      <flight>
          <number>LOT123</number>
          <aircraft>B738</aircraft>
          <departure>
              <airport>EPWA</airport>
              <time>2025-04-05T10:00:00Z</time>
          </departure>
          <arrival>
              <airport>EGLL</airport>
              <time>2025-04-05T12:00:00Z</time>
          </arrival>
          <status>scheduled</status>
      </flight>
  </flights>
  """


def test_parse_returns_expected_flights():
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".xml") as f:
        f.write(sample_xml)
        f.seek(0)
        flights = parse_flights(f.name)

    assert len(flights) == 1

    flight = flights[0]
    assert flight.number == "LOT123"
    assert flight.aircraft == "B738"
    assert flight.departure_airport == "EPWA"
    assert flight.departure_time == "2025-04-05T10:00:00Z"
    assert flight.arrival_airport == "EGLL"
    assert flight.arrival_time == "2025-04-05T12:00:00Z"
    assert flight.status == "scheduled"
