import time
import redis
from flask import Flask
from threading import Thread

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_call_count():
	retries = 5
	while True:
		try:
			return cache.incr('hits')
		except redis.exceptions.ConnectionError as exc:
			if retries == 0:
				raise exc
			retries -= 1
			time.sleep(0.5)

@app.route('/')
def hello():
	count = get_call_count()
	return 'Hello from Docker! I have been seen {} times.\n'.format(count)

@app.get('/status')
def list_status():
   return 'Will be replaced later with\n'

@app.get('/values/sensor/<sensor_id>')
def get_sensor_value(sensor_id):
   return 'received sensor_id: {}.\n'.format(sensor_id)