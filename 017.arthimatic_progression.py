# We are creating the Arthimatic Progression calculator
# Asking the user to enter the values
a = input("Enter the value of first term: ")
n = input("Enter the value of position: ")
d = input("Enter the value of common difference: ")
# Converting the string to float
a = float(a)
n = float(n)
d = float(d)
# This is the formual of Arthimatic Progression
sum = a+(n-1)*d
# Print the output
print(f"The value Arthimatic Progression calculator is : {sum} Cm")

####OUTPUT####
# Enter the value of first term: 2
# Enter the value of position: 3
# Enter the value of common difference: 5
# The value Arthimatic Progression calculator is : 12.0 Cm