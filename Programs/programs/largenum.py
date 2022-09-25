from functools import reduce
lst=[98,3,34,30,5,8]
str_lst=[str(n) for n in lst]
lar_num=reduce(lambda n1,n2:(n1+n2) if (n1+n2) > (n2+n1) else (n2+n1),str_lst)
num_sort=sorted(lar_num,reverse=True)
large_num=reduce(lambda n1,n2:n1+n2,num_sort)
print(large_num)