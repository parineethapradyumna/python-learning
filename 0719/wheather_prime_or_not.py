# For Loop
n = int(input("Enter a number: "))
flag = True
for i in range(2,n//2,1):
    if (n%i==0):
        flag = False
        break
if(flag == True):
    print(f"{n}, it is a prime number")
else:
    print(f"{n}, it is ot a prime number")




# While Loop
n = int(input("Enter a number: "))
flag = True
i =2
while i<=n//2:
    if (n %i==0):
        flag = False
        break
    i = i+1

if(flag == True):
    print(f"{n}, it is a prime number")
else:
    print(f"{n}, it is ot a prime number")


####Output####
# Enter a number: 12
# 12, it is ot a prime number

#######
# Enter a number: 11
# 11, it is a prime number

########
# Enter a number: 7
# 7, it is a prime number

