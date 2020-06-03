#!/usr/bin/python3
"""Load, Add, Save"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


try:
    List1 = load_from_json_file('add_item.json')
except:
    List1 = []

for arguments in argv[1:]:
    List1.append(arguments)

save_to_json_file(List1, 'add_item.json')
