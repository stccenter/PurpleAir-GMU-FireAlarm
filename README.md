# GMU AQ In-Situ API Endpoints

**Sensor types and providers are the key building blocks for using the API:**  

- A **sensor type** refers to a low-cost sensor network that supplies data (e.g., *OpenAQ Clarity* or *PurpleAir*).  

- A **provider** refers to a specific data stream within a sensor type, which defines **temporal resolution and how the data is processed** (e.g., minute-wise, hourly, outlier-removed, calibrated).  
---

## Sensor Types

- **OpenAQ Clarity**  
- **PurpleAir**  


## Providers

| Sensor Type     | Provider Name                | Description                                           | Status             | Source         |
|-----------------|------------------------------|-------------------------------------------------------|--------------------|----------------|
| OpenAQ Clarity  | Clarity-GMU-Raw              | 3-minute data from Clarity sensors                    | Under Development  | From OpenAQ API    |
| OpenAQ Clarity  | Clarity-GMU-Raw-Hourly       | Hourly data from Clarity sensors                      | Supported          | From OpenAQ API    |
| OpenAQ Clarity  | Clarity-GMU-Intermediate     | Hourly data with outliers removed                     | Supported          | Derived (GMU)    |
| OpenAQ Clarity  | Clarity-GMU-Cal        | Hourly data calibrated against AirNow using AI/ML with 95% Confidence Interval     | Supported          | Derived (GMU)  |
| OpenAQ Clarity  | Clarity-GMU-Raw-Daily            | Daily data from Clarity sensors                       | Under Development  | From OpenAQ API    |
| PurpleAir       | PurpleAir-GMU-Raw            | 2-minute data from PurpleAir sensors (available up to 2023-10-17 03:00:00)                  | Supported          | From PurpleAir API    |
| PurpleAir       | PurpleAir-GMU-Raw-Hourly     | Hourly data aggregated from 2-minute PurpleAir data (available up to 2023-10-17)   | Supported          | Derived (GMU)  |
| PurpleAir       | PurpleAir-GMU-Intermediate   | Hourly data with outliers removed (available up to 2023-10-17)                     | Supported          | Derived (GMU)  |
| PurpleAir       | PurpleAir-GMU-Cal      | Hourly data calibrated against AirNow using AI/ML (available up to 2023-10-17)     | Under Development        | Derived (GMU)  |
| PurpleAir       | PurpleAir-GMU-Raw-Daily          | Daily data from PurpleAir sensors (available up to 2023-10-17)                     | Supported          | Derived (GMU)  |

## API Endpoints Overview  

The AQ in-situ API provides two core endpoints for accessing sensor data:  

- **`sensor_data`** – used to query which sensors are available within a specified Region of Interest (ROI) for a given date.
- **`activities`** – used to retrieve the measurement data for selected sensors.  

*Note*: When using the API, the first step is to call **`sensor_data`** to identify which sensors are available in your region of interest. Once you have the sensor IDs, the next step is to use **`activities`** to retrieve their measurements. The type of measurements returned depends on the **provider** you specify (e.g., Raw-Hourly, Intermediate, Calibrate, Daily).  Below, you can find step-by-step instructions on how to use the API.  

### Response Codes  

- 200 Success → Request successful, data found and returned  
- 204 No Content → Request successful, but no data found for the request  
- 500 Internal Server Error → Server-side failure while processing the request  

##
## Raw-Hourly Provider Endpoints

- If `sensor_type = openaq_clarity` → `provider = Clarity-GMU-Raw-Hourly`  
- If `sensor_type = purpleair` → `provider = PurpleAir-GMU-Raw-Hourly` 

### Request

| Endpoint    | Required Parameters                                   | Optional Parameters                          | Defaults                   | Constraints                                                                                       |
|-------------|-------------------------------------------------------|-----------------------------------------------|----------------------------|--------------------------------------------------------------------------------------------------|
| sensor_data | date, min_lon, max_lon, min_lat, max_lat, provider    | variable (e.g., pm2_5, temperature, humidity) | variable: pm2_5 <br> sensor_type: purpleair           | • For sensor_type=purpleair, data is available only up to 2023-10-17 03:00:00                                                                           |
| activities  | sensor_ids, sd (start date), ed (end date), provider  | –                                             | 	sensor_type: purpleair                          | • End date is required  <br> • Start date must be earlier than end date (cannot be the same or earlier)  <br> • If more than 5 sensors are requested, the date range cannot exceed 7 days   <br> • A maximum of 500 sensors is allowed per request <br> • For sensor_type=purpleair, data is available only up to 2023-10-17 03:00:00 | |

### Response

| Endpoint     | Response fields       |
|--------------|-------------|
| sensor_data  | platform_id, latitude, longitude |            |
| activities   | date, latitude, longitude, platform_id, pm2_5, Temperature, RelativeHumidity |


### Step-by-step instructions for using the **Raw-Hourly** provider (OpenAQ example)

