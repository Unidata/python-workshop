# Installing Python with Conda

## Python and libraries
- Python provides a basic interpreter
- Standard libraries
- Install additional libraries

## What is Conda
- Cross-platform package manager
- Provides environments
- Conda manages shell environment to configure environment
  - stable vs. test environment
  - different versions of libraries
  - different versions of Python
- `conda --version`

## Creating environments
- `conda create -n playground python=3`
- `conda env list`
- `(source) activate playground`
- `conda env list`
- `python --version`
- `conda list`

## Installing packages
- `import numpy`
- `conda install numpy`
- `import numpy`
- `conda remove numpy`
- `conda search`
- `conda install numpy=1.9`
- `conda update numpy`
- `conda update --all`

## Channels and conda-forge
- What is conda-forge?
- `conda search metpy`
- `conda config --add channels conda-forge`
- `conda search metpy`

## Create an environment from a config
- `(source) deactivate`
- `conda env create`
- `conda env list`
- `(source) activate unidata-workshop`
