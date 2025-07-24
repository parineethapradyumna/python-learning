rows = int(input("Enter a number: "))
row = rows
while row > 0:

    num_space = rows- row
    col = 1
    while (col<= num_space):
        print(" ",end = " ")
        col = col+1

    num_star = 2*row-1
    col = 1
    while (col <= num_star):
        print("*",end= " ")
        col +=1

    
    
    print()
    row -= 1
    
