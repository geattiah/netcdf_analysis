import os
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import csv

csv_direct =  "C:/Users/ReSEC2021/Downloads"

file_name = "C:/Users/ReSEC2021/Downloads/net/gsl/2003.05.14.nc"

with open(os.path.join(csv_direct,'phenolo-gsl')+".csv", 'w', newline = '') as table:
    writer = csv.writer(table)
    writer.writerow(['Year','Max_freezeup','Min_freezeup', 'Max_breakup','Min_breakup','Breakup_period','Freezeup_period'])

    c = -1
    year = 2002

    data = Dataset(file_name)

    lats = data.variables['lat'][:]
    lons = data.variables['lon'][:]
    years = data.variables['year'][:]
    bu = data.variables['Bu'][:]
    fu = data.variables['Fu'][:]
    
    for i in range(18):
        c = c + 1
        year = year + 1

        bu_y = bu[c,:]
        fu_y = fu[c,:]

        bu_max = np.max(bu_y)
        fu_max = np.max(fu_y)
        bu_min = np.min(bu_y)
        fu_min = np.min(fu_y)
        fu_p = fu_max - fu_min
        bu_p = bu_max - bu_min

        writer.writerow([year,fu_max, fu_min, bu_max, bu_min, bu_p, fu_p])

