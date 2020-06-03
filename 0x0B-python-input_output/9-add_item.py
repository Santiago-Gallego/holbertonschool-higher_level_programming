#!/usr/bin/python3
""" Load, Add, Save """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file

try:
    list1 = load_json("add_item.json")
    save_to_json_file(list1, "add_item.json")
except:
    list1 = []
for i in range(1, len(sys.argv)):
    list1.append(sys.argv[i])
