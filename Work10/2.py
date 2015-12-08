A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
E = A.difference(B).intersection(C.difference(D)) \
	.union(D.difference(A).intersection(B.difference(C)))
print(E)