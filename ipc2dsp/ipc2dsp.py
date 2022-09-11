import zmq
import time
import os

# define fct for publisher with default values for ip and port
def main():
    # ZMQ connection
    url = "tcp://0.0.0.0:5555"
    print("Going to bind to: {}".format(url))
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind(url)  # publisher binds to port
    print("Pub bind to: {}\nSending data...".format(url))

    # Initialize counter "num" with value 0
    num = 0

    while True:
        # Update content in python object
        work_message = { 'num' : num }
        # Send python object as JSON in ZMQ message
        socket.send_json(work_message)
        # Print current num to console for debugging
        print("Sending msg with {} ...".format(num))
        # Increase counter "num"
        num += 1
        # wait for 1 second
        time.sleep(1)

# start publisher
if __name__ == "__main__":
    main()