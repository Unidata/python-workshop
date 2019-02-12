# Plot wind barbs
skew.plot_barbs(sounding['pressure'], sounding['u_wind'], sounding['v_wind'])

# Add dry adiabats
skew.plot_dry_adiabats()

# Add moist adiabats
skew.plot_moist_adiabats()

# Add mixing ratio lines
skew.plot_mixing_lines()

# Redisplay figure
fig
