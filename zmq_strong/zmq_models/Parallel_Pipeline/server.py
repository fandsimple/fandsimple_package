#!/usr/bin/python
# -*- coding: utf-8 -*-

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5557")
count = 0
while True:
    count += 1
    socket.send_string(str(count))
    print('已发送%s' % count)
    time.sleep(1)

