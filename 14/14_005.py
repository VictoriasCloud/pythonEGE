d="0123456789qwertyh"
def f(n,q):
    if n<q:
        return d[n]
    else:
        return f(n//q, q)+ d[n%q]
print(f(57, 4))
