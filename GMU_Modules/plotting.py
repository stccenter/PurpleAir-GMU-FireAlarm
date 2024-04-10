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
import textwrap
import matplotlib.colors as colors

def basemap(padding: float = 2.5, bounds: dict = {}):
    # Define the projection (Plate Carree in this case)
    projection = ccrs.PlateCarree()

    # Initialize a matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': projection})

    bounds = (bounds['minx'] - padding,
                  bounds['maxx'] + padding,
                  bounds['miny'] - padding,
                  bounds['maxy'] + padding)
    
    osm_tiles = OSM()
    ax.add_image(osm_tiles, 8)

    ax.set_extent([-10, 10, 45, 55])
    ax.coastlines('10m')
    #ax.imshow(np.random.rand(4, 4), interpolation='spline16', cmap='viridis')
    return ax

def map_points(points: List, title='', zoom=False, roads=True, bounds=None, legend=True):
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

