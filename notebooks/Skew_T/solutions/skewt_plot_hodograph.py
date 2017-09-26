fig = plt.figure(figsize=(3, 3))
h = Hodograph()
h.plot_colormapped(u[mask], v[mask], windspeed[mask])  # Plot a line colored by wind speed
h.add_grid(increment=20)