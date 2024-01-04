#!/usr/bin/python3
# Author - Jonathan Esokawu

i = 0
for x in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(x - i)), end="")
    i = 32 if i == 0 else 0
