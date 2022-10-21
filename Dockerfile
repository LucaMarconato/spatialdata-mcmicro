FROM python:3.8-slim

LABEL base_image="python:3.8-slim"
LABEL software="spatialdata"
LABEL about.summary=""
LABEL about.home=""
LABEL about.license=""
LABEL about.license_file=""
LABEL about.documentation=""


MAINTAINER Niklas Stotzem


ARG DEBIAN_FRONTEND="noninteractive"

ENV LANG en_US.UTF-8 \
    LC_ALL en_US.UTF-8 \
    LANGUAGE en_US:en  \
    NUMBA_CACHE_DIR=/tmp

RUN apt-get update -qq && \
    apt-get install -y -q --no-install-recommends \
            gcc \
            git \
            python3-dev \
            python3-pip \
            python3-wheel \
            libblas-dev \
            liblapack-dev \
            libatlas-base-dev \
            gfortran \
            apt-utils \
            bzip2 \
            ca-certificates \
            curl \
            locales \
            unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 


RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen

RUN pip install -U pip

### Install 2 different Repos
RUN pip install git+https://github.com/scverse/spatialdata-io.git@main
RUN pip install git+https://github.com/scverse/spatialdata.git@feature/transform_and_coord_spaces
RUN pip install loguru scanpy click

