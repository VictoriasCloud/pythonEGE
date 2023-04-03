A=[int(i) for i in open('17_tresh.txt')]
max_sum=0
count=0
for i in range(len(A)):
    for k in range(i+1, len(A)):
        if (A[i]+A[k])%8==0:
            count+=1
            if (A[i]+A[k])>max_sum:
                max_sum=(A[i]+A[k])
print(count, max_sum)
