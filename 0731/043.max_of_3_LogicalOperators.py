a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
if a>b and a>c:
    print(f"Max = {a}")
elif b>a and b>c:
    print(f"Max = {b}")
elif c>a and c>b:
    print(f"Max = {c}")

###OUTPUT###
# Enter a number(a): 67
# Enter a number(b): 89
# Enter a number(c): 56
# Max = 89