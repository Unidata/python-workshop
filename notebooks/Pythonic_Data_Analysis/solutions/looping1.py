linestyles = {'wind_speed': '-', 'wind_gust': '--', 'pressure': '-'}

fig, axes = plt.subplots(1, len(plot_variables), sharex=True, figsize=(18, 6))

for ax, var_names in zip(axes, plot_variables):

    for var_name in var_names:
        # Grab the color from our dictionary and pass it to plot()
        color = colors[var_name]
        linestyle = linestyles[var_name]
        ax.plot(df.time, df[var_name], color, linestyle=linestyle)

    ax.set_ylabel(var_name)
    ax.set_title(f'Buoy {var_name}')

    ax.grid(True)
    ax.set_xlabel('Time')
    ax.xaxis.set_major_formatter(DateFormatter('%m/%d'))
    ax.xaxis.set_major_locator(DayLocator())
