#!/usr/bin/env python
import socket
import os
from _thread import *
import threading
import struct

lock = threading.Lock()
data=False

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    print("over there!!!")
    global data
    while True:
        d = connection.recv(4)
        if not d:
            print("no data was sent closing socket!!!")
            break
        posicio = struct.unpack("i",d)
        print("READ POSITION IS: "+ str(posicio))
        if posicio[0]==1 and not data:
            lock.acquire()
            data=True
            lock.release()
    connection.close()


def multi_threaded_local_client(connection):
    print("-----------------yeeeeeeeeeeeeeees--------------------")
    global data
    print(data)
    while True:
        if(data):
            lock.acquire()
            data=False
            print("after")
            print(data)
            lock.release()
            break
        print("waiting robot...")
    connection.close()
        

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    if(ThreadCount==0):
        print("Main thread Starting!")
        start_new_thread(multi_threaded_client, (Client, ))
    else:
        print("SECOND THREAD")
        start_new_thread(multi_threaded_local_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()