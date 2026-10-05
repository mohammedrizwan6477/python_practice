# 1. If-Else Conditional Statements
# Write a program that asks the user for a number and prints whether it is
# positive, negative, or zero.
# Create a program that checks if a person is eligible to vote (age >= 18).
# Write a program that takes a number from the user and prints “Even” if it is
# even, otherwise “Odd”.

age = int(input("Enter number (positive, negative, or zero): "))

if (age > 0):
    print("Number is positive!")
elif (age < 0):
    print("Number is negative!")
else:
    print("Number is Zero")

if( age >= 18):
    print("You are eligible to Vote!")
else:
    print("You are not eligible to Vote!")


if age % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Match Case Statements
# Ask the user to enter a day number (1–7) and print the corresponding day of
# the week using match case .

num = int(input("Enter a number: "))

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
        print("Nothing")

# Write a program using match case that simulates a simple calculator.
# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case .

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num1: "))

operation = input("Enter operation (+, -, *, /): ")

match operation:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("nothing") 

