# For Loop
n = int(input("Enter an number: "))
flag = True
for i in range(2,n//2+1,1):
    if (n%i == 0):
        flag = False
        break
if (flag==True):
        print("It is a prime number")
else:
        print("It is not a prime number")


# While Loop
n = int(input("Enter a number: "))
flag = True
i =2
while i<=n//2:
      if n%i==0:
            flag= False
            break
      i = +1
if (flag==True):
            print("It is a prime")
else:
            print("It is not a prime")
      


####Output####
# Enter an number: 12
# It is not a prime

# ####

# Enter an number: 11
# It is a prime