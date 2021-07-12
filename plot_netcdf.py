# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-05-11
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Extract values, perform mathematical equations from netcdf to csv
# ----------------------------------------------------------------------------

import os
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import csv

csv_direct =  "C:/Users/ReSEC2021/Downloads"

folder = "C:/Users/ReSEC2021/Downloads/net"

with open(os.path.join(csv_direct,'stats')+".csv", 'w', newline = '') as table:
    writer = csv.writer(table)
    writer.writerow(['Date','Max_thickness','Min_thickness','Mean_thickness','Difference', 'Percentage'])

    for file in sorted(os.listdir(folder)) :
        if file.endswith('.nc'):
            dat= os.path.join(folder,file)
            print(dat)
        
            data = Dataset(dat)
        
            lats = data.variables['lat'][:]
            lons = data.variables['lon'][:]
            years = data.variables['year'][:]
            di = data.variables['Di'][:]

            di_max = np.max(di)
            di_min = np.min(di)
            di_mean = np.mean(di)
            dif = di_max - di_min
            cnt_all = np.count_nonzero(di>-0.1)
            cnt_part = np.count_nonzero(di>0)
            per = (cnt_part/cnt_all)*100

            print(di_max)
            print(di_min)
            print(di_mean)
            print(dif)
            print(per)

            writer.writerow([file[:-3],di_max, di_min, di_mean, dif, per])

