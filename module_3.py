# Variables
age = 18
sibling_age = 9

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

if searched_fruit in fruits:
    print("Found", searched_fruit)

else:
    print(searched_fruit, "not_ found")