n = int(input())
a = [0]*n
for i in range(n):
	a[i] = [0]*2
for i in range(n):
	a[i][0],a[i][1] = map(int,input().split())
t = int(input())
k=0

for i in range(n):
	if a[i][0]<=t and a[i][1]>=t:
		k+=1
print(k)