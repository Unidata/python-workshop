#!/bin/bash

# Update package manager
#apt-get update
#apt-get -y upgrade

# Install some packages
sudo apt-get install -y git emacs24

# Add the anaconda path to the vagrant users path.
sudo -u vagrant echo 'PATH=/home/vagrant/anaconda/bin:$PATH' >> /home/vagrant/.bashrc

# Until we can automate the download,
# check to see if the install file is
# already in /vagrant.

INSTFILE="Anaconda-2.0.1-Linux-x86_64.sh"
if [ ! -f "/vagrant/$INSTFILE" ]; then
    echo "Error: Need to download anaconda install file by hand and place in host directory."
    exit 1
fi

cp /vagrant/$INSTFILE /home/vagrant
# Install Anaconda
sudo -u vagrant bash $INSTFILE -bf -p /home/vagrant/anaconda

# Install some conda packages
sudo -u vagrant /home/vagrant/anaconda/bin/conda create --yes -n workshop python numpy matplotlib netcdf4 basemap pandas ipython pyzmq jinja2 tornado sympy

sudo -u vagrant /home/vagrant/anaconda/bin/conda install --yes --quiet -n workshop -c https://conda.binstar.org/rsignell owslib

sudo -u vagrant /home/vagrant/anaconda/bin/conda install --yes --quiet -n workshop -c https://conda.binstar.org/Unidata/pyudl

sudo -u vagrant source activate workshop

#sudo -u vagrant git clone https://github.com/Unidata/unidata-python-workshop.git



# Clean up
chown -R vagrant:vagrant /home/vagrant
