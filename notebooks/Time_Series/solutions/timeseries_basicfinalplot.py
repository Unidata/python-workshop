fig, ax = plt.subplots(figsize=(10, 6))
axb = ax.twinx()

# Same as above
ax.set_xlabel('Time')
ax.set_ylabel('Wave Height')
ax.set_title('Buoy 41056 Data')
ax.grid(True)
ax.legend(loc='upper left')

# Plotting on the first y-axis
ax.plot(df.time, df.wave_height, color='tab:blue', label='Waveheight',
        linestyle='None', marker='o')

# Plotting on the second y-axis
axb.set_ylabel('Windspeed')
axb.plot(df.time, df.wind_speed, color='tab:green', label='Windspeed')

ax.xaxis.set_major_locator(DayLocator())
ax.xaxis.set_major_formatter(DateFormatter('%b %d'))

# Handling of getting lines and labels from all axes for a single legend
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = axb.get_legend_handles_labels()
axb.legend(lines + lines2, labels + labels2, loc='upper left')