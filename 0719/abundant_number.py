n = int(input("Enter a number: "))
sum = 0
i = 1
while i<n:
    if n%i==0:
        sum = sum +i
        i = i+1

if sum<n:
    print("It is a abundant number")
else:
    print("It is not a abundant number")

###OUTPUT####
# Enter a number: 2
# It is a abundant number

######

# Enter a number: 28
# It is not a abundant number
