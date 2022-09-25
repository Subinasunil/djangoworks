master_word="aabbccaadtdteegg"
chk_word="egg"
my_dic={}
for char in master_word:
    if char in mw_dic:
        my_dic[char]+=1
    else:
        my_dic[char]=1
for char in chk_word:
    if char in mc_count:
        cur_count=mc_count[char]

