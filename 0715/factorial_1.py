n = int(input("Enter a number: "))
product = 1
for i in range(n,0,-1):
    product = product*i
    print(f"Product = {product}")


####OUTPUT####
# Enter a number: 6
# Product = 6
# Product = 30
# Product = 120
# Product = 360
# Product = 720
# Product = 720