import string
import numpy as np
import matplotlib as mpl
from pydap.client import open_url
from xml.dom import minidom as md
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import datetime as dt

def radar_colormap():
    nws_reflectivity_colors = [
    "#646464", # ND
    "#ccffff", # -30
    "#cc99cc", # -25
    "#996699", # -20
    "#663366", # -15
    "#cccc99", # -10
    "#999966", # -5
    "#646464", # 0
    "#04e9e7", # 5
    "#019ff4", # 10
    "#0300f4", # 15
    "#02fd02", # 20
    "#01c501", # 25
    "#008e00", # 30
    "#fdf802", # 35
    "#e5bc00", # 40
    "#fd9500", # 45
    "#fd0000", # 50
    "#d40000", # 55
    "#bc0000", # 60
    "#f800fd", # 65
    "#9854c6", # 70
    "#fdfdfd" # 75
    ]

    cmap = mpl.colors.ListedColormap(nws_reflectivity_colors)

    return cmap

def basic_http_request(full_url, return_response = False):
    #
    # just a basic http request
    #
    import urllib2

    url_request = urllib2.Request(full_url)
    #url_request.add_header('User-agent', "your user agent here")
    try:
        response = urllib2.urlopen(url_request)
        if return_response:
            return response
        else:
            del response
    except IOError, e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: {}'.format(e.reason)
            print 'Full  url: {}'.format(full_url)
            raise
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: {}'.format(e.code)
            print 'TDS response: {}'.format(e.read())
            print 'Full  url: {}'.format(full_url)
            raise
        else:
            print 'error not caught!'
            raise

def get_latest_data_url(site,date):
    #
    # Get the latest data for site and given day
    #
    # read the xml file, and figure out where latest.xml currently points
    #
    top_level_url = "http://thredds.ucar.edu/thredds"
    # base_url example http://thredds.ucar.edu/thredds/"catalog/nexrad/level2
    base_url = string.join([top_level_url, "catalog/nexrad/level2"],'/')

    # latest_xml_doc example http://thredds.ucar.edu/thredds/"catalog/nexrad/level2/KTLX/20130429/latest.xml
    latest_xml_doc = string.join([base_url, site, date, "latest.xml"],'/')

    xml_data = basic_http_request(latest_xml_doc, return_response = True)
    doc = md.parse(xml_data)
    root = doc.firstChild
    for cn in root.childNodes:
        if cn.nodeName == "dataset":
            dataset_url_path = cn.getAttribute("urlPath")

    latest_data_url = string.join([top_level_url, "dodsC", dataset_url_path], "/")

    return latest_data_url

# basic input
site = "KFTG"
variable = "Reflectivity"
scan = 0
#
# get latest data url
#
date = dt.date.today().strftime("%Y%m%d")
latest_data_url = get_latest_data_url(site,date)

# open url using pydap
dataset = open_url(latest_data_url)

# get some basic info from the global metadata
global_attrs = dataset.attributes['NC_GLOBAL']
station_lat = global_attrs["StationLatitude"]
station_lon = global_attrs["StationLongitude"]
station_id = global_attrs["StationName"]

# get data array and metadata
data = dataset[variable][scan,::].squeeze()
theta = dataset["azimuthR"][scan,::].squeeze()
tilt = dataset["elevationR"][scan,0]
r = dataset["distanceR"][:]
data_attrs = dataset[variable].attributes

# check for scale and offset
if data_attrs.has_key("scale_factor"):
    data = data * data_attrs["scale_factor"]

if data_attrs.has_key("add_offset"):
    data = data + data_attrs["add_offset"]

data = np.ma.masked_array(data, data < 5)

theta = theta * np.pi / 180.
d = r * np.cos(tilt * np.pi / 180.)
x = np.array((np.matrix(np.cos(theta)).transpose() * np.matrix(d)))
y = np.array((np.matrix(np.sin(theta)).transpose() * np.matrix(d)))
height = np.abs(x.min()) + np.abs(x.max())
width = np.abs(y.min()) + np.abs(y.max())
x = x + height / 2.
y = y + width / 2.

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

m=Basemap(lat_0=station_lat,lon_0=station_lon,resolution='l',projection='laea',height=height,width=width,ax=ax)

station_x, station_y = m(station_lon, station_lat)

cmap = radar_colormap()
norm = mpl.colors.Normalize(vmin=-35, vmax=80)

ax.text(station_x, station_y, "+{}".format(site))

cax = m.pcolormesh(y, x, data, cmap=cmap, norm=norm)
m.drawcoastlines()
m.drawstates()
m.drawcountries()
cbar = m.colorbar(cax)
cbar.set_label(data_attrs["units"])
ax.set_title(station_id)
plt.show()
