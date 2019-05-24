myfig, myax = plt.subplots(figsize=(10, 6))

# Plot temperature
myax.plot(df.time, df.air_temperature, color='tab:blue', linestyle='-.', label='Temperature')


myax.set_xlabel('Time')
myax.set_ylabel('Temperature (degC)')
myax.set_title('Buoy 41056 Data')
myax.grid(True)


# format x axis labels
myax.xaxis.set_major_locator(DayLocator())
myax.xaxis.set_major_formatter(DateFormatter('%b %d'))


myax.legend(loc='upper left');
fig
