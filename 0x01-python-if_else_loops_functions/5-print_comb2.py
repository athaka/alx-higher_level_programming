#!/usr/bin/python3
# Author: Jonathan Esokawu
"""Print numbers from 0 to 99 in a given format"""
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
