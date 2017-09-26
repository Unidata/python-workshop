# Calculate the LFC and plot it if it exists
lfc_pressure, lfc_temperature = mpcalc.lfc(p, T, Td)

if lfc_pressure:
    skew.ax.axhline(lfc_pressure, color='tab:brown')
    
# Calculate the EL and plot it if it exists
el_pressure, el_temperature = mpcalc.el(p, T, Td)

if el_pressure:
    skew.ax.axhline(el_pressure, color='tab:blue')
    
fig