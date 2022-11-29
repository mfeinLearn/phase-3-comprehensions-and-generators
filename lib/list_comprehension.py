#!/usr/bin/env python3

def return_evens(num_list):
    list_comprehension = [n for n in num_list if n%2==0 ]
    print(list_comprehension)
    return list_comprehension


def make_exclamation(sentence_list):
    list_comprehension = [n+'!' for n in sentence_list ]
    print(list_comprehension)
    return list_comprehension
