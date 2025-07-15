n = int(input("Enter a number: "))
sum = 0
for i in range(1,(2*n)+1,2):
    sum = sum+i
    print(f"Sum = {sum}")


####OUTPUT#####
# Enter a number: 5
# Sum = 1
# Sum = 4
# Sum = 9
# Sum = 16
# Sum = 25