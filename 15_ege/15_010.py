def f(a,x):
    return (((x%3==0)<=(not(x%5==0))) or ( x + a >= 90))
for a in range(1, 100):
    flag=1
    for x in range(1, 100):
        if f(a,x)==0:
            flag=0
    if flag==1:
        print(a)
