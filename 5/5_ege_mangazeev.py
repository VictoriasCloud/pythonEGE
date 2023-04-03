def alg(N):
    two=bin(N)[2:]
    if two.count("1")%2==0:
        two+="0"
    else:
        two+='1'
    return two
print(int(alg(78), 10))
