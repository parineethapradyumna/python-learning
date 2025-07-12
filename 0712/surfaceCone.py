import math
r = int(input("Enter the value of radius(r): "))
h = int(input("Enter the value of height(h): "))
pi = 3.14
sum = pi*r*(r+ math.sqrt(h**2 + r**2))
print(f"This is the value of Surface of cone: {sum} cm")

####OUTPUT######
# Enter the value of radius(r): 3
# Enter the value of height(h): 4
# This is the value of Surface of cone: 75.36