def f(a,x):
    return ((x&29!=0)<=((x&17==0)<=(x&a!=0)))
for a in range(1, 500):
    flag=1
    for x in range(1,500):
        if f(a,x)==0:
            flag=0
    if flag==1:
        print(a)
