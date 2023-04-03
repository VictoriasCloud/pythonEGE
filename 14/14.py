d="0123456789ASDFGHJKLPOIUYTREWZCVBNMsdfghjkzxcvbnmqwertyuiop"
def n_to_q(n,q):
    if n<q:
        return d[n]
    else:
        return n_to_q(n//q, q)+d[n%q]
for b in range(0, 18):
    c=(n_to_q(b, 3))
    print(b, c)
