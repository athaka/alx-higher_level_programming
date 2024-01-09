#!/usr/bin/python3
# Author: Jonathan Esokawu


def multiple_returns(sentence):
    a = len(sentence)
    if sentence == "":
        return (a, None)
    else:
        return (a, sentence[0])
