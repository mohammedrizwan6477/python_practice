# Python Practice Set 1 (Beginners)
# Welcome to your first Python practice set!
# This set is based on the topics we’ve covered so far: installation, syntax, variables,
# typecasting, user input, comments, and operators.
# Try to solve each problem on your own before looking at the solution.

# Q1: Your First Program
# Write a program that prints:
# Hello, World! Welcome to Python.
print("Hello, World! Welcome to python.")

# Q2: Print a Poem
# Write a program that prints the following poem using a single print() statement:
# Twinkle, twinkle, little star,
# How I wonder what you are!
# (Hint: Use \n for a new line.)
print("Twinkle, Twinkle, little start, \
How I wonder what you are!")

# Q3: Variables & Data Types
# Create variables to store: - Your name (string)
# - Your age (integer)
# - Your height in meters (float)
# - A boolean value representing whether you are a student
# Print all of them in one line.

name = "Mohammed Rizwan"
age = int(27)
height = float(5.9)
student = False

print(f"Hello {name}. You are {age} year old and your height is {height}ft and your student id status is {student}")

# Q4: Typecasting Practice
# You are given a string:
# num = "45"
# Convert it into an integer and add 10 to it. Print the result.
num = "45"
print(int(num)+ 10)

# Q5: Taking User Input
# Write a program that:
# 1. Asks the user for their favorite food.
# 2.Prints:
# Wow! I also like <food>.
input_value = input("")
print(f"wow! I also like {input_value}")

# Q6: Simple Calculator
# Write a program that:
# 1. Takes two numbers as input from the user.
# 2. Prints their sum, difference, product, and quotient.

input_1 = input("Enter first Number: ")
input_2 = input("Enter second Number: ")
input_1 = int(input_1)
input_2 =int(input_2)
user = input_1 + input_2
print(f"output = {user}")

# Q7: Escape Sequences
# Print the following output using escape sequences:
# Harry said, "Python is awesome!"
# This is on a new line.
# This is a tab -> <- here
print("Harry said, \"Python is awesome!\"")
print("\nThis is on a new line.")
print("This is a tab -> \t<- here")

# Q8: Operator Challenge
# Write a program that:
# 1. Takes an integer as input from the user.
# 2. Prints the square and cube of that number.
input = int(input("Enter a number: "))

print(input * 5)
print(input ** 5)

# Q9: Quick Quiz (True/False)
# Mark True or False:

# 1. Python code must always end with a semicolon ;  # False
# 2. The # symbol is used for comments in Python.    # True
# 3. "123" and 123 are the same in Python.           # False
# 4. The * operator is used for multiplication.      # True
# 5. \n creates a new line.                          # True
# 6. Variables in Python can start with numbers.     # False
# 7. int("10") + 5 gives 15 .                        # True