# use __init__.py to setup the namespace
# for example, the follwing will allow for users to
#  access functions in util.py by doing the following:
#
# import pytds
#
# pytds.util.get_latest_dods_url(dataset_url)
#
import util
#
# If you would rather have the namespace like this:
#
# pytds.get_latest_dods_url(dataset_url)
#
# then you would need to remove
#
# import util
#
# and use
#
# from util import *

