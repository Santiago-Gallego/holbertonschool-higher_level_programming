#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            else:
                r += (a ** b) / i
        except:
            r = b + a
            break
    return r
