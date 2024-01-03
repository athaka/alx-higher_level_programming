#!/usr/bin/python3
"""Print the alphabet in lowercase, except q aand e,
not followed by a new line."""

for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        print("{}".format(chr(i)), end="")
