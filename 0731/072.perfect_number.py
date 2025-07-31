n = int(input("Enter a number: "))
sum = 0
i = 1
while(i<=n//2):
    if(n%i==0):
       sum = sum +i
if (sum == n):
    print("It is a Perfect Nummber")
else:
    print("It is a Not a perfect number")


###OUTPUT####
# Enter a number: 28
# It is a Perfect Nummber
    