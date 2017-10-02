# -*- coding: utf-8 -*-
"""
Dec:
Created on: 2017.10.02
Author: Iflier
"""
print(__doc__)


from xmlrpc.server import SimpleXMLRPCServer


def onePrint(contents):
    """RPC function"""
    print("I'm server, received an arguments: {0}.".format(contents))
    return contents

server = SimpleXMLRPCServer(('127.0.0.1', 8000))
print("Server listening on port 8000 ...")
server.register_function(onePrint, "onePrint")
server.serve_forever()
