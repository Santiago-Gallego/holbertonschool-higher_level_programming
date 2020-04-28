#!/usr/bin/python3
for i in range(100):
    if i // 10 < i % 10:
        print("{:d}{:d}".format(i // 10, i % 10), end="")
        if i != 89:
            print(", ", end="")
        else:
            print("")
