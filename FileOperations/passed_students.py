f1=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\all_students.txt","r")

f2=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\datasets\\failed.txt","r")

all_students=[]

for students in f1:

    students=students.rstrip("\n")

    all_students.append(students)

print(all_students)


failed_students=[]

for students in f2:

    students=students.rstrip("\n")

    failed_students.append(students)

print(failed_students)

# passed_students=[student for student in all_students if student not in failed_students] 

# print(passed_students)
#another method

passed_students=set(all_students)-set(failed_students)

print(set(passed_students))

f1.close()
f2.close()