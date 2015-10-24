from __future__ import print_function
from math import factorial

# get first line of input
ways_of_cutting = int(raw_input())

# check if there is a remaining line of input (should return "None" and exit if EOF reached)
while ways_of_cutting:
    print(factorial(ways_of_cutting))

    # get next line of input
    ways_of_cutting = int(raw_input())
