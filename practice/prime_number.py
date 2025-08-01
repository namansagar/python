n = int(input("enter your number : "))
flag = False
for i in range(2 , n):   
    if n % i == 0:
        flag = True
        break;

if (flag == True): print("Number is not Prime")
else: print("Number is Prime")