p = int(input("Enter the value principal amount(p): "))
r = int(input("Enter the value of rate of intrest(r): "))
t = int(input("Enter the value of time(t): "))
n = int(input("Enter the value of time anually(n): "))
sum= p*(1+r/100*n)**n*t
print(f"This is the value of compound intrest: {sum}")

####OUTPUT####
# Enter the value principal amount(p): 10000
# Enter the value of rate of intrest(r): 5
# Enter the value of time(t): 1
# Enter the value of time anually(n): 2
# This is the value of compound intrest: 12100.000000000002