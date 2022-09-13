 # syntax=docker/dockerfile:1
# Define image to start from
FROM python:3.10-alpine

# Set work directory (where files are copied, etc.)
WORKDIR /app

# prevents creattion of pychache on disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents buffering of stdout and stderr
ENV PYTHONUNBUFFERED 1

# install maybe required packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements file to container WORKDIR
COPY requirements.txt requirements.txt

# Install all requirements in container
RUN pip install -r requirements.txt

# Expose ports for ipc2dsp
# n/a

# Copy application to WORKDIR
COPY interface_sub.py interface_sub.py

# Run ipc2dsp python app
CMD ["python3","interface_sub.py"]
