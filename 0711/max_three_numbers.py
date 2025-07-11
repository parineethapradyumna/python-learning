a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a > b:
    if a >c:
        print(f"Max = {a}")
    else:
        print(f"Max = {c}")
else:
    if a > b:
        print(f"Max = {a}")
    else:
        print(f"Max = {b}")

####OUTPUT####
# Enter a number: 9
# Enter a number: 7
# Enter a number: 8
# Max = 9
