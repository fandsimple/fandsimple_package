#!/usr/bin/python
# -*- coding: utf-8 -*-


import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5559")

while True:
    response = socket.recv()
    print("response: %s" % response.decode('utf8'))

