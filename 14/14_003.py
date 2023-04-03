d="0123456789qwertyasdfasdfghjkzxcvbnmQWERTYUKJHGFDSAZXCVBNM"
def n_to_q(n, q):
    if n<q:
        return d[n]
    else:
        return n_to_q(n//q, q) + d[n%q]
for i in range(2, 50):
    if (n_to_q(180, i))[-1]=="0" and len(n_to_q(180, i))==3:
        print(i)
