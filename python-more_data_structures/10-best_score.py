#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        best_value = 0
        best_key = 0
        for i, value in a_dictionary.items():
            if value > best_value:
                best_key = i
                best_value = value
        return best_key
    return None  
