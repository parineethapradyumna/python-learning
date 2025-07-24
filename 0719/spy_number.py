n = int(input("Enter a number: "))
sum = 0
product = 1

while n > 0:
    rem = n % 10
    sum = sum +rem
    product =product* rem
    n = n// 10

if sum == product:
    print("It is a Spy number")
else:
    print("It is not a Spy number")



####OUTPUT#####
# Enter a number: 9
# 9 is a Spy number

# ######

# Enter a number: 8
# It is a Spy number

