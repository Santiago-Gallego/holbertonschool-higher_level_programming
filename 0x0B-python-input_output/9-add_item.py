#!/usr/bin/python3
""" Load, Add, Save """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    itemJs = load_from_json_file('add_item.json')
    save_to_json_file(itemJs + argv[1:], 'add_item.json')
except:
    save_to_json_file(argv[1:], 'add_item.json')
