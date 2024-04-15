from datetime import datetime
from typing import List, Tuple
from matplotlib import dates
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import cartopy.crs as ccrs
import cartopy.feature as cf
from cartopy.io.img_tiles import OSM
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER
import numpy as np
import matplotlib.patches as mpatches


def basemap(ax=None, padding: float = 2.5, bounds: dict = {}):
    # Define the projection (Plate Carree in this case)
    projection = ccrs.PlateCarree()

    # Initialize a matplotlib figure
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={
                            'projection': projection})

    bounds = (bounds['minx'] - padding,
              bounds['maxx'] + padding,
              bounds['miny'] - padding,
              bounds['maxy'] + padding)

    osm_tiles = OSM()
    ax.add_image(osm_tiles, 8)

    ax.set_extent([-10, 10, 45, 55])
    ax.coastlines('10m')
    return ax


def map_points(points: List, title='', zoom=False, bounds=None, legend=True):
    '''
    Plots lat lon points on map
    points: list of tuples (lat, lon, label)
    '''
    ax = basemap(bounds=bounds)
    ax.scatter([p[1] for p in points], [p[0] for p in points],
               s=10, c='red', zorder=1000, label='PurpleAir Sensor')

    for p in points:
        ax.text(p[1], p[0], f'SID: {p[2]}', fontsize=9)

    ax.set_title(title)

    ax.legend().set_zorder(102)
    ax.set_xlim(bounds['minx'], bounds['maxx'])
    ax.set_ylim(bounds['miny'], bounds['maxy'])

    return ax


def plot_sensor_readings(sensor_readings: dict, focus_range=None):
    ax = plt.gca()

    for sensor_id, sensor_values in sensor_readings.items():
        dates = sensor_values[0]
        pm2_5_values = sensor_values[1]
        ax.plot_date(dates, pm2_5_values, linestyle='solid',
                    label=f'Sensor {sensor_id}')
        
    if focus_range:
        ax.axvline(focus_range[0], color='blue', linestyle='--')
        ax.axvline(focus_range[1], color='blue', linestyle='--')

    very_unhealthy_min = 150
    unhealthy_min = 100
    moderate_min = 50
    good_max = 50

    # Add horizontal spans for different air quality levels
    ax.axhspan(very_unhealthy_min, ax.get_ylim()[1], color='purple', alpha=0.3, label='Very Unhealthy')
    ax.axhspan(unhealthy_min, very_unhealthy_min, color='red', alpha=0.3, label='Unhealthy')
    ax.axhspan(moderate_min, unhealthy_min, color='orange', alpha=0.3, label='Moderate')
    ax.axhspan(0, good_max, color='green', alpha=0.3, label='Good')
    plt.figure(figsize=(10, 15))
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel('Date')
    ax.set_ylabel('PM2.5: µg/m³')
    ax.set_title('PM2.5 Readings State / County [2022-07-01 to 2022-07-03]')
    plt.tight_layout()
    ax.legend()
    
    return ax

def plot_map_and_sensor_readings(sensor_readings: dict, points: List, title='', zoom=False, roads=True, bounds=None, legend=True):
    # Initialize a figure with 2 subplots
    fig = plt.figure(figsize=(10, 15))  # Increase figure size to ensure both plots fit

    # Create a GeoAxes for the map with the appropriate projection
    ax1 = fig.add_subplot(2, 1, 1, projection=ccrs.PlateCarree())
    basemap(bounds=bounds, ax=ax1)
    ax1.scatter([p[1] for p in points], [p[0] for p in points],
                s=10, c='red', zorder=1000, label='PurpleAir Sensor')

    for p in points:
        ax1.text(p[1], p[0], f'SID: {p[2]}', fontsize=9)

    ax1.legend().set_zorder(102)
    ax1.set_xlim(bounds['minx'], bounds['maxx'])
    ax1.set_ylim(bounds['miny'], bounds['maxy'])

    ax2 = fig.add_subplot(2, 1, 2)
    # Second subplot for the time series
    for sensor_id, sensor_values in sensor_readings.items():
        dates = sensor_values[0]
        pm2_5_values = sensor_values[1]
        ax2.plot_date(dates, pm2_5_values, linestyle='solid', label=f'Sensor {sensor_id}')

    very_unhealthy_min = 150
    unhealthy_min = 100
    moderate_min = 50
    good_max = 50

    # Add horizontal spans for different air quality levels
    ax2.axhspan(very_unhealthy_min, ax2.get_ylim()[1], color='purple', alpha=0.3, label='Very Unhealthy')
    ax2.axhspan(unhealthy_min, very_unhealthy_min, color='red', alpha=0.3, label='Unhealthy')
    ax2.axhspan(moderate_min, unhealthy_min, color='orange', alpha=0.3, label='Moderate')
    ax2.axhspan(0, good_max, color='green', alpha=0.3, label='Good')

    fig.autofmt_xdate()
    ax2.set_xlabel('Date')
    ax2.set_ylabel('PM2.5: µg/m³')
    ax2.set_title('PM2.5 Readings Over Time')
    ax2.legend()

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.4)
    plt.show()
