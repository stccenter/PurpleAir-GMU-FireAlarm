import requests
import urllib3
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime
from collections import defaultdict
import numpy as np

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API = "https://insitu-api.stcenter.net"
COUNTIES_ENDPOINT = f"{API}/list/countiesByState"
SENSOR_ENDPOINT = f"{API}/sensor_data"
ACTIVITIES_ENDPOINT = f"{API}/activities"

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

def retrieve_sensor_readings(date: list, sensor_ids: list, provider='PurpleAir-GMU-Raw-Hourly'):
    PARAMS = {'sd': date[0], 'ed': date[1], 'sensor_ids': ','.join([str(id) for id in sensor_ids]), 'provider': provider}
    
    request = requests.get(url = ACTIVITIES_ENDPOINT, params = PARAMS, verify=False).json()['observations']
    sensor_readings = {}

    for entry in request:
        platform_id = entry["platform_id"]
        
        date = datetime.strptime(entry["date"], '%Y-%m-%dT%H:%M:%SZ')

        if platform_id not in sensor_readings:
            # If not, initialize a new list of lists for this platform_id
            sensor_readings[platform_id] = [[], []]

        sensor_readings[platform_id][0].append(date)
        sensor_readings[platform_id][1].append(entry["pm2_5"])

    return sensor_readings
