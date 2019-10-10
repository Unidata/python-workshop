xy = proj.transform_points(ccrs.PlateCarree(), tx_one_time['Long'].values, tx_one_time['Lat'].values)
tx_mask = mpcalc.reduce_point_density(xy, 50000)

#Plot

# Set up a plot with map features
fig = plt.figure(figsize=(12, 12))
proj = ccrs.Stereographic(central_longitude=-100, central_latitude=35)
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.add_feature(cfeature.STATES.with_scale('50m'), edgecolor='black')
ax.gridlines()

# Create a station plot pointing to an Axes to draw on as well as the location of points
stationplot = StationPlot(ax, ok_data['LON'].values[ok_mask], ok_data['LAT'].values[ok_mask], transform=ccrs.PlateCarree(),
                          fontsize=10)
stationplot.plot_parameter('NW', ok_data['TAIR'][ok_mask], color='red')
stationplot.plot_parameter('SW', ok_dewpoint[ok_mask], color='green')
stationplot.plot_barb(ok_u[ok_mask], ok_v[ok_mask])

# Texas Data
stationplot = StationPlot(ax, tx_one_time['Long'].values[tx_mask], tx_one_time['Lat'].values[tx_mask], transform=ccrs.PlateCarree(),
                          fontsize=10)
stationplot.plot_parameter('NW', tx_one_time['2m_temperature'][tx_mask], color='red')
stationplot.plot_parameter('SW', tx_one_time['dewpoint'][tx_mask], color='green')
stationplot.plot_barb(tx_u[tx_mask], tx_v[tx_mask])