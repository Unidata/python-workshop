print(df.groupby('station').temperature.min())
print(df.groupby('station').temperature.max())
print(df.groupby('station').temperature.std())
