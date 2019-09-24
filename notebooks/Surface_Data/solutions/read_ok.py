ok_data = pd.read_csv('201903222300.mdf', skiprows=2, delim_whitespace=True, na_values=-999)
ok_stations = pd.read_csv('Oklahoma_stations.csv', usecols=[1,7,8])
print(ok_data.head())
print(ok_stations.head())