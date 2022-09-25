# num1=int(input("enter a number1"))
# num2=int(input("enter a number2"))
# try:
#     res=num1/num2
#     print(f"result{res}")
#
# except Exception as e:
#     num2=int(input("enter the value"))
#     res=num1/num2
#     print(res)
# finally:
#     print("db transaction")
#     print("file operation")

# age=int(input("enter the age"))
#
# if(age<18):
#     raise Exception("not eligible for taking booster dose")
# else:
#     print("eligible")

phone_number=input("enter the number:")
if(len(phone_number)!=10):
    raise Exception("invalid phone number")
else:
    print("valid")