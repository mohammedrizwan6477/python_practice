# number = 50

# match number:
#     case 122:
#         print(f"The value is matched 122")
#     case 24:
#         print(f"The value is matched 24")
#     case 29:
#         print(f"The value is matched 29")
#     case 25:
#         print(f"The value is matched 25")
#     case 30:
#         print(f"The value is matched 30")
#     case 50:
#         print(f"The value is matched 50")
#     case _:
#         print(f"The value is not metioned")


# Q1. Simple Calculator

# Write a Python program that:

# Takes two numbers from the user.
# Takes an operator: +, -, *, or /.
# Uses match-case to perform the selected operation.
# Prints the result.
# If the user enters another operator, print "Invalid operator".

# Example:

# Enter first number: 10
# Enter second number: 5
# Enter operator: *

# Output:
# Result: 50

# Hint: Your match value should be the operator.

# num1 = float(input("Enter first Number: "))
# num2 = float(input("Enter second Number: "))
# operator = input("Enter operator (+, -, *, /): ")

# match operator:
#     case "+":
#         print("Result:", num1 + num2)
#     case "-":
#         print("Result:", num1 - num2)
#     case "*":
#         print("Result:", num1 * num2)
#     case "/":
#         print("Result:", num1 / num2)
#     case _:
#         print("Invalid operator")


# Q2. Day of the Week

# Write a Python program that:

# Takes a number from the user between 1 and 7.
# Uses match-case.
# Prints the corresponding day.

# For example:

# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# ...
# 7 → Sunday

# If the user enters anything other than 1–7, print:

# Invalid day

# Example:

# Enter day number: 3

# Output:
# Wednesday

num = int(input("Enter day number (1-7): "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")