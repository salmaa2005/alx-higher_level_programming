#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ones = number % 10
if (ones < 0):
    ones = ones * -1
if (ones > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, ones))
elif (ones == 0):
    print("Last digit of {} is {} and is 0".format(number, ones))
elif (ones < 6 and ones != 0):
    print(f"Last digit of {number} is {ones} and is less than 6 and not 0")
