n = int(input("Enter a number: "))
square = n*n
i = square
sum = 0
while (i>0):
    rem = i%10
    sum = sum+rem
    i = i//10
if (sum ==n):
    print("Neon Number")
else:
    print("Not a Neon Number")

####OUTPUT####
# Enter a number: 145
# Not a Neon Number