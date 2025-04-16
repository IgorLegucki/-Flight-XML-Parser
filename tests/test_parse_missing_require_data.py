import pytest
from parser.flight_parser import parse_flights

import tempfile


@pytest.mark.parametrize("missing_tag, expected_error", [
    ("number", "Missing required element: number"),
    ("aircraft", "Missing required element: aircraft"),
    ("status", "Missing required element: status"),
    ("dep_airport", "Missing required element: departure airport"),
    ("dep_time", "Missing required element: departure time"),
    ("arr_airport", "Missing required element: arrival airport"),
    ("arr_time", "Missing required element: arrival time"),
])
def test_parse_missing_require_data(missing_tag, expected_error):
    number_tag = "" if missing_tag == "number" else "<number>LOT123</number>"
    aircraft_tag = "" if missing_tag == "aircraft" else "<aircraft>B738</aircraft>"

    dep_airport = "" if missing_tag == "dep_airport" else "<airport>EPWA</airport>"
    dep_time = "" if missing_tag == "dep_time" else "<time>2025-04-05T10:00:00Z</time>"

    arr_airport = "" if missing_tag == "arr_airport" else "<airport>EGLL</airport>"
    arr_time = "" if missing_tag == "arr_time" else "<time>2025-04-05T12:00:00Z</time>"

    status_tag = "" if missing_tag == "status" else "<status>scheduled</status>"

    invalid_xml = f"""
        <flights>
            <flight>
                {number_tag}
                {aircraft_tag}
                <departure>
                    {dep_airport}
                    {dep_time}
                </departure>
                <arrival>
                    {arr_airport}
                    {arr_time}
                </arrival>
                {status_tag}
            </flight>
        </flights>
        """

    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".xml") as f:
        f.write(invalid_xml)
        f.seek(0)

        with pytest.raises(ValueError) as excinfo:
            parse_flights(f.name)

        assert expected_error in str(excinfo.value)
