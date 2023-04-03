A = [int(i) for i in open('17 (5).txt')]
#print(A)
count = 0
max_sum = 0
for i in range(len(A)-1):
    if (A[i]*A[i+1])%15==0 and ((A[i]+A[i+1])%7==0):
        count+=1
        if (A[i]+A[i+1]) > max_sum:
            max_sum=A[i]+A[i+1]
print(count, max_sum)
