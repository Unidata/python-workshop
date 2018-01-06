# Vorticity and Absolute Vorticity Calculations

# Planetary Vorticity
f = mpcalc.coriolis_parameter(np.deg2rad(lat)).to('1/s')

# Relative Vorticity
vor_500 = mpcalc.vorticity(uwnd_500, vwnd_500, dx, dy,
                           dim_order='yx')

# Abosolute Vorticity
avor_500 = vor_500 + f
