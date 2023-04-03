def f(n):
    if n==1:
        return 1
    if n>1:
        return G(n-1)+5*n
def G(n):
    if n>1:
        return 2*f(n-1)*n
    if n==1:
        return 0
print(f(4)-G(3))
