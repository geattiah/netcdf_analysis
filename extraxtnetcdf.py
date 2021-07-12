# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-01-31
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Estracting netcdf file into a single one based on date 
# ----------------------------------------------------------------------------

import os
import xarray as xr
import rioxarray
import pandas as pd
import geopandas as gp
from shapely.geometry import mapping

ncdf_file = r"C:/Users/ReSEC2021/Documents/GSL-YZF_S-All_F-None_75p_2003-2016.nc"
folder = r"C:/Users/ReSEC2021/Documents/ncdata"
xds = xr.open_dataset(ncdf_file)

#dates, datasets = zip(*ds.resample(time='1D').mean('time').groupby('time'))
dates, datasets =  zip(*xds.groupby('date'))
filenames = [pd.to_datetime(date).strftime('%Y.%m.%d') + '.nc' for date in dates]
xr.save_mfdataset(datasets, os.path.join(folder,filenames))

