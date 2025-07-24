num = []
squares = []
cube =[]
for i in range(20):
    n = i+1
    num.append(n)
    squares.append(n*n)
    cube.append(n**3)

for i in range(20):
    print(f"{num[i]}, {squares[i]}, {cube[i]}")
