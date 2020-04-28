#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n2 = abs(number) % 10
if number < 0:
    n2 = n2 * -1
if n2 > 5:
    print("Last digit of",number," is ",n2," and is greater than 5")
elif n2 < 6 and n2 != 0:
    print("Last digit of",number,"is",n2,"and is less than 6 and not 0")
else:
    print("Last digit of",number,"is",n2,"and is 0")
