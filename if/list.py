#we can store many primitive datatyopes in a list like : string ,float,boolean,integer.
marks = [95, 98, 97]
print(marks)   #  here this variable marks is a list
#now if we want to add maths as a string in this we can add it like:
#marks = [95, 98, 97, "maths"]

#and if we only want to print any single any single subject marks then we have to tell its index 

print(marks[0])

# if we only want to print only first two subjects marks and not including third marks

print(marks[1:3])    #here we will make a new list where we will tell that from which to where do we need marks of by writing its index from first to last the last index thatwe will write will not be included in the list

#we can also use -1,-2... as index this means that we are going to count index from to last to first.

print(marks[-1])


#we can also apply forloop on each item(score) in this "marks" list.


#FOR LOOP IN LIST
#lets say that we have the same list marks = [95, 98, 97]


for score in marks :
    print(score)


#we can also perform operation on list like we did it with string.


#1. append operation:- means to add something
#for example if we want to add maths marks in these three subject

marks.append(99)
print(marks)    # it will add 99 in marks


#2. insert operation:-means if we want to add marks of some different subject at an index
#code: marks.insert(index at which we want to add that number, that number)

marks.insert(0, 99)
print(marks)

#3. ro check the existence of that item in marks.

print(99 in marks)

# we cn also find the length of that list (means number of element in list)

print(len(marks))

#while loop in list:-

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

    # now if we want to clear this entire list.
marks.clear()     #this will clear the entire list
print(marks)
