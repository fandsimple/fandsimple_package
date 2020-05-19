#!/usr/bin/python
# -*- coding: utf-8 -*-

s = open('./test.py', 'r').read()
co = compile(s, 'test.py', 'exec')
import dis
dis.dis(co)

