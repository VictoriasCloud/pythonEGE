d="0123456789qwertyuiasdfghjzxcvbn"
def f(n, q):
    if n<q:
        return d[n]
    else:
        return f(n//q, q)+d[n%q]
for i in range(2, 26):
    if (f(i, 4))[-2::]=="11":
        print(i)
