n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1,1):
    sum = sum+i
    print(f"Sum = {sum}")

####OUTPUT####
# Enter a number: 5
# Sum = 1
# Sum = 3
# Sum = 6
# Sum = 10
# Sum = 15