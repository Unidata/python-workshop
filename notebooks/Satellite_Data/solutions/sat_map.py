fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=proj)

# Plot the data using imshow
ax.imshow(dat, origin='upper',
          extent=(x.min(), x.max(), y.min(), y.max()))

# Add country borders and states (use your favorite linestyle!)
ax.add_feature(cfeature.BORDERS, linewidth=2, edgecolor='black')
ax.add_feature(cfeature.STATES, linestyle=':', edgecolor='black')

# Bonus/Daily Double
timestamp = datetime.strptime(ds.start_date_time, '%Y%j%H%M%S')
add_timestamp(ax, timestamp, pretext='GOES-16 Ch.{} '.format(channel),
              high_contrast=True, fontsize=16, y=0.01)
