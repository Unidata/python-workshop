# Import the Iowa state simple web service upper air object
from siphon.simplewebservice.iastate import IAStateUpperAir

# Create the datetime and station variables you'll need
request_time = datetime(2011, 4, 14, 18)
station = 'OUN'

# Make the request for the data
df = IAStateUpperAir.request_data(request_time, station)

# Attach units to the data
sounding = pandas_dataframe_to_unit_arrays(df)
