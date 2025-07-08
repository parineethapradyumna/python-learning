# Program to calculate the volume  of a Cylinder
#Asking the user to enter the value
r = input("Enter the value of Radius(r): ")
h = input("Enter the value of Height(h): ")
#convert the string to float
r = float(r)
h = float(h)
#The formula for volume  of a Cylinder
sum = 3.14*r**2*h
#print the statement
print(f"Volume  of a Cylinder is: {sum} Cm")



######OUTPUT########
# Enter the value of Radius(r): 4
# Enter the value of Height(h): 10
# Volume  of a Cylinder is: 502.40000000000003 Cm