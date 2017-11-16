def read_buoy_data(fname):
    """Handy function to read and cleanup the buoy data files."""
    col_names = ['year', 'month', 'day', 'hour', 'minute', 'wind_direction', 'wind_speed',
             'wind_gust', 'wave_height', 'dominant_wave_period', 'average_wave_period',
             'dominant_wave_direction', 'pressure', 'temperature', 'water_temperature', 'dewpoint',
             'visibility', '3hr_pressure_tendency', 'water_level_above_mean']
    
    widths = [4, 3, 3, 3, 3, 4, 5, 5, 6, 6, 6, 4, 7, 6, 6, 6, 5, 5, 6]
    
    df = pd.read_fwf(fname, skiprows=2, na_values='MM', names=col_names, widths=widths)

    df['time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']])

    # Using inplace means the return is None and the dataframe is simply modified.
    df.drop(['year', 'month', 'day', 'hour', 'minute'], axis='columns', inplace=True)
    
    idx = (df.time >= datetime(2017, 9, 6)) & (df.time <= datetime(2017, 9, 8))
    df = df[idx]
    
    df.reset_index(drop=True, inplace=True)
    
    return df


files = ['41056.txt', '41052.txt']

fig, axes = plt.subplots(len(files), len(plot_variables), sharex=True, figsize=(14, 10))

for row, filename in enumerate(files):
    df = read_buoy_data(filename)
    

    for col, var_names in enumerate(plot_variables):
        ax = axes[row,col]
        for var_name in var_names:
            title, label = format_varname(var_name)
            color = colors[var_name]
            linestyle = linestyles[var_name]
            ax.plot(df.time, df[var_name], color, linestyle=linestyle, label=label)

        ax.set_ylabel(title)
        ax.set_title('Buoy {} {}'.format(filename.split('.')[0], title))

        ax.grid(True)
        ax.set_xlabel('Time')
        ax.xaxis.set_major_formatter(DateFormatter('%m/%d'))
        ax.xaxis.set_major_locator(DayLocator())