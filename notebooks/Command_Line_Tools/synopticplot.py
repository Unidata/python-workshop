# synopticplot.py - A simple synoptic plotting tool to plot visible satellite
# and GFS model data together.

import argparse
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import netCDF4
import numpy as np
import urllib.request

from datetime import datetime, timedelta
from matplotlib import patheffects
from metpy.cbook import get_test_data
from metpy.io import GiniFile
from metpy.plots import ctables
import scipy.ndimage as ndimage
from siphon.catalog import TDSCatalog
from siphon.ncss import NCSS


def get_closest_gfs(time, level, field):
    """
    Retreive the current best 0.25 deg GFS model for a given field, level, time.

    time : datetime object
    level : level of results (in hPa)
    field : CF field to retrieve
    """

    # Get the catalog and best GFS entry
    catalog = TDSCatalog('http://thredds.ucar.edu/thredds/catalog/grib/NCEP/GFS/Global_0p25deg/catalog.xml')
    best_gfs = list(catalog.datasets.values())[1]

    # Using NCSS, build a query and getch the data
    ncss = NCSS(best_gfs.access_urls['NetcdfSubset'])
    query = ncss.query()
    query.lonlat_box(north=90, south=10, east=360, west=160)
    query.vertical_level(level)
    query.time(time)
    query.accept('netcdf4')
    query.variables(field)
    data = ncss.get_data(query)

    # Pull out the variables we will use
    lat_var = data.variables['lat']
    lon_var = data.variables['lon']
    data_var = data.variables[field]

    # Find the correct time dimension name
    for coord in data_var.coordinates.split():
        if 'time' in coord:
            time_var = data.variables[coord]
            break

    # Convert number of hours since the reference time into an actual date
    time_vals = netCDF4.num2date(time_var[:].squeeze(), time_var.units)

    # Combine 1D latitude and longitudes into a 2D grid of locations
    lon_2d, lat_2d = np.meshgrid(lon_var[:], lat_var[:])

    # Filter the data to smooth it out a bit
    data_var = ndimage.gaussian_filter(data_var[:][0][0], sigma=1.5, order=0)

    return time_vals, lat_2d, lon_2d, data_var


def get_closest_satellite_vis(time):
    """
    Get the super national 8 km visible satellite image. The image closest to
    the requested time will be returned.

    time : datetime object of image
    """

    catalog = TDSCatalog('http://thredds.ucar.edu/thredds/catalog/satellite/VIS/'
                         'SUPER-NATIONAL_8km/current/catalog.xml')

    # Figure out the closest image to the requested time in the catalog
    datasets = list(catalog.datasets)
    dt_stamps = []
    for dataset in datasets:
        fmt = 'SUPER-NATIONAL_8km_VIS_%Y%m%d_%H%M.gini'
        dt_stamps.append(datetime.strptime(dataset, fmt))
    closest_time = min(dt_stamps, key=lambda x: abs(x - time))
    index = dt_stamps.index(closest_time)

    # Request that image and convert it to a netCDF like dataset
    satellite = list(catalog.datasets.values())[index]
    sat_data = GiniFile(urllib.request.urlopen(satellite.access_urls['HTTPServer']))
    ds = sat_data.to_dataset()

    # Pull out the variables we need
    x = ds.variables['x'][:]
    y = ds.variables['y'][:]
    channel_data = ds.variables['Visible']
    time_var = ds.variables['time']
    proj_var = ds.variables[channel_data.grid_mapping]

    # Make a globe and projection for this dataset
    globe = ccrs.Globe(ellipse='sphere', semimajor_axis=proj_var.earth_radius,
                       semiminor_axis=proj_var.earth_radius)

    proj = ccrs.Stereographic(central_longitude=proj_var.straight_vertical_longitude_from_pole,
                          central_latitude=proj_var.latitude_of_projection_origin,
                         true_scale_latitude=proj_var.standard_parallel, globe=globe)

    timestamp = netCDF4.num2date(time_var[:].squeeze(), time_var.units)
    return timestamp, globe, proj, x, y, channel_data


