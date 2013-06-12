tds-python-workshop
===================

This private repository contains notes and ipython notebooks in preparation for the TDS Python workshop.

# Workshop Outline

### Unidata Technology with Python
- What is Python?
- Why Unidata technology with Python?
- Language popularity measured by search hits on AMS [web site](https://ams.confex.com/ams/93Annual/webprogram/start.html#srch=words%7Cjava%7Cmethod%7Cand%7Cpge%7C2)
- Enthought Python Distribution (EPD)
- Outline of lectures
- Background material

### ipython notebook
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

### netCDF File Exploration with Python and NumPy
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
#### Remote data access via the TDS
- When accessing via TDS many data formats are supported

## Geoscience visualization with matplotlib ##

- Some Examples
- Plotting netCDF data
- Basic Plot
- Let's improve upon the plot into something that is more ready for publication.
- Matplotlib Basemap

### Exploring THREDDS netCDF Subset Service (NCSS) with Pandas
- Let's explore some Short Range Ensemble Forecast (SREF) data from the TDS
- Let's make the columns nicer.
- Let's prepare the data for plotting
- Let's resample the data to one hourly data
- Now let's plot
- Pandas has powerful data slicing and dicing capability.
- I prefer to exercise when the temperature is less than 80 F during "daylight hours". 
- What are the minimun and maximum temperatures in the forthcoming days

### Accessing data via Pydap
- Searching and retrieving NAM data from a THREDDS data server
- Helper function to get latest NAM data
- Retrieving the data
- Plotting with matplotlib and Basemap

## TODO

- Send out a note pre-workshop and have users review https://github.com/jrjohansson/scientific-python-lectures and gain familiarity with ipynb
- Section on writing netdf4 files (Russ)
- Start writing a TDS catalog XML parser module (Sean and Marcos). Write a get latest dataset function.
- Investigate ipython notebook client options (Ward?)
- Get proof of concept working for mobile devices. (e.g. ipad) (Ward)
- Make recommendation on Python IDE in intro (Julien)
- When the notebook are finished, post them on http://nbviewer.ipython.org/
- Incorporate more material from the "Study" below
- example with ncss grib subsetting where you can make the request in lat/lon space and get back a netcdf CF file. REST based API.
- In the netcdf section, emphasize seamless access to remote access and different data sources (e.g., grib)
- Investigate using wms to find indices from lat lon
- Study WMS/TDS example See: https://pypi.python.org/pypi/OWSLib/
- Put greater emphasis on remote data access through opendap (Julien)
- Render radar from a TDS (Sean)
- Render satellite data from ADDE (Julien)
- Set up meeting for the week of June 10 (Julien)
- Write a section on data analysis with Pandas
- Another NCSS example with gridded data?
- clean up pydap example
- incorporate Rich Signell's wave example
- Continue writing schedule below
- At some point, start writing exercises for students
- Satellite from TDS (Julien)

- June 20 th meeting, first draft

John's TODOs

TDS access thru pyhon

- ncss grid as point (sean)
- ncss grid subset (ethan)
- cdmrf point subset (lansing)
- WMS server (marcos)

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
- http://nbviewer.ipython.org/4113653/
- https://ams.confex.com/ams/93Annual/flvgateway.cgi/id/23312?recordingid=23312
- http://polar.ncep.noaa.gov/global/examples/usingpython.shtml
- http://matplotlib.org/basemap/users/examples.html
- http://stackoverflow.com/questions/15432587/converting-netcdf-to-grib2
- "AMS Short Course on Intermediate Python: Using NumPy, SciPy, and Matplotlib" (see Julien or PPTs)
- https://github.com/ResearchComputing/python_hpc
- Lectures on scientific computing with python, as IPython notebooks: https://github.com/jrjohansson/scientific-python-lectures
- Why Python is the next Wave in earth sciences computing: http://journals.ametsoc.org/doi/pdf/10.1175/BAMS-D-12-00148.1
- Spell check notebooks

## Questions

- How to bring non-Enthought stuff into this environment?

## Schedule for with workshop 

- 8-8:30 Breakfast
- 8:30-9 Welcome/Logistics, staff introduction, overview
- 9:00-9:45 ipython notebook intro
- Staff and student introduction / logistics

## Enthought
enpkg ipython package manager

