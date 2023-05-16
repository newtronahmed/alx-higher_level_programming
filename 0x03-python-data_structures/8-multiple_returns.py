#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence[0]:
        first_char = sentence[0]
    else:
        first_char = None
    t = (length, first_char)
    return t
