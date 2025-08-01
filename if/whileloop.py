#in while= jab tak loop we will give our condition.our program will be continous till the condtion is true after it gets false the process will stop.
i = 1

while i <= 5:
    print(i)
    i= i + 1   #if we will will not write this equation then it will become an infinite loop that can crash our code.

# now if we have to print a pattern instead of number we would have done this.
p = 1

while p <= 5:
    print(p * "*")
    p = p + 1   #it means where

# like it is there in concatenation that our strings gets add up like that only it happens in multiplication that if we will multiply an integer with any string it will make that string that times as the number that has been multiplied by it.
#now for reverse pattern 
q = 5
while q >= 0:
    print(q * "*")
    q = q - 1