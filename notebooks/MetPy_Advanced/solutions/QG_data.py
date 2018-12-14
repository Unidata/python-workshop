# Remaining variables needed to compute QG Omega forcing terms
hght_500 = (ds.Geopotential_height_isobaric.sel({lev_name:500,
                                                time_name:'{:%Y-%m-%d}'.format(dt)}).values
            * units(ds.Geopotential_height_isobaric.units))
uwnd_500 = (ds['u-component_of_wind_isobaric'].sel({lev_name:500,
                                                   time_name:'{:%Y-%m-%d}'.format(dt)}).values
            * units(ds['u-component_of_wind_isobaric'].units))
vwnd_500 = (ds['v-component_of_wind_isobaric'].sel({lev_name:500,
                                                   time_name:'{:%Y-%m-%d}'.format(dt)}).values
            * units(ds['v-component_of_wind_isobaric'].units))
uwnd_900 = (ds['u-component_of_wind_isobaric'].sel({lev_name:900,
                                                   time_name:'{:%Y-%m-%d}'.format(dt)}).values
            * units(ds['u-component_of_wind_isobaric'].units))
vwnd_900 = (ds['v-component_of_wind_isobaric'].sel({lev_name:900,
                                                   time_name:'{:%Y-%m-%d}'.format(dt)}).values
            * units(ds['v-component_of_wind_isobaric'].units))