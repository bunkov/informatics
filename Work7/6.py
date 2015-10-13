import numpy as np
import matplotlib.pyplot as plt
from math import *
import pylab
from matplotlib import mlab
f=open('input.txt','r')

A=' '.join(f.readlines()).split()
k=[0]*len(A)
n=0
for i in range(len(A)):
	k[i]=len(A[i])
y=[0]*max(k)
for i in range(max(k)):
	
	y[i]=k.count(i+1)

x=[i+1 for i in range(max(k))]

print(x)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.axis([0, max(x), 0, max(y)])
plt.grid(True)
plt.show()
