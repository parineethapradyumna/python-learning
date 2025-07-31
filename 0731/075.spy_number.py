n = int(input("Enter a number: "))
sum = 0
product = 1
while n>0:
    rem= n%10
    sum = sum+rem
    product= product*rem
    i = i//10
if (sum == product):
    print("Spy Number")
else:
    print("Not a Spy Number")