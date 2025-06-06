"""
Description: Introduction to Import Statements and File I/O
Author: Ivan Estropigan
Date: June 6, 2025
Usage: To execute, press the play button in the VSC IDE.
"""
# IMPORT STATEMENTS
import math
import random

# Variables used in this demonstration
radius = 12.5
square = 144
fruits = ["apple", "banana", "cherry"]

# USING IMPORTED MODULES
from math import sqrt

area = math.pi * radius ** 2


# RANDOM
print(random.random())  # Output: some random float < 1
print(random.randint(1, 6))  # Output: some random int (1-6)
print(random.choice(fruits)) # Output: random fruit

random.shuffle(fruits)
print(fruits) # Output: list is rearranged

# FILE I/O
file = open("example.txt", "r")
file.close()

# File operations here
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Writing to a file
file = open("output.txt", "w")
file.write("Hello world!")
file.close()

# WITH CLAUSE
with open("example.txt", "r") as file:
  content = file.read()
  print(content)



# READ INTO DICTIONARY
from pprint import pprint

data = {}
with open("dict_example.txt", "r") as input_file:
    for line in input_file:
        key, value = line.strip().split('*')
        data[key] = int(value)
print(data)
pprint(data)

