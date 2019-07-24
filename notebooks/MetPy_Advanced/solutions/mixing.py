# Needed to make numpy broadcasting work between 1D pressure and other 3D arrays
# Use .metpy.unit_array to get numpy array with units rather than xarray DataArray
pressure_for_calc = press.metpy.unit_array[:, None, None]  

# Calculate mixing ratio using something from mpcalc
mixing = mpcalc.mixing_ratio_from_relative_humidity(rh, temperature, pressure_for_calc)


# Take the return and convert manually to units of 'dimenionless'
mixing.ito('dimensionless')


# Interpolate all the data
isen_level = np.array([295]) * units.kelvin
ret = mpcalc.isentropic_interpolation(isen_level, press, temperature, mixing, u, v)
isen_press, isen_mixing, isen_u, isen_v = ret


# Squeeze the returned arrays
isen_press = isen_press.squeeze()
isen_mixing = isen_mixing.squeeze()
isen_u = isen_u.squeeze()
isen_v = isen_v.squeeze()


# Create Plot -- same as before
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.LambertConformal(central_longitude=-100))

levels = np.arange(300, 1000, 25)
cntr = ax.contour(lon, lat, isen_press, transform=data_proj,
                  colors='black', levels=levels)
cntr.clabel(fmt='%d')


lon_slice = slice(None, None, 8)
lat_slice = slice(None, None, 8)
ax.barbs(lon[lon_slice], lat[lat_slice],
         isen_u[lat_slice, lon_slice].to('knots').magnitude,
         isen_v[lat_slice, lon_slice].to('knots').magnitude,
         transform=data_proj, zorder=2)


# Contourf the mixing ratio values
mixing_levels = [0.001, 0.002, 0.004, 0.006, 0.010, 0.012, 0.014, 0.016, 0.020]
ax.contourf(lon, lat, isen_mixing, transform=data_proj,
            levels=mixing_levels, cmap='YlGn')


ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linewidth=2)
ax.add_feature(cfeature.STATES, linestyle=':')


ax.set_extent((-120, -70, 25, 55), crs=data_proj)
