fig, ax = create_map_background()

# Contour 1
clev500 = np.arange(0, 7000, 60)
cs = ax.contour(lon, lat, hght_500, clev500, colors='k',
                linewidths=1.0, linestyles='solid', transform=dataproj)
plt.clabel(cs, fontsize=10, inline=1, inline_spacing=4,
           fmt='%i', rightside_up=True, use_clabeltext=True)

# Filled contours
# Set contour intervals for Absolute Vorticity
clevavor500 = [-4, -3, -2, -1, 0, 7, 10, 13, 16, 19,
               22, 25, 28, 31, 34, 37, 40, 43, 46]

# Set colorfill colors for absolute vorticity
# purple negative
# yellow to orange positive
colorsavor500 = ('#660066', '#660099', '#6600CC', '#6600FF',
                 '#FFFFFF', '#ffE800', '#ffD800', '#ffC800',
                 '#ffB800', '#ffA800', '#ff9800', '#ff8800',
                 '#ff7800', '#ff6800', '#ff5800', '#ff5000',
                 '#ff4000', '#ff3000')

cf = ax.contourf(lon, lat, avor_500 * 10**5, clevavor500,
                 colors=colorsavor500, transform=dataproj)
plt.colorbar(cf, orientation='horizontal', pad=0, aspect=50)

# Vector
ax.barbs(lon, lat, uwnd_500.to('kts').m, vwnd_500.to('kts').m,
         regrid_shape=15, transform=dataproj)

# Titles
plt.title('500-hPa Geopotential Heights, Absolute Vorticity \
          (1/s), and Wind Barbs (kts)', loc='left')
plt.title('VALID: {}'.format(vtime), loc='right')

plt.tight_layout()
plt.show()
