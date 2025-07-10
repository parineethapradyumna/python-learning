# We are creating sum of Cube of first N natural number calculator
# Asking the user to enter a number
n = input("Enter a number: ")
# Converting it to string to int
n = int(n) 
# This is the formula of sum of Cube of first N natural numbers
sum = (n*(n+1)/2)**2
# Printing the statement
print(f"The value of sum of Cube of first N natural numbers is : {sum}")


####OUTPUT####
# Enter a number: 2
# The value of sum of Cube of first N natural numbers is : 9.0