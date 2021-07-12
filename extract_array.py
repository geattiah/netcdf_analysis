# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-02-19
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Unravelling latlong of netcdf file test code
# ----------------------------------------------------------------------------

# Standard Library imports
import os
import sys
import glob

# Additional Dependencies
import numpy as np
import datetime as dt
from netCDF4 import Dataset

ERARef = r"C:/Users/ReSEC2021/Downloads/mx_ex.nc"

tmpera = Dataset(ERARef)
eralon = tmpera.variables['lon'][:]
eralat = tmpera.variables['lat'][:]
#mixval = tmpera.variables['md'][:,:,:]

lon, lat = np.meshgrid(eralon,eralat, sparse = False, indexing ='xy')
#print(lon)

ext =  tmpera.variables['md'][238:(240+1),335:(337+1)].ravel()
print(ext)
one = [1,2,3,4,5,6]
ten = [10,20,30,40,50,60]

tog = list(zip(one,ten))
print(tog)

dat = dict(zip(tog,ext))
print(dat)

k = dat[1,10]
print(k)

#lo =lon.ravel()
#print(lo)


#la =lat.ravel()

#z = np.array(list(zip(lon.ravel(), lat.ravel())))

#print(y)
#lo = [row[0] for row in z]
#print(lo)

#print(z)

#extract =  tmpera.variables['md']

#mix = mixval.ravel()
#m= np.mean(mix)
#print(m)
#print(mix)[2200:2500]

#print(mixval)

#d = np.array(list(zip(eralon.ravel(), eralat.ravel(), mixval.ravel())))

#print(d)