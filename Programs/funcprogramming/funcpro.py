from functools import reduce
lst=[10,6,15,5,25,1,3,29]
# num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
# print(num_out)
# square=list(map(lambda n:n**2,lst))
# print(square)
# cube=list(map(lambda n:n**3,lst))
# print(cube)
even=list(filter(lambda n:n%2==0,lst))
print(even)
gt_ten=list(filter(lambda n:n>10,lst))
print(gt_ten)

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

product=reduce(lambda n1,n2:n1*n2,lst)
print(product)


max=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max)

min=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(min)
