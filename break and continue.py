#BREAK:-
students = ["ram", "shyam", "kishan", "Radha", "Radhika"]

for student in students:
    if student == "Radha":
        break;
    print(student)

#CONTINUE:-
#suppose kishan has left this school and now we dont want to print kishan's name. 
for student in students:
    if student == "kishan":
        continue;    #means run the loop again but dont do any work of the present loop. 
    print(student)