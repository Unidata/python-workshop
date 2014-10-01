% Reproducible Science with Conda and Binstar

# Conda

- Cross platform package manager
- Goes beyond pip (and friends) capability
- Endorsed by Python Packaging Authority (PyPA)

# What is a package manager?

- "collection of software tools to automate the process of installing, upgrading, configuring, and removing software packages" - wikipedia
- In practical terms "I am a researcher, and I need to import numpy. How do I do that?"

# Problems w/ traditional Python Packaging

- [Stackoverflow: Differences between distribute, distutils, setuptools and distutils2?](http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2) 
- "Python packaging/installation has way too many alternatives with no clear guidance from the community."  -Sabuncu
- "I love Python, but the state of Python packaging is nothing less than hellish!" -Zearin

# pip

- Works well for Python
- Not great if you are linking against C and Fortran libraries (e.g., HDF5)

# Conda to the rescue

- Python agnostic package manager
- Cross-platform
- No admin privileges required
- Smart dependency management
- Easy to work w/ different versions of packages (e.g., numpy 1.7 vs. 1.9)

# Some conda definitions...

# Conda packages

- binary tarballs containing system-level libraries, Python modules, executable programs
- Can also build own conda packages for distribution via binstar channels

# Conda environments

- a conda environment is a collection of packages
- simply a directory on the file system containing conda packages
- environments nicely compartamentalized
- easy to set up environments.
- easy to invoke and switch between environments

# Conda channels

- conda packages originate from "channels"
- there are default channels for most standard packages
- add custom channels to find special packages
- you can become your own channel binstar
- examine channel list in .condarc

# Working with conda from the command line

# The `conda` command

- primary interface for managing Python packages

# Asking conda for help

- `conda --help`
- `conda [command] --help`

# `conda info`

- Display information about current conda install.
- `conda info --all`
- `conda info --envs`
- `conda info --system`

# `conda create` a new environment

- Create a new conda environment from a list of specified packages
- `conda create -n unidataws python`
- must supply at least one package (unfortunately)
- Lots of optional arguments

# Conda default "anaconda" environment

- numpy
- pandas
- matplotlib
- lots of stuff
- `conda create -n <env> anaconda`

# `conda install`

- Install a list of packages into a specified conda environment.
- `conda install -n unidataws matplotlib`
- Dealing with specific package versions
- `conda install -n unidataws matplotlib=1.2`

# `conda list`

- List linked packages in a conda environment.
- `conda list`

# Reproducing science w/ `conda list --export`

- `conda list --export > exported_packages.txt`
- share your exported_packages.txt w/ colleague
- `conda create -n newenv --file exported_packages.txt`

# `conda update`

- Update conda packages
- Typically `conda update --all`
- Lots of options

# `conda search`

# `source deactivate`

- To deactivate the environment

# Binstar
