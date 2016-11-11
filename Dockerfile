FROM andrewosh/binder-base

MAINTAINER Ryan May <rmay@ucar.edu>

USER main

# Update conda.
RUN conda update conda --yes
ADD environment.yml environment.yml
RUN conda-env create environment.yml

# Work around pip-installed jupyter in base image
RUN /bin/bash -c "source activate unidata-workshop && ipython kernel install --user"
