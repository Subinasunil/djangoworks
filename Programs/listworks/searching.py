lst=[10,11,12,14,15,16,17]
element=20
flag=0
for i in range(0,len(lst)):
    if element==lst[i]:
        flag=1
        break
print("elment found" if flag!=0 else "not found")