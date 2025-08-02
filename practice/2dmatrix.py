a = [[1,2,3,4],
     [4,4,3,5],
     [7,8,9,0],
     [-1,2,4,6],]

for row in range(0, 4):
    for col in range(0, 4):
        if a[row][col] % 2 == 0:
            print(a[row][col], end="")
        else: print("*", end="")
    print("")