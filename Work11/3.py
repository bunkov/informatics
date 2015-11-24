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
m=[0]*n
summa_x = summa_y = sum_mass = 0
for i in range (n):
	A[i]=Point(input())
	m[i]=A[i].mass
	summa_x += m[i]*A[i].x
	summa_y += m[i]*A[i].y
	sum_mass += m[i]
R = ((summa_x/sum_mass)**2 + (summa_y/sum_mass)**2)**0.5
print(R)
