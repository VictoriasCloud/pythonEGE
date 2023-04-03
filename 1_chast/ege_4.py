s=3240142
print(s)
digits="01234"
def n_to_q(n, q):
    if n<q:
        return digits
    else:
        return n_to_q(n//q, q)+digits[n%q]
print(n_to_q(s, 2))
