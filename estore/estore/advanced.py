# try:
#     x=int(input("enter number"))
#     y=int(input("enter a number"))
#     z=x/y
#     print(z)
# except ZeroDivisionError:
#     print("division error")
# else:
#     print("successfull division")
try:
    x = int(input("enter number"))
    y = int(input("enter a number"))
    z = x / y
    print(z)
except:
    print("error")
else:
    print("successfull division")
