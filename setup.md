# Setup instructions for workshop attendees

## Before the workshop

If you do not have one already obtain [sign up for a github account](https://github.com/join). Please remember your login and password when attending workshop.

**Desktop computers will be provided for workshop attendees. However, if you plan on working on your own laptop please download and install:**

- [git](http://git-scm.com/downloads)
- [conda](http://continuum.io/downloads)

If working in a Unix or Mac OS X environment, make sure `git` and `conda` are one your path.

You will also need some sort of text editor you are comfortable working with. On Unix or OS X this can be vi, emacs, or pico. On Windows, you can use notepad.


## Setup at start of Workshop

The workshop instructors will guide through the following.

Fork the workshop repository: <https://github.com/Unidata/unidata-python-workshop>

From the Unix command line:

### git setup

```
git config --global user.name "YOUR NAME"

git config --global user.email "YOUR EMAIL ADDRESS"

git clone https://github.com/YOUR-USERNAME/unidata-python-workshop.git

cd unidata-python-workshop
```

### conda setup


```
conda update conda

conda update anaconda

conda config --add channels https://conda.binstar.org/rsignell

conda config --add channels https://conda.binstar.org/Unidata

conda create -n workshop python=2 numpy matplotlib cartopy ipython ipython-notebook netcdf4 owslib pyudl

source activate workshop

ipython notebook
```
