import math
r = float(input("Enter the value of radius: "))
h = float(input("Enter the value of height: "))
pi= 3.14
sum = pi*r*(r+math.sqrt(h**2+r**2))
print(f"This is the value of surface of cone: {sum}")

###OUTPUT###
# Enter the value of radius: 8
# Enter the value of height: 6
# This is the value of surface of cone: 452.16