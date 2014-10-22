#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error, pass 32 or 64 to bootstrap script."
    exit 1
fi

CONDALOCK="/home/vagrant/.condainstalled"

if [ "$1" == "32" ]; then
    echo "Error: 32-bit VM is unsupported."
    exit 1
    INSTFILE="Anaconda-2.0.1-Linux-x86.sh"
elif [ "$1" == "64" ]; then
    INSTFILE="Anaconda-2.0.1-Linux-x86_64.sh"
else
    echo "Error, pass 32 or 64 to bootstrap script."
    exit 1
fi
# Update package manager
apt-get update
#apt-get -y upgrade

# Install some packages
sudo apt-get install -y git emacs24 htop wget

# Add the anaconda path to the vagrant users path.
sudo -u vagrant -i echo 'PATH=/home/vagrant/anaconda/bin:$PATH' >> /home/vagrant/.bashrc

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
    sudo -u vagrant -i cp /vagrant/$INSTFILE /home/vagrant
fi

# If Anaconda has been installed, just skip next
# stanza.
if [ ! -f "$CONDALOCK" ]; then

    # Install Anaconda
    sudo -u vagrant -i bash /home/vagrant/$INSTFILE -bf -p /home/vagrant/anaconda

     ###
    # Add channels, create configuration.
    ###
    if [ "$1" == "64" ]; then
        sudo -u vagrant -i /home/vagrant/anaconda/bin/conda config --add channels https://conda.binstar.org/rsignell
    else
        sudo -u vagrant -i /home/vagrant/anaconda/bin/conda config --add channels https://conda.binstar.org/wardf
    fi

    sudo -u vagrant -i /home/vagrant/anaconda/bin/conda config --add channels https://conda.binstar.org/Unidata

    sudo -u vagrant -i /home/vagrant/anaconda/bin/conda create -n workshop --yes python=2 numpy matplotlib cartopy ipython ipython-notebook netcdf4 owslib pyudl networkx basemap

fi

#
# Create a text file explaining how to activate the workshop.
#

OFILE="/home/vagrant/WORKSHOP_README.txt"

if [ -f "$OFILE" ]; then
    rm $OFILE
fi

echo -e "\e[2J\n" > $OFILE
echo -e "\n\e[92mUnidata Python Workshop\e[39m\n=======================\n" >> $OFILE
echo -e "This Virtual Machine provides a complete environment" >> $OFILE
echo -e "for the Unidata Python workshop.\n" >> $OFILE
echo -e "Usage:\n" >> $OFILE
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
echo -e "notebooks will not disappear if the VM is destroyed!\n" >> $OFILE

#
# End workshop readme.
#

# Have the user see the WORKSHOP_README.txt file every time the log in.

if [ ! -f "$CONDALOCK" ]; then

    sudo -u vagrant -i echo 'if [ -f "/home/vagrant/WORKSHOP_README.txt" ]; then' >> /home/vagrant/.bashrc
    sudo -u vagrant -i echo '  cat /home/vagrant/WORKSHOP_README.txt' >> /home/vagrant/.bashrc
    sudo -u vagrant -i echo 'fi' >> /home/vagrant/.bashrc
    sudo -u vagrant -i echo 'source activate workshop' >> /home/vagrant/.bashrc

    sudo -u vagrant -i touch "$CONDALOCK"


fi

# Clean up
chown -R vagrant:vagrant /home/vagrant
