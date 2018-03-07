plot_variables = ['wind_speed', 'pressure']
plot_names = ['Windspeed', 'Atmospheric Pressure']

for var, name in zip(plot_variables, plot_names):
    print('Plotting variable', var, 'as', name)
