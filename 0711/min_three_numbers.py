a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a < b:
    if b < c:
        print(f"Min = {b}")
    else:
        print(f"Min = {c}")
else:
    if a < c:
        print(f"Min = {a}")
    else:
        print(f"Min = {c}")

####OUTPUT####
# Enter a number: 6
# Enter a number: 7
# Enter a number: 2
# Min = 2