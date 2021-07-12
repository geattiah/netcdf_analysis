# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2020-10-07
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# crop netcdf data based on shapefile and plot
# ----------------------------------------------------------------------------

import geopandas
import rioxarray
import xarray
import matplotlib.pyplot as plt
from shapely.geometry import mapping
import numpy as np
from mpl_toolkits.basemap import Basemap



grace_netcdf = xarray.open_dataset('/home/gift/grace_1.nc')
grace_netcdf.rio.set_spatial_dims(x_dim="lon", y_dim="lat", inplace=True)
grace_netcdf.rio.write_crs("epsg:4326", inplace=True)
grace_shape = geopandas.read_file("/home/gift/Downloads/Sel_lakes/Grace_Lake.shp")

clipped = grace_netcdf.rio.clip(grace_shape.geometry.apply(mapping), grace_shape.crs, drop=False)


pr = clipped.variables['Di'][0]
 
# show the precipitation
#plt.imshow(pr)
#plt.show()
# get the longitude information
lons = clipped.variables['lon'][:]
# get the latitude information
lats = clipped.variables['lat'][:]
#plt.imshow(clipped)
#plt.show()
mp = Basemap(projection='merc',
             llcrnrlon=-114.9,   # lower longitude
             llcrnrlat=62.1,    # lower latitude
             urcrnrlon=-114.1,   # uppper longitude
             urcrnrlat=62.8,   # uppper latitude
            resolution = 'i')


lon, lat = np.meshgrid(lons,lats)  #this converts coordinates into 2D arrray
x,y = mp(lon,lat) #mapping them together
plt.figure(figsize=(6,8)) #figure size
c_scheme = mp.pcolor(x,y,np.squeeze(clipped[0,:,:]),cmap = 'jet') # [0,:,:] is for t$

# consider this as the outline for the map that is to be created
mp.drawcoastlines()
mp.drawstates()
mp.drawcountries()
cbar = mp.colorbar(c_scheme,location='right',pad = '10%') # map information
plt.title('Average Temperature for: Day 1 of year 2019')
plt.show()




