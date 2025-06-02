# Variables
age = 18
sibling_age = 9

fruits = ['banana', 'strawberry', 'cherry']

number = 0
horizontal_position = 0
vertical_position = 0

# If, elif and else 
if age < 13: 
    print("Child")

elif age < 18:
    print("Teen")

elif age < 20: 
    print("Young Adult")

else: 
    print("Adult")

if horizontal_position > 0:
    if vertical_position > 0:
        print("Horizontal and Vertical are positive.")
    
    else:
        print("Horizontal is positive, but vertical is not")
else: 

    if vertical_position > 0: 
        print("Vertical is positive but horizontal is not.")
    
    else:
        print("Both horizontal and vertical are Positive.")
# Output: Horizontal and vertical are positive.

# COMPARISON OPERATORS
first_operand = 5
second_operand = 10 

print("first_operand == second opereand") # False
print("first_operand != second operand") # True
print("first_operand < second operand") # True
print("first_operand > second operand") # False
print("first_operand <= second operand") # True 
print("first_operand >= second_operand") # False

#If statement age and sibling
if age > 0 and sibling_age > 0:
    print("Both values are positive.")
if age > 9 and sibling_age > 9:
    print("At least one value is greater than 9.")
if not age > 10:
    print("Age is not greater than 10.")

# TERNARY EXPRESSIONS 
if number % 2 == 0:
    result = "Even"

else: 
    result = "Odd"
print(result)

# WRITTEN AS A TERNARY EXPRESSIONS:
result = "Even" if number % 2 == 0 else "Odd"
print(result)

# or 
print("Even" if number % 2 == 0 else "Odd")


# Checking with Conditionals
searched_fuit = "banana"

#if searched_fruit in fruits:
#    print("Found", searched_fruit)

#else:
#    print(searched_fruit, "not_ found")

# Iterate through a collection (list of fruit):
# 'fruit' isnew (temporary) variable which is 
# available only withinthe for loop block.
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


name = input("What is your name?")
salary = float(input("What is your current salary?"))

print(f"name: {name} \nSalary: ${salary:.2f}")
# what is this \n below?
# print(f"Name: {name} \nSalary: ${salary:,.2f}")

# PROGRAMMING LOOPS - WHILE LOOP
favourite_number = 0
while favourite_number < 100:
    favourite_number = int(input("Enter your favourite number (but not 7!), 100 & up to quit: "))

    if favourite_number == 7:
        print("You broke this game!")
        break
    
else: 
    print("Your favourite number is too big!")

# CONTINUE
# USE a for loop to iterate over the range of integers from 1 to 9 (exclusive).
for number in range (1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:

        continue
    # Print all other integers 
    print(number)

# Output: 1, 2, 4, 5, 7, 8


#BREAK
# USE a for loop to iterate over the range of integers
for number in range (1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5: 
        break
    # Print all other integers.
    print(number)

# Output: 1, 2, 3, 4, 5