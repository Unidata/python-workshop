fig=plt.figure(1, figsize=(15.,12.))

# Upper-Left Panel
ax=plt.subplot(111,projection=plotproj)
ax.set_extent([-125.,-73,25.,50.],ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.STATES,linewidth=0.5)

# Contour #1
cs = ax.contour(lons, lats, hght_700s, clev_hght_700,colors='k',
                linewidths=1.5, linestyles='solid', transform=dataproj)
plt.clabel(cs, fontsize=10, inline=1, inline_spacing=3, fmt='%i',
           rightside_up=True, use_clabeltext=True)

# Contour #2
cs2 = ax.contour(lons, lats, tmpc_700s, clev_tmpc_700, colors='grey',
                linewidths=1.0, linestyles='dotted', transform=dataproj)
plt.clabel(cs2, fontsize=10, inline=1, inline_spacing=3, fmt='%d',
           rightside_up=True, use_clabeltext=True)

# Colorfill
cf = ax.contourf(lons, lats, (term_A+term_B)*10**12, clev_omega,
                 cmap=plt.cm.RdYlBu_r, extend='both', transform=dataproj)
plt.colorbar(cf, orientation='horizontal', pad=0.0, aspect=50, extendrect=True)

# Vector
ax.barbs(lons.m, lats.m, uwnd_700s.to('kts').m, vwnd_700s.to('kts').m,
         regrid_shape=15, transform=dataproj)

# Titles
plt.title('700-hPa Geopotential Heights, Temperature (C),\n'
          'Winds (kt), and QG Omega Forcings ($*10^{12}$ kg m$^{-3}$ s$^{-3}$)',loc='left')
plt.title('VALID: ' + vtime_str, loc='right')

plt.show()
