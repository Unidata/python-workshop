bounds = {'Wind': (0, 30),
          'Pressure': (975, 1015)}

type_styles = {'Pressure': dict(color='black'),
               'Wind': dict(linestyle='-')}


variable_styles = {'pressure': dict(),
                   'wind_speed': dict(color='tab:orange', linewidth=2),
                   'wind_gust': dict(color='tab:olive', linewidth=0.5)}


fig, axes = plt.subplots(len(buoys), len(plot_variables), sharex=True, figsize=(14, 10))


for row, buoy in enumerate(buoys):
    df = read_buoy_data(buoy)
    for col, var_names in enumerate(plot_variables):
        ax = axes[row, col]
        for var_name in var_names:
            title, label = format_varname(var_name)
            style = type_styles[title].copy()  # So the next line doesn't change the original
            style.update(variable_styles[var_name])
            ax.plot(df.time, df[var_name], **style)
            ax.set_ylim(bounds[title])


    ax.set_ylabel(title)
    ax.set_title('Buoy {} {}'.format(buoy, title))

    ax.grid(True)
    ax.set_xlabel('Time')
    ax.xaxis.set_major_formatter(DateFormatter('%m/%d'))
    ax.xaxis.set_major_locator(DayLocator())
