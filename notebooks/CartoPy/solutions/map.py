fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())

ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, facecolor='tab:brown')
ax.add_feature(cfeature.OCEAN, facecolor='tab:cyan')
ax.add_feature(cfeature.BORDERS, linewidth=2)
ax.add_feature(cfeature.STATES, linestyle='--', edgecolor='black')


ax.plot(-101.877, 33.583, marker='o', color='tab:green', transform=ccrs.PlateCarree())


ax.set_extent([-108, -93, 25, 37])