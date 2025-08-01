name = "Tony Stark"
# we can make different type of changes in our defined string.
print(name.upper())
print(name)
#this dot upper function will not directly convert our original string to upper case.instead it will give us a new string in which all the characters in our string will be in upper case!
print(name.lower())

# second : find operation
#it will find us any particular character
#if it is able to find the character in our string then in output it will tell us the index(position of it ) that starts from zero place
#if not it will give us a minus 1
print(name.find('S'))
print(name.find('Stark'))
print(name.find('stark'))

#third: replace operation
print(name.replace("Tony Stark","Iron Man"))
#but this will not replace our original string!

 