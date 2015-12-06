n = int(input())
a = [1]
b = [1]
print(' '.join(map(str,a)))
for i in range(n):
	if len(a) != 1:
		for j in range(1,len(a)):
			a[j] = b[j]+b[j-1]
	a.append(1)
	b.append(1)
	for j in range(1,len(a)-1):
		b[j] = a[j]
	print(' '.join(map(str,a)))