**Step 1:** Find all sensors in Los Angeles for a given date using the `sensor_data` endpoint.

 https://insitu-api.stcenter.net/sensor_data?sensor_type=openaq_clarity&provider=Clarity-GMU-Raw-Hourly&date=2024-07-01&variable=pm2_5&min_lon=-118.95&max_lon=-117.65&min_lat=32.75&max_lat=34.82

**Step 2:** Fetch measurements with the `activities` endpoint. Use the `platform_id` values returned in Step 1 as the `sensor_ids` (multiple IDs can be provided as a comma-separated list).

 https://insitu-api.stcenter.net/activities?sensor_type=openaq_clarity&provider=Clarity-GMU-Raw-Hourly&sensor_ids=929705,923365,923364,947150,947151,947152&sd=2024-07-01&ed=2024-07-02

*Note*: For PurpleAir, change `sensor_type` to `purpleair` and set the matching provider `PurpleAir-GMU-Raw-Hourly`. If `sensor_type` is not specified, the API defaults to PurpleAir.  

##
## Intermediate Provider Endpoints

- If `sensor_type = openaq_clarity` → `provider = Clarity-GMU-Intermediate`  
- If `sensor_type = purpleair` → `provider = PurpleAir-GMU-Intermediate`  

| Endpoint    | Required Parameters                                   | Optional Parameters                          | Defaults                   | Constraints                                                                                       |
|-------------|-------------------------------------------------------|-----------------------------------------------|----------------------------|--------------------------------------------------------------------------------------------------|
| sensor_data | date, min_lon, max_lon, min_lat, max_lat, provider    | variable (e.g., pm2_5, temperature, humidity) | variable: pm2_5 <br> sensor_type: purpleair           | • For sensor_type=purpleair, data is available only up to 2023-10-17 03:00:00                                                                          |
| activities  | sensor_ids, sd (start date), ed (end date), provider  | –                                             | 	sensor_type: purpleair                          | • End date is required  <br> • Start date must be earlier than end date (cannot be the same or earlier)  <br> • If more than 5 sensors are requested, the date range cannot exceed 7 days   <br> • A maximum of 500 sensors is allowed per request <br> • For sensor_type=purpleair, data is available only up to 2023-10-17 03:00:00 | |

### Response

| Endpoint     | Response fields       |
|--------------|-------------|
| sensor_data  | platform_id, latitude, longitude |            |
| activities   | date, latitude, longitude, platform_id, pm2_5, Temperature, RelativeHumidity |

### Step-by-step instructions for using the **Intermediate** provider (OpenAQ example)

**Step 1:** Find all sensors in Los Angeles for a given date using the `sensor_data` endpoint.

 https://insitu-api.stcenter.net/sensor_data?sensor_type=openaq_clarity&provider=Clarity-GMU-Intermediate&date=2024-07-01&variable=pm2_5&min_lon=-118.95&max_lon=-117.65&min_lat=32.75&max_lat=34.82

**Step 2:** Fetch measurements with the `activities` endpoint. Use the `platform_id` values returned in Step 1 as the `sensor_ids` (multiple IDs can be provided as a comma-separated list).

 https://insitu-api.stcenter.net/activities?sensor_type=openaq_clarity&provider=Clarity-GMU-Intermediate&sensor_ids=929705,923365,923364,947150,947151,947152&sd=2024-07-01&ed=2024-07-02

*Note*: For PurpleAir, change `sensor_type` to `purpleair` and set the matching provider `PurpleAir-GMU-Intermediate`. If `sensor_type` is not specified, the API defaults to PurpleAir.  

##
## Calibration Provider Endpoints

The calibration endpoint is available only for sensors located in California and provides the calibrated measurements along with their associated uncertainties (95% confidence interval).

**Note:** This endpoint may take longer to respond. Please wait for the response rather than refreshing or sending too many repeated requests.  

- `sensor_type = openaq_clarity` → `provider = Clarity-GMU-Cal`  


| Endpoint    | Required Parameters                                   | Optional Parameters                          | Defaults                   | Constraints                                                                                       |
|-------------|-------------------------------------------------------|-----------------------------------------------|----------------------------|--------------------------------------------------------------------------------------------------|
| sensor_data | date, min_lon, max_lon, min_lat, max_lat, provider    | variable (pm2_5)    | variable: pm2_5 <br> sensor_type: purpleair | • Only pm2_5 variable is supported <br> • Bounding box (min_lon, max_lon, min_lat, max_lat) must be within California |
| activities  | sensor_ids, sd (start date), ed (end date), provider  | –                                             | 	sensor_type: purpleair                          | • Only 1 sensor_id is allowed per request <br> • Sensor must be located within California <br> • End date is required  <br> • Start date must be earlier than end date (cannot be the same or earlier) | |

### Response

| Endpoint     | Response fields       |
|--------------|-------------|
| sensor_data  | platform_id, latitude, longitude |            |
| activities   | date, latitude, longitude, platform_id, pm2_5, pm2_5_total_uq, Temperature, RelativeHumidity |

