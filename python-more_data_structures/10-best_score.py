#!/usr/bin/python3


def best_score(a_dictionary):
    if len(a_dictionary)>0:
        best_value = 0
        best_key = 0
        for i in a_dictionary.items():
            if a_dictionary[i] > best_value:
                best_key = i
        return best_key
    return a_dictionary  
