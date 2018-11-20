---
Title: Installation
---

We'll run the workshop out of [Jupyter notebooks](http://jupyter.org/) and use
conda for our package management. We'll go over all of the details in the
class, but we'd like you to get setup before arrival to give us more time to
teach you more Python!

To get ready we'll install conda and setup the Python environment will all of
the packages you'll need. The instructions for Mac, Windows, and Linux are
outlined below in text form as well as videos for each operating system.

## Video Guides

### Mac/Linux
<iframe width="560" height="315" src="https://www.youtube.com/embed/lmAulLlXNOc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Windows
<iframe width="560" height="315" src="https://www.youtube.com/embed/5DFDXKzqkrU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Installing Conda
Head over to [conda.io/miniconda.html](https://conda.io/miniconda.html) and
download the miniconda installer for your operating system. You'll want the
Python 3.X version. **Windows 32-bit machines are NOT supported by most
packages and cannot be used.**

### Windows
* After downloading the installer, open it and click through the graphical
install utility. Accept all of the default installation settings.
* You should now have a program called "Anaconda Prompt" installed. Open it
  (this will be your Python command prompt).

### Mac/Linux
* After downloading the bash installer, open a command prompt (terminal program
on the Mac).
* Change the directory at the terminal to wherever the installer was downloaded.
  On most systems, this will default to the downloads directory in your user
  account. If that's the case, `cd ~/Downloads` will get you there, or replace
  the path with wherever you saved the file.
* Run the installer script by typing `bash Miniconda3-latest-MacOSX-x86_64.sh`.
  **Note: Your file name may be different depending upon your operating system!
  replace Miniconda3-latest-MacOSX-x86_64.sh with whatever the name of the file
  you downloaded was.**
* Accept the defaults.
* After the installer has completed completely close and restart your terminal
  program (this sources the newly modified path).
* Verify that your install is working by typing `conda --version` into the terminal.
  You should see a response like `conda 4.5.11` or similar (though yours may be a
  different version number).

## Setting up the environment
* We'll be using conda environments for the workshop (again, we'll explain more
  during the course or checkout [this MetPy Monday](https://www.youtube.com/watch?v=15DNH25UCi0)
  if you can't wait). After installing conda, open a terminal (or the Anaconda Prompt
  if you're on a Windows machine).
* Download the `environment.yml` file that will tell your system what all we need for the
  workshop. Note where you download it, this will be the `Downloads` directory by default on
  most systems, which is fine. Right click and "save"
  <a href="https://raw.githubusercontent.com/Unidata/python-workshop/master/environment.yml">this link</a>
  to download.
* Open a terminal (Anaconda prompt on Windows) and navigate to whatever directory the `environment.yml`
  file was saved in. Generally `cd ~/Downloads`.
* Run the command `conda env create` and wait for the installation to finish.
* Run the command `conda activate unidata` to activate the unidata environment and
  verify that everything is ready.
