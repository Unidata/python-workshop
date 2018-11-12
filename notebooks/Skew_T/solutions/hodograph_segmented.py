# Create figure/axis
fig, ax = plt.subplots(1, 1, figsize=(6, 6))

# Create a hodograph object/fiducial lines
h = Hodograph(ax, component_range=60.)
h.add_grid(increment=20)

# Plot the data
l = h.plot_colormapped(sounding['u_wind'],
                       sounding['v_wind'],
                       sounding['height_agl'],
                       bounds=boundaries, colors=colors)

# BONUS - add a colorbar
plt.colorbar(l)
