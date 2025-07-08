# Program to calculate the surface of a cylinder
#Asking the user to enter the value
r = input("Enter the value of Radius(r): ")
h = input("Enter the value of Height(h): ")
#convert the string to float
r = float(r)
h = float(h)
#the formula for surface of a cylinder
sum = 2*3.14*r*h + 2*3.14*r**2
#print the statement
print(f"Surface of a cylinder is: {sum} Cm")

########OUTPUT#########
# Enter the value of Radius(r): 5
# Enter the value of Height(h): 10
# Surface of a cylinder is: 471.0 Cm