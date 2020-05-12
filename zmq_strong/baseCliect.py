#!/usr/bin/python
# -*- coding: utf-8 -*-

from zmq_strong.mq import client


base = client()

data = {}
res = base.send(type='t', data=data)
print(res)