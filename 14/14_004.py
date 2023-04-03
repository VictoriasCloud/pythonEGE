s=25**5+5**14-5
k=0
while s>0:
    if s%5==4:
        k+=1
    s=s//5
print(k)
