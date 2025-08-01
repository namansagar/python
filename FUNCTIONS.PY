# 1. IN-BUIT FUNCTION:- those function which already exists in python and we can directly use them.
int()
str()
bool()
float()

# 2. MODULE FUNCTION :- many modules(in which many functions are already stored in it) exists in python and we can directly use them like math module.
import math   
print(dir(math))     # this will print every function in math module

#but if we have to pick any one function from it (let say square root) we will write
from math import sqrt
print(sqrt(16))     # this will give us the square root of any no.
# if we want to use all functions then we will use *
from math import *

# 3. USER DEFINED FUNCTION :- those function that we define by ourselves
# def function_name(parameter): 
#//do something        (here we can write block of code of that function)
 # def means we are defining a function
# parameter (like in calculator the output depends on operators(ON WHICH THE DEPENDS) so operator is the parameter of calculator)



# LET SAY WE WANT TO DEFINE FUNCTION THAT PRINTS SUM OF ANY TWO NUMBER:-

def print_sum(first, second = 4):
    print(first + second)
#after this we we call our function means we will execute it    
print_sum(1,2)    #these are our parameter whose sum is going to be our output.
# and if we forgot to write our second parameter then the value we gave to that second parameter that is going to add in first. 
# like if wrote this print_sum(1)  then it will add 4 to 1 