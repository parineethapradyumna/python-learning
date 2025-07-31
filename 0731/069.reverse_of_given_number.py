n = int(input("Enter a number: "))
i = n
rev = 0
while (i>0):
    rem = i%10
    rev = rev*10+rem
    i = i//10
    print(rev)

####OUTPUT####
# Enter a number: 1783
# 3
# 38
# 387
# 3871