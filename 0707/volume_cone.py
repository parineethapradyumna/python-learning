# Program to calculate the volume  of a Cone
#Asking the user to enter the value
r = input("Enter the value of Radius(r): ")
h = input("Enter the value of Height(h): ")
#convert the string to float
r = float(r)
h = float(h)
#the formula for volume  of a Cone
sum = 3.14*(r**2) *h/3
#print the statement
print(f"Volume  of a Cone is: {sum} Cm")

########OUTPUT########
# Enter the value of Radius(r): 5
# Enter the value of Height(h): 9
# Volume  of a Cone is: 235.5 Cm