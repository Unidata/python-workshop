ok_dewpoint = mpcalc.dewpoint_rh(ok_data['TAIR'].values * units.degC, ok_data['RELH'].values * units.percent)
ok_u, ok_v = mpcalc.wind_components(ok_data['WSPD'].values * units.mph, ok_data['WDIR'].values * units.degrees)
tx_u, tx_v = mpcalc.wind_components(tx_one_time['10m_scalar_wind_speed'].values * units.mph, tx_one_time['10m_wind_direction'].values * units.degrees)