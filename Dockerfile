FROM busybox

# Fixes permissions when used with other images
RUN adduser -D jupyter

ADD . /notebooks/unidata-python-workshop/

RUN chown -R jupyter:jupyter /notebooks

USER jupyter
