from math import *
def f(x):
	y=log(1/(exp(sin(x)+1))/(5/4+1/x**15),1+x**2)
	return(y)
print(f(1),f(10),f(1000))
