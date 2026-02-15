<div align="center">

# GO Transit GTFS Wrapper
![License](https://img.shields.io/github/license/kenrickzhang/GO-Transit-API-Python-Wrapper)
![Issues](https://img.shields.io/github/issues/kenrickzhang/GO-Transit-API-Python-Wrapper)
![PyPI](https://img.shields.io/pypi/v/gotransit)

The GO Transit GTFS wrapper for Python simplifies access to the [GO Transit / Metrolinx Open Data API](https://api.openmetrolinx.com/OpenDataAPI).
</div>

## Features
- Access next service times for stops
- Retrieve stop details and destinations
- Query train and bus schedules
- Fetch General Transit Feed Specification (GTFS) feeds: alerts, trip updates, vehicle positions
- Service updates: alerts, marketing, exceptions
- Fare lookup between stops
- Modular design: `Client` routes requests to endpoint classes (e.g., `Stop`, `Schedule`)


## Installation
GO Transit GTFS wrapper is supported on Python 3.10+. It can be installed via pip:
```sh
pip install gotransit
```

## Quickstart
You must have a GO Transit API key to access GTFS information. You can apply for an API key [here](https://api.openmetrolinx.com/OpenDataAPI/Help/Registration/en).  
Once you have an API key, you can instantiate a client like so:

```sh
import gotransit

go_client = gotransit.Client(api_key="API_KEY")
```

You can pass the `go_client` instance into distinct endpoints to organize access:
```sh
import json
import gotransit

go_client = gotransit.Client(api_key="API_KEY")

# Pass the main client to the Stop endpoint
stop_api = gotransit.Stop(go_client)

# We want Stop information for Union Station, code 'UN'
stop_code = "UN"

# Request and store the result of the Next Service endpoint with the 'UN' stop code
data = stop_api.next_service(stop_code)

# Format and dump the result to a local JSON file for easy viewing
with open("union_station_stops.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("API Response ==> union_station_stops.json")
```

Refer to the [GO API](https://api.openmetrolinx.com/OpenDataAPI/Help/Index/en) documentation for a comprehensive list of available endpoints.
