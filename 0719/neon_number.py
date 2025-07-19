n = int(input("Enter a number: "))
square = n*n
i = square
sum = 0
while (i>0):
       rem = i%10
       sum = sum + rem
       i = i//10
if (sum == n):
              print("This is a neon number")
else:
            print("This is not a neon number")
# Only 0,1,9 are called as neon numbers




####OUTPUT####
# Enter a number: 9
# This is a neon number

# #####

# Enter a number: 10
# This is not a neon number