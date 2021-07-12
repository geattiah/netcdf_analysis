from netCDF4 import Dataset
import numpy as np
import pandas as pd
import os
import csv

csv_direct =  "C:/Users/ReSEC2021/Downloads"

directory = "C:/Users/ReSEC2021/Downloads/net/"

name = os.path.basename(os.path.normpath(directory))

with open(os.path.join(csv_direct,'comp')+".csv", 'w', newline = '') as table:
    writer = csv.writer(table)
    writer.writerow(['Date', 'Lat', 'Lon', 'Thickness'])
    
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            filepath = subdir + os.sep + filename
            # print(filepath)
            # Reading in the netCDF file
            data = Dataset(filepath, 'r')
            
            # Storing the chla_mean into the variables 
            time = data.variables['year'][:]
            lat = data.variables['lat'][:]
            lon = data.variables['lon'][:]
            di = data.variables['Di'][:]
            bu = data.variables['Bu'][:]
            fu = data.variables['Fu'][:]
            # Add more fields as needed.
             
            # Storing the lat and lon of in-situ station 1 into variables 
            lat_stat1 =  61.4
            lon_stat1 =  -114.7
                                    
            # Squared difference of lat and lon 
            sq_diff_lat = (lat - lat_stat1)**2
            sq_diff_lon = (lon - lon_stat1)**2
            
            # Identifying the index of the minimum value for lat and lon 
            min_index_lat = sq_diff_lat.argmin()
            min_index_lon = sq_diff_lon.argmin()
            
            # Extracting data from closest raster pixel
            di_value = di[min_index_lat][min_index_lon]
            #bu_value = bu[min_index_lat][min_index_lon]
            #fu_value = fu[min_index_lat][min_index_lon]
            
            # Extracted pixel coordinates
            pixel_lat = lat[min_index_lat]
            pixel_lon = lon[min_index_lon]
            
            # Adds data row to Excel time series file
            writer.writerow([name, pixel_lat, pixel_lon, di_value])
            
            
        
        
        
        
        
        
