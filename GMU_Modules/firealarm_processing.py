import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


API = "https://insitu-api.stcenter.net"
COUNTIES_ENDPOINT = f"{API}/list/countiesByState"
SENSOR_ENDPOINT = f"{API}/sensor_data"



def retrieve_bounding_box(state, county):
    PARAMS = {'state': state}

    request = requests.get(url = COUNTIES_ENDPOINT, params = PARAMS, verify=False)

    counties_data = request.json()
    
    for i in range(len(counties_data)):
        if counties_data[i]['county_name'].lower() == county.lower():
            return counties_data[i]['bounding_box']
        
    return 'Error: County or state not found.'

def retrieve_sensors(bounding_box, date):
    provider = 'PurpleAir-GMU-Raw-Hourly'
    PARAMS = {'date': date, 'min_lon': bounding_box['minx'], 'min_lat': bounding_box['miny'],
              'max_lon': bounding_box['maxx'], 'max_lat': bounding_box['maxy'], 'provider': provider}

    request = requests.get(url = SENSOR_ENDPOINT, params = PARAMS, verify=False)
    sensor_data = request.json()
    return sensor_data
