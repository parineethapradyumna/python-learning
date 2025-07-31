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

# ###OUTPUT###
# 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 