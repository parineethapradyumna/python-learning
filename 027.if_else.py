# We are making the if and else statement 
# Asking the user to enter there name
name = input("Enter your name: ")
# Asking the user to enter there age and we have already converted the string to int in one statement
age = int(input("Enter your age: "))
# If the user age is greater than or equa to 18 then he is eligible to vote
if age>=18:
# We have to print the statement that there are eligible to vote
    print(f"Hi {name}, Your are eligible to vote")
# Or we have to say there are not not eligible
else:
    print("Your not eligible to vote")
# At last we have to print the Thankyou for both the outputs
print("ThankYou")


####OUTPUT####
# Enter your name: Charan
# Enter your age: 19
# Hi Charan, Your are eligible to vote
# ThankYou

######

# Enter your name: Mayukha
# Enter your age: 16
# Your not eligible to vote
# ThankYou


