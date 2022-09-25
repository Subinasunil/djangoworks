account={"acno":1000,"opening_date":"1-7-2022","type_acc":"saving","pname":"sreya","balance":5000}
print(account["acno"])

print(account.get("pname"))
# if "balance" in account:
#     account["balance"]=5000
# else:
#     account["balance"]=6000
account["balance"]=5000 if "balance" in account else "6000"
print(account)
if account["balance"]>5000:
    account["balance"]-=1000
else:
    account["balance"]-=500
print(account)
