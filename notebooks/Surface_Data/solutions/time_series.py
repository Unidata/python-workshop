# define the time range we are interested in
end_time = datetime(2017, 9, 12, 0)
start_time = end_time - timedelta(days=2)

# build the query
query = ncss.query()
query.lonlat_point(-155.1, 19.7)
query.time_range(start_time, end_time)
query.variables('altimeter_setting', 'temperature', 'dewpoint',
                'wind_direction', 'wind_speed')
query.accept('csv')

data = ncss.get_data(query)

station_id = data['station'][0].tostring()
station_id = station_id.decode('ascii')

time = [datetime.strptime(s.decode('ascii'), '%Y-%m-%dT%H:%M:%SZ') for s in data['time']]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(time, data['temperature'], color='tab:red')
ax.plot(time, data['dewpoint'], color='tab:green')

ax.set_title(f'Site: {station_id}      Date: {time[0]:%Y/%m/%d}')
ax.set_xlabel('Hour of day')
ax.set_ylabel('Temperature/Dewpoint')
ax.grid(True)

# Improve on the default ticking
locator = AutoDateLocator()
hoursFmt = DateFormatter('%H')
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(hoursFmt)