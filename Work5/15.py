n = int(input())
a = list(map(int,input().split()))
a = a[:n]
k = int(input())
max = None

for i in range(n-k+1):
	if max is None or max < sum(a[i:i+k]):
		max = sum(a[i:i+k])
print(max)