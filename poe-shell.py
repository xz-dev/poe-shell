#!/usr/bin/env python3

import os
from poe import Client
from sys import argv

TOKEN = os.environ["POE_TOKEN"]

client = Client(TOKEN)

_ = argv.pop(0)
func = getattr(client, argv.pop(0))
parameter_list = []
for arg in argv:
    try:
        parameter_list.append(int(arg))
    except:
        parameter_list.append(arg)

if callable(func):
    print(func(*argv))
else:
    print(func)
