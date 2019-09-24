# Find common time between TX and OK data
tx_data = tx_data[tx_data['Time'] == 2300]
tx_data = pd.merge(tx_data, tx_stations, left_on='Station_ID', right_on='Logger ID')
tx_data