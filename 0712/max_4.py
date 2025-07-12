a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

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
        if b>c:
            print(f"Max: {b}")
        else:
            print(f"Max: {c}")

    else:
        if b>d:
            print(f"Max = {b}")
        else:
            print(f"Max = {d}")

 

######OUTPUT#####
# Enter a number: 6
# Enter a number: 5
# Enter a number: 4
# Enter a number: 3
# Max = 6













