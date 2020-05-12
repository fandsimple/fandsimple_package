#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import zmq


class server(object):

    def __init__(self, ip='127.0.0.1', port='30100'):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.address = "tcp://{}:{}".format(ip, port)
        self.socket.bind(self.address)

    def recv(self, handler):
        req_data = self.socket.recv_json()

        try:
            rep_data = handler(req_data)
        except Exception as e:
            logging.error("mq server handler except when handling %s" % req_data)
            logging.error(e)
            rep_data = {"success": False, "msg": "server internal error"}

        self.socket.send_json(rep_data)


class client(object):

    def __init__(self, ip='127.0.0.1', port='30100', recv_timeout=1000):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.address = "tcp://{}:{}".format(ip, port)
        self.socket.connect(self.address)
        self.poller = zmq.Poller()
        self.poller.register(self.socket, zmq.POLLIN)
        self.recv_timeout = recv_timeout

    def send(self, type, data):
        msg = {
            'type': type,
            'data': data
        }

        self.socket.send_json(msg)

        if self.poller.poll(self.recv_timeout):
            r = self.socket.recv_json()
            if r['success']:
                logging.debug("Notificate send [%s : %s] successfully" % (type, data))
            else:
                logging.error("Failed to notificate [%s : %s]\n Error: %s" % (type, data, r['msg']))
            return r
        else:
            self.socket.setsockopt(zmq.LINGER, 0)
            self.socket.close()
            self.poller.unregister(self.socket)
            self.socket = self.context.socket(zmq.REQ)
            self.socket.connect(self.address)
            self.poller.register(self.socket, zmq.POLLIN)
            # raise Exception('Server no response, trying reconnect.')
            logging.error("Poll timeout. Failed to notificate [%s : %s]\n " % (type, data))
            return None
