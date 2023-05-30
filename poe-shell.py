#!/usr/bin/env python3

import os
from json import dumps, loads
from poe import Client
from sys import argv
from collections.abc import Iterable


TOKEN = os.environ["POE_TOKEN"]

client = Client(TOKEN)

_ = argv.pop(0)
func = getattr(client, argv.pop(0))
parameter_list = []
parameter_dict = {}

argv_first = None
try:
    argv_first = argv.pop(0)
    parameter_dict = loads(argv_first)
except:
    if argv_first is not None:
        argv.insert(0, argv_first)

for arg in argv:
    try:
        parameter_list.append(int(arg))
    except:
        parameter_list.append(arg)


def print_output(content):
    try:
        print(dumps(content))
    except:
        print(content)


if callable(func):
    func_return = func(*parameter_list, **parameter_dict)
    if isinstance(func_return, Iterable):
        for content in func(*parameter_list, **parameter_dict):
            print_output(content)
        print()
    else:
        print_output(func_return)
else:
    print_output(func)
