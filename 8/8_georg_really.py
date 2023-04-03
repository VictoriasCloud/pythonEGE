from itertools import*
words=[]
k=0
for p in product('георгий', repeat=7):
    s="".join(p)
    if (s.count('г')==2 and s.count('е')==1 and s.count('о') ==1and s.count('р')==1and s.count('и')==1 and s.count('й')==1):
        k+=1
        if s not in words:
            words.append(s)
print(len(words), k)
