# Installing Python with Conda

## Presenter Notes
- Be sure you have renamed/moved your existing conda installation.
- Ensure you're using BASH.
- Cleanup your prompt or other custom settings.

## Python and libraries
- Python provides a basic interpreter
- Standard libraries ("batteries included")
- Install additional libraries for more domain specific/less general functionality

## What is Conda
- Cross-platform package manager
- Provides environments
- Conda manages shell environment to configure environment
  - stable vs. test environment
  - different versions of libraries
  - different versions of Python
  - research/publication environments
- Miniconda is like Conda, but with less of the prepackaged libraries included.

## Installing Miniconda
- Download miniconda installer [here](https://conda.io/miniconda.html)
- *Windows*: Launch the exe installer and follow the on screen instructions.
- *Mac/Linux*: Run the downloaded bash script: `bash Miniconda3-latest-MacOSX-x86_64.sh`
- Restart your terminal
- Check installation: `conda --version` (Use the Anaconda prompt on Windows)

## Creating environments
- Create a simple testing environment: `conda create -n playground python=3`
- Currently we are in the root environment: `conda env list`
- Switch to the new environment: `(source) activate playground`
  `source` is necessary on Mac and Linux only.
- We're now in the playground environment: `conda env list`
- Check the Python version: `python --version`
- List what's installed in this environment: `conda list`

## Installing packages
- Launch interpreter: `import numpy` (does not work!)
- Install numpy: `conda install numpy`
- Launch interpreter: `import numpy` (works!)
- Remove a package: `conda remove numpy`
- Search for a package: `conda search numpy`
- Install a specific version of a package: `conda install numpy=1.9`
- Update a package: `conda update numpy`
- Update all packages: `conda update --all`

## Channels and conda-forge
- Let's say we want to install MetPy: `conda search metpy` It's not built and
  distributed by Continuum!
- What is [conda-forge](https://conda-forge.org)? A community driven set of
  package distributions. The place to get the most up-to-date set of packages
  and many packages that are not build by Continuum.
- Let's add conda-forge to our channels (we could do this at install on a
  package by package basis, but the global configuration is the best daily
  driver for most users.): `conda config --add channels conda-forge`
- Now we can find MetPy and install it: `conda search metpy`

## Create an environment from a config
- Let's go back to the root environment: `(source) deactivate`
- Make sure we're in the workshop directory.
- Create a new environment based what's in the `environment.yml` file: `conda env create`
- Make sure our new environment is there: `conda env list`
- Activate the new environment: `(source) activate unidata-workshop`

## Cleaning up
- Conda stores a lot of information on your system. Tarballs, indexes, caches, etc.
- The `conda clean` command can free up gigabytes of space on your disk!
- Recommended invocation: `conda clean -tp` (tarballs and unused cached packages)
