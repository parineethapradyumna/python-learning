#For Loop
n = int(input("Enter a number: "))
product = 1
for i in range(n,0,-1):
    product = product*i
    print("Product =", product)


#While Loop
n = int(input("Enter a number: "))
product = 1
i = n
while i > 0:
    product = product * i
    i = i-1
    print("Product =", product)



####OUTPUT####
# Enter a number: 5
# Product = 5
# Product = 20
# Product = 60
# Product = 120
# Product = 120

