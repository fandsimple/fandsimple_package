#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import argparse
from zmq_strong import mq

logger = logging.getLogger(__name__)


def t(): # 测试专用
    print('test')


evt_handlers = {
    't': t, # 测试专用
}


def handler(evt):
    if not isinstance(evt, dict):
        return {"success": False, "msg": "evt is not dict"}
    else:
        if evt['type'] in evt_handlers and isinstance(evt['data'], dict):
            res = evt_handlers[evt['type']](**evt['data'])
        else:
            return {"success": False, "msg": "unknown type %s or data require dict" % (evt['type'])}
        return {"success": True, "msg": res}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='notification.')
    parser.add_argument("--port", dest='port', default='30100', help="port to bind zmq server on")
    args = parser.parse_args()
    server = mq.server(port=args.port)

    while True:
        server.recv(handler)
