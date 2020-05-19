#!/usr/bin/python
# -*- coding: utf-8 -*-


import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')  # 消息过滤
while True:
    response = socket.recv()
    print("response: %s" % response.decode('utf8'))
