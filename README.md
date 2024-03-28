## PurpleAir GMU InSitu API Endpoints for FireAlarm

Below are the details of the available InSitu API endpoints:


| Provider | Endpoint | Required Variables | Optional Variables | Constraints | Example Request |
|----------|----------|--------------------|--------------------|-------------|-----------------|
| PurpleAir-GMU-Raw | `/sensor_data` | `date`, `min_lon`, `max_lon`, `min_lat`, `max_lat` | `variable`, `provider` | No specific constraints | [`/sensor_data`](http://insitu-api.stcenter.net/sensor_data?date=YYYY-MM-DD&...) |
|          | `/activities` | `sensor_ids`, `sd` (start date) | `ed` (end date), `provider` | Max 10 sensors, no end date for raw data | [`/activities`](http://insitu-api.stcenter.net/activities?sensor_ids=ID1,ID2,...&sd=YYYY-MM-DD) |

