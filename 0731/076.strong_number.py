n = int(input("Enter a number: "))
i = n
sum = 0
while(i>0):
    rem = i%10
    fact = 1
    for j in range(rem,1,-1):
        fact = fact*j
    sum = sum +fact
    i = i//10

if (sum ==n):
    print("Strong Number")
else:
    print("Not a strong Nmber")


####OUTPUT####
# Enter a number: 13
# Not a strong Nmber