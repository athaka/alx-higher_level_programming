#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = abs(number) % 10

if number < 0:
    last = -last

output_format = f"Last digit of {number} is {last} and is"

if last > 5:
    output_format += " greater than 5"
elif last == 0:
    output_format += " 0"
else:
    output_format += " less than 6 and not 0"

print(output_format)
