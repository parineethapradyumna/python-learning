a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
d = int(input("Enter a number(d): "))
if a>b and a>c and a>d:
    print(f"Max = {a}")
elif b>a and b>c and b>d:
    print(f"Max = {b}")
elif c>a and c>b and c>d:
    print(f"Max = {c}")
else:
    print(f"Max = {d}")


# ###OUTPUT###
# Enter a number(a): 34
# Enter a number(b): 23
# Enter a number(c): 65
# Enter a number(d): 32
# Max = 65