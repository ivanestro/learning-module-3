# Module 3

## Description

- This module is to understand the concepts of module 3

## Author

Ivan Estropigan

## INTRODUCTION TO LOGIC AND LOOPS - CONTROL STRUCTURES

- Control Structures are essential in programming because they allow you to control the flow of your code.

- There are three types of control strucutres: Sequential, selection and iteration.

  1. Sequential statements are executed in the order they are written
  2. Selection statements are executed based on a condition.
  3. Iteration statements are executed repeatedly.

- Control structures enable you to create more complex programs that can perform different tasks based on specific conditions.

## INTRODUCTION TO LOGIC AND LOOPS - PYTHON CONTROL STRUCTURES

- In Python the primary control structures are conditional statements and loops.

- Conditional statements allow your program to make decision based on specific conditions, leading to different outcomes. 
  - "If it is raining outside, I will grab an umbrella" (otherwise I will not)
  - "If it is a weekday, I will wake up at 6am, otherwise I will wake up at 8am"

- Loops enable you to perform the same operation multiple times without writing the same code repeatedly, making your code more efficient and easier to maintain.

  - "For each grocery item on the conveyer belt I will: grab it, scan it, put it in a bag."

  - "As long as the pool is not filled, I will add water to it."

## INTRODUCTION TO LOGIC AND LOOPS - PROPER INDENTATION

- In python indentation is essential for defining code blocks within control structures, loops and functions. 
  - By adding indentation, we separate the code into sections and subsections.

- Unlike other programming languages that use brackets or keyboard to denote code blocks, python relies on indentation.
  - Proper indentation improves code readability and makes it easier to understand and maintain.

## PYTHON CONDITIONAL STATEMENTS

- Conditional Statements allow your program to make decision based on specific conditions. 

- Python has three keyboards for this purpose:

  - "If": evaluates a condition and executes the following code block if the condition is True. 
  - "If it is Friday Sept.29th then there are no classes"

- "elif": (else if ): checks another condition if the previous if statement is False 
  - "else if it October 31st then we eat candy"
  - You can have multiple elif statements.

- "else": executes the code block if none of the previous conditions are True.
  - "else/otherwise, we go to classes and work on our assignments"

## IF STATEMENT

- Go to the #Conditionals placeholder in the given file and add this if-statement

- What will this code do?
- Note: age is a given variable with a value of 18:

```csharp
if age < 13: 
    print("Child")
```

## IF-ELSE STATEMENT

- Modify the statement to add the else block:
- What will this code do?
- Note: age is a given variable with a value of 18:

``` csharp
    ""if age < 13: 
    print("Child") 
    else: print("Teen or Adult")
```

## IF-ELIF-ELSE STATEMENT

- Modify the statement to add the following elif-else block:
- What will this code do?
- Note: age is given variable with a value of 18:

```csharp
if age < 13:
    print("Child")
elif age < 18: 
    print("Teenager")
elif age < 20:
    print("Young Adult")
else:
    print("Adult")
```

## NESTED CONDITIONALS

- Nested conditionals can be useful for creating more complex decision structures.

- If the outer expression evaluates to True, then the nested condition is evaluated:

  - "If I have a car, I should make sure it is in good condition:"
  - "If the fuel tank is low, I should add more gas"
  - "If I have driven more than 5,000Kms then I should change the oil"
  - "If the windshield washer fluid is low I should fill it"

- Go to the # NESTED CONDITIONALS placeholder in the given file and add this code.
  - Note the additional indentation for the nested portion of the code.
  - Note: horizontal position and vertical position are given variables with values of 3 and 5.

```csharp
if horizontal_position > 0:
    if vertical_position > 0:
        print("Horizontal and vertical are positive.")
    else: 
        print("Horizontal is positive, but vertical is not.")

    else:
        if vertical_position > 0:
            print("Vertical is positive, but horizontal is not.") 

        else:

        print("Both horizontal and vertical are negative.") 
        # Output: Horizontal and vertical are positive. 
```

## COMPARISON OPERATORS

- Comparison operators are used to compare two values and return a boolean
- Common comparison operators in python are:
  - == (Equal To)
  - != (Not Equal To)
  - < (Less than)
  - > (Greater Than)
  - <= (Less Than Or Equal To)
  - >= (Greater Than Or Equal To)
- Go to # Comparison operators placeholder and uncomment the given code

