# #For loop
# n = int(input("Enter a number: "))
# for i in range(1,n+1,1):
#     if n %i ==0:
#         print(i)


#While Loop
n = int(input("Enter a number: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
        i += 1
