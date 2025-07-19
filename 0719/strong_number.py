n = int(input("Enter a number: "))
i = n
sum = 0
while i > 0:
    rem = i % 10
#########
    fact = 1
    for j in range(1, rem + 1):
        fact =fact* j
########
    sum = sum + fact
    i //= 10

if sum == n:
    print("It is a strong number")
else:
    print("It is not a strong number")



####OUTPUT#####
# Enter a number: 145
# It is a strong number

# #####

# Enter a number: 178
# It is not a strong number
