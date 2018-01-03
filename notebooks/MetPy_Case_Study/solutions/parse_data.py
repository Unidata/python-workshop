# Extract data and assign units
tmpk = gaussian_filter(data.variables['Temperature'][0], sigma=1.0) * units.K
hght = gaussian_filter(data.variables['Geopotential_height'][0],
                       sigma=1.0) * units.meter
uwnd = gaussian_filter(data.variables['u_wind'][0], sigma=1.0) * units('m/s')
vwnd = gaussian_filter(data.variables['v_wind'][0], sigma=1.0) * units('m/s')

# Extract coordinate data for plotting
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
lev = data.variables['isobaric'][:]
