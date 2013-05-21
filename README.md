tds-python-workshop
===================

This private repository contains notes and ipython notebooks in preparation for the TDS Python workshop.

# Workshop Outline

## Unidata Technology with Python
- What is Python?
- Why Unidata technology with Python?
- Language popularity measured by search hits on AMS [web site](https://ams.confex.com/ams/93Annual/webprogram/start.html#srch=words%7Cjava%7Cmethod%7Cand%7Cpge%7C2)
- Enthought Python Distribution (EPD)
- Outline of lectures
- Background reading material

## ipython notebook
- Starting IPython Notebook
- Notebook Cells
- Hello world
- Embedding Markdown
- Nice Errors
- Inline Documentation
- Tab Completion
- Plotting
- Interrupts
- LaTeX 
- Run Shell Commands with `!`
- Local or Remote Images and Even Videos
- Take Python Code and Display it in LaTeX (Wow!)
- Load External Codes
- Sharing

## netCDF File Exploration with Python and NumPy
- netcdf4-python
- Interactively Exploring a netCDF File
- NumPy
- List variables
- List the Dimensions
- Let's find out more about temperature.
- What is the sea surface temperature and salinity at 50N, 140W?
- Finding the latitude and longitude indices of 50N, 140W
- Now we have all the information we need to find our answer.
- What is the sea surface temperature and salinity at 50N, 140W?
- Closing your netCDF file

## Geoscience plotting with matplotlib
- Some Examples
- Plotting netCDF data
- Basic Plot
- Let's improve upon the plot into something that is more ready for publication.
- Matplotlib Basemap

## TODO
- Incorporate material from "AMS Short Course on Intermediate Python: Using NumPy, SciPy, and Matplotlib"
- Incorporate material from CU Python HPC class: <https://github.com/ResearchComputing/python_hpc>

## Study

- Checkout <http://sea.ucar.edu/event/arm-ncar-collaboration-lrose-and-py-art>
- Huge number of good examples: <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>
- numpy tutorial: <http://www.meetup.com/University-of-Colorado-Computational-Science-and-Engineering/files/>
- SciTools <http://www.scitools.org.uk/> <https://github.com/SciTools>
- http://nbviewer.ipython.org/4251308
- http://nbviewer.ipython.org/4740419
- http://nbviewer.ipython.org/5092905
- http://nbviewer.ipython.org/4113653
- http://nbviewer.ipython.org/5492513
- https://ams.confex.com/ams/93Annual/flvgateway.cgi/id/23312?recordingid=23312
- http://polar.ncep.noaa.gov/global/examples/usingpython.shtml
- http://matplotlib.org/basemap/users/examples.html
-  http://stackoverflow.com/questions/15432587/converting-netcdf-to-grib2

## Questions

Do we want to cover more about netcdf. In particular, how to create a netcdf file via netcdf4-python api

## Enthought
enpkg ipython package manager

## TODO

keep it netcf and tds focused
suggest users review basics
pyngl and pynio
talk to phillip at scipy

## Sean

Get your scripts on github
figure out cartopy

## Russ

Talk to Dave Brown
IS it better to use pynio or netcdf4-python

## Longer Term

investigate python-netcdf4 

## Ward

python notebook on the client

## Marcos

Helping Sean with Python with catalog parsing

## Ben

Evaluate workshop material
In particular, getting your environment going and investigating client environments (android, etc.)





netcdf write
sean xml
python with tds and netcdf
how to bring in non-enthought stuff
no dave brown stuff
touch base with phillip
communicate scitools project

further study Rich's examples for TDS example

example: ncss grib subsetting where you can make the request in lat/lon space and get back a netcdf CF file. REST based API.

student: play around with ipython notebook

netcdf section: seamless transition remote access. By the way, these are grib files.

using wms to find indices from lat lon

WMS/TDS example See: https://pypi.python.org/pypi/OWSLib/

write code for the workshop in modules and ipnb snippets for dealing with the tds
- get latest dataset
- 

8-8:30 Breakfast
8:30-9 Welcome/Logistics, staff introduction, overview
9:00-9:45 ipython notebook intro


Staff and student introduction / logistics


TODO:

Russ: Provide that Rich Signell link

Sean: Show both pydap and netcdf4


John's notes

TDS access thru pyhon

- rmote access thru opendap (Julian)
- get latest dataset - pydap and netcf lib (sean)
- ncss grid as point (sean)
- ncss grid subset (ethan)
- cdmrf point subset (lansing)
- WMS server (marcos)
- write netdf4 file (Russ ?)
- Rich's examples (John)
- Radar example (Sean)

netcdf does not come automatically with free enthought

Julien: enthought side wide license

Next meeting June 11

