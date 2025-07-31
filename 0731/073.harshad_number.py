n = int(input("Enter a number: "))
i = n
sum = 0
while i>0:
    rem= i%10
    sum = sum +rem
    i = i//10
if (n%sum==0):
    print("Harshad Number")
else:
    print("Not a Harshad number")

###OUTPUT###
# Enter a number: 45
# Harshad number

# ######

# Enter a number: 321
# Not a Harshad number