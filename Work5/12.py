N = int(input())
A = list(map(int,input().split()))
A = A[:N]

sup = max(A)
maxim = None

for i in range((len(A)-1)//2):
	for j in range(len(A)):
		if A[j] < sup:
			if maxim is None or maxim <= A[j] and maxim < sup:
				maxim = A[j]
	sup = maxim
	maxim = None
print(sup)
