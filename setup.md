# Setup instructions for workshop attendees

## Before the workshop

If you do not have one already, [sign up for a github account](https://github.com/join). Please remember your login and password when attending workshop.

## For those bringing their own laptop computers

**Desktop computers will be provided for workshop attendees. However, if you plan on working on your own laptop, you have two options:**


### Option 1, download git and conda

Download and install:

- [git](http://git-scm.com/downloads)
- [conda](http://continuum.io/downloads)

If working in a Unix or Mac OS X environment, make sure `git` and `conda` are on your path.

You will also need a text editor you are comfortable working with. On Unix or OS X this can be `vi`, `emacs`, `gedit`, or `pico`. On Windows, you can use notepad.

### Option 2, Vagrant

Vagrant is free, open-source software to create virtual environments. In practical terms, this means Vagrant is an alternative option to easily set up the workshop environment. [Instructions for working with Vagrant](https://github.com/Unidata/unidata-python-workshop/blob/master/VAGRANT_README.md).

## Setup at start of workshop

The workshop instructors will guide you through the following steps:

- Login to your computer

- Find and start the "Terminal" application

From the command line:

~~`git clone https://github.com/Unidata/unidata-python-workshop`~~

~~`conda config --add channels https://conda.binstar.org/rsignell`~~

~~`conda config --add channels https://conda.binstar.org/Unidata`~~

~~`conda create -n workshop python=2 numpy matplotlib cartopy ipython ipython-notebook netcdf4 owslib pyudl networkx basemap`~~

```
cd unidata-python-workshop

# in case there were last minute changes
git pull

source activate workshop

ipython notebook
```

### github setup

- Login to github.

- Fork the workshop repository: <https://github.com/Unidata/unidata-python-workshop> by clicking the fork button.

![Fork](https://github-images.s3.amazonaws.com/help/repository/fork_button.jpg)


```
git config --global user.name "YOUR NAME"

git config --global user.email "YOUR EMAIL ADDRESS"

git remote add myfork https://github.com/YOUR-USERNAME/unidata-python-workshop.git

git remote set-url myfork https://YOUR-USERNAME@github.com/YOUR-USERNAME/unidata-python-workshop.git

# Later if you wish to save (i.e., push out) your commits

git push myfork master

```