```csharp
first_operand = 5
second_operand = 10 

print("first_operand == second operand") # False
print("first_operand != second operand") # True
print("first_operand < second operand") # True
print("first_operand > second operand") # False
print("first_operand <= second operand") # True 
print("first_operand >= second_operand") # False
```

## LOGICAL OPERATORS

- Logical operators are used to combine multiple conditions
- Python has three logical operators:
  - and (returns True if both conditions are True)
  - or (returns True if at least one of the condition is True)
  - not (returns True if the condition is False, and False if the condition is True)

- Go to # LOGICAL_OPERATORS, add these conditional statements with logical operators 
  - Note age and sibling_age are given variables with values of 18 and 9:

```csharp
#Variables
age = 10
sibling_age = 12

#If statement age and sibling
if age > 0 and sibling_age > 0:
    print("Both values are positive.")
if age > 9 and sibling_age > 9:
    print("At least one value is greater than 9.")
if not age > 10:
    print("Age is not greater than 10.")

# Output:
#Both ages are positive.
#At Least one value is greater than 9.
#Sibling age is not greater than 10. 
```

## TERNARY EXPRESSIONS

- Ternary expressions also known as conditional expressions are a more concise way of writing simple if-else statements
- They have the following syntax:
  - "value_if_true if condition else value_if_false"
  - "I will be rich if I win the lottery, otherwise I will be poor."

- Go to #TERNARY EXPRESSION and rewrite the condition as TERNARY EXPRESSION
  - Note Number is a given variable with the value of 5:
  - Note age and sibling_age are given variables with values of 18 and 9:

```csharp
# GIVEN EXPRESSIONS
if number % 2 == 0:
    result = "even"

else: 
    result = "Odd"
print(result)

# WRITTEN AS A TERNARY EXPRESSIONS:
result = "Even" if number % 2 == 0 else "Odd"
print(result)

# or 
print("Even" if number % 2 == 0 else "Odd")
```

## MEMBERSHIP CHECKING AND OPERATORS

- Membership checking is powerful technique that allows you to determine if a value is a member of a sequence such as a list, tuple, or string.
  - Aka: "Is this word/etc found in this sentence/list?"
  - It is very useful feature when working with data structures in python.

- Python provides two operators for membership checking:
  - The "in" operator: checks if "banana" is in the list of fruits.
    - For example, we can check whether a value is not present in a sequence.
  
- The "not in" operator: checks whether a value is not present in a sequence.
  - For example, we can check if "Orange" is not in the list of fruits:

- Go to # MEMBERSHIP CHECKING and add this code
  - Note fruits is a given list and contains apple, bannana and chery. 

```csharp 
print("banana" in fruits) # True

print("orange" not in fruits) # True

text = "Hello world!"
print("world" in text) # True
```

## MEMBERSHIP CHECKING WITH CONDITIONAS

- Membership checking can be combined with loops and conditionals to create more powerful and expressive code.
- For example, we can use membership checking to search for a specific element in a list.
  - We can do this by using an "if" statement and checking if the element is in the list.

```csharp
searched_fuit = "banana"

if searched_fruit in fruits:
    print("Found", searched_fruit)

else:
    print(searched_fruit, "not_ found")
```

## PROGRAMMOING LOOPS

- Loops are used in programming to execute a block of code multiple times, based on some condition or sequence of data.

- In Python, there are two types of loops: for loops amd while loops.

- For loops are used to iterate over a sequence (such as a list, tuple, dictionary, or string) and execute a block of code for each element in the sequence.

- While loops are used to execute a block of code multiple times, based on a specific condition.
  - The loop will continue to execute the block of code until the condition is no longer true.
  While loops are best when you don't know exactly how many iterations are needed.

## PROGRAMMING LOOPS - FOR LOOP

- For loops are used to iterate over a sequence (such as a list, tuple, dictionary, or string) and execute a block of code for each element in the sequence

- Modify module_03_loops.py to include the student as the author and add this code:

## PROGRAMMING LOOPS - RANGE FUNCTION

- The range function can define a range of values.
- The arguments work in similar fashion as those used with slicing:

  - Start (optional): This is the starting value of the sequence.
        - It Specifies where the sequence of numbers should begin.
        - If not provided, it is default to 0.

  - Stop (required): This is the ending value of the sequence.
        - The range() function generates numbers up to but not including this value.
        - It is a required parameter and you must specify it.

  - Step (optional): This is the step size or the increment by which the sequence should proceed.
        - It determines the difference between each consecutive value in the sequence.
        - If not provided, it defaults to 1.

