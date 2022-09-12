# syntax=docker/dockerfile:1

# base image to start from with this container
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# prevents creattion of pychache on disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents buffering of stdout and stderr
ENV PYTHONUNBUFFERED 1

# Copy list of required Python packages to container
COPY requirements.txt requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

# Copy list of required Python packages to container
COPY requirements.txt requirements.txt

# Install required Python packages
RUN pip install -r requirements.txt

# Expose port 5000 within multi-container network
EXPOSE 5100

# Copy application to WORKDIR
COPY . /app/

# Start Flask app
CMD ["flask", "run"]
