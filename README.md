# Module 3

## Description

- This module is to understand the concepts of module 3

## Author

Ivan Estropigan

## INTRODUCTION TO LOGIC AND LOOPS - CONTROL STRUCTURES: 

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

- Loops enable you to perform the same operation multiple times without writing the same code repeatedly, making your code more efficent and easier to maintain.

  - "For each grocery item on the conveyer belt I will: grab it, scan it, put it in a bag."

  - "As long as the pool is not filled, I will add water to it."

## INTRODUCTION TO LOGIC AND LOOPS - PROPER INDENTATION 

- In python indentation is essential for defining code blocks within control structues, loops and functions. 
  - By adding indentation, we seperate the code into sections and subsections.

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
  - Note: horizonal position and vertical position are given variables with values of 3 and 5.

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

print("first_operand == second opereand") # False
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
  - "value_if_true if conditiom else value_if_false"
  - "I will be rich if I win the lottery, otherwise I will be poor."

- Go to #TERNARY EXPRESSION and rewrite the condition as TERRARY EXPRESSION
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
  - The "in" opereator: checks if "banana" is in the list of fruits.
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

- While loops are used to execute a block of code multiple times, based on a sepcific condition.

- The loop will continue to execute the block of code until the condition is no longer true.
    - While loops are best used when you don't know exactly how many iterations are needed.
- Go to # WHILE LOOP and add this code:

```csharp
favourite_number = 0 
while favourite_number < = 100: 
    favoureite_number = int(input("Enter your favourite number, 100 % up to quit: "))
```

- In Python, the else block can be applied to a while loop.

- The else block of a while loop is executed when the loop's conditional expressions becomes False, and the loop exits normally (that is, not through a break statement.)
  - The else block is skipped if the loop terminates prematurely using break.
- Modify the while loop as follows to include an else block:

```csharp
favourite_number = 0
while favourite_number < 100:
    favourite_number = int(input("Enter your favourite number, 100 & up to quit:"))

else:
    print("Your favourite number is too big!")
```

- We can use the "break" statement to exit a loop early
- Modify the while loop as follows to include a break statement:

```csharp
favourite_number = 0 
while favourite_number < 100:
    favourite_number = int(input("Enter your favourite number (but not 7!, 100 & up to quit:"))

    if favourite_number == 7:
        print("You broke this game!")
        break

else: 
    print("Your favourite number is too big!")
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
