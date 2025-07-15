marks_1=int(input("Enter marks 1: "))
marks_2 = int(input("Enter marks 2: "))
marks_3 = int(input("Enter marks 3: "))
Pass = 35
total = marks_1+marks_2+marks_3
avg = total/3
status = "PASS"

if marks_1<Pass and marks_2<Pass and marks_3<Pass:
    status= "FAIL"

if avg <100 and avg >= 70:
    grade = "A"

elif avg >70 and avg >= 50:
    grade = "B"
else:
    grade = "C"


print("--Report Card--")
print("               ")
print(f"Marks 1: {marks_1}")
print(f"Marks 2: {marks_2}")
print(f"Marks 3: {marks_3}")
print(f"Total  : {total} ")
print(f"Percentage: {avg}")
print(f"Status : {status}")
print(f"Grade : {grade}")



####OUTPUT#####
# Enter marks 1: 89
# Enter marks 2: 98
# Enter marks 3: 79
# --Report Card--
               
# Marks 1: 89
# Marks 2: 98
# Marks 3: 79
# Total  : 266 
# Percentage: 88.66666666666667
# Status : PASS
# Grade : A