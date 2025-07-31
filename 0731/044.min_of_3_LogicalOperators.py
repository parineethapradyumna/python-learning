a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
if a<b and a<c:
    print(f"Min = {a}")
elif b<a and b<c:
    print(f"Min = {b}")
elif c<a and c<b:
    print(f"Min = {c}")

###Output###
# Enter a number(a): 67
# Enter a number(b): 98
# Enter a number(c): 43
# Min = 43