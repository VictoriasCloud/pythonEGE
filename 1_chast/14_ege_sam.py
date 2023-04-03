x=9
digits='01234567'
def n_to_q(n, q):
    if int(n)< int(q):
        return n
    else:
        return n_to_q(n//q, q)+digits[n%q]
print(n_to_q(x, 2))
