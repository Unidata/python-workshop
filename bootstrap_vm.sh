#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error, pass 32 or 64 to bootstrap script."
    exit 1
fi

CONDALOCK="/home/vagrant/.condainstalled"

if [ "$1" == "32" ]; then
    INSTFILE="Anaconda-2.0.1-Linux-x86.sh"
elif [ "$1" == "64" ]; then
    INSTFILE="Anaconda-2.0.1-Linux-x86_64.sh"
else
    echo "Error, pass 32 or 64 to bootstrap script."
    exit 1
fi
# Update package manager
#apt-get update
#apt-get -y upgrade

# Install some packages
sudo apt-get install -y git emacs24 firefox nethogs htop wget

# Add the anaconda path to the vagrant users path.
sudo -u vagrant echo 'PATH=/home/vagrant/anaconda/bin:$PATH' >> /home/vagrant/.bashrc

# Until we can automate the download,
# check to see if the install file is
# already in /vagrant.


if [ ! -f "/vagrant/$INSTFILE" ]; then
    wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/$INSTFILE

    if [ ! -f "/home/vagrant/$INSTFILE" ]; then
        echo "Error downloading $INSTFILE."
        exit 1
    fi

    cp $INSTFILE /vagrant/
else
    sudo -u vagrant cp /vagrant/$INSTFILE /home/vagrant
fi

# If Anaconda has been installed, just skip next
# stanza.
if [ ! -f "$CONDALOCK" ]; then

    # Install Anaconda
    sudo -u vagrant bash /home/vagrant/$INSTFILE -bf -p /home/vagrant/anaconda

    # Install some conda packages
    sudo -u vagrant /home/vagrant/anaconda/bin/conda create --yes -n workshop python numpy matplotlib netcdf4 basemap pandas ipython pyzmq jinja2 tornado sympy

    # Rich only makes owslib availabe for 64-bit. I'll try to build
    # and make available for 32-bit.
    if [ "$1" == "64" ]; then
        sudo -u vagrant /home/vagrant/anaconda/bin/conda install --yes --quiet -n workshop -c https://conda.binstar.org/rsignell owslib
    else
        sudo -u vagrant /home/vagrant/anaconda/bin/conda install --yes --quiet -n workshop -c https://conda.binstar.org/wardf owslib
    fi

    sudo -u vagrant /home/vagrant/anaconda/bin/conda install --yes --quiet -n workshop -c https://conda.binstar.org/Unidata pyudl

fi

#
# Create a text file explaining how to activate the workshop.
#

OFILE="/home/vagrant/WORKSHOP_README.txt"

if [ -f "$OFILE" ]; then
    rm $OFILE
fi

echo -e "\n\e[92mUnidata Python Workshop\e[39m\n=======================\n" > $OFILE
echo -e "This Virtual Machine provides a complete environment" >> $OFILE
echo -e "for the Unidata Python workshop.\n" >> $OFILE
echo -e "Usage:\n" >> $OFILE
echo -e '    $ cd \e[32m/vagrant\e[39m' >> $OFILE
echo -e '    $ \e[95mipython notebook\e[39m' >> $OFILE
echo -e ""
echo -e "\nThis will launch ipython notebook in firefox over x11." >> $OFILE
echo -e "\nIf you want to use an external browser from" >> $OFILE
echo -e "your host machine, you must start ipython notebook" >> $OFILE
echo -e "as follows:\n" >> $OFILE
echo -e '    $ cd \e[32m/vagrant\e[39m' >> $OFILE
echo -e "    $ \e[95mipython notebook --ip=* --no-browser\e[39m" >> $OFILE
echo -e "\nYou may then open a browser on your host machine and" >> $OFILE
echo -e "navigate to:\n" >> $OFILE
if [ "$1" == "64" ]; then
    echo -e "    \e[33mhttp://127.0.0.1:8864\e[39m" >> $OFILE
else
    echo -e "    \e[33mhttp://127.0.0.1:8832\e[39m" >> $OFILE
fi

echo -e "\nNote: the \e[32m/vagrant/\e[39m directory is mapped to" >> $OFILE
echo -e "the unidata-python-workshop/ directory on your" >> $OFILE
echo -e "host machine.  This way any changes made to the" >> $OFILE
echo -e "notebooks will not dissapear if the VM is destroyed!\n" >> $OFILE

#
# End workshop readme.
#

# Have the user see the WORKSHOP_README.txt file every time the log in.

if [ ! -f "$CONDALOCK" ]; then

    sudo -u vagrant echo 'if [ -f "/home/vagrant/WORKSHOP_README.txt" ]; then' >> /home/vagrant/.bashrc
    sudo -u vagrant echo '  cat /home/vagrant/WORKSHOP_README.txt' >> /home/vagrant/.bashrc
    sudo -u vagrant echo 'fi' >> /home/vagrant/.bashrc
    sudo -u vagrant touch "$CONDALOCK"
fi
# Clean up
chown -R vagrant:vagrant /home/vagrant
