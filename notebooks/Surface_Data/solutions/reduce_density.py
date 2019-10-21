# Use reduce_point_density
mask = mpcalc.reduce_point_density(xy, 75000)

# Set up a plot with map features
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.add_feature(cfeature.STATES, edgecolor='black')
ax.coastlines(resolution='50m')
ax.gridlines()

# Create a station plot pointing to an Axes to draw on as well as the location of points
stationplot = StationPlot(ax, lons[mask], lats[mask], transform=ccrs.PlateCarree(),
                          fontsize=12)
stationplot.plot_parameter('NW', tair[mask], color='tab:red')
stationplot.plot_barb(u[mask], v[mask])
stationplot.plot_symbol('C', cloud_cover[mask], sky_cover)

# Plot dewpoint
stationplot.plot_parameter('SW', dewp[mask], color='tab:green')

# Plot altimeter setting
stationplot.plot_parameter('NE', alt[mask], color='tab:blue',
                           formatter=lambda v: str(int(v * 10))[-3:])

# Plot station id
stationplot.plot_text((2, 0), stid[mask])