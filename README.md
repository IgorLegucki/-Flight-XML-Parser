# Flight-XML-Parser
The Python project designed to parse, validate, and filter flight data from an XML file. Built with clean architecture and SOLID principles, the parser ensures proper data separation and error handling.
## Features

- Parses flight data from an XML file
- Validates:
  - Flight number format (e.g. `LOT123`)
  - 4-letter airport codes (e.g. `EPWA`)
  - DateTime in ISO 8601 format (e.g. `2025-04-05T12:00:00Z`)
- Validates required XML elements
- Logs errors (both validation and XML format issues)
- Filters flights by status (`scheduled`, `delayed`, `cancelled`)
- Contains unit tests using `pytest`

## 🛠 How to Run

Make sure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
python main.py
```
You will be prompted to filter flights by their status.

To run the prepared tests, enter in terminal:
```bash
pytest tests/test_parser.py
pytest tests/test_parse_missing_require_data.py
pytest tests/test_parse_returns_expected_flights.py
```

## Example XML Format
```xml
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
```
