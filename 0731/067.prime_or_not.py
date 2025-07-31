n = int(input("Enter a number: "))
flag = True
i = 2
while i<=n//2:
    i = i+1
    if (n%i==0):
        flag = False
        break
if (flag == True):
    print("This is a prime number")
else:
    print("Ths is not a prime number")

####OUTPUT####
# Enter a number: 12
# Ths is not a prime number

# #####

# Enter a number: 7
# This is a prime number

    