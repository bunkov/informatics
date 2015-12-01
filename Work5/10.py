A = list(map(int,input().split()))
t = int(input())

for i in range(t):
	A.insert(-1-A[-1],A[-1])
	A.pop()
print(' '.join(map(str,A)))
