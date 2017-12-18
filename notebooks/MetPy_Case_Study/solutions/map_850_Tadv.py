fig, ax = create_map_background()

# Contour 1 - Temperature, dotted
cs2 = ax.contour(lon, lat, tmpk_850.to('degC'), range(-50, 50, 2),
                 colors='grey', linestyles='dotted', transform=dataproj)

plt.clabel(cs2, fontsize=10, inline=1, inline_spacing=10, fmt='%i',
           rightside_up=True, use_clabeltext=True)

# Contour 2
clev850 = np.arange(0, 4000, 30)
cs = ax.contour(lon, lat, hght_850, clev850, colors='k',
                linewidths=1.0, linestyles='solid', transform=dataproj)

plt.clabel(cs, fontsize=10, inline=1, inline_spacing=10, fmt='%i',
           rightside_up=True, use_clabeltext=True)

# Filled contours - Temperature advection
contours = [-3, -2.2, -2, -1.5, -1, -0.5, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
cf = ax.contourf(lon, lat, tmpc_adv_850*3600, contours,
                 cmap='bwr', extend='both', transform=dataproj)
plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50,
             extendrect=True, ticks=contours)

# Vector
ax.barbs(lon, lat, uwnd_850.to('kts').m, vwnd_850.to('kts').m,
         regrid_shape=15, transform=dataproj)

# Titles
plt.title('850-hPa Geopotential Heights, Temperature (C), \
          Temp Adv (C/h), and Wind Barbs (kts)', loc='left')
plt.title('VALID: {}'.format(vtime), loc='right')

plt.tight_layout()
plt.show()
