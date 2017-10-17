ax.plot(df.time, df.wind_gust, color='tab:olive', linestyle='--',
        label='Wind Gust')

ax.xaxis.set_major_formatter(DateFormatter('%b %d'))

ax.legend(loc='upper left')

fig