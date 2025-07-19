#arm strong
# limit = int(input("Enter the limit: "))

# for num in range(1, limit + 1):
#     temp = num
#     order = len(str(num))
#     sum = 0

#     for digit_char in str(num):  # Nested loop over each digit
#         digit = int(digit_char)
#         power = 1

#         for i in range(order):   # Inner nested loop to calculate digit ** order
#             power *= digit
        
#         sum += power

#     if sum == num:
#         print(f"{num} is an Armstrong number")










# # Check if a number is a Strong Number using nested for loop
# num = int(input("Enter a number: "))
# temp = num
# sum = 0

# # Outer loop to extract each digit
# for digit in str(num):
#     digit = int(digit)
#     fact = 1
    
#     # Inner loop to calculate factorial
#     for i in range(1, digit + 1):
#         fact = fact * i
    
#     sum += fact

# # Check if sum of factorials equals the number
# if sum == num:
#     print(f"{num} is a Strong Number")
# else:
#     print(f"{num} is not a Strong Number")








# # Check whether a number is a perfect number
# num = int(input("Enter a number: "))
# sum = 0

# # Loop to find all divisors of the number (excluding itself)
# for i in range(1, num):
#     if num % i == 0:
#         sum = sum + i

# # Check if sum of divisors equals the number
# if sum == num:
#     print(f"{num} is a Perfect Number")
# else:
#     print(f"{num} is not a Perfect Number")
















# # Check if a number is a Neon number using for loop
# num = int(input("Enter a number: "))
# square = num * num
# sum_digits = 0

# # Convert square to string and loop through digits
# for digit in str(square):
#     sum_digits += int(digit)

# # Compare sum with original number
# if sum_digits == num:
#     print(f"{num} is a Neon Number")
# else:
#     print(f"{num} is not a Neon Number")

