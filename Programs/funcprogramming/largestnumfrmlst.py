from functools import reduce
lst=[98,3,34,30,5,8]
str_lst=[str(n) for n in lst]
str_lst=sorted(str_lst,reverse=True)

lar_num=reduce(lambda n1,n2:(n1+n2) if (n1+n2) > (n2+n1) else (n2+n1),str_lst)
print(lar_num)



#lst=[3,4,5,6,2]
 # 3 sum pair