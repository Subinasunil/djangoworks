pattern="ABACCD"
char_count={}
rec_char=[]
for char in pattern:
    if char in char_count:
        rec_char.append(char)

    else:
        char_count[char]=1
print(rec_char[1],"second recursive number")

