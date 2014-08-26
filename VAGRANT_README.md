# Vagrant Virtual Environment

The Unidata Python Workshop iPython Notebook environment has been configured to work with `Vagrant`, a tool for creating on-demand virtual machines.  This allows us to create a standardized linux VM, fully kitted out for the workshop with Anaconda and other dependent packages. The iPython notebooks are located on the host machine in the `unidata_python_workshop/` directory, so changes made in the VM will not be lost when the VM is removed.

## Installing Vagrant

Vagrant works on Windows, OSX and Linux systems.

Vagrant install files may be downloaded from http://www.vagrantup.com/downloads.html.  Vagrant relies on `VirtualBox`, the free virtual machine engine provided by Oracle.  It may be downloaded from https://www.virtualbox.org/wiki/Downloads.  

    You will need to install VirtualBox plus the VirtualBox extension pack, available from the same webpage.

# Using Vagrant

## Creating the Workshop Environment

    Two virtual environments are provided; workshop32 and workshop64.  These are 32-bit and64-bit environments, respectively.  For the purpose of the following examples, we'll assume we're using the 64-bit environment.

From the `unidata_python_workshop/` directory, perform the following actions.  

> $ vagrant up workshop64

This step will take 5-10 minutes.  The VM will be instantiated and the required packages will be installed.

## Connecting to the Workshop VM

Once the workshop environment has been provisioned, you can connect via `ssh` as follows.

> $ vagrant ssh workshop64

This will log you in to the workshop VM over ssh.  

## Working in the VM Environment

Once logged into the VM, you are in a standard `Ubuntu` linux environment.  In the VM, the directory `/vagrant/` is mapped to the `unidata_python_workshop/` directory on the host machine.  Changes made in this directory will persist beyond the life of the VM!  We will work from this location for the workshop.

### Launching iPython Notebook

There are two ways to run iPython Notebooks from the VM.  Before doing either, you will want to change your active directory to `/vagrant/` as follows:

> $ cd /vagrant

If your host machine is linux or OSX, it's likely you have an X11 server running.  If this is the case, you can run ipython notebooks within a browser from the VM.  In this case, you will launch ipython notebooks as follows:

> $ ipython notebook

If this does not work, or if you prefer to use the browser on your host machine, you will do the following:

> $ ipython notebook --ip=* --no-browser

Then, open your browser of choice and navigate to the following address:  `http://127.0.0.1:[port]` where `[port]` is `8832` if you are using a 32-bit VM and `8864` if you are using a 64-bit VM.

# Cleaning Up

When you are done with the VM, you will exit with `exit` from the command line.  From the command line on the host machine, you will destroy the VM as follows:

> $ vagrant destroy workshop64

This will destroy the VM, but any changes made in the `/vagrant/` directory will remain.