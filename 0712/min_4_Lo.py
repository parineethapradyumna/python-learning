a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
c = int(input("Enter a Number: "))
d = int(input("Enter a Number: "))

if a<b and a<c and a<d:
    print(f"Min = {a}")

elif b<a and b<c and b<d:
    print(f"Min = {b}")

elif c<a and c<b and c<d:
    print(f"Min = {c}")

elif d<a and d<b and d<c:
    print(f"Min = {d}")


####OUTPUT#####
# Enter a Number: 9
# Enter a Number: 3
# Enter a Number: 4
# Enter a Number: 5
# Min = 3