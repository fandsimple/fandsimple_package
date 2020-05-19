#!/usr/bin/python
# -*- coding: utf-8 -*-


import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send_string('Are you OK?')
response = socket.recv()
print("response: %s" % response)
