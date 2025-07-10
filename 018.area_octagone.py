# We are creating the Area of a Octagone calculator
#Asking the user to enter the value
import math
a = input("Enter the value of side(a): ")
#convert the string to float
a = float(a)
#the formula for area of a Octagone
sum = (2*(1+math.sqrt(2))*a**2)
#print the statement
print(f"The value of Area of a Octagone is: {sum} Cm")


####OUTPUT####
# Enter the value of side(a): 7 
# The value of Area of a Octagone is: 236.5929291125633 Cm