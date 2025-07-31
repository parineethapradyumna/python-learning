a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
d = int(input("Enter a number(d): "))
if a<b:
    if a<c:
        if a<d:
            print(f"Min = {a}")
        else:
            print(f"Min = {d}")
    else:
        if c<d:
            print(f"Min = {c}")
        else:
            print(f"Min = {d}")
else:
    if b<c:
        if b<d:
            print(f"Min = {b}")
        else:
            print(f"Min = {d}")
    
    else:
        if c<d:
            print(f"Min = {c}")
        else:
            print(f"Min = {d}")

####OUTPUT####
# Enter a number(a): 89
# Enter a number(b): 78
# Enter a number(c): 34
# Enter a number(d): 12
# Min = 12