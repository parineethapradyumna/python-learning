marks_1 = int(input("Enter Marks: "))
marks_2 = int(input("Enter Marks: "))
marks_3 = int(input("Enter Marks: "))

Pass = 35
total = marks_1+marks_2+marks_3
avarage = total/3
if marks_1 >= Pass and marks_2>= Pass and marks_3>= Pass:
    status = "PASS"
else:
    status = "FAIL"


print("                      ")
print("--REPORT CARD--")
print(f"  Marks1 : {marks_1}")
print(f"  Marks2 : {marks_2}")
print(f"  Marks3 : {marks_3}")
print(f"  Total  : {total}")
print(f"  Percentage(%) : {avarage}")
print(f"  Status : {status}")