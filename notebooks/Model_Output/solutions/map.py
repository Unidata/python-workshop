import numpy as np

# Set up an NCSS query from thredds using siphon
query = ncss.query()
query.accept('netcdf4')
query.variables('Temperature_isobaric', 'Geopotential_height_isobaric')
query.vertical_level(50000)
now = datetime.utcnow()
query.time_range(now, now + timedelta(days=1))
query.lonlat_box(west=-110, east=-45, north=50, south=10)

# Download data using NCSS
data = ncss.get_data(query)
ds = xr.open_dataset(NetCDF4DataStore(data))

temp_var = ds.metpy.parse_cf('Temperature_isobaric')
height_var = ds.metpy.parse_cf('Geopotential_height_isobaric')
longitude = temp_var.metpy.x
latitude = temp_var.metpy.y
time_index = 0

# Plot using CartoPy and Matplotlib
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal())

contours = np.arange(5000, 6000, 80)
ax.pcolormesh(longitude, latitude, temp_var[time_index].squeeze(),
              transform=data_projection, zorder=0)
ax.contour(longitude, latitude, height_var[time_index].squeeze(), contours, colors='k',
           transform=data_projection, linewidths=2, zorder=1)
ax.set_title(temp_var.metpy.time[time_index].values)

# add some common geographic features
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.add_feature(cfeature.BORDERS)

# add some lat/lon gridlines
ax.gridlines()