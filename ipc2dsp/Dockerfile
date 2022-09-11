 # syntax=docker/dockerfile:1
# Define image to start from
FROM python:3.7-alpine

# Set work directory (where files are copied, etc.)
WORKDIR /app

# install maybe required packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy requirements file to container WORKDIR
COPY requirements.txt requirements.txt

# Install all requirements in container
RUN pip install -r requirements.txt

# Expose ports for ipc2dsp
# PUB-port for status
EXPOSE 5555
# REQ-REPL-port for requests / replies
EXPOSE 6000

# Copy application to WORKDIR
COPY ipc2dsp.py ipc2dsp.py

# Run ipc2dsp python app
CMD ["python3","ipc2dsp.py"]
