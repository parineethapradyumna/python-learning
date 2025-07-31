a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
if a>b:
    if a>c:
        print(f"Max = {a}")
    else:
        print(f"Max = {c}")
else:
    if a>b:
        print(f"Max = {a}")
    else:
        print(f"Max = {b}")

####OUTPUT####
# Enter a number(a): 67
# Enter a number(b): 98
# Enter a number(c): 65
# Max = 98