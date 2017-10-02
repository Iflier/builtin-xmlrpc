# -*- coding: utf-8 -*-
"""
Dec:
Created on: 2017.10.02
Author: Iflier
"""
print(__doc__)


import argparse
from xmlrpc.client import ServerProxy

ap = argparse.ArgumentParser()
ap.add_argument('-c', '--contents', default='Happy', help="Content of send to\
                server")
args = vars(ap.parse_args())


proxy = ServerProxy("http://localhost:8000/", allow_none=True,
                    use_builtin_types=True)
print("Pass content: {0} to server, result: {1}".format(args['contents'],
      proxy.onePrint(args['contents'])))
