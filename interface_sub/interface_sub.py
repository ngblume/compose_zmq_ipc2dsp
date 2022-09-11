import zmq
import os
import sys

def main():
    # Get values from ENV variables
    ZMQ_PUB_ADDRESS = os.environ["ZMQ_PUB_ADDRESS"]

    # ZMQ connection
    print("Going to connect to: {}".format(ZMQ_PUB_ADDRESS))
    ctx = zmq.Context()
    socket = ctx.socket(zmq.SUB) # create SUB socket
    socket.connect(ZMQ_PUB_ADDRESS)  # subscriber connects to port
    socket.setsockopt_string(zmq.SUBSCRIBE,"") # any topic

    print("Sub connected to: {}\nSending data...".format(ZMQ_PUB_ADDRESS))

    while True:
        # wait for publisher data
        recv_obj = socket.recv_json()
        print(recv_obj)
        # print("On topic {}, received data: {}".format(topic, msg))

if __name__ == "__main__":
    main()