type_styles = {'Pressure': dict(color='black'),
               'Wind': dict(linestyle='-')}

variable_styles = {'pressure': dict(),
                   'wind_speed': dict(color='tab:orange', linewidth=2),
                   'wind_gust': dict(color='tab:olive', linewidth=0.5)}

fig, axes = plt.subplots(1, len(plot_variables), sharex=True, figsize=(14, 5))

for col, var_names in enumerate(plot_variables):
    ax = axes[col]
    for var_name in var_names:
        title, label = format_varname(var_name)
        style = type_styles[title].copy()  # So the next line doesn't change the original
        style.update(variable_styles[var_name])
        ax.plot(df.time, df[var_name], **style)

    ax.set_ylabel(title)
    ax.set_title('Buoy 41056 {}'.format(title))

    ax.grid(True)
    ax.set_xlabel('Time')
    ax.xaxis.set_major_formatter(DateFormatter('%m/%d'))
    ax.xaxis.set_major_locator(DayLocator())
