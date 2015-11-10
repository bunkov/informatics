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
maximum = None
r=[0]*n
for i in range (n):
	r[i]=abs(Point(input()))
	if maximum == None or maximum <= r[i]:
		maximum = r[i]
print(maximum)
