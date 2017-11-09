cat = TDSCatalog('http://thredds-test.unidata.ucar.edu/thredds/catalog/'
                 'casestudies/irma/goes16/catalog.xml')
meso = cat.catalog_refs['Mesoscale-1'].follow()
channel = meso.catalog_refs['Channel02'].follow()
date_cat = channel.catalog_refs['20170906'].follow()

date = datetime(2017, 9, 6, 21)
datasets = date_cat.datasets.filter_time_range(date - timedelta(hours=1),
                                               date + timedelta(hours=1))
print(datasets)
