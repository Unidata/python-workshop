fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal(central_longitude=-100))
ax.coastlines()

levels = np.arange(300, 1000, 25)
cntr = ax.contour(lon, lat, isen_press, transform=ccrs.PlateCarree(), colors='black', levels=levels)
ax.clabel(cntr, fmt='%.0f')

lon_slice = slice(None, None, 5)
lat_slice = slice(None, None, 5)
ax.barbs(lon[lon_slice], lat[lat_slice],
         isen_u[lon_slice, lat_slice].to('knots').magnitude,
         isen_v[lon_slice, lat_slice].to('knots').magnitude,
         transform=ccrs.PlateCarree(), zorder=2)

levels = np.arange(-6, 7)
cs = ax.contourf(lon, lat, lift.to('microbar/s'), levels=levels, cmap='RdBu',
                 transform=ccrs.PlateCarree(), extend='both')
plt.colorbar(cs)

ax.set_extent((-120, -70, 25, 55), crs=ccrs.PlateCarree())
