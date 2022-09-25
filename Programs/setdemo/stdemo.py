# lst=[5,7,9,2,34,56,5,3,10]
# st=set(lst)
# print(st)
# print(dir(set))



# st1={2,4,5,6,8}
# st2={9,10,11,4,5}
# # st1.add(90)
# union_set=st1.union(st2)
# print(union_set)
# intersection_set=st1.intersection(st2)
# print(intersection_set)
# difference_set=st1.difference(st2)
# print(difference_set)

students=["ram","hari","ravi","tom","nikhil","jain","jhon"]
passed_students=["ram","hari","jain"]
stud=set(students)
print(stud)
pass_st=set(passed_students)
print(pass_st)
failed_students=stud.difference(pass_st)
print(failed_students)