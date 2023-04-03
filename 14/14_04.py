d="0123456789QWERTYUIASDFGHJZXCVBNMWERTYUSDFGHCVBN"
def n_to_q(n, q):
    if n<q:
        return d[n]
    else:
        return n_to_q(n//q, q)+d[n%q]

for x in range(4, 36):
    if int("103", x)+11==int("103", x+1):
        print(x)
