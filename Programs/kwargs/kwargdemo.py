def add_nums(**kwargs):
    print(sum([v for v in kwargs.values()]))
    print(kwargs)
add_nums(n1=10,n2=20,n3=30)