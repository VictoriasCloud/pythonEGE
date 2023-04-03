d="0123456789QWERTYUIASDFGHJZXCVBNMWERTYUSDFGHCVBN"
def n_to_q(n, q):
    if n<q:
        return d[n]
    else:
        return n_to_q(n//q, q)+d[n%q]
for b in range(6, 100):
    c=n_to_q(29, b)
    #print(c)
    if c[-1:]=="5":
        print(b,"-----", c)
