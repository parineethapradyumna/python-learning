n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n // 2:
    if n % i == 0:
        sum =sum + i
        i =i+ 1
    
if (sum == n):  
    print("It is a Perfect Number")
else:
    print("It is not a Perfect Number")


    

####OUTPUT#####
# Enter a number: 4
# It is not a Perfect number

# #####

# Enter a number: 6
# It is a Perfect Number

    

