row = int(input("enter number of rows : "))
column = int(input("enter number of columns : "))
for i in range(0,row + 1):
    for j in range(0,column + 1):
        if i == 0 or j == 0 or i == row or j == column :
            print("*", end ="")
        else: print(" ",end ="")
    print("")