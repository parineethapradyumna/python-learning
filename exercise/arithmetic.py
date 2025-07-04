#Arithmetic operations
a = input("enter a number= ")
b = input("enter a number= ")
a = int(a)
b = int(b)

sum = a+b
difference = a-b
division = a/b
product = a*b
remainder = a%b

print(f'{a}+{b} = {sum}')
print(f'{a}-{b} = {difference}')
print(f'{a}*{b} = {product}')
print(f'{a}/{b}= {division}')
print(f'{a}%{b}={remainder}')