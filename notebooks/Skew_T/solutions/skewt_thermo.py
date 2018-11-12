# Get data for the sounding
df = WyomingUpperAir.request_data(datetime(1999, 5, 3, 12), 'OUN')

# Calculate the ideal surface parcel path
sounding['profile'] = mpcalc.parcel_profile(sounding['pressure'],
                                            sounding['temperature'][0],
                                            sounding['dewpoint'][0]).to('degC')

# Calculate the LCL
lcl_pressure, _ = mpcalc.lcl(sounding['pressure'][0],
                             sounding['temperature'][0],
                             sounding['dewpoint'][0])

# Calculate the LFC
lfc_pressure, _ = mpcalc.lfc(sounding['pressure'],
                             sounding['temperature'],
                             sounding['dewpoint'])

# Calculate the EL
el_pressure, _ = mpcalc.el(sounding['pressure'],
                           sounding['temperature'],
                           sounding['dewpoint'])

# Create a new figure and SkewT object
fig = plt.figure(figsize=(10, 10))
skew = SkewT(fig)

# Plot the profile and data
skew.plot(sounding['pressure'], sounding['profile'], color='black')
skew.plot(sounding['pressure'], sounding['temperature'], color='tab:red')
skew.plot(sounding['pressure'], sounding['dewpoint'], color='tab:blue')

# Plot the LCL, LFC, and EL as horizontal lines
if lcl_pressure:
    skew.ax.axhline(lcl_pressure, color='tab:orange')
    
if lfc_pressure:
    skew.ax.axhline(lfc_pressure, color='tab:brown')
    
if el_pressure:
    skew.ax.axhline(el_pressure, color='tab:olive')

# Set axis limits
skew.ax.set_xlim(-60, 30)
skew.ax.set_ylim(1000, 100)

# Add fiducial lines
skew.plot_dry_adiabats()
skew.plot_moist_adiabats()
skew.plot_mixing_lines()