def make_basemap(proj):
    """
    Create a simple map with country, state, and province borders.

    proj: Cartopy projection to build map with
    """
    # Make state boundaries feature
    states_provinces = cfeature.NaturalEarthFeature(category='cultural',
                                                    name='admin_1_states_provinces_lakes',
                                                    scale='50m', facecolor='none')

    # Make country borders feature
    country_borders = cfeature.NaturalEarthFeature(category='cultural',
                                                   name='admin_0_countries',
                                                   scale='50m', facecolor='none')

    fig = plt.figure(figsize=(10.5, 7))
    ax = fig.add_subplot(1, 1, 1, projection=proj)
    ax.coastlines('50m', edgecolor='black', linewidth=0.5, zorder=-100)
    ax.add_feature(states_provinces, edgecolor='black', linewidth=0.5)
    ax.add_feature(country_borders, edgecolor='black', linewidth=0.5)

    return fig, ax


if __name__ == '__main__':

    # Parse out the command line arguments
    parser = argparse.ArgumentParser(description='''Make a combination map of
                                     visible satellite imagery with the
                                     corresponding GFS forecast timestep from
                                     the most recent quarter degree run.''')
    parser.add_argument('--gfsfield', default='Geopotential_height_isobaric',
                        help='CF field name of data to contour from the GFS model.')
    parser.add_argument('--gfslevel', default=500, type=int,
                        help='Model level to plot (in hPa)')
    parser.add_argument('--hours', default=0,
                        help='Time to plot (must be present or past)', type=int)
    parser.add_argument('--savefig', action='store_true',
                        help='Save out figure instead of displaying it')
    parser.add_argument('--imgformat', default='png',
                        help='Format to save the resulting image as.')
    args = parser.parse_args()
    args.gfslevel *= 100  # Model expects pressure level in Pa

    # Determine the time of interest
    requested_time = datetime.utcnow() - timedelta(hours=args.hours)

    # Go get satellite data
    (satellite_time, satellite_globe, satellite_proj, satellite_x,
     satellite_y, satellite_data) = get_closest_satellite_vis(requested_time)

    # Go get GFS data
    gfs_time, gfs_lat_grid, gfs_lon_grid, gfs_data_grid = get_closest_gfs(requested_time, args.gfslevel, args.gfsfield)
    fig, ax = make_basemap(satellite_proj)

    # Plot the satellite image
    im = ax.imshow(satellite_data[:], zorder=0, cmap='Greys_r',
                   extent=(satellite_x.min(), satellite_x.max(),
                   satellite_y.min(), satellite_y.max()), origin='upper')

    # Contour the GFS data
    c = ax.contour(gfs_lon_grid, gfs_lat_grid, gfs_data_grid, colors='C3',
                   lw=2, transform=ccrs.PlateCarree())

    plt.clabel(c, fontsize=14, inline=1, inline_spacing=1, fmt='%i', rightside_up=True)

    # Set the limits of the plot to match the bounding box of the vis sat
    ax.set_xlim(satellite_x.min(), satellite_x.max())
    ax.set_ylim(satellite_y.min(), satellite_y.max())

    # Add text of satellite image time
    text = ax.text(0.99, 0.01, satellite_time.strftime('Satellite: %d %B %Y %H%MZ'),
                   horizontalalignment='right', transform=ax.transAxes,
                   color='white', fontsize='x-large', weight='bold')
    text.set_path_effects([patheffects.Stroke(linewidth=2, foreground='black'),
                           patheffects.Normal()])

    # Add text of GFS data time
    text_gfs = ax.text(0.99, 0.04, gfs_time.strftime('GFS: %d %B %Y %H%MZ'),
                       horizontalalignment='right', transform=ax.transAxes,
                       color='white', fontsize='x-large', weight='bold')
    text_gfs.set_path_effects([patheffects.Stroke(linewidth=2, foreground='black'),
                              patheffects.Normal()])

    # Help reduce whitespace around figure
    fig.tight_layout()

    # Save or show figure
    if args.savefig:
        plt.savefig('{}.{}'.format(datetime.strftime(requested_time, '%Y%m%d_%H%MZ'),
                    args.imgformat))
    else:
        plt.show()
