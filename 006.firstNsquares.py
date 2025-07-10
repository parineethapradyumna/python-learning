# We are creating the First N squares calculator
# asking the user to enter a value
n = input("Enter a number: ")
# convert the string to int
n = int(n)
# This the formual for sum of square of first N natural numbers 
sum = n*(n+1)*(2*n+1)/6
# We are giving the output
print(f"The value of sum of square of first N natural numbers is: {sum}")

####OUTPUT####
# Enter a number: 3
# The value of sum of square of first N natural numbers is: 14.0

