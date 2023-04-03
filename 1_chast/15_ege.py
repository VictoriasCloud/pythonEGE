def f(x, A):
    return ((A < 50) and (x%A!=0) <= ((x%10==0) <= (x%12!=0)))


for A in range(1, 100):
    flag=1
    for x in range(1, 100):
        if f(x,A)==0:
            flag=0
            break
    if flag==1:
        print(A)






    #


