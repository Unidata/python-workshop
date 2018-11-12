# Make a figure
fig = plt.figure(figsize=(10, 10))

# Make a SkewT object
skew = SkewT(fig)

# Plot the temperature and dewpoint
skew.plot(sounding['pressure'], sounding['temperature'], linewidth=2, color='tab:red')
skew.plot(sounding['pressure'], sounding['dewpoint'], linewidth=2, color='tab:green')
