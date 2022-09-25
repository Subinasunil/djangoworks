lst=[11,12,13,14,15,12,12,100]
evenlist=[]
# lst.remove(11)
# print(lst)
# lst.append(131)
# print(lst)
for num in lst:
    if num%2==0:
        evenlist.append(num)
print(evenlist)
evenlist.sort(reverse=True)
print(evenlist)