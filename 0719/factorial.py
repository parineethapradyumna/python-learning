# For Loop
n = int(input("Enter a number: "))
product = 1
for i in range(n,0,-1):
    product = product*i
    print(product)



# While Loop
n = int(input("Enter a number: "))
product =1
i = n
while i>0:
    product = product *i
    i = i-1
    print(product)


###Output###
# Enter a number: 5
# 5
# 20
# 60
# 120
# 120