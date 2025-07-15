marks_1 =int(input("Enter marks 1: "))
marks_2 = int(input("Enter marks 2: "))
marks_3 = int(input("Enter marks 3: "))

Pass = 35
total = marks_1+marks_2+marks_3
avg = total/3

if marks_1>=Pass and marks_2>= Pass and marks_3>= Pass:
    status = "PASS"
else:
    status="FAIL"

print("               ")
print("               ")
print("--Report Card--")
print("               ")
print(f"Marks 1: {marks_1}")
print(f"Marks 2: {marks_2}")
print(f"Marks 3: {marks_3}")
print(f"Total  : {total} ")
print(f"Percentage: {avg}")
print(f"Status : {status}")