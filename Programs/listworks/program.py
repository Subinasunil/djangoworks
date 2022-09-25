master_word="abbcceddffggt"
chk_word="acg"
result=[]
# for w in master_word:
#     if w in chk_word:
#         if chk_word[0] in master_word:
#             result.append(chk_word[0])
#
#     break
# print(result)

for i in range(0,len(master_word)):
    for j in range(0,len(chk_word)):
        if chk_word[j] not in master_word:

            break
        else:
            print(f"form word {chk_word}")
            # print(chk_word[i])
            break
print("not form this word")