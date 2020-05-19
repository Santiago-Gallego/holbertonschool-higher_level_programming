#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        s = "Exception: " + str(e) + "\n"
        sys.stderr.write(s)
        return None
