df.temperature = df.temperature.round()
df.groupby('temperature').count()
