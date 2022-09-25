# lst=[11,12,13,14,15,12,12,100]
# oddlist=[]
# lst.remove(11)
# print(lst)
# lst.append(131)
# print(lst)
# for num in lst:
#     if num%2!=0:
#         oddlist.append(num)
# print(oddlist)
# oddlist.sort(reverse=True)
# print(oddlist)

#search an element
# lst=[10,21,34,123,5,3]
# n=34
# for num in lst:
#     if n==num:
#         print("found")
#         break
#     else:
#         print("not found")
#         break

#common nummbers from these list
lst1=[10,12,13,14,15]
lst2=[12,13,14,15,16]
dup_lst=[]
for num in lst1:
    if num in lst2:
        dup_lst.append(num)
print(dup_lst)