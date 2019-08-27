# 700-hPa Temperature Advection
tadv_700 = mpcalc.advection(tmpk_700s, (uwnd_700s, vwnd_700s), (dx, dy)).to_base_units()
# Laplacian of Temperature Advection
lap_tadv_700 = mpcalc.laplacian(tadv_700, deltas=(dy, dx))

# Final term B calculation with constants
term_B = (-Rd / (sigma * (700 * units.hPa)) * lap_tadv_700).to_base_units()
print(term_B.units)