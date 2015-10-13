import numpy as np
import matplotlib.pyplot as plt
from math import *
import pylab
from matplotlib import mlab

x=np.arange(-10,10.01,0.01)
plt.xkcd()
plt.plot(x,eval(input()))
plt.grid(True)
plt.show()
