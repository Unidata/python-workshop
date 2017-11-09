from netCDF4 import num2date

# Load data
cat = TDSCatalog('http://thredds-test.unidata.ucar.edu/thredds/catalog/casestudies/irma/model/gfs/catalog.xml')
best_ds = cat.datasets['Best GFS Half Degree Forecast Time Series']

# Access the best dataset using the subset service and request data
ncss = best_ds.subset()

# Set up query
query = ncss.query().accept('netcdf4')
query.lonlat_box(west=-90, east=-55, south=15, north=30)
query.variables('Pressure_surface', 'Wind_speed_gust_surface')
query.time_range(datetime(2017, 9, 6, 12), datetime(2017, 9, 11, 12))

# Pull useful pieces out of nc
nc = ncss.get_data(query)
lon = nc.variables['longitude'][:]
lat = nc.variables['latitude'][:]
press = nc.variables['Pressure_surface']
winds = nc.variables['Wind_speed_gust_surface']
time_var = nc.variables['time1']
times = num2date(time_var[:], time_var.units)

# Create a figure for plotting
proj = ccrs.LambertConformal(central_longitude=-70)
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines()
add_metpy_logo(fig, x=15, y=15)

# Setup up the animation, looping over data to do the plotting that we want
pressure_levels = np.arange(95000, 105000, 800)
wind_levels = np.arange(0., 100., 10.)
artists = []

for press_slice, wind_slice, time in zip(press, winds, times):
    press_contour = ax.contour(lon, lat, press_slice, pressure_levels,
                               transform=ccrs.PlateCarree(), colors='black')
    wind_contour = ax.contour(lon, lat, wind_slice, wind_levels,
                              transform=ccrs.PlateCarree(), colors='blue')
    text = ax.text(0.5, 1.01, time, transform=ax.transAxes, ha='center')
    artists.append(press_contour.collections + wind_contour.collections + [text])

manimation.ArtistAnimation(fig, artists, interval=100)
