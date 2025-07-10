# we are creating odd number calculator
# we are asking the user to enter any number
n = input("Enter a number: ")
# converting the string to int
n = int (n)
# this says that if any number that is divisible by 2 but have a remainder the it is called as odd number 
sum = (n%2!=0)
# now we have to show the output
print(f"The {n} is a Odd Number? : {sum} ")

####OUTPUT####
# Enter a number: 3
# The 3 is a Odd Number? : True
### When if it is not True then###
# Enter a number: 8
# The 8 is a Odd Number? : False
