# we store key value pair in dictionary.
#here    key= subject   value=marks of that subject
marks = {"english" : 95, "mathematics" : 98}
# to access any information let say for chemistry
print(marks["mathematics"])  # here we can write key of the subject instead of writing its index.

marks["physics"] = 97;
print(marks)
# we can also change marks
marks["physics"] = 99;
print(marks)