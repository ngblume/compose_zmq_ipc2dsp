# syntax=docker/dockerfile:1

# base image to start from with this container
FROM python:3.10-alpine

# Mount folde to container (also at creation, not just later during docker compose)
VOLUME /app

# prevents creattion of pychache on disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents buffering of stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set ENVIRONMENT variables for FLASK to work smoothless
# Flask app itself
ENV FLASK_APP=/app/interface_flask.py 
# Bind to all network interfaces
ENV FLASK_RUN_HOST=0.0.0.0
# Bind to port 5000 with the app (debug=true usually binds to 5000, if no port is specified)
ENV FLASK_RUN_PORT=5000
# Debug mode
ENV FLASK_DEBUG=True

# set work directory
WORKDIR /

# Copy list of required Python packages to container
COPY requirements.txt requirements.txt

# Install add packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Install required Python packages
RUN pip install -r requirements.txt

# Expose port 5000 within multi-container network
EXPOSE 5000
