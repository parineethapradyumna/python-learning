#asking the user to enetr a number
n = input("Enter a number: ")
#converting the string to integer
n = int(n)
#If (n % 2 != 0)the any number that is NOT divisible by 2 
sum = ( n%2!=0)

#If The number is odd → result will be True
#The number is Even → result will be False 
print(f"The Number {n} is a Odd Number: {sum}")



# OUTPUT
"""
If it is a Even Number
Enter a number: 21
The Number 21 is a Odd Number: True

####

If it is a Odd Number
Enter a number: 22
The Number 22 is a Odd Number: False
"""