def greet(str,str1):
    val = str + str1
    return val

result = greet(25,50)
print(result)


# lambda function
# square = lambda x = x * x # single liner function

plus = lambda x: x + x
print(plus(5))

square = lambda x,y: x * y

print(square(3,5))