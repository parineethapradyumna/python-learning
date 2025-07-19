n = int(input("Enter a number: "))
i = n
sum = 0
while(i>0):
    rem = i%10
    sum = sum +(rem**3)
    i = i//10
if sum ==n:
    print("It is a arm strong number")
else:
    print("It is not a arm strong number")


####OUTPUT####
# Enter a number: 123
# It is not a arm strong number

# #####

# Enter a number: 153
# It is a arm strong number