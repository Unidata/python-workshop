fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

ax.add_feature(cfeat.COASTLINE)
ax.add_feature(cfeat.LAND, facecolor='tab:brown')
ax.add_feature(cfeat.OCEAN, facecolor='tab:cyan')
ax.add_feature(cfeat.BORDERS, linewidth=2)
ax.add_feature(state_borders, linestyle="--", edgecolor='black')

ax.plot(-101.877, 33.583, marker='o', color='tab:green', transform=ccrs.PlateCarree())

ax.set_extent([-108, -93, 25, 37])
