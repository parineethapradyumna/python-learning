a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a<b and a<c and a<d:
    print(f"Min = {a}")

elif b<a and b<c and b<d:
    print(f"Min = {b}")

elif c<a and c<b and c<d:
    print(f"Min = {c}")

elif d<a and d<b and d<c:
    print(f"Min = {d}")

####OUTPUT####
# Enter a number: 9
# Enter a number: 4
# Enter a number: 6
# Enter a number: 2
# Min = 2