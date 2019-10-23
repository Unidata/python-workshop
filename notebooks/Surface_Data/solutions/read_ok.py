ok_data = pd.read_csv('201903222300.mdf', skiprows=2, delim_whitespace=True, na_values=-999,
                                          parse_dates=[2], date_parser=partial(parse_ok_date, start_date=start_date))
ok_stations = pd.read_csv('Oklahoma_stations.csv', usecols=[1,7,8])
print(ok_data.head())
print(ok_stations.head())