d="0123456789qwertasdfgqwertyuiozxcvbnm,QWERTYUSDFGHZXCVBNM"
def f(n, q):
    if n<q:
        return d[n]
    else:
        return f(n//q, q)+d[n%q]
for i in range(2, 50):
    if f(12, i)=="110":
        print(i)
