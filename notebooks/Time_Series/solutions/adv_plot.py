myfig, myax = plt.subplots(figsize=(10, 6))
myaxb = myax.twinx()

# Same as above
myax.set_xlabel('Time')
myax.set_ylabel('Wave Height (m)')
myax.set_title('Buoy Data')
myax.grid(True)

# Plotting on the first y-axis
myax.plot(df.time, df.wave_height, color='tab:blue', label='Waveheight (m)',
        linestyle='None', marker='o')

# Plotting on the second y-axis
myaxb.set_ylabel('Windspeed (m/s)')
myaxb.plot(df.time, df.wind_speed, color='tab:green', label='Windspeed (m/s)')

myax.xaxis.set_major_locator(DayLocator())
myax.xaxis.set_major_formatter(DateFormatter('%b %d'))

# Handling of getting lines and labels from all axes for a single legend
mylines, mylabels = myax.get_legend_handles_labels()
mylines2, mylabels2 = myaxb.get_legend_handles_labels()
myax.legend(mylines + mylines2, mylabels + mylabels2, loc='upper left');
