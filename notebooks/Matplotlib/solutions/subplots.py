fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 2, 1)

# Specify how our lines should look
ax.plot(times, temps, color='tab:red', label='Temperature (surface)')
ax.plot(times, temps_1000, color='tab:red', linestyle=':',
        label='Temperature (isobaric level)')

# Same as above
ax.set_xlabel('Time')
ax.set_ylabel('Temperature')
ax.set_title('Temperature Forecast')
ax.grid(True)
ax.legend(loc='upper left')

ax2 = fig.add_subplot(1, 2, 2, sharex=ax, sharey=ax)
ax2.plot(times, dewpoint, color='tab:green', label='Dewpoint (surface)')
ax2.plot(times, dewpoint_1000, color='tab:green', linestyle=':', marker='o',
         label='Dewpoint (isobaric level)')

ax2.set_xlabel('Time')
ax2.set_ylabel('Dewpoint')
ax2.set_title('Dewpoint Forecast')
ax2.grid(True)
ax2.legend(loc='upper left')
ax2.set_ylim(257, 312)
ax2.set_xlim(95, 162)
