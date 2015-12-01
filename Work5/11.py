A = list(map(int,input().split()))
for i in range(0,len(A),2):
	a = A.pop()
	A.insert(i+1,a)
print(' '.join(map(str,A)))
