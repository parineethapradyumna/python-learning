rows = 5
row= 1
while row<= rows:
    u_col = 1
    while u_col<= rows-row:
        print(" ",end=" ")
        u_col+=1
    s_col = 1
    while s_col<=row:
        print("*  ",end=" ")
        s_col+= 1
    print()
    row +=1

###OUTPUT###
#         *   
#       *   *   
#     *   *   *   
#   *   *   *   *   
# *   *   *   *   * 