# We are creating the Area of a pentagone calculator
# Asking the user to enter the value
import math
a = input("Enter the value of side(a): ")
# Convert the string to float
a = float(a)
# This is the formual of area of a pentagone
sum = 1/4*math.sqrt (5*(5+2*math.sqrt(5)))*a**2
# Print the output
print(f"The value of Area of a pentagone is: {sum} Cm")

####OUTPUT####
# Enter the value of side(a): 5
# The value of Area of a pentagone is: 43.01193501472417 Cm