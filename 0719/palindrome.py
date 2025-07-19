# While Loop
n = int(input("Enter a number: "))
i = n
rev = 0
while(i>0):
    rem = i%10
    rev = rev*10+rem
    i = i//10
if (rev == n):
    print("It is a palindrome")
else:
    print("It is not a palindrome")



# For Loop
n = int(input("Enter a number: "))
i = n
rev = 0
for i in range(n,-1,1):  
    rem = i % 10
    rev = rev * 10 + rem
    i = i // 10
if (rev == n):
    print("It is a palindrome")
else:
    print("It is not a palindrome")


####Output####
# Enter a number: 33
# It is a palindrome

######

# Enter a number: 24
# It is not a palindrome