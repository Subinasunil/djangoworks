students=open("students.txt")
all_students=[stud.rstrip("\n") for stud in students]
f_students=open("failed.txt")
failed_students=[stud.rstrip("\n") for stud in f_students]
passed=open("passed.txt","w")

passed_students=set(all_students)-set(failed_students)
print(passed_students)
for st in passed_students:
    st+="\n"
    passed.write(st)


