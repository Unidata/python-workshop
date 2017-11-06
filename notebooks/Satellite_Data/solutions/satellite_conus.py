cat = TDSCatalog('http://thredds-test.unidata.ucar.edu/thredds/catalog/casestudies/irma/goes16/CONUS/Channel10/20170909/catalog.xml')
ds = cat.datasets.filter_time_nearest(datetime(2017, 9, 9, 6))
print(ds.name)
ds = ds.remote_access(service='OPENDAP')
timestamp = datetime.strptime(ds.start_date_time, '%Y%j%H%M%S')
data_var = ds.variables['Sectorized_CMI']

x = ds.variables['x'][:]
y = ds.variables['y'][:]
proj_var = ds.variables[data_var.grid_mapping]

# Create a Globe specifying a spherical earth with the correct radius
globe = ccrs.Globe(ellipse='sphere', semimajor_axis=proj_var.semi_major,
                   semiminor_axis=proj_var.semi_minor)

# Select the correct projection.

if proj_var.grid_mapping_name == 'lambert_conformal_conic':
   proj = ccrs.LambertConformal(central_longitude=proj_var.longitude_of_central_meridian,
                                central_latitude=proj_var.latitude_of_projection_origin,
                                standard_parallels=[proj_var.standard_parallel],
                                globe=globe)

else:
   proj = ccrs.Mercator(central_longitude=proj_var.longitude_of_projection_origin, 
                        latitude_true_scale=proj_var.standard_parallel,
                        globe=globe)

wv_norm, wv_cmap = registry.get_with_range('WVCIMSS_r', 195, 265)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=proj)

im = ax.imshow(data_var[:], extent=(x.min(), x.max(), y.min(), y.max()), origin='upper',
               cmap=wv_cmap, norm=wv_norm)
ax.coastlines(resolution='50m', color='black')
ax.add_feature(state_boundaries, linestyle=':', edgecolor='black')
ax.add_feature(cfeat.BORDERS, linewidth=2, edgecolor='black')

# Add text (aligned to the right); save the returned object so we can manipulate it.
text_time = ax.text(0.99, 0.01, timestamp.strftime('%d %B %Y %H%MZ'),
               horizontalalignment='right', transform=ax.transAxes,
               color='white', fontsize='x-large', weight='bold')

text_channel = ax.text(0.5, 0.97, 'Experimental GOES-16 Ch.{}'.format(channel),
               horizontalalignment='center', transform=ax.transAxes,
               color='white', fontsize='large', weight='bold')

outline_effect = [patheffects.withStroke(linewidth=2, foreground='black')]
text_time.set_path_effects(outline_effect)
text_channel.set_path_effects(outline_effect)

fig = add_metpy_logo(fig)