#!/usr/bin/python3
# Author: Jonathan Esokawu

def islower(c):
    """A Function that checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
