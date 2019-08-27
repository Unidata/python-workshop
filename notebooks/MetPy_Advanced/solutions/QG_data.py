# Remaining variables needed to compute QG Omega forcing terms
hght_500 = ds.Geopotential_height_isobaric.metpy.sel(vertical=500 * units.hPa,
                                                     time=vtime)
uwnd_500 = ds['u-component_of_wind_isobaric'].metpy.sel(vertical=500 * units.hPa,
                                                        time=vtime)
vwnd_500 = ds['v-component_of_wind_isobaric'].metpy.sel(vertical=500 * units.hPa,
                                                        time=vtime)
uwnd_900 = ds['u-component_of_wind_isobaric'].metpy.sel(vertical=900 * units.hPa,
                                                        time=vtime)
vwnd_900 = ds['v-component_of_wind_isobaric'].metpy.sel(vertical=900 * units.hPa,
                                                        time=vtime)