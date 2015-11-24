class Point:
	def __init__(self, string='0,0'):
		a = string.split(',')
		self.x, self.y = map(float, a)
	def __str__(self):
		return str(self.x) + ',' + str(self.y)
	def __add__(self, other):
		return Point(str(self.x + other.x) + ','+ str(self.y + other.y))
	def __sub__(self, other):
		return Point(str(self.x - other.x) + ','+ str(self.y - other.y))
	def __abs__(self):
		return (self.x**2 + self.y**2)**0.5

n=int(input())
max_P = None
pts=[0]*n
for i in range (n):
	pts[i]=Point(input())
for i in range(n-2): # 0 - n-3
	for j in range(i+1,n-1): # 1 - n-2
		a = abs(pts[i] - pts[j])
		for k in range(i+2,n): # 2 - n-1
			b = abs(pts[j] - pts[k])
			c = abs(pts[i] - pts[k])
			P = a + b + c
			if max_P == None or max_P < P:
				max_P = P
print(max_P)