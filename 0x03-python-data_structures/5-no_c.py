#!/usr/bin/python3
def no_c(str):
    string = list(str)
    try:
        string.remove('c')

    except ValueError:
        pass
    try:
        string.remove('C')
    except ValueError:
        pass
    str = ''.join(string)
    return (str)
