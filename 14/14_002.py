d="0123456789ASDFGHJKLQWERTYйцукенгшщзфывапролдячсмитьЙЦУКЕНГШЩЗФЫВАПРОЛДЯЧСМИТЬUIOPXCVBNMqwertyuiopasdfghjk"
#s=25**5 + 5**14 -5
def n_to_q(n, q):
    if n<q:
        return d[n]
    else:
        return n_to_q(n//q, q)+d[n%q]
for b in range(1, 70):
    c=str(n_to_q(b, 7))
    k=str(n_to_q(b, 6))
    o=str(n_to_q(b, 11))
    if len(c)==2:
        if len(k)==3:
            if o[-1:]=="2":
                print(b)


#print((n_to_q(s, 5)).count("4"))
