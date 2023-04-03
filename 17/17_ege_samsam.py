A=[int(i) for i in open('17 (8).txt')]
#print(A)
count=0
max_sum=0
B=[i for i in A if i%2==1]
print(B)
d=sum(B)/len(B)
print(d)
for i in range(len(A)-1):
    if (((A[i]*A[i+1])%5==0)and((A[i]<d) or (A[i+1]<d))):
        count+=1
        if A[i]+A[i+1]>max_sum:
            max_sum=(A[i]+A[i+1])
print(count, max_sum)
