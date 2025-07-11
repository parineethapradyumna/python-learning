a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a>b and a>c and a>d:
    print(f"Max = {a}")

elif b>a and b>c and b>d:
    print(f"Max = {b}")

elif c>a and c>b and c>d:
    print(f"Max = {c}")

elif d>a and d>b and d>c:
    print(f"Max = {d}")


####OUTPUT####
# Enter a number: 7
# Enter a number: 9
# Enter a number: 4
# Enter a number: 3
# Max = 9