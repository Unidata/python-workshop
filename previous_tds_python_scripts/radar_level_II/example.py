import string
import numpy as np
import matplotlib as mpl
from pydap.client import open_url
from xml.dom import minidom as md
import matplotlib.pyplot as plt
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
site = "KBRO"
date = "20130611"
variable = "Reflectivity"
scan = 0
#
# get latest data url
#
latest_data_url = get_latest_data_url(site,date)

# open url using pydap
dataset = open_url(latest_data_url)

# get some basic info from the global metadata
global_attrs = dataset.attributes['NC_GLOBAL']
lat = global_attrs["StationLatitude"]
lon = global_attrs["StationLongitude"]
station_id = global_attrs["StationName"]

# get data array and metadata
data = dataset["Reflectivity"][scan,::].squeeze()
theta = dataset["azimuthR"][scan,::].squeeze()
r = dataset["distanceR"][:]
data_attrs = dataset["Reflectivity"].attributes

# check for scale and offset
if data_attrs.has_key("scale_factor"):
    data = data * data_attrs["scale_factor"]

if data_attrs.has_key("add_offset"):
    data = data + data_attrs["add_offset"]

data = np.ma.masked_array(data, data < 5)

print("number of radials: {}".format(r.shape[0],))
print("number of azimuth angles: {}".format(theta.shape[0],))
print("dimensions of data: ({}, {})".format(data.shape[0],data.shape[1]))

theta = theta * np.pi / 180.
r = r / 1000.
x = np.array((np.matrix(np.cos(theta)).transpose() * np.matrix(r)))
y = np.array((np.matrix(np.sin(theta)).transpose() * np.matrix(r)))

cmap = radar_colormap()
norm = mpl.colors.Normalize(vmin=-35, vmax=80)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(0, 0, '+')
cax = ax.pcolormesh(y,x,data, cmap=cmap, norm=norm)
ax.set_xlim(-200,200)
ax.set_ylim(-200,200)
cbar = fig.colorbar(cax)
plt.show()
