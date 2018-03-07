# Set up plot basics and use StationPlot class from MetPy to help with plotting
fig = plt.figure(figsize=(14, 8))
proj = ccrs.LambertConformal(central_latitude=50, central_longitude=-107)
ax = plt.subplot(111, projection=proj)
ax.coastlines('50m', edgecolor='grey', linewidth=0.75)
ax.add_feature(cfeature.STATES, edgecolor='grey', linewidth=0.5)

# Set up station plotting using only every third
# element from arrays for plotting
stationplot = StationPlot(ax, lon[::3, ::3].ravel()[mask],
                          lat[::3, ::3].ravel()[mask],
                          transform=ccrs.PlateCarree(), fontsize=12)

# Plot markers then data around marker for calculation purposes
ax.scatter(lon[::3, ::3].ravel()[mask], lat[::3, ::3].ravel()[mask],
           marker='o', transform=dataproj)
stationplot.plot_parameter((0, 1), hght_500[::3, ::3].ravel()[mask])
stationplot.plot_parameter((-1.5, -1), uwnd_500[::3, ::3].ravel()[mask],
                           formatter='.1f')
stationplot.plot_parameter((1.5, -1), vwnd_500[::3, ::3].ravel()[mask],
                           formatter='.1f')

# Title
plt.title('Geopotential (m; top), U-wind (m/s; Lower Left), \
          V-wind (m/s; Lower Right)')

plt.tight_layout()
plt.show()
