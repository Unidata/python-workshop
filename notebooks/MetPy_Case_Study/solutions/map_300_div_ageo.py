fig, ax = create_map_background()

# Contour 1
clev300 = np.arange(0, 11000, 120)
cs2 = ax.contour(lon, lat, div_300 * 10**5, range(-10, 11, 2),
                 colors='grey', transform=dataproj)
plt.clabel(cs2, fontsize=10, inline=1, inline_spacing=4,
           fmt='%i', rightside_up=True, use_clabeltext=True)

# Contour 2
cs = ax.contour(lon, lat, hght_300, clev300, colors='k',
                linewidths=1.0, linestyles='solid', transform=dataproj)
plt.clabel(cs, fontsize=10, inline=1, inline_spacing=4,
           fmt='%i', rightside_up=True, use_clabeltext=True)

# Filled Contours
spd300 = np.arange(50, 250, 20)
cf = ax.contourf(lon, lat, wspd_300, spd300, cmap='BuPu',
                 transform=dataproj, zorder=0)
plt.colorbar(cf, orientation='horizontal', pad=0.0, aspect=50)

# Vector of 300-hPa Ageostrophic Wind Vectors
ax.quiver(lon, lat, uageo_300.m, vageo_300.m, regrid_shape=15,
          pivot='mid', transform=dataproj, zorder=10)

# Titles
plt.title('300-hPa Geopotential Heights, Divergence (1/s),\
          Wind Speed (kts), Ageostrophic Wind Vector (m/s)',
          loc='left')
plt.title('VALID: {}'.format(vtime), loc='right')

plt.tight_layout()
plt.show()
