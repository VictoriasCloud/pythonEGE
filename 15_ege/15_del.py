def f(a,x):
    return ((a<50)and((x%a!=0)<=((x%10==0)<=(x%18!=0))))
for a in range(1,500):
    flag=1
    for x in range(1, 500):
        if f(a, x)==0:
            flag=0
    if flag==1:
        print(a)
