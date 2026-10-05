# 3. For Loops
# Print numbers from 1 to 10 using a for loop.
# Print the multiplication table of a number (entered by user).
# Calculate the sum of all numbers from 1 to 100 using a for loop.
# Print the following pattern using a for loop:
            # *
            # **
            # ***
            # ****

for i in range(0,11):
    print(i)

num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{i} * {num} =", num * i)

sum = 0
for i in range(1,101):
    sum = sum + i
print("Total",sum)

for i in range(0,5):
    for j in range(i):
        print("*", end="")
    print()