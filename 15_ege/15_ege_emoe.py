def f(a, x, y):
    return (((2*x+3*y)<a) or (x>=y)or(y>24))
for a in range(1, 200):
    flag=1
    for x in range(1, 200):
        for y in range(1, 200):
            if f(a, x, y)==0:
                flag=0
                break
    if flag:
        print(a)
        break
