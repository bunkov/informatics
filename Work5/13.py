a = list(map(int,input().split()))
n = len(a)
for i in range(n-1):	#граница почему-то не изменяется
	if i>=len(a):	#поэтому добавлено условие для i
		break
	if a[i]==2 and a[i+1]>2:
		a.pop(i)
		n-=1
print(sum(a)//n)