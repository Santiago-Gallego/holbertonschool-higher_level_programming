#!/usr/bin/python3
def best_score(a_dictionay):
    if a_dictionay == {} or a_dictionay is None:
        return None
    counter = list(a_dictionay.keys())[0]
    for key in a_dictionay.keys():
        if a_dictionay[key] > a_dictionay.get(counter):
            counter = key
    return counter
