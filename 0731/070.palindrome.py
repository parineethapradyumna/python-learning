n = int(input("Enter a number: "))
i = n
rev = 0
while(i>0):
    rem = i%10
    rev = rev*10+rem
    i = i//10
if(rev==n):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

####OUTPUT####
# Enter a number: 123
# It is not a palindrome

# #####

# Enter a number: 121
# It is a palindrome