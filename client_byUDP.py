#!/usr/bin/env python

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
#udpCliSock.setblocking(0)
#udpCliSock.settimeout(0.5)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data,ADDR)
    data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data

udpCliSock.close()