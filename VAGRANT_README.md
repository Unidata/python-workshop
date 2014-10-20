# Vagrant Virtual Environment

The Unidata Python Workshop iPython Notebook environment has been configured to work with `Vagrant`, a tool for creating on-demand virtual machines.  This allows us to create a standardized linux VM, fully kitted out for the workshop with Anaconda and other dependent packages. The iPython notebooks are located on the host machine in the `unidata_python_workshop/` directory, so changes made in the VM will not be lost when the VM is removed.

## Requirements

You will need the following to work with Vagrant.  

* `Vagrant`: http://vagrantup.com
* `Virtualbox`: https://www.virtualbox.org/wiki/Downloads
* `Virtualbox Extension Pack`: https://www.virtualbox.org/wiki/Downloads

> NOTE: You must install the Virtualbox Extension Pack or else the VM won't work correctly.

### **IMPORTANT NOTE FOR WINDOWS USERS**

By default, Windows is not distributed with an ssh client.  There are many options, some of them very convoluted.  The path of least resistance is to download and install the `git shell for windows`, which installs a command-line ssh client.  


* `Git SCM for Windows`: http://msysgit.github.io/


# Using Vagrant

## Creating the Workshop Environment

A single environment is provided: `workshp64`.

From the `unidata_python_workshop/` directory, perform the following actions from the system command line.  

> $ vagrant up workshop64

This step will take 5-10 minutes.  The VM will be instantiated and the required packages will be installed.

## Connecting to the Workshop VM

Once the workshop environment has been provisioned, you can connect via `ssh` as follows.

> $ vagrant ssh workshop64

This will log you in to the workshop VM via ssh.  

## Working in the VM Environment

Once logged into the VM, you are in a standard `Ubuntu` linux environment.  In the VM, the directory `/vagrant/` is mapped to the `unidata_python_workshop/` directory on the host machine.  Changes made in this directory will persist beyond the life of the VM!  We will work from this location for the workshop.

### Launching iPython Notebook

You will launch IPython Notebook from inside the VM as follows.

> $ cd /vagrant

> $ ipython notebook --ip=* --no-browser

Then, open your browser of choice and navigate to the following address:  `http://127.0.0.1:[port]` where `[port]` is `8864` if you are using a 64-bit VM.

# Cleaning Up

When you are done with the VM, you will exit with `exit` from the command line.  From the command line on the host machine, you will destroy the VM as follows:

> $ vagrant destroy workshop64

This will destroy the VM, but any changes made in the `/vagrant/` directory will remain.  Don't forget to commit any of your changes back into the git repository!