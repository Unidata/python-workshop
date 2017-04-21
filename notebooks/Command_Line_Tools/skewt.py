# skewt.py - A simple Skew-T plotting tool

import argparse
from datetime import datetime

import matplotlib.pyplot as plt
import metpy.calc as mpcalc
from metpy.io.upperair import get_upper_air_data
from metpy.plots import Hodograph, SkewT
from metpy.units import units
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpldatacursor import datacursor
import numpy as np

def get_sounding_data(date, station):

    ds = get_upper_air_data(date, station)

    p = ds.variables['pressure'][:]
    T = ds.variables['temperature'][:]
    Td = ds.variables['dewpoint'][:]
    u = ds.variables['u_wind'][:]
    v = ds.variables['v_wind'][:]
    windspeed = ds.variables['speed'][:]

    return p, T, Td, u, v, windspeed

def plot_sounding(date, station):
    p, T, Td, u, v, windspeed = get_sounding_data(date, station)

    lcl_pressure, lcl_temperature = mpcalc.lcl(p[0], T[0], Td[0])
    lfc_pressure, lfc_temperature = mpcalc.lfc(p, T, Td)
    parcel_path = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')

    # Create a new figure. The dimensions here give a good aspect ratio
    fig = plt.figure(figsize=(8, 8))
    skew = SkewT(fig)

    # Plot the data
    skew.plot(p, T, color='tab:red')
    skew.plot(p, Td, color='tab:green')

    # Plot thermodynamic parameters and parcel path
    skew.plot(p, parcel_path, color='black')

    if lcl_pressure:
        skew.ax.axhline(lcl_pressure, color='black')

    if lfc_pressure:
        skew.ax.axhline(lfc_pressure, color='0.7')

    # Add the relevant special lines
    skew.ax.axvline(0, color='c', linestyle='--', linewidth=2)
    skew.plot_dry_adiabats()
    skew.plot_moist_adiabats()
    skew.plot_mixing_lines()

    # Shade areas representing CAPE and CIN
    skew.shade_cin(p, T, parcel_path)
    skew.shade_cape(p, T, parcel_path)

    # Add wind barbs
    skew.plot_barbs(p, u, v)

    # Add an axes to the plot
    ax_hod = inset_axes(skew.ax, '30%', '30%', loc=1, borderpad=3)

    # Plot the hodograph
    h = Hodograph(ax_hod, component_range=100.)

    # Grid the hodograph
    h.add_grid(increment=20)

    # Plot the data on the hodograph
    mask = (p >= 100 * units.mbar)
    h.plot_colormapped(u[mask], v[mask], windspeed[mask])  # Plot a line colored by wind speed

    # Set some sensible axis limits
    skew.ax.set_ylim(1000, 100)
    skew.ax.set_xlim(-40, 60)

    return fig, skew

if __name__ == '__main__':
    # Parse out the command line arguments
    parser = argparse.ArgumentParser(description='''Make an advanced SkewT
                                     plot of upper air observations.''')
    parser.add_argument('--date', required=True,
                        help='Date of the sounding YYYYMMDD')
    parser.add_argument('--hour', required=True,
                        help='Time of the sounding in hours')
    parser.add_argument('--station', default='OUN',
                        help='Station three letter identifier')
    parser.add_argument('--savefig', action='store_true',
                        help='Save out figure instead of displaying it')
    parser.add_argument('--imgformat', default='png',
                        help='Format to save the resulting image as.')
    args = parser.parse_args()

    # Parse out the date time stamp
    date = datetime.strptime('{0}{1}'.format(args.date, args.hour), '%Y%m%d%H')

    # Make the sounding figure
    fig, skew = plot_sounding(date, args.station)

    # Save or show figurexs
    if args.savefig:
        plt.savefig('{0}_{1}.{2}'.format(args.station,
                                        datetime.strftime(date, '%Y%m%d_%HZ'),
                                        args.imgformat))
    else:
        datacursor(formatter=u'{y:.02f} hPa \n{x:.02f}\u00B0C'.format, bbox=dict(fc='white'))
        plt.show()
