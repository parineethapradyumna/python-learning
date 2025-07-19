# For Loop
n = int(input("Enter a number: "))
print(1)
for i in range(2,(n//2)+1,1):
    if(n%i==0):
        print(i)
print(n)



# While Loop
n = int(input("Enter a number: "))
print(1) 
i = 2
while i <= (n // 2):
    if n % i == 0:
        print(i)
    i += 1
if n > 1:
    print(n)


###Output###

# Enter a number: 12
# 1
# 2
# 3
# 4
# 6
# 12


# ######
# Enter a number: 3
# 1
# 3


# #####
# Enter a number: 11
# 1
# 11