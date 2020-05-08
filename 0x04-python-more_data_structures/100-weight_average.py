#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    result = []
    weights = []

    for i in my_list:
        result.append(i[0] * i[1])
        weights.append(i[1])

    return sum(result) / sum(weights)
