FROM busybox

# Fixes permissions when used with other images
RUN adduser -u 1001 -s /bin/bash -h /home/jupyter -D jupyter

ADD . /notebooks/unidata-python-workshop/

RUN chown -R jupyter:jupyter /notebooks

USER jupyter

# Try to expose as a volume
VOLUME /notebooks
