#!/usr/bin/python3
# Author: Jonathan Esokawu


def print_last_digit(number):
    """Function to prints the last digit of a number"""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