## PROGRAMMING LOOPS - FOR LOOP

- A for loop can be applied to the result of a range function to iterate through the range of numbers:
- Here are some examples, you can just replace each example with the next:

```csharp 
for i in range(10): #0 -> 9
    print(i)

for i in range(2, 8): # 2 -> 7
    print(i)

for i in range(1, 10, 2) # 1 - > 9 by 2 
    print(i)

for i in range (-10, 0): # -10 -> 0
    print(i)
```

## PROGRAMMING LOOPS - INPUT FUNCTION

- The input function returns the user's input based on their response to the input's prompt.
  - "Hello! What is your name?"

- The input function always returns the data as a string.
    - Therefore, the result of the input function may need to be cast to another data type.
    - "Hello! How old are you?"

- Go to #INPUT and add this code:

```csharp 
name = input("What is your name?")
salary = float(input("What is your current salary?"))

# What is this \n below? : It is to tab down 
# print(f"Name: {name} \nSalary: ${salary:,.2f}")
```

## PROGRAMMING LOOP - WHILE LOOP

- While loops are used to execute a block of code multiple times, based on a specific condition.

- The loop will continue to execute the block of code until the condition is no longer true.
    - While loops are best used when you don't know exactly how many iterations are needed.
- Go to # WHILE LOOP and add this code:

```csharp
favorite_number = 0 
while favorite_number < = 100: 
    favorite_number = int(input("Enter your favorite number, 100 % up to quit: "))
```

- In Python, the else block can be applied to a while loop.

- The else block of a while loop is executed when the loop's conditional expressions becomes False, and the loop exits normally (that is, not through a break statement.)
  - The else block is skipped if the loop terminates prematurely using break.
- Modify the while loop as follows to include an else block:

```csharp
favorite_number = 0
while favorite_number < 100:
    favorite_number = int(input("Enter your favorite number, 100 & up to quit:"))

else:
    print("Your favorite number is too big!")
```

- We can use the "break" statement to exit a loop early
- Modify the while loop as follows to include a break statement:

```csharp
favorite_number = 0 
while favorite_number < 100:
    favorite_number = int(input("Enter your favorite number (but not 7!, 100 & up to quit:"))

    if favorite_number == 7:
        print("You broke this game!")
        break

else: 
    print("Your favorite number is too big!")
```

## LOOP CONTROL STATEMENTS - CONTINUE

- Loop control statement change the flow of loops during execution.
  - ``continue``: Skips the remaining code in the current iteration and starts the next iteration. 
  - ``break``: Terminates the loop and exits.

- Go to # LOOP CONTROL STATEMENTS and add this ``continue`` codee: 

```csharp
# CONTINUE
# USE a for loop to iterate over the range of integers from 1 to 9 (exclusive).
for number in range (1, 10):
    # Use continue statement to skip over multiples of 3.
    if number % 3 == 0:

        continue
    # Print all other integers 
    print(number)

# Output: 1, 2, 4, 5, 7, 8
```

# LOOP CONTROL STATEMENTS - BREAK

- Loop control statements change the flow of loops during execution.
    - ``continue``: Skips the remaining code in the current iteration and starts the next iteration.
    - ``break``: Terminates the loop and exits.
- Go to # LOOP CONTROL STATEMENTS and add this break code:

```csharp
#BREAK
# USE a for loop to iterate over the range of integers
for number in range (1, 10):
    # Use the break statement to exit the loop if the integer is greater than 5
    if number > 5: 
        break
    # Print all other integers.
    print(number)

# Output: 1, 2, 3, 4, 5
```

## INFINITE LOOPS, HOW TO AVOVID THEM

- Infinite loops occur when the loop's condition never becomes false, causing the loop to run indefinitely.

- To avoid infinite loops, ensure that there's a way for the loop condition to become false at some point during execution.

- Go to #INFINITE LOOP and add this code:

```csharp
number = 10
while number > 0:
    number += 1
    print(number)

# How could we avoid this?
# To prevent the infinite loop
number = 10 
while number > 0:
    if number > 100:
        break
    number += 1
    print(number)
```

## NESTED LOOPS

- Nested loops are loops within other loops. They can be useful for iteration through multidimensional data structures, such as lists of lists or grids.

- Define a matrix as a list of lists and use nested for loops to iterate through and print each element to the console.
  - Note: In programming, 'i' is often used as the counter for the outer loop, and 'j' is used for the inner loop. In this example, 'row' and 'element' are used.
  - Note: In the example below, end = overrides the default behavior of a print function by ending each printed statement with a <space> rather than a line feed.

