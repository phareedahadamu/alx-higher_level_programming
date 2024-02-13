#!/usr/bin/python3
""" A script that adds all arguments to a Python list,
and then save them to a file 'add_item.json'"""

import sys
import json
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if not os.path.exists('add_item.json'):
    my_list = []
else:
    my_list = load_from_json_file('add_item.json')
i = 1
while i < len(sys.argv):
    my_list.append(sys.argv[i])
    i += 1
save_to_json_file(my_list, 'add_item.json')
load_from_json_file('add_item.json')
