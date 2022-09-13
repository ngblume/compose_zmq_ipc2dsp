 # syntax=docker/dockerfile:1
# Define image to start from
FROM python:3.10-alpine

# Mount folde to container (also at creation, not just later during docker compose)
VOLUME /app

# prevents creattion of pychache on disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents buffering of stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set work directory (where files are copied, etc.)
WORKDIR /

# Copy list of required Python packages to container
COPY requirements.txt requirements.txt

# install maybe required packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Install all requirements in container
RUN pip install -r requirements.txt

# Expose ports for ipc2dsp
# n/a
