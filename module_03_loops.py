"""
Description: Introduction to Loops
Author: Student Name
Date: September 2023
Usage: To execute, press the play button in the VSC IDE.
"""

# Variables used in this demonstration:
fruits = ["apple", "orange", "banana", "cherry"]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Iterate through a collection (list of fruit):
# 'fruit' is new (temporary) variable which is
# available only within the for loop block.


# FOR LOOP
for fruit in fruits:
    print("fruit")

for i in range(10): #0 -> 9
    print(i)

for i in range(2, 8): # 2 -> 7
    print(i)

for i in range(1, 10, 2): #Starts at 1 and increment by 2 1- > 9
    print(i)

for i in range (-10, 0): # -10 -> 0
    print(i)

# INPUT FUNCTION
name = input("What is your name?")
salary = float(input("What is your current salary?"))

print(f"name: {name} \nSalary: ${salary:.2f}")
# print(f"Name: {name} \nSalary: ${salary:,.2f}")

# what is this \n below?
# print(f"Name: {name} \nSalary: ${salary:,.2f}")

# WHILE LOOP
favorite_number = 0
while favorite_number < 100:
    favorite_number = int(input("Enter your favorite number (but not 7!), 100 & up to quit: "))

    if favorite_number == 7:
        print("You broke this game!")
        break
    
else:
    print("Your favorite number is too big!")

# LOOP CONTROL STATEMENTS
# CONTINUE
# USE a for loop to iterate over the range of integers from 1 to 9 (exclusive).
for number in range (1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:
        continue

    # Print all other integers
    print(number)

#BREAK:
"""
# Use a for loop to iterate over the range of integers 
for number in range(1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5:
        break
    # Print all other integers.
    print(number)
"""

# USE a for loop to iterate over the range of integers
for number in range (1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5:
        break
    # Print all other integers.
    print(number)

# Output: 1, 2, 3, 4, 5

# INFINITE LOOP
"""number = 10
while number > 0:
    number += 1
    print(number)
"""
# How could we avoid this?

# To prevent the infinite loop
number = 10
while number > 0:
    if number > 100:
        break
    number += 1
    print(number)


# NESTED LOOP
# matrix variable defined at top of editor.
# for every iteration of outer loop, inner loop will execute in its entirety

for row in matrix:
    for element in row:
        # end = ' ' overrides the line feed with a space
        print(element, end = ' ')
    # Use the empty print() function for line feed after row