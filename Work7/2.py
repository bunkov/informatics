import numpy as np
import matplotlib.pyplot as plt
from math import *
def f(x):
	return(x*x-6-x)
def solve(a,b,f):
	while abs(a-b)>=0.01:
		if f(a)*f((a+b)/2)<0:
			b=(a+b)/2
		elif f(b)*f((a+b)/2)<0:
			a=(a+b)/2
		x0=(a+b)/2
	return(x0)
x=np.arange(-10,10.01,0.01)
plt.plot(x,f(x))
plt.grid(True)
print(solve(-10,-0.01,f),solve(0.01,10,f))
plt.show()
