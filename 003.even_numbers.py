# we are creating even number calculator
# we are asking the user to enter any number
n = input("Enter a number: ")
# converting the string to int
n = int (n)
# this says that if any number that is divisible by 2 without getting any remainder that is a even number
sum = (n%2==0)
# now we have to show the output
print(f"The {n} is a even number? : {sum} ")

####OUTPUT####
# Enter a number: 8
# The 8 is a even number? : True
### When if it is not True then###
# Enter a number: 3
# The 3 is a even number? : False