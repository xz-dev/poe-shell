#!/usr/bin/env python3

import os
from json import loads
from poe import Client
from sys import argv
from collections.abc import Iterable


TOKEN = os.environ["POE_TOKEN"]

client = Client(TOKEN)

_ = argv.pop(0)
func = getattr(client, argv.pop(0))
parameter_list = []
parameter_dict = {}

argv_first = argv.pop(0)
try:
    parameter_dict = loads(argv_first)
except:
    argv.insert(0, argv_first)

for arg in argv:
    try:
        parameter_list.append(int(arg))
    except:
        parameter_list.append(arg)

if callable(func):
    func_return = func(*parameter_list, **parameter_dict)
    if isinstance(func_return, Iterable):
        for content in func(*parameter_list, **parameter_dict):
            print(content)
        print()
    else:
        print(func_return)
else:
    print(func)