### Step-by-step instructions for using the **Calibration** provider (OpenAQ example)

**Step 1:** Find all sensors in California for a given date using the `sensor_data` endpoint.

 https://insitu-api.stcenter.net/sensor_data?sensor_type=openaq_clarity&provider=Clarity-GMU-Cal&date=2025-01-01&variable=pm2_5&min_lon=-124.41&max_lon=-114.13&min_lat=32.53&max_lat=42.01

**Step 2:** Fetch measurements with the `activities` endpoint. Use the `platform_id` values returned in Step 1 as the `sensor_ids`.

 https://insitu-api.stcenter.net/activities?sensor_type=openaq_clarity&provider=Clarity-GMU-Cal&sensor_ids=947168&sd=2025-01-01&ed=2025-01-08

##
## Raw Provider Endpoints

| Endpoint    | Required Parameters                                   | Optional Parameters                          | Defaults                        | Constraints                                                                 |
|-------------|-------------------------------------------------------|-----------------------------------------------|---------------------------------|----------------------------------------------------------------------------|
| sensor_data | date, min_lon, max_lon, min_lat, max_lat, provider    | variable (e.g., pm2_5, temperature, humidity) | variable: pm2_5 <br> sensor_type: purpleair | • For sensor_type=purpleair, data is available only up to 2023-10-17 03:00:00 |
| activities  | sensor_ids, sd (start date), provider                 | –                                             | sensor_type: purpleair          | • End date is not allowed  <br> • A maximum of 10 sensor_ids is allowed per request • For sensor_type=purpleair, data is available only up to 2023-10-17 03:00:00 |

Step 1: Find all sensors in Los Angeles for a given date using the sensor_data endpoint.

https://insitu-api.stcenter.net/sensor_data?sensor_type=purpleair&provider=PurpleAir-GMU-Raw&date=2023-01-01&variable=pm2_5&min_lon=-118.95&max_lon=-117.65&min_lat=32.75&max_lat=34.82

Step 2: Fetch measurements with the activities endpoint. Use the platform_id values returned in Step 1 as the sensor_ids.

https://insitu-api.stcenter.net/activities?sensor_type=purpleair&provider=PurpleAir-GMU-Raw&sensor_ids=83747,69031&sd=2023-01-01

----
## Statistics Metadata Endpoints

**statistics – used to query the number of available observations for a platform (sensor), along with metadata such as time coverage, location (lat/lon), observation counts, platform ID, platform short name, total observations, and measurement units.**


- If `sensor_type = openaq_clarity` → `provider = Clarity-GMU-Raw-Hourly` or `provider = Clarity-GMU-Intermediate` or `provider = Clarity-GMU-Cal`  
- If `sensor_type = purpleair` → `provider = PurpleAir-GMU-Raw` or `provider = PurpleAir-GMU-Raw-Hourly` or `provider = PurpleAir-GMU-Intermediate` or `provider = PurpleAir-GMU-Raw-Daily`  

### Request  

| Endpoint   | Required Parameters          | Optional Parameters              | Defaults     |
|------------|------------------------------|----------------------------------|--------------|
| statistics | provider | startTime, endTime                                | sensor_type: purpleair           | 


### Response

Each platform block includes:  
- lat  
- lon  
- min_datetime
- max_datetime  
- observation_counts  
- platform  
- platform_short_name  
- total  
- units  

### Sample Endpoints
----

#### OpenAQ Clarity (sensor_type = openaq_clarity)
----
**Provider: Clarity-GMU-Raw-Hourly**  
https://insitu-api.stcenter.net/statistics?sensor_type=openaq_clarity&provider=Clarity-GMU-Raw-Hourly

**Provider: Clarity-GMU-Intermediate**  
https://insitu-api.stcenter.net/statistics?sensor_type=openaq_clarity&provider=Clarity-GMU-Intermediate

**Provider: Clarity-GMU-Cal**  
https://insitu-api.stcenter.net/statistics?sensor_type=openaq_clarity&provider=Clarity-GMU-Cal  

----
#### PurpleAir (sensor_type = purpleair)
----
**Provider: PurpleAir-GMU-Raw**  
https://insitu-api.stcenter.net/statistics?sensor_type=purpleair&provider=PurpleAir-GMU-Raw&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z  

**Provider: PurpleAir-GMU-Raw-Hourly**  
https://insitu-api.stcenter.net/statistics?sensor_type=purpleair&provider=PurpleAir-GMU-Raw-Hourly&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z  

**Provider: PurpleAir-GMU-Intermediate**  
https://insitu-api.stcenter.net/statistics?sensor_type=purpleair&provider=PurpleAir-GMU-Intermediate&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z  

**Provider: PurpleAir-GMU-Raw-Daily**  
https://insitu-api.stcenter.net/statistics?sensor_type=purpleair&provider=PurpleAir-GMU-Raw-Daily&startTime=2022-07-01T00:00:00Z&endTime=2022-07-02T00:00:00Z  
