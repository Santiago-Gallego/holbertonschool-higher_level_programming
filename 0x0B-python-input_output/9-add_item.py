#!/usr/bin/python3
""" Load, Save """
from sys import argv

load_json = __import__('8-load_from_json_file').load_from_json_file
save_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    li = load_json('add_item.json')
    save_json_file(li + argv[1:], 'add_item.json')
except Exception:
    save_json_file(argv[1:], 'add_item.json')
