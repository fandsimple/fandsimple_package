#!/usr/bin/python
# -*- coding: utf-8 -*-

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    print('发送消息')
    socket.send_string("消息群发")
    time.sleep(1)
