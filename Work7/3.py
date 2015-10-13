import numpy as np
import matplotlib.pyplot as plt
from math import *
def y(x):
	return(1+np.tan(1/(1+np.sin(x)**2)))
def z(x):
	return(np.exp(-np.abs(x)/10))

x=np.arange(-10,10.01,0.01)
plt.plot(x,np.log((x**2+1),y(x))*z(x))
plt.grid(True)
plt.show()
