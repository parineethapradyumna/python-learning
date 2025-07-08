import math
# Program to calculate the surface of a Cone
#Asking the user to enter the value
r = input("Enter the value of Radius(r): ")
h = input("Enter the value of Height(h): ")
#convert the string to float
r = float(r)
h = float(h)
#the formula for surface of a Cone
sum = 3.14*r *(r + math.sqrt(h**2 + r**2))
#print the statement
print(f"Surface of a Cone is: {sum} Cm")


#########OUTPUT########
# Enter the value of Radius(r): 3
# Enter the value of Height(h): 4
# Surface of a Cone is: 75.36 Cm
