# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-01-17
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Crop netcdf with xarray
# ----------------------------------------------------------------------------

import xarray
import rioxarray
import geopandas
from shapely.geometry import mapping

ncdf_file = r"C:/Users/ReSEC2021/Documents/ERA5_Reanalysis_SingleLevel_202012_Regridded_0.01x0.01.nc"
shp_file = r"C:/Users/ReSEC2021/Documents/GSL.shp"
xds = xarray.open_dataset(ncdf_file)

#xds = xds.rename(Longitude='lon', Latitude='lat')
xds = xds[['10m_u_component_of_wind','10m_v_component_of_wind','2m_temperature','snowfall','total_cloud_cover']].transpose('time', 'lat', 'lon')
xds.rio.set_spatial_dims(x_dim= "lon", y_dim= "lat", inplace=True)
xds.rio.write_crs("EPSG:4326", inplace=True)
geodf = geopandas.read_file(shp_file, crs="epsg:4326")

storage_path = r"C:/Users/ReSEC2021/Downloads/output_true.nc"

clipped = xds.rio.clip(geodf.geometry.apply(mapping), geodf.crs, drop = True)
clipped.to_netcdf(path=storage_path, mode='w', format="NETCDF4", group=None, engine="netcdf4", encoding=None, unlimited_dims=None, compute=True, invalid_netcdf=False)
