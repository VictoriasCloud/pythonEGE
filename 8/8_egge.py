from itertools import *
words=[]
for p in product('амух', repeat=4):
    print(p)
    s="".join(p)
    words.append(s)
print(words.index('хухх')+1)
