#asking the user to enetr a number
n = input("Enter a number: ")
#converting the string to integer
n = int(n)
#If (n % 2 == 0)the any number that is divisible by 2 without giving the remainder..
sum = ( n%2==0)

#The number is Even → result will be True
#If The number is odd → result will be False 
print(f"The Number {n} is a Even Number: {sum}")


"""
If it is a Even Number
Enter a number: 22
The Number 22 is a Even Number: True

####

If it is a Odd Number
Enter a number: 23
The Number 23 is a Even Number: False
"""