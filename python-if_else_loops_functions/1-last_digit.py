#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    value = number % 10
else:
    number = -number
    value = -1 * (number % 10)
    number = -number
if value > 5:
    print(f"Last digit of {number:d} is {value:d} and is greater than 5")
elif value == 0:
    print(f"Last digit of {number:d} is {value:d} and is 0")
elif value < 6 and value != 0:
    print(f"Last digit of {number:d} is {value:d} \
and is less than 6 and not 0")
else:
    print(f"{number:d} doesn't exist")
