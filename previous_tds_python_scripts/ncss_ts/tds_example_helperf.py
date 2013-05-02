__all__ = ['get_zip_dict', 'convert_date', 'strip_date',
           'get_latest_nam12_url', 'k_to_f']

def get_zip_dict():
    '''
    Open data file with lat, lon, city, state, and zip code
    information and return a dict with zipcode as the key
    '''
    zips_f = open('./resources/zipcode.csv', 'r')
    zip_data = zips_f.readlines()
    zips_f.close()
    # pop off header
    zip_data.pop(0)
    zip_dict = {}
    for line in zip_data:
        if line != '\n':
            tmp = line.replace('"','').split(',')
            info_dict = {'lat' : float(tmp[3]),
                         'lon' : float(tmp[4]),
                         'state' : tmp[2].replace(' ',''),
                         'city' : tmp[1].replace(' ' ,'')}

            zip_dict[tmp[0]] = info_dict

    del info_dict, tmp, zip_data
    return zip_dict

def convert_date(x):
    '''
    Convert date from contained in datafile to an iso date, and
    return a datetime object.
    '''
    import datetime as dt
    print(x);
    return dt.datetime.strptime(str(x).split('.')[0],
                                "%Y-%m-%dT%H:%M:%SZ")

def strip_date(x):
    '''
    A method to skip reading the date string from the datafile
    by simply returning -999 for that column of information.
    '''
    return -999

def get_latest_nam12_url(kind = 'grid'):
    ''''
    This function is used to retrieve the url on the motherlode
    THREDDS server for the latest NAM12 model run.

    Parameters
    ----------
    kind : string
        A string that describes the type of data the user wishes to
        retrieve. Must be 'grid' or 'point'

    Returns
    -------
    data_url : string
        The URL that points to the datafile using the ncss service
        (kind = 'point') or the DoDS (kind = 'grid') protocol.
    '''
    import urllib2

    base_data_url = "http://motherlode.ucar.edu/thredds/catalog/fmrc/NCEP/RAP/CONUS_13km/files/latest.html"

    ava_data = urllib2.urlopen(base_data_url)

    data_links = []
    for line in ava_data:
        if '<a href' in line:
            data_links.append(line)

    ava_data.close()

    latest_data = data_links[0].split("'")[1]

    base_url = base_data_url.replace('/catalog/',
                    '/ncss/grid/').replace('latest.html','')

    data_file_name = latest_data.split('/')[-1]

    data_url = base_url + data_file_name

    if kind == 'grid':
        data_url = data_url.replace('ncss','dodsC').replace('/grid','')

    return data_url

def k_to_f(x):
    '''
    Convert an array of temperatures with units K to an array of
    temperatures with units of F.

    Parameters
    ----------
    x : ndarray
        Numpy array of temperatures in K

    Returns
    -------
    f : ndarray
        Numpy array of temperatures in F
    '''
    f = 9./5.*(x - 273.) + 32.
    return f
