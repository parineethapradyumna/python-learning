marks_1 = int(input("Enter a number of marks(1): "))
marks_2 = int(input("Enter a number of marks(2): "))
marks_3 = int(input("Enter a number of marks(3): "))
Pass =  35
total = marks_1+marks_2+marks_3
avg = total /3
if marks_1>= Pass and marks_2>= Pass and marks_3>= Pass:
    status = "Pass"
else:
    status = "Fail"

print("        ")
print("-Report Card-")
print(f"Marks 1: {marks_1}")
print(f"Marks 2: {marks_2}")
print(f"Marks 3: {marks_3}")
print(f"Total : {total}")
print(f"Percentage : {avg}")
print(f"Status : {status}")

####OUTPUT####
# Enter a number of marks(1): 45
# Enter a number of marks(2): 67
# Enter a number of marks(3): 69
        
# -Report Card-
# Marks 1: 45
# Marks 2: 67
# Marks 3: 69
# Total : 181
# Percentage : 60.333333333333336
# Status : Pass