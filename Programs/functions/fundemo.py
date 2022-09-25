# total=sum(range(1,101))
# print(total)


def add_numbers(n1,n2):
    return n1+n2
print(add_numbers(10,20))

def sub_numbers(n1,n2):
    return n1-n2
print(sub_numbers(10,5))

def factorial(num):
    fact=1
    for i in range(1,(num+1)):
        fact=fact*i
    return fact
print(factorial(3))

#lambda functions
# def sub(n1,n2):
#     return n1-n2

sub=lambda n1,n2:n1-n2
print(sub(100,20))

def square(n):
    return n**2

def cube(n):
    return n**3


sq=lambda n:n**2

cu=lambda n:n**3

def maxtwo(n1,n2):
    return n1 if n1>n2 else n2
mtwo=lambda n1,n2: n1 if n1>n2 else n2