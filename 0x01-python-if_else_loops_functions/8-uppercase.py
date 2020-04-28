#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < ord('z') + 1 and ord(str[i]) > ord('a') - 1:
            l = chr(ord(str[i]) - 32)
        else:
            l = chr(ord(str[i]))
        print("{:s}".format(l), end="")
    print("")
