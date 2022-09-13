# syntax=docker/dockerfile:1

# base image to start from with this container
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# prevents creattion of pychache on disk
ENV PYTHONDONTWRITEBYTECODE 1
# prevents buffering of stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set ENVIRONMENT variables for FLASK to work smoothless
# Flask app itself
ENV FLASK_APP=interface_flask.py 
# Bind to all network interfaces
ENV FLASK_RUN_HOST=0.0.0.0
# Bind to port 5000 with the app (debug=true usually binds to 5000, if no port is specified)
ENV FLASK_RUN_PORT=5000
# Debug mode
ENV FLASK_DEBUG=1

# Install add packages
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy list of required Python packages to container
COPY requirements.txt requirements.txt

# Install required Python packages
RUN pip install -r requirements.txt

# Expose port 5000 within multi-container network
EXPOSE 5000

# Copy "interface_flask.py" to WORKDIR
COPY interface_flask.py interface_flask.py

# Start Flask app
CMD ["flask", "run"]
