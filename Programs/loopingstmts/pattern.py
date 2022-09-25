# for row in range(1,4):
#     for col in range(1,5):
#         print(col,end=" ")
#     print()



# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end="\t")
#     print()


# for row in range(1,5):
#     for col in range(1,row+1):
#         print("*",end="\t")
#     print()

# for row in range(1,5):
#     for col in range(5,row,-1):
#         print("*",end="\t")
#     print()



for row in range(1,5):
    for col in range(5,row,-1):
        print("#",end="\t")
    print()

