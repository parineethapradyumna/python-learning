#For loop
n = int(input("Enter a number: "))
flag = True
for i in range(2,n//2,1):
    if (n%i==0):
        flag = False
        break
if (flag==True):
    print(f"It is a prime")
else:
    print(f"Not a prime")




#While Loop
n = int(input("Enter a number: "))
flag = True
i = 2

while i <= n // 2:
    if n % i == 0:
        flag = False
        break
    i += 1

if flag == True:
    print("It is a prime")
else:
    print("Not a prime")
