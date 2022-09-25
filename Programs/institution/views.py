class Course:
    course_name:str
    active_status:bool

    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")

    def __str__(self):
        return self.course_name


class Batch:
    course:Course
    batch_code:str
    start_date:str

    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code

class Student:
    student_name:str
    gender:str
    roll:str
    batch:Batch
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.roll=kwargs.get("roll")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name


django=Course()
django.add_course(course_name="django",active_status=True)

bigdata=Course()
bigdata.add_course(course_name="bigdata",active_status=True)

db1=Batch()
db1.add_batch(course=django,batch_code="djmay2022",start_date="5-7-2022")

bg1=Batch()
bg1.add_batch(course=bigdata,batch_code="bgmay2022",start_date="6-7-2022")

# print(db1)
# print(bg1)

rishi=Student()
rishi.add_student(student_name="rishi",gender="male",roll="534",batch=db1)

sneha=Student()
sneha.add_student(student_name="sneha",gender="female",roll="234",batch=db1)

sreya=Student()
sreya.add_student(student_name="sreya",gender="female",roll="986",batch=bg1)
print(sreya.batch)
print(rishi.batch.course.course_name)
