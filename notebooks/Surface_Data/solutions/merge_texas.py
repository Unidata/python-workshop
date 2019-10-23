# Find common time between TX and OK data
tx_data = pd.merge(tx_data, tx_stations, left_on='Station_ID', right_on='Logger ID')
tx_one_time = tx_data[tx_data['Time'] == '2019-3-22 23:00']
tx_one_time