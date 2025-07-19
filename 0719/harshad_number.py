n = int(input("Enter a number: "))
i = n 
sum = 0
while i>0:
    rem = i%10
    sum = sum + rem
    i =i//10
if n%sum ==0:
    print("It is a harshad number")
else:
    print("It is not a harshad number")


####OUTPUT#####
# Enter a number: 18
# It is a harshad number

# ######

# Enter a number: 78
# It is not a harshad number