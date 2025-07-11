# We are creating the maximum of three numbers
# Asking the user to enetr any three number from which there are able to find the max
# We have converted it into string to int 
a = int(input("Enter a number(a): "))
b = int(input("Enter a number(b): "))
c = int(input("Enter a number(c): "))
# if the a is greater than b
if a > b:
# if "a" is greater than "c"
    if a > c:
# Then we can print "a" is max
        print(f"Max = {a}")
# Other wise "c" is max
    else:
        print(f"Max = {c}")
# if from "a" and "b", "a" is greater than "b"
else:
# if "a" is greater than "b"
    if a > b:
# Then we can print "a" is max    
        print(f"Max = {a}")
# Other wise "b" is max
    else:
        print(f"Max = {b}")
   
####OUTPUT####
# Enter a number(a): 7
# Enter a number(b): 5
# Enter a number(c): 2
# Max = 7