numbers = 20
a = 0
b = 1
next = b  
count = 1

while count <= numbers:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()