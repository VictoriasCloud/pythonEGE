def f(x, p):
    if x>=101 or p>4:
        return p==4
    if p%2!=0:
        return f(x+1,p+1) or f(x*5, p+1)
    else:
        return f(x+1,p+1) and f(x*5, p+1)
for s in range(1, 100+1):
    if f(s, 1):
        print(s)
