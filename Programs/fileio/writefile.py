f=open("abc.txt","w")
lst=["python","javascript","c#"]
for lan in lst:
    lan+="\n"
    f.write(lan)