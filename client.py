import zmq
import json
import time

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(1): 
    socket.send(b"Is the ISS over me?")

    time.sleep(2)

    message = socket.recv()
    decoded = message.decode()
    notification = json.loads(decoded)

    if notification != []:
        print(notification[0])
    else:
        print(notification)

