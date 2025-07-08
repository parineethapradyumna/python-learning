#Calculator: n-th term and sum of n terms
a = input("Enter the value of first term(a):  ")
n = input("Enter the value of Position(n):  ")
d = input("Enter the value of Common Differance(d): ")
#Converting to Integer
a = int(a)
n = int(n)
d = int(d)
#Formula of A.P
sum = (a + (n-1)*d)
#Then we can Print 
print(f"This the value of your Arthimatic Progression: {sum}")



############OUTPUT##################
# Enter the value of first term(a):  2
# Enter the value of Position(n):  5
# Enter the value of Common Differance(d): 3
# This the value of your Arthimatic Progression: 14