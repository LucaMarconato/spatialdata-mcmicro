FROM continuumio/miniconda3

# if one doesn't want to use conda (smaller image size), can do something like this:
# RUN apt-get update -qq && apt-get install -y -q --no-install-recommends \
	# libgdal-dev \
	# gcc

# but we use conda because it's easier to setup
RUN conda install -c conda-forge mamba
RUN mamba install python=3.10

# complex dependencies that needs to be solved with conda
RUN mamba install -c conda-forge gcc libgdal gxx imagecodecs -y

# satellite spatialdata projects
RUN pip install git+https://github.com/scverse/spatialdata-io.git@main
RUN pip install git+https://github.com/scverse/spatialdata-plot.git@main
# one could try to make napari work across the docker image and use X forwarding. In that case one needs to install napari-spatialdata
# RUN pip install git+https://github.com/scverse/napari-spatialdata.git@spatialdata

# this command needs to be run last so it overwrites the installation of spatialdata from spatialdata-io (we need a branch that is not the main branch)
# main package
RUN pip install git+https://github.com/scverse/spatialdata.git@fixes/transforms

# additional dependencies
RUN pip install loguru scanpy click datashader
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# example usage
RUN cd /home && git clone https://github.com/giovp/spatialdata-sandbox
RUN cd /home/spatialdata-sandbox/merfish && python download.py && python to_zarr.py
