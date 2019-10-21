import matplotlib.pyplot as plt
fig = plt.figure()
ax= fig.add_subplot(111)
station_data.plot('Time', 'solar_radiation', ax=ax)
station_hourly_mean.plot('Time', 'solar_radiation', ax=ax)