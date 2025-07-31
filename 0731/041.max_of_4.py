a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
d = int(input("Enter a number(d): "))
if a>b:
    if a>c:
        if a>d:
            print(f"Max = {a}")
        else:
            print(f"Max = {d}")
    else:
        if c>d:
            print(f"Max = {c}")
        else:
            print(f"Max = {d}")
else:
    if b>c:
        if b>d:
            print(f"Max = {b}")
        else:
            print(f"Max = {d}")
    
    else:
        if c>d:
            print(f"Max = {c}")
        else:
            print(f"Max = {d}")

###OUTPUT###
# Enter a number(a): 78
# Enter a number(b): 98
# Enter a number(c): 56
# Enter a number(d): 55
# Max = 98