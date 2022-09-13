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
    socket.setsockopt(zmq.RCVTIMEO, 2000) # set timeout of 2 seconds for RECV

    print("Sub connected to: {}".format(ZMQ_PUB_ADDRESS))

    recv_timeout_counter = 0

    while True:
        # wait for publisher data
        try:
            recv_obj = socket.recv_json()
            # decrease timeout counter if greater than 0 upon successful recv
            if (recv_timeout_counter > 0):
                recv_timeout_counter -= 1
            print(recv_obj)
        except zmq.ZMQError as e:
            if e.errno == zmq.EAGAIN:
                # timeout occured => no msg received
                # increase timeout counter upon failed recv
                recv_timeout_counter += 1
                pass
            else:
                raise
        
        print(recv_timeout_counter)
        if (recv_timeout_counter > 20):
            break

if __name__ == "__main__":
    main()