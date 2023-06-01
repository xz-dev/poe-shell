#!/usr/bin/env python3

from os import environ
from json import dumps, loads
from poe import Client
from sys import argv
from collections.abc import Iterable
from inspect import signature


TOKEN = environ["POE_TOKEN"]

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
        parameter_list.append(float(arg))
    except:
        parameter_list.append(arg)


ui_mode = r"{input}" in parameter_list

if ui_mode:
    print("UI mode enabled")

def get_input(prompt):
    input_str_all = ""
    while True:
        try:
            input_str = input(prompt)
        except EOFError:  # Ctrl+D
            break
        input_str_all += input_str
    print()
    return input_str_all

def print_output(content):
    try:
        if not ui_mode:
            print(dumps(content))
        else:
            print(content)
    except:
        print(content)


if callable(func):
    func_parameter_list = list(signature(func).parameters)
    if ui_mode:
        print(f"function parameters: {func_parameter_list}")
    for i, parameter in enumerate(parameter_list):
        if parameter == r"{input}":
            parameter_list[i] = get_input(f"{func_parameter_list[i]}: ")
    func_return = func(*parameter_list, **parameter_dict)
    if isinstance(func_return, Iterable):
        for content in func(*parameter_list, **parameter_dict):
            print_output(content)
        print()
    else:
        print_output(func_return)
else:
    print_output(func)
