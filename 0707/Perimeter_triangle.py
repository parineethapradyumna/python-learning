#Creating the perimeter of the triangle Calculater
#asking the user to enter the value of a,b,c
a = input("Enter the length of side a: ")
b = input("Enter the length of side b: ")
c = input("Enter the length of side c: ")

# Convert the input values from string to integer
a = float(a)
b = float(b)
c = float(c)
#This is the formula of perimeter of the triangle
sum = a+b+c
#Printing the value
print(f"The Value of perimeter of the triangle is: {sum} Cm")

#######OUTPUT#######
# Enter the length of side a: 6
# Enter the length of side b: 6
# Enter the length of side c: 6
# The Value of perimeter of the triangle is: 18.0 Cm