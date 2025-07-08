import math
# Program to calculate the Area of a Octagone
#Asking the user to enter the value
a = input("Enter the value of side(a): ")
#convert the string to float
a = float(a)
#the formula for area of a Octagone
sum = 2*(1+math.sqrt(2))*a**2
#print the statement
print(f"Area of a Octagone is: {sum} Cm")


########OUTPUT##########
# Enter the value of side(a): 4
# Area of a Octagone is: 77.25483399593904 Cm