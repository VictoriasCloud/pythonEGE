s=(343**6)-(7**10)+47
k=0
while s>0:
    if s%7==6:
        k+=1
    s=s//7
print(k)
