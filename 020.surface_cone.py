# We are creating the surface of a Cone calculator
# Asking the user to enter the value of radius and height
import math
r = input("Enter the value of Radius(r): ")
h = input("Enter the value of Height(h): ")
# Convert the string to float
r = float(r)
h = float(h)
# The formula for surface of a Cone
sum = 3.14*r *(r + math.sqrt(h**2 + r**2))
# Print the statement
print(f"Surface of a Cone is: {sum} Cm")


####OUTPUT####
# Enter the value of Radius(r): 9
# Enter the value of Height(h): 6
# Surface of a Cone is: 560.0186371338372 Cm