def f(a,x):
    return ((90%a==0)and((x%a!=0)<=((x%15==0)<=(x%20!=0))))
for a in range(1, 180):
    flag=1
    for x in range(1, 180):
        if f(a,x)==0:
            flag=0
    if flag:
        print(a)

