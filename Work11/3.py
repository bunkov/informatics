class Point:
	mass = 1
	def __init__(self, string='0,0,1'):
		a = string.split(',')
		if len(a)==3:
			self.x, self.y, self.mass = map(float, a)
		elif len(a)==2:
			self.x, self.y = map(float, a)
		elif len(a)==1:
			self.x = float(a[0])
			self.y = 0

	def __str__(self):
		return str(self.x) + ',' + str(self.y) + ',' + str(self.mass)
	def __add__(self, other):
		return Point(str(self.x + other.x) + ','+ str(self.y + other.y))
	def __sub__(self, other):
		return Point(str(self.x - other.x) + ','+ str(self.y - other.y))
	def __abs__(self):
		return (self.x**2 + self.y**2)**0.5

n=int(input())
A=[0]*n
r=[0]*n
m=[0]*n

summa = sum_mass = 0
for i in range (n):
	A[i]=Point(input())
	r[i]=abs(A[i])
	m[i]=A[i].mass
	summa += m[i]*r[i]
	sum_mass += m[i]
R = summa/sum_mass
print(R)
