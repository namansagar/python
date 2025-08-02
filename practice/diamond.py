# (2 * i) - 1
# (n - i)
n = int(input("enter total number of rows : "))
i = 1
while i <= n:
    print((n - i)* " ",((2 * i)-1)* "*")
    i += 1
i = (n - 1)
while i >= 1:
    print((n - i)* " ",((2 * i)-1)* "*")
    i -= 1
