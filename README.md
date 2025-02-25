# Notification Microservice
Microservice A for Christian Ritchie


# Dependancies
Python3,
Zeromq, and
JSON

installation of local dependencies:

pip install pyzmq


# Communication Contract


### Requesting Data from the Microservice

You can request data from the microservice by connecting to the server using a client program. This could look something like:

```markdown
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.send(b"Requesting information")
```
The server is being hosted on port 5555. Connecting to the server requests the information. 

### Receiving Data from the Microservice
After you have successfully connected to the server you can receive the sent data like this:
```markdown
message = socket.recv()
decodedMsg = message.decode()
notification = json.loads(decodedMsg)
```
The returned notification includes:

the timestamp, type, contact, and message as seen within the notifications.json file
















