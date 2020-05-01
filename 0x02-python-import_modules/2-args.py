#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("1 argument:")
        print("{0}: {1}".format(1, argv[1]))
    else:
        print("{} arguments:".format(count - 1))
        for i in range(1, count):
            print("{0}: {1}".format(i, argv[i]))
