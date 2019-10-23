# Starting data
pressure = np.array([1000, 850, 500, 300])
temps = np.linspace(20, 30, 24).reshape(4, 3, 2)

temps * np.exp(pressure[:, np.newaxis, np.newaxis] / 1000)
