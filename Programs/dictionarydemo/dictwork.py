employee={"name":"rishi","department":"sales","salary":10000,"workingdays":4}
print(employee["name"])
print(employee["department"])
print(employee["workingdays"])
print("offdays" in employee)
employee["offdays"]=3
print(employee)
employee["salary"]=15000
print(employee)
employee["salary"]+=1000
print(employee)