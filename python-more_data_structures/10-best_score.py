#!/usr/bin/python3


def best_score(a_dictionary):
    if len(a_dictionary)>0:
        let best_key = 0
        for i in a_dictionary.keys():
            if a_dictionary[i] > best_key:
                best_key = a_dictionary[i]
        return best_key
    return a_dictionary  
