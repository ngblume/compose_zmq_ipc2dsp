ipc2dsp

This is the process which directly communicates with the control algorithm.
Every other process, mostly the interfaces, must communicate with this process via ZMQ.

This process provides:
PUB-SUB > 5555 to publish the state of the process
REQ-REPL > 6000 to send cmds to the control system and receive replies from it.