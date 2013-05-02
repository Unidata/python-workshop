import os
import pytz
import urllib2
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from string import join
from matplotlib.dates import HourLocator, DateFormatter, date2num
from tds_example_helperf import get_zip_dict, convert_date, strip_date, \
                                get_latest_nam12_url, k_to_f

if __name__ == '__main__':
    '''

    This script uses the netCDF subservice feature of the THREDDS
    data server to extract the timeseries output from a single grid
    point in the latest NAM 12km run output. The grid point used
    is chosen such that it is the closest to the zipcode entered
    by the user.

    '''
    # prompt the user to input their 5 digit zipcode
    zipcode = str(raw_input("Please enter your 5 digit zipcode:"))

    print('\n...get lat, lon, city, and state info for zipcode {0}\n'.format(zipcode,))
    # get a dict that contains the zipcode info
    zip_dict = get_zip_dict()
    zip_info = zip_dict[str(zipcode)]

    # pull out the relevant info for the given zipcode
    lat = zip_info['lat']
    lon = zip_info['lon']
    city = zip_info['city']
    state = zip_info['state']

    print('...get the time series output for the grid point closest to zipcode {0}\n'.format(zipcode))
    # get the url of the latest NAM12 model run
    ncss_url = "http://motherlode.ucar.edu:9080/thredds/ncss/grid/grib/NCEP/SREF/CONUS_40km/ensprod_biasc/collection"
    start_time = dt.datetime.utcnow() - dt.timedelta(hours=12)
    # create string to request temperature data from the grid point
    #  closest to the given lat/long
    var_request = "var=Temperature_height_above_ground_weightedMean&var=Temperature_height_above_ground_stdDev"
    lat_lon_request = "latitude={0}&longitude={1}".format(lat,lon)
    #time_request = "time_start=2012-10-20T00:00:00.000Z&time_end=2012-10-24T00:00:00.000"
    time_request = "time_start={0}&time_duration=P3DT12H".format(start_time.strftime("%Y-%m-%dT%H"))
    return_type = "accept=csv&point=true"
    data_request_string = join([var_request,lat_lon_request,time_request,return_type], '&')
    print data_request_string
    #data_request_string = "?var=Temperature_height_above_ground_weightedMean&Temperature_height_above_ground_stdDev&latitude={0}&longitude={1}&temporal=all&accept=csv&point=true".format(lat,lon)
    #var=Temperature_height_above_ground_stdDev&var=Temperature_height_above_ground_weightedMean&latitude=40&longitude=-105&time_start=2012-10-20T00%3A00%3A00.000Z&time_end=2012-10-24T00%3A00%3A00.000Z&vertCoord=&accept=csv
    # Request the data and store them to a tmp file
    response = urllib2.urlopen(join([ncss_url, data_request_string], '?'))
    data_info = response.readlines()
    tmp_file = 'tmp.txt'
    f = open(tmp_file, 'w')
    for line in data_info:
        f.write(line)
    f.close()
    print('...load the data\n')
    # load the date/time info into an array of datetime objects
    date = np.loadtxt(tmp_file, skiprows=1, converters={0:convert_date},
                      delimiter=',',usecols=[0],dtype=np.object)
    # load in the temperature data
    data = np.loadtxt(tmp_file, skiprows=1, converters={0:strip_date},
                      delimiter=',')[:,3:]
    data[:,-1] = 9./5. * (data[:,-1])
    data[:,-2] = k_to_f(data[:,-2])

    # grab the current time in UTC and format it for use in plotting
    ctu = dt.datetime.now(tz=pytz.utc)
    ctime_for_plot = dt.datetime(ctu.year, ctu.month, ctu.day, ctu.hour)

    # setup plotting environment to work with dates on the x-axis
    hours = HourLocator(interval=6)

    # find the max and min of the Temperature data
    ymin = data[:,-2].min() -  2*data[:,-1].max()
    ymax = data[:,-2].max() + 2*data[:,-1].max()
    print('...create plot!\n')
    # plot the data
    fig = plt.figure()
    fig.subplots_adjust(bottom = 0.1)
    ax1 = fig.add_subplot(111)
    ax1.plot(date,data[:,-2],'r')
    # configure x-axis
    ax1.xaxis.set_major_locator(hours)
    ax1.xaxis.set_major_formatter(DateFormatter('%m/%d\n%HZ'))
    ax1.grid()
    # add a vertical line to indicate the current time and shade
    # the times that are in the past
    ax1.axvline(date2num(ctime_for_plot))
    ax1.fill_betweenx(np.array([ymin-2,ymax+2]),date[0],ctime_for_plot,color='k',alpha=0.5)
    bottom_bound = data[:,-2] - 2*data[:,-1]
    top_bound = data[:,-2] + 2*data[:,-1]
    ax1.fill_between(date, bottom_bound, top_bound,color='r',alpha=0.2)
    # set title
    ax1.set_title('2m Temp forecast using the SREF 40km (biasCorrected) Ensemble for {0}, {1}'.format(city, state))
    # set limits and labels for y-axis
    ax1.set_ylim((ymin-2,ymax+2))
    ax1.set_ylabel("Temperature (F)")
    plt.show()
    plt.close()
    print('...remove tmp datafile :-)\n')
    # remove the tmp datafile from the disk
    os.remove(tmp_file)
