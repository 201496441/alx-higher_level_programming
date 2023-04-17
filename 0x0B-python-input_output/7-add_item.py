#!/usr/bin/python3
"""This script adds all arguments to a Python list and saves them to a file"""

import sys
import json
from os import path
from typing import List
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: List[str], filename: str):
    """
    This function adds all arguments to a Python list and saves them to a file.

    Args:
        args: A list of arguments to add to the list
        filename: The name of the file to save the list to
    """
    my_list = []

    # check if the file exists
    if path.exists(filename):
        # if it exists, load the list from the file
        my_list = load_from_json_file(filename)

    # add the arguments to the list
    my_list.extend(args)

    # save the list to the file
    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    # remove the script name from the arguments list
    args = sys.argv[1:]
    # add the arguments to the list and save to the file
    add_item(args, "add_item.json")
