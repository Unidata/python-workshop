df = pd.read_fwf(fname, skiprows=2, na_values='MM', names=col_names)

df['time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']])

# Using inplace means the return is None and the dataframe is simply modified.
df.drop(['year', 'month', 'day', 'hour', 'minute'], axis='columns', inplace=True)

df.head()