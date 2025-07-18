#For Loop
n= int(input("Enter a number: "))
print(1)
for i in range (2,(n//2)+1,1):
    if (n%1==0):
        print(i)

#While Loop
n = int(input("Enter a number: "))
print(1) 
i = 2
while i <= (n // 2):
    if n % i == 0:
        print(i)
    i += 1
if n > 1:
    print(n)