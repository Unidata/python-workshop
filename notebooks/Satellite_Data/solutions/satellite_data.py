cat = TDSCatalog('http://thredds-test.unidata.ucar.edu/thredds/catalog/casestudies/irma/goes16/Mesoscale-1/Channel09/20170910/catalog.xml')
ds = cat.datasets.filter_time_nearest(datetime(2017, 9, 10, 0))
print(ds.name)
ds = ds.remote_access(service='OPENDAP')