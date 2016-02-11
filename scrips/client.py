#!/usr/bin/env python
import socket
import time
import struct

def send_to_robot(posicio):
    # Create a TCP client to 127.0.0.1:2001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('84.88.129.200', 2005)) # Replace this for the Robot IP and Port that you have defined
        # Codifies the data to be send as 6 big-endian floats woth 4bytes each
        d = struct.pack(">f",posicio)
        # Send data
        n = s.send(d)
        print("send: {} bytes {}".format(n,d))
        time.sleep(0.1)
    except:
        print("REFUSET CONNEXIO TO ROBOT SERVER")
        print("CLOSING SOCKET :(")
        s.close()

def getStatusRobot():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('84.88.129.178', 2004)) # Replace this for the Robot IP and Port that you have defined
    # Codifies the data to be send as 6 big-endian floats woth 4bytes each
    closed=False
    while not closed:
        try:
            s.sendall('conected')
            print("waiting robot!!")
        except:
            closed=True
            break
            print("ROBOT END WORKING")
    s.close()

def send_to_local_server(posicio):
    # Create a TCP client to 127.0.0.1:2001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('84.88.129.178', 2004)) # Replace this for the Robot IP and Port that you have defined
    # Codifies the data to be send as 6 big-endian floats woth 4bytes each
    while True:
        d = struct.pack("i",posicio)
        # Send data
        print("sendingggggg...")
        print(d)
        n = s.send(d)
        print("send: {} bytes {}".format(n,d))
        time.sleep(0.1)
    s.close()

