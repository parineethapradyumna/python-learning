# While Loop
n = int(input("Enter a number: "))
i = n 
rev = 0
while (i>0):
    rem = i%10
    rev = rev*10+rem
    i = i//10
print(rev)


# For loop
n = int(input("Enter a number: "))
rev =0
for i in range(n, -1, -1):
    rem = n%10
    rev = rev*10+rem
    n = n//10
print(rev)


####OUTPUT####
# Enter a number: 123
# 321
