## PurpleAir GMU InSitu API Endpoints for FireAlarm

Below are the details of the available InSitu API endpoints:

| Provider | Endpoint | Required Variables | Optional Variables | Constraints | Example Request |
|----------|----------|--------------------|--------------------|-------------|-----------------|
| PurpleAir-GMU-Raw | `/sensor_data` | `date`, `min_lon`, `max_lon`, `min_lat`, `max_lat` | `variable`, `provider` | Max 10 sensors for `activities` | `http://<host>:<port>/sensor_data?date=YYYY-MM-DD&...` |
| PurpleAir-GMU-Raw | `/activities` | `sensor_ids`, `sd` (start date) | `ed` (end date), `provider` | No end date allowed for raw data | `http://<host>:<port>/activities?sensor_ids=ID1,ID2,...&sd=YYYY-MM
