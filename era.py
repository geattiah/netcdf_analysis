import xarray
import rioxarray
import geopandas
from shapely.geometry import mapping

ncdf_file = r"C:/Users/ReSEC2021/Documents/ERA5_Reanalysis_SingleLevel_202011.nc"
#shp_file = r"C:/Users/ReSEC2021/Downloads/Lake_Erie/Lake_Erie.shp"
xds = xarray.open_dataset(ncdf_file)

xds = xds.rename(longitude='lon', latitude='lat')
xds = xds[['sf', 't2m','tcc','u10','v10']].transpose('time', 'lat', 'lon')
xds.rio.set_spatial_dims(x_dim= "lon", y_dim= "lat", inplace=True)
#xds.rio.write_crs("EPSG:4326", inplace=True)
#geodf = geopandas.read_file(shp_file, crs="epsg:4326")

storage_path = r"C:/Users/ReSEC2021/Downloads/era.nc"

#clipped = xds.rio.clip(geodf.geometry.apply(mapping), geodf.crs, drop = True)
xds.to_netcdf(path=storage_path, mode='w', format="NETCDF4", group=None, engine="netcdf4", encoding=None, unlimited_dims=None, compute=True, invalid_netcdf=False)
