# For Loop
n = int(input("Enter a number: "))
i = n
while i>0:
    rem = i%10
    print(rem)
    i = i//10


# While Loop
n = int(input("Enter a number: "))
i =n
length = len(str(n))
for i in range(length):
    rem = n%10
    print(rem)
    n = n//10



###Output###
# Enter a number: 456789
# 9
# 8
# 7
# 6
# 5
# 4



