age = int(input("Enter your age: "))

if age <5:
    print("Infant")
elif age <13:
    print("Child")
elif age <20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Sr.Citizen")