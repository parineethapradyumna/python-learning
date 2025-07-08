import math
# Program to calculate the Area of a pentagone
#Asking the user to enter the value
a = input("Enter the value of side(a): ")
#convert the string to float
a = float(a)
#the formula for area of a pentagone
sum =  (1/4)* math.sqrt(5*(5+2*math.sqrt(5)))*a**2

#print the answer with the statement
print(f"Area of a pentagone is: {sum} Cm")

#######OUTPUT########
# Enter the value of side(a): 5
# Area of a pentagone is: 43.01193501472417 Cm