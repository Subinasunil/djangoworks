f=open("abc.txt")
out=[line.rstrip("\n") for line in f]
print(out)
