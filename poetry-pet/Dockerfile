FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu18.04

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.11
ENV LANG C.UTF-8

# Update
RUN apt-get clean 
RUN apt-get update -y
RUN apt-get upgrade -f -y


# RUN apt-get update && apt-get install -y software-properties-common gcc && \
#     add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.6 python3-distutils python3-pip

#RUN update-alternatives --install /usr/bin/python2.7 python /usr/bin/python3.6
#RUN update-alternatives --config python3

# System deps:
RUN pip3 install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

#RUN export PYTHONIOENCODING=utf8

# Project initialization:
RUN python3 -m pip install --upgrade pip
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code
