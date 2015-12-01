#Exercise 4.1
A=list(map(int,input().split()))
for i in range(0,len(A)-1,2):
	A[i],A[i+1]=A[i+1],A[i]
print(' '.join(map(str,A)))
#Exercise 4.2
A=list(map(int,input().split()))
a=list(map(int,str(A.pop()))) #6_9
print(' '.join(map(str,a+A)))
#Exercise 4.3
A=list(map(int,input().split()))
for i in range(len(A)):
	if A.count(A[i])==1:
		print(A[i],end=' ')
print()
#Exercise 4.4
A=list(map(int,input().split()))
index=max=None
for i in range(len(A)):
	if max==None or A.count(A[i])>max:
		max=A.count(A[i])
		index=i
print(A[index])
