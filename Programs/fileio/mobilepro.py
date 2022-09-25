fread=open("mobiles.txt")
all_mobiles=[]
for line in fread:
    mobile=line.rstrip("\n").split(",")
    all_mobiles.append(mobile)
print(all_mobiles)
costly_mobile=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mobile)
fiveg=[mob for mob in all_mobiles if mob[3]=="5g"]
print(fiveg)


