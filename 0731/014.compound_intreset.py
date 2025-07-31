p = int(input("Enter the value of principal amount: "))
r = int(input("Enter the rate of intreset: "))
t = int(input("Enter the value of time: "))
n = int(input("Enter the time value annually: "))
sum = p*(1+r/100*n)**n*t
print(f"This is the value of compound Intreset: {sum}")

###OUTPUT###
# Enter the value of principal amount: 10000
# Enter the rate of intreset: 4
# Enter the value of time: 1
# Enter the time value annually: 2
# This is the value of compound Intreset: 11664.000000000002