import xarray
import rioxarray
import geopandas
from shapely.geometry import mapping

ncdf_file = r"C:/Users/ReSEC2021/Documents/ERA5_Reanalysis_SingleLevel_202012_Regridded_0.01x0.01.nc"
shp_file = r"C:/Users/ReSEC2021/Documents/shapefiles/GreatBearLake.shp"
xds = xarray.open_dataset(ncdf_file)

xds = xds.rename(longitude='lon', latitude='lat')
xds = xds[['v10','u10','tcc','t2m','sf']].transpose('time', 'lat', 'lon')
xds.rio.set_spatial_dims(x_dim= "lon", y_dim= "lat", inplace=True)
xds.rio.write_crs("EPSG:4326", inplace=True)
geodf = geopandas.read_file(shp_file, crs="epsg:4326")

storage_path = r"C:/Users/ReSEC2021/Downloads/output_REG.nc"

clipped = xds.rio.clip(geodf.geometry.apply(mapping), geodf.crs, drop = True)
clipped.to_netcdf(path=storage_path, mode='w', format="NETCDF4", group=None, engine="netcdf4", encoding=None, unlimited_dims=None, compute=True, invalid_netcdf=False)
