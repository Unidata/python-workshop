import argparse
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from datetime import datetime
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import metpy.calc as mpcalc
from metpy.plots import add_timestamp, add_metpy_logo
import numpy as np
from siphon.simplewebservice.ndbc import NDBC
from metpy.units import units


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make a plot of buoy data.')
    parser.add_argument('--cmap', default='Oranges', help='mpl color map')
    parser.add_argument('--var', default='water_temperature', help='variable to plot')
    parser.add_argument('--savefig', action='store_true', help='save a figure instead of displaying')
    parser.add_argument('--imgformat', default='png', help='saved image foramt')
    parser.add_argument('--min', default=None, type=int, help='Minimum color bar bound.')
    parser.add_argument('--max', default=None, type=int, help='Maximum color bar bound.')
    parser.add_argument('--msize', default=5, type=int, help='Marker size')
    args = parser.parse_args()

    print('Downloading data...')
    df = NDBC.latest_observations()
    print(f'Complete. {len(df)} stations')
    print(df.columns)
    # Drop any rows with NaN for the data we want
    df.dropna(subset=[args.var], inplace=True)
    print(f'{len(df)} stations with variable {args.var}\nPlotting...')
    # Make an LCC map projection
    proj = ccrs.LambertConformal()

    # Plot the map
    fig = plt.figure(figsize=(12, 7))
    ax = plt.axes(projection=proj)
    ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
    ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    ax.add_feature(cfeature.LAND.with_scale('50m'))
    ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')
    ax.add_feature(cfeature.STATES.with_scale('50m'), linestyle=':')
    ax.add_feature(cfeature.LAKES.with_scale('50m'), alpha=0.5)
    ax.add_feature(cfeature.RIVERS.with_scale('50m'), alpha=0.5)

    add_timestamp(ax)
    add_metpy_logo(fig, x=300, y=350)

    scatter = ax.scatter(df.longitude, df.latitude,
                         c=df[args.var], transform=ccrs.PlateCarree(),
                         cmap=plt.get_cmap(args.cmap), vmin=args.min, vmax=args.max,
                         s=args.msize) # cm.Oranges or Use plt.get_cmap(str)

    plt.colorbar(scatter, orientation='horizontal',
                 label=args.var.replace('_', ' ').title(),
                 shrink=0.6, pad=0.05)

    #u, v = mpcalc.wind_components(df.wind_direction.values * units('m/s'), df.wind_direction.values * units.degrees)
    #x = df.longitude.values
    #y = df.latitude.values
    #ax.quiver(x, y, u.m, v.m, transform=ccrs.PlateCarree(), units='dots')

    # Save or show figurexs
    if args.savefig:
        plt.savefig('buoys_{dt:%Y%m%d_%H%MZ}.{ext}'.format(dt=datetime.utcnow(),
                                                           ext=args.imgformat))
    else:
        plt.show()
