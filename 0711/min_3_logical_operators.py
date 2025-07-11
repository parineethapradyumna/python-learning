a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))



if a < b and a < c:
    print(f"Min = {a}")

elif b < a and b < c:
    print(f"Min = {b}")

elif c < a and c < b:
    print(f"Min = {c}")


####OUTPUT####
# Enter a number: 6
# Enter a number: 4
# Enter a number: 3
# Min = 3
