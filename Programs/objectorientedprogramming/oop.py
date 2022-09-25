class Student:
    def __init__(self,name,rollno,course):
        self.name=name
        self.rollno=rollno
        self.course=course
    def print_student(self):
        print(self.name,self.rollno,self.course)

    def set_student(self):
        pass


s1=Student("sreya",30,"bca")
s2=Student("sneha",30,"bca")
#s1.set_student()
s1.print_student()
s2.print_student()
