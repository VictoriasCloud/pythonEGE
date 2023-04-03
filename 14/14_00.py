d="0123456789ASDFGHJKLOIUYTREWXCVBN"
def n_to_q(n, q):
    if n<q:
        return d[n]
    else:
        return n_to_q(n//q, q)+d[n%q]

for b in range(1, 100):
    c=n_to_q(668, b)
    c=str(c)
    if len((c))==4 or c[-1:]=="2":
        print(b)
