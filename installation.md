---
Title: Installation
---

For this workshop, we will be using the following Python libraries:

-   [numpy](http://www.numpy.org/)
-   [netcdf4-python](http://github.com/Unidata/netcdf4-python)
-   [matplotlib](http://matplotlib.org/)
-   [cartopy](http://scitools.org.uk/cartopy/)
-   [OWSLib](http://pypi.python.org/pypi/OWSLib/)
-   [siphon](http://github.com/Unidata/siphon)
-   [MetPy](http://github.com/metpy/MetPy)
-   [python-awips](http://github.com/Unidata/python-awips)
-   [xarray](http://xarray.pydata.org)

Downloading the Material
------------------------
The material for the workshop can be cloned from our
[GitHub repository](https://github.com/Unidata/unidata-python-workshop)
or can be directly downloaded as a zip file
[here](https://github.com/Unidata/unidata-python-workshop/archive/master.zip).

Installing git
--------------
We'll be showing you the basics of the git version control system and you can
use it to retrieve the material for the workshop with the `git clone` command.

## Mac
The XCode command line tools need to be installed.
1. Install XCode if it isn't already. XCode is  available in the Mac App Store
for free.
2. Launch XCode and accept the license agreement.
3. Quit XCode.
4. Open a new terminal and run the command `xcode-select --install`
5. Select install on the pop-up menu.

## Linux
Use your package manager. For example, using aptitude you would run the
following terminal command: `sudo apt-get install git`

## Windows
Download and install the [GitHub desktop tools](https://desktop.github.com).

Running Locally
---------------
The easiest way to install these libraries is with
[conda](http://conda.io/).

1.  [Install Miniconda (Python 3.5) from Continuum
    Analytics](http://conda.io/miniconda.html). ([Determine if
    your OS 32 or 64 bit](http://www.akaipro.com/kb/article/1616#os_32_or_64_bit))
2.  Once Miniconda is installed, from the command line (e.g., OS X
    terminal, cmd.exe), run these instructions to clone the repository
    and create the environment:

```shell
git clone https://github.com/Unidata/unidata-python-workshop

cd unidata-python-workshop

conda env create -f environment.yml
```

### From a Unix command line (e.g., OS X terminal)

If your default shell is NOT bash, first type `bash`. To activate or
switch to a conda environment, you can `source activate <environment>`.
For example,

```shell
source activate unidata-workshop
```

To switch and/or deactivate environments:

```shell
source deactivate
source activate <environment>
```

### From a Windows command line (e.g., cmd.exe)

To activate or switch to a conda environment, you can `activate <environment>`.
For example,

```shell
activate unidata-workshop
```

To switch and/or deactivate environments:

```shell
deactivate
activate <environment>
```

Running the notebooks
---------------------
```shell
cd unidata-python-workshop

# unix, use bash. windows omit 'source'
source activate unidata-workshop

jupyter notebook
```

Binder
------
It is also possible to run a temporary notebook session using binder by
visiting
[mybinder.org](http://mybinder.org/repo/Unidata/unidata-python-workshop).
