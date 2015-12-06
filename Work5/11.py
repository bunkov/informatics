k,n=map(int,input().split())

A=[]
for i in range(k):
    A.append(1)
for i in range(k,n+1):
    A.append(sum(A[len(A)-k:]))

print(A[n])
