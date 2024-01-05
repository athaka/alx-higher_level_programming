#!/usr/bin/python3
# Author: Jonathan Esokawu

if __name__ == "__main__":
    from sys import argv

    # Subtract 1 to exclude the script name
    num_arguments = len(argv) - 1

    # Print the number of arguments and whether it's singular or plural
    print("{} argument{}".format(num_arguments,
                                 "s" if num_arguments != 1 else ""), end="")

    # Check if there are any arguments
    if num_arguments > 0:
        print(":", end="\n")

        # Print each argument and its position
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print(".")
