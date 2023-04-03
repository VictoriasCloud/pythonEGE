p=list(range(3, 14))
q=list(range(12, 23))
a=[]
for x in range(0, 30):
    if (((x in a)<=(x in p))or(x in q))==0:
        a.append(x)
print(a)
#не то
