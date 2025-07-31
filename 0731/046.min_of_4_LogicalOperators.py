a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
d = int(input("Enter a number(d): "))
if a<b and a<c and a<d:
    print(f"Min = {a}")
elif b<a and b<c and b<d:
    print(f"Min = {b}")
elif c<a and c<b and c<d:
    print(f"Min = {c}")
else:
    print(f"Min = {d}")

###OUTPUT###
# Enter a number(a): 56
# Enter a number(b): 47
# Enter a number(c): 42
# Enter a number(d): 25
# Min = 25