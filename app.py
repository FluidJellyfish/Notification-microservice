
import time
import zmq
import json
from datetime import datetime, timezone


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

#timestamp format from .json file
timestampFormat = "%Y-%m-%dT%H:%M:%S"

def utcTime():
    timeInUTC = datetime.now(timezone.utc)
    strippedUTCTime = timeInUTC.strftime("%H:%M")
    return strippedUTCTime





while True:



    message = socket.recv()
    print(f"Received request: {message}")

    #opens json file and loads it into data
    file = open('notifications.json', 'r')
    data = json.load(file)

    #empty list to hold noti obj when there is a passover
    passoverTime = [] #clears between loops
    emptyList = []


    strippedUTCTime = utcTime()


    #convert timestamps into datetime so that they can be stripped for HH:MM
    for notification in data['notifications']:
        timestamps = datetime.strptime(notification["timestamp"], timestampFormat)
        strippedTimestamp = timestamps.strftime('%H:%M') #strip timestamp data to only get HH:MM
        if strippedTimestamp == strippedUTCTime:
            passoverTime.append(notification) #appends the notification with the correct timestamp to a new list
    file.close()

    time.sleep(2)
    if passoverTime != []:
        #convert passoverList to json
        jsonNoti = json.dumps(passoverTime)
        #converts jsonNoti to bytes and sends it to client
        socket.send(jsonNoti.encode())
        #passoverTime = [] #clears passoverTime
    else:
        socket.send(json.dumps(emptyList).encode()) #if it is not above send an empty list

