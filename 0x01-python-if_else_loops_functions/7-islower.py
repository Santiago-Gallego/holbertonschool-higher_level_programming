#!/usr/bin/python3
def islower(c):
    if ord(c) < ord('z') + 1 and ord(c) > ord('a') - 1:
        return True
    else:
        return False
