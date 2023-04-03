def f(a,x):
    return (((x<a)<=(x**2<100))and((y**2<=64)<=(y<=a)))
for a in range(1,100):
    flag=1
    for x in range(1, 100):
        for y in range(1, 100):
            if f(a,x)==0:
                flag=0
    if flag==1:
        print(a)
