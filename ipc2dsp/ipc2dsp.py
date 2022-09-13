import zmq
import time
import os
from time import sleep
import threading
# random number generator
from random import seed
from random import random
import signal

# Class for graceful shutdown when SIGTERM i received
class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, *args):
    self.kill_now = True

# seed random number generator
seed(1)

# ========================================================

# create events for stopping threads
stop_COM_RT = threading.Event()
stop_ZMQ_pub = threading.Event()
stop_ZMQ_REQ_REPL_Values = threading.Event()
stop_ZMQ_REQ_REPL_Cmds = threading.Event()

# ========================================================

# define commonly shared data
cvt = {
    "pressure_supply": 466.78234,
    "pressure_vacuum": 0.78234,
    "pressure_sensor_1": 1.5264572,
    "pressure_sensor_2": 1.567824572,
}

# ========================================================

def list_threads():
    print("MAIN: Active threads:")
    for thread in threading.enumerate(): 
        print("> " + thread.name)

# ========================================================

# define fcts for various threads

# COM_RT thread
# > Interface with ReTiCoP
# > BUT for now: change values in CVT
def COM_RT():
    print("Starting updating CVT data")
    while True:
        # Check if STOP event is set
        if stop_COM_RT.is_set():
            # stop this thread
            break
        # Update values in CVT
        cvt["pressure_supply"] = 400 + random()
        cvt["pressure_vacuum"] = 0 + random()
        cvt["pressure_sensor_1"] = 10 + random()
        cvt["pressure_sensor_2"] = 20 + random()
        # wait some time
        time.sleep(0.1)

# ZMQ_pub thread
# > publish data from CVT to inter-container network as PUB-SUB
def ZMQ_pub():
    print("Starting ZMQ_pub")
    # ZMQ connection
    url = "tcp://0.0.0.0:5555"
    print("Going to bind to: {}".format(url))
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind(url)  # publisher binds to port
    print("Pub bind to: {}\nSending data...".format(url))

    while True:
        # Check if STOP event is set
        if stop_ZMQ_pub.is_set():
            # stop this thread
            break
        # Update content (cvt) in python object with "cvt_obj"
        work_message = { 'cvt' : cvt }
        # Send python object as JSON in ZMQ message
        socket.send_json(work_message)
        # wait for 1 second
        time.sleep(1)
    
    print("Stopped ZMQ_pub ...")

# ZMQ_REQ_REPL_Values thread
# > Provide REQ / REPL interface for the values
def ZMQ_REQ_REPL_Values():
    while True:
        # Check if STOP event is set
        if stop_ZMQ_REQ_REPL_Values.is_set():
            # stop this thread
            break
        # Do nothing but sleep for now
        time.sleep(1)
    
    print("Stopped ZMQ_REQ_REPL_Values ...")

# ZMQ_REQ_REPL_Cmds thread
# > Provide REQ / REPL interface for the CMDs to the COM_RT
def ZMQ_REQ_REPL_Cmds():
    while True:
        # Check if STOP event is set
        if stop_ZMQ_REQ_REPL_Cmds.is_set():
            # stop this thread
            break
        # Do nothing but sleep for now
        time.sleep(1)
    
    print("Stopped ZMQ_REQ_REPL_Cmds ...")

# ========================================================

# MAIN == MAIN == MAIN

if __name__ == "__main__":        
    # Define way to gracefully shutdown when receiving SIGINT, SIGTERM
    killer = GracefulKiller()

    # Define threads
    thread_COM_RT = threading.Thread(target=COM_RT, name="COM_RT")
    thread_ZMQ_pub = threading.Thread(target=ZMQ_pub, name="ZMQ_pub")
    thread_ZMQ_REQ_REPL_Values = threading.Thread(target=ZMQ_REQ_REPL_Values, name="ZMQ_REQ_REPL_Values")
    thread_ZMQ_REQ_REPL_Cmds = threading.Thread(target=ZMQ_REQ_REPL_Cmds, name="ZMQ_REQ_REPL_Cmds")

    # Start threads
    thread_COM_RT.start()
    sleep(1)
    thread_ZMQ_pub.start()
    sleep(1)
    thread_ZMQ_REQ_REPL_Values.start()
    sleep(1)
    thread_ZMQ_REQ_REPL_Cmds.start()
    sleep(1)

    
    while not killer.kill_now:
        list_threads()
        time.sleep(5)
    
    print("Starting graceful shutdown ...")

    # Set events so that threads start stopping
    # ZMQ_REQ_REPL_Cmds 
    # send signal to stop
    stop_ZMQ_REQ_REPL_Cmds.set()
    # wait until thread has finished
    thread_ZMQ_REQ_REPL_Cmds.join()
    # ZMQ_REP_REPL_Values
    stop_ZMQ_REQ_REPL_Values.set()
    thread_ZMQ_REQ_REPL_Values.join()
    # ZMQ_Pub
    stop_ZMQ_pub.set()
    thread_ZMQ_pub.join()
    # COM_RT
    stop_COM_RT.set()
    thread_COM_RT.join()

    # List active threads > shall be none
    list_threads()

    print("=====================================")
    print("End of the program. I was killed gracefully :)")
