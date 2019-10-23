import matplotlib.pyplot as plt
fig = plt.figure()
ax= fig.add_subplot(111)
ax.plot(station_hourly_mean['Time'], station_hourly_mean['solar_radiation'])
ax.plot(station_data['Time'], station_data['solar_radiation'])