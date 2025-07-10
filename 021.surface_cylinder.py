# We are creating the surface of a Cylinder calculator
# Asking the user to enter the value of radius and height
r = input("Enter the value of Radius(r): ")
h = input("Enter the value of Height(h): ")
#Convert the string to float
r = float(r)
h = float(h)
# This is the formual of surface of a Cylinder
sum = 2*3.14*r*h+2*3.14*r**2
# Print the output
print(f"The value of Surface of a Cylinder is : {sum} Cm")

####OUTPUT####
# Enter the value of Radius(r): 8
# Enter the value of Height(h): 2
# The value of Surface of a Cylinder is : 502.40000000000003 Cm

