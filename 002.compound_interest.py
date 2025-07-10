# we are creating the compound interest calculator
# asking the user to enter the values
p = input("Enter the value of Principal amount(p): ")
r = input("Enter the value of Rate of intreset per annum(r): ")
t = input("Enter the value of time period(t): ")
n = input("Enter the value of times per year(n): ")
# converting the string to float
p = float(p)
r = float(r)
t = float(t)
n = float(n)
# this is the formula for compound interest
sum = p*(1+r/(100*n))**(n*t)
# at last we have to print the result
print(f"This is the value of Compound Interest: {sum}")


####OUTPUT####
# Enter the value of Principal amount(p): 12600
# Enter the value of Rate of intreset per annum(r):10
# Enter the value of time period(t):1
# Enter the value of times per year(n):2