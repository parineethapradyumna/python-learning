n = int(input("Enter a number: "))
sum = 0
for i in range(1,(2*n)+1,2):
    sum = sum+i
    print(f"Sum = {sum}")

###Output###
# Enter a number: 5
# Sum = 0
# Sum = 3
# Sum = 8
# Sum = 15
# Sum = 24