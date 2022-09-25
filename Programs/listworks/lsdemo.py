# names=["ram","hari",100,100.5,True]
# print(names)
#
# expenses=[1200,69283,89238,2553]
# print(expenses[0])
# print(expenses[1])
# print(expenses[-1])
#
# for i in range(0,4):
#     print(expenses[i])
#
# for amount in expenses:
#     print(amount)


# names=["c++","c","python","javascript","java"]
#
# for i in range(0,len(names)):
#     print(names[i])

# employee_names=["rahul","sabir","sooraj","ratheesh"]
# for i in range(0,len(employee_names)):
#    print(employee_names[i])



# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num%2==0:
#         print(num)

# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num%2!=0:
#         print(num)



# for num in numbers:
#     if num>15:
#         print(num+1)
#     elif num<15:
#         print(num-1)
#     elif num==15:
#         print(num)



# count=0
# for num in numbers:
#     if num in range(14,18):
#         count+=1
# print(count)


numbers=[3,8,-2,-7,8,2,0,1,-9,0]
p_count=0
n_count=0
z_count=0

for n in numbers:
    if n>0:
        p_count+=1
    elif n<0:
        n_count+=1
    elif n==0:
        z_count+=1
print(f"{p_count} {n_count} {z_count}")
