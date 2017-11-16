import numpy as np

# Set up an NCSS query from thredds using siphon
query = ncss.query()
query.accept('netcdf4')
query.variables('Temperature_isobaric', 'Geopotential_height_isobaric')
query.vertical_level(50000)
query.time_range(datetime(2017, 9, 5), datetime(2017, 9, 6))
query.lonlat_box(west=-110, east=-45, north=50, south=10)

# Download data using NCSS
data = ncss.get_data(query)

longitude = data.variables['longitude'][:]
latitude = data.variables['latitude'][:]
temp_var = data.variables['Temperature_isobaric']
height_var = data.variables['Geopotential_height_isobaric']

# Find the correct time dimension name
for coord in ncvar.coordinates.split():
    if 'time' in coord:
        timevar = data.variables[coord]
        break
time = num2date(timevar[:], timevar.units)

data_projection = ccrs.PlateCarree()
time_index = 0

# Plot using CartoPy and Matplotlib
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal())

contours = np.arange(5000, 6000, 80)
ax.pcolormesh(longitude, latitude, temp_var[time_index].squeeze(),
              transform=data_projection, zorder=0)
ax.contour(longitude, latitude, height_var[time_index].squeeze(), contours, colors='k',
           transform=data_projection, linewidths=2, zorder=1)
ax.set_title(time[time_index])

# add some common geographic features
ax.coastlines(resolution='10m', color='black', zorder=1)
ax.add_feature(states_provinces, edgecolor='black', zorder=1)
ax.add_feature(cfeat.BORDERS)

# add some lat/lon gridlines
ax.gridlines()
