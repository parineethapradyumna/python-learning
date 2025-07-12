a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a>b and a>c:
    print(f"Max : {a}")

elif b>a and b>c:
    print(f"Max : {b}")

elif c>a and c>b:
    print(f"Max : {c}")


####OUTPUT####
# Enter a number: 7
# Enter a number: 8
# Enter a number: 5
# Max : 8
