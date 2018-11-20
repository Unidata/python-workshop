# Calculate surface based cape/cin
surface_cape, surface_cin = mpcalc.surface_based_cape_cin(sounding['pressure'],
                                                          sounding['temperature'],
                                                          sounding['dewpoint'])

# Print CAPE and CIN
print('CAPE: {}\tCIN: {}'.format(surface_cape, surface_cin))

# Shade CAPE
skew.shade_cape(sounding['pressure'],
                sounding['temperature'],
                sounding['profile'])

# Shade CIN
skew.shade_cin(sounding['pressure'],
               sounding['temperature'],
               sounding['profile'])

# Redisplay the figure
fig
