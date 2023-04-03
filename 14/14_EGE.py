d="0123456789asdfghjklwertyuiozxcvbnm"
a=(int("65", 8))
for i in range(2, 50):
    def n_to_q(n, q):
        if n==q:
            return 1
        if n<q:
            return d[n]
        else:
            return n_to_q(n//q, q) + d[n%q]
    if str(n_to_q(a, i))=="311":
        print(i)


