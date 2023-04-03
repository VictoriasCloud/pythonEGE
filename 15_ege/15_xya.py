def f(a, x, y):
    return ((x*y<140)or(y>a)or(x>a))
for a in range(0, 500):
    flag=1
    for x in range(1, 500):
        for y in range(1, 500):
            if f(a, x, y)==0:
                flag=0
    if flag==1:
        print(a)
