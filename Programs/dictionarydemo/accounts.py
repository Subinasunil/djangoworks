accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
]

#q4 prit all phone pay transactions

# all_trans=[ac["transactions"] for ac in accounts]
# phn_pay=[trans for tlist in all_trans for trans in tlist if trans["method"]=="phone-pay"]
# print(phn_pay)

#q4 prit all transactions where transaction amount > 500

# all_trans=[ac["transactions"] for ac in accounts]
# trans_amt=[trans for tlist in all_trans for trans in tlist if trans["amount"]>500]
# print(trans_amt)

#q5 crredit transactions of 1002

# all_trans=[ac["transactions"] for ac in accounts]
# credit_trans=[trans for tlist in all_trans for trans in tlist if trans["to"]==1002]
# print(credit_trans)


#q6 aggregate transactions based on payment mode

pms={}
all_trans=[ac["transactions"] for ac in accounts]
transactions=[t for tlist in all_trans for t in tlist]
for transaction in transactions:
    p_methods=transaction["method"]
    amount=transaction["amount"]
    if p_methods in pms:
        pms[p_methods]+=amount
    else:
        pms[p_methods]=amount
print(pms)

max_amt=max(pms.items(),key=lambda it:it[1])
print(max_amt)