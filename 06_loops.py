
for i in range(1,11):
    print(f"6 x {i} = {6 * i}")


i = 1

while i < 11:
    print(i)
    i = i + 1
    print("->",i)

for i in range(0,20):
    if i == 13:
        break
    print(i)

for i in range(0,20):
    if i == 12:
        continue
    print(i)