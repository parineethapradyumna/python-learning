# we are calculating the simple intrest
# asking the user to enter the values
p = input("Enter the principal amount: ")
r = input("Enter the rate of intrest: ")
t = input("Enter the time period: ")
#converting the string to float
p = float(p)
r = float(r)
t = float(t)
# this is simple intrest formula
sum = p*r*t/100
# we have to print the statement
print(f"The value of Simple Intrest is: {sum}")



####OUTPUT####
# Enter tthe principal amount: 10000
# Enter the rate of intrest: 4
# Enter the time period: 1
# The value of Simple Intrest is: 400.00