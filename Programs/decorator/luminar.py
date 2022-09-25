# class Staff(object):
#     def __init__(self,*args,**kwargs):
#         self.id=kwargs.get("id")
#         self.name=kwargs.get("name")
#         self.role=kwargs.get("role")
#     def __str__(self):
#         return self.name
#
# user=Staff(id=10,name="sreya",role="sale")
# print(user)

class Employee:
    def __init__(self,**kwargs):
        self.eid=kwargs.get("eid")
        self.ename=kwargs.get("ename")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.ename


employee=Employee(id=1,ename="sreya",role="admin")
# print(employee)

class Department():
    def __init__(self,**kwargs):
        user=kwargs.get("user")
        if user.role=="admin":
            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("not accesible")
    def __str__(self):
        return self.dept_name
department=Department(dept_name="sales",user=employee)
print(department)
print(department.user)

list.append()