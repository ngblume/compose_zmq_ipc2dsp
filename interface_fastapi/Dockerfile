# syntax=docker/dockerfile:1

# base image to start from with this container
FROM python:3.10-alpine

# Mount folde to container (also at creation, not just later during docker compose)
VOLUME /app

# prevents creattion of pychache on disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents buffering of stdout and stderr
ENV PYTHONUNBUFFERED 1

# set work directory for BUILD
WORKDIR /

# Copy requirements file to container WORKDIR
COPY requirements.txt requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

# Install required Python packages
RUN pip install -r requirements.txt

# Expose port 5100 within multi-container network
EXPOSE 5100
