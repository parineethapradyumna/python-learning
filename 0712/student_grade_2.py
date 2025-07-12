marks_1 = int(input("Enter Marks(1): "))
marks_2 = int(input("Enter Marks(2): "))
marks_3 = int(input("Enter Marks(3): "))

Pass = 35
total = marks_1+marks_2+marks_3
avg = total/3
status = "PASS"

if marks_1 < Pass or marks_2 < Pass or marks_3 < Pass:
    status= "FAIL"
if avg < 100 and avg >= 70:
        grade="A"
elif avg <70 and avg >=50:
       grade="B"
else:
        grade="C"

print(f"               ")
print(f"--Report Card--")
print(f"Marks(1)     : {marks_1}")
print(f"Marks(2)     : {marks_2}")
print(f"Marks(3)     : {marks_3}")
print(f"Total        : {total}")
print(f"Percentage(%): {avg}")
print(f"Status       : {status}")
print(f"Grade        : {grade}")




#####OUTPUT######
# Enter Marks(1): 50
# Enter Marks(2): 61
# Enter Marks(3): 59
               
# --Report Card--
# Marks(1)     : 50
# Marks(2)     : 61
# Marks(3)     : 59
# Total        : 170
# Percentage(%): 56.666666666666664
# Status       : PASS
# Grade        : B



# ########

# Enter Marks(1): 69
# Enter Marks(2): 79
# Enter Marks(3): 89
               
# --Report Card--
# Marks(1)     : 69
# Marks(2)     : 79
# Marks(3)     : 89
# Total        : 237
# Percentage(%): 79.0
# Status       : PASS
# Grade        : A

# ########

# Enter Marks(1): 20
# Enter Marks(2): 20
# Enter Marks(3): 20
               
# --Report Card--
# Marks(1)     : 20
# Marks(2)     : 20
# Marks(3)     : 20
# Total        : 60
# Percentage(%): 20.0
# Status       : FAIL
# Grade        : C