```csharp
# for every iteration of outer loop, inner loop will execute in its entirety

for row in matrix:
    for element in row:
        # end = ' ' overrides the line feed with a space
        print(element, end = ' ')
    # Use the empty print() function for line feed after row
    print()
```

# IMPORT STATEMENTS AND BUILT-IN FUNCTIONS 

- Python has a vast library of modules that you can import into your programs to extend their functionality. Modules are essentially Python files that contain definitions and statements. We can use the import keyword followed by the module name to import the entire module into our program.

- For instance, we can import the math module, which provides mathematical functions and constants, using the following statement:

- Go to # IMPORT STATEMENTS  placeholder in the given file and add the following:
  - import math

- We can also import specific functions or classes from a module using the from ... import ... statement. For instance, to import the sqrt() function from the math module

- Add the following statement:
  - from math import sqrt

- Go to the # USING IMPORTED MODULES  placeholder in the given file and add this code:

```csharp
area = math.pi * radius ** 2

# no need to qualify with 'math.' when using sqrt
root = sqrt(square)

```

## BUILT-IN FUNCTIONS - RANDOM

- One commonly used module is the random module, which provides various functions to generate random numbers. we can import the random module using the following statement

- Go to the #IMPORT STATEMENTS placeholder in the given file and add the following:
  - import random

- We can use various methods the random module provides to generate random numbers or values.
  - We can use the random() method to generate a random float between 0 and 1:
  - We can use the randint() method to generate a random integer between two values(inclusive):
- Go to the #RANDOM placeholder in the given file and add the following:

```csharp
print(random.random()) #Output: some random float < 1
print(random.randInt(1, 6)) # Outputs: some random int (1,6)
```

- Another useful method provided by the random module is the choice() method, which randomly selects an element from a sequence( such as a list, tuple or string):

- Add the following under the #RANDOM placeholder

```csharp
print(random.choice(fruits))  # Output: random fruit
```

- Finally, we can use the shuffle() method to randomly reorder the element of a list:

```csharp
random.shuffle(fruits)
print(fruits) # Output: list is rearranged
```

## FILE INPUT/OUTPUT IN PYTHON - OPEN

- To work with files in Python, you need to open them first.

- The open() function is ued to open a file and returns a file object.
  - It takes two arguments the file's path and an optional mode.
  - The file's path is the file's location on your computer, and the mode specifies whether you want to read, write, or append to the file.
  - There are different modes ('r') write mode ("w'), append mode ('a') exclusive creation mode ('x') and binary mode ('b') which is used for non-text files, such as images.

- Once you're done working with a file, its crucial to close it.
  - To close a file, use the close() method. This ensures that your program releases the resources used by the file and ensures that the file is not left open unnecessarily.

```csharp
file = open("example.txt", "r")
# File operations here
file.close()
```

## FILE INPUT/OUTPUT - READ/WRITE

- To read/write data from/to a file, you can use the read(), readline(), readlines() and write(string) methods.
  - The read() method reads the entire content of the file as string
  - The readline() method reads a single line from the file
  - The readlines() method reads all lines from the file and returns them as a list of strings
  - Finally the write(string) method writes the specified string to the file.

- We can open() a file, read() its contents into a variable, and then print() the contents.
- We can also write() to a file, much like we would print().

```csharp
file = open ("example.txt.", "r")
content = file.read()
print(content)
file.close()

# Writing to a file
file = open("output.txt", "w")
file.write("Hello world!")
file.close()
```

## FILE INPUT/OUTPUT - WITH STATEMENT

- Using 'with' statements is considered best practice for file handling, as it helps prevent issues like file leaks or accidentally leaving a file open.

- With this statement, you can open a file and execute operations on it within the block of code under 'with.'
  - Once the block is exited, the file is automatically closed.

```csharp
with open("example.txt", "r") as file:
  content = file.read()
  print(content)
```

## READING DELIMITED DATA FROM FILES

- Often we want to handle data from files that is delimited in some way like the dict_example.txt file
  - As an aside, when printing out data structures like dictionaries, the "pretty print" function can be very useful but requires importing

```csharp
from pprint import pprint

data = {}
with open("dict_example.txt", "r") as input_file:
    for line in input_file:
        key, value = line.strip().split('*')
        data[key] = int(value)
print(data)
pprint(data)
```