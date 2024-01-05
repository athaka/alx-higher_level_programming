#!/usr/bin/python3
# Author: Jonathan Esokawu

from sys import argv

if __name__ == "__main__":
    # Extract command-line arguments (excluding the script name)
    arguments = argv[1:]

    # Convert each argument to an integer and sum them
    result = sum(int(arg) for arg in arguments)

    # Print the result
    print(result)
