x= 440+102
print(x)
digits='01234'
def n_to_q(n, q):
    if n<q:
        return digits
    else:
        return n_to_q(n//q,q)+digits[n%q]
    
print(n_to_q(x,2))

#cool!
