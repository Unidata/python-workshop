pressures = pd.Series([1012.1, 1010.6, 1008.8, 1011.2], index=['TOP', 'OUN', 'DEN', 'DAL'])
pressures.name = 'pressure'
pressures.index.name = 'station'
print(pressures[dewpoints < 15])
