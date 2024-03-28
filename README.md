## PurpleAir GMU InSitu API Endpoints for FireAlarm

Below are the details of the available InSitu API endpoints:


| Provider | Endpoint | Required Variables | Optional Variables | Constraints | Example Request |
|----------|----------|--------------------|--------------------|-------------|-----------------|
| PurpleAir-GMU-Raw | sensor_data | `date`, `min_lon`, `max_lon`, `min_lat`, `max_lat` | `variable`, `provider` | No specific constraints | [http://insitu-api.stcenter.net/sensor_data?date=YYYY-MM-DD&...](http://insitu-api.stcenter.net/sensor_data?date=YYYY-MM-DD&...) |
|          | activities | `sensor_ids`, `sd` (start date) | `ed` (end date), `provider` | Max 10 sensors, no end date for raw data | [http://insitu-api.stcenter.net/sensor_data?date=YYYY-MM-DD&...](http://insitu-api.stcenter.net/activities?sensor_ids=ID1,ID2,...&sd=YYYY-MM-DD) |



| Provider | Endpoint | Required Variables | Optional Variables | 
|----------|----------|---------------------|---------------------|
| `PurpleAir-GMU-Raw` | `/sensor_data` | `date`, `min_lon`, `max_lon`, `min_lat`, `max_lat` | `variable` |
|  |  | **Sample Request**: [`/sensor_data?date=2022-07-01&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0`](http://127.0.0.1:5000/sensor_data?date=2022-07-01&min_lon=-123.0&max_lon=-122.0&min_lat=37.0&max_lat=38.0) |  |
| `PurpleAir-GMU-Cal` | `/sensor_data` | `date`, `min_lon`, `max_lon`, `min_lat`, `max_lat`, `provider` | `variable` |
|  |  | **Sample Request**: [`/sensor_data?date=2022-07-01&min_lon=-118.67&max_lon=-118.15&min_lat=33.70&max_lat=34.34&provider=PurpleAir-GMU-Cal`](http://127.0.0.1:5000/sensor_data?date=2022-07-01&min_lon=-118.67&max_lon=-118.15&min_lat=33.70&max_lat=34.34&provider=PurpleAir-GMU-Cal) |  |
| `PurpleAir-GMU-Raw-Hourly` | `/activities` | `sensor_ids`, `sd`, `provider` | `ed` |
|  |  | **Sample Request**: [`/activities?sensor_ids=135442,96855&sd=2022-07-01&provider=PurpleAir-GMU-Raw-Hourly`](http://127.0.0.1:5000/activities?sensor_ids=135442,96855&sd=2022-07-01&provider=PurpleAir-GMU-Raw-Hourly) |  |


