import numpy
import matplotlib.pyplot as plt
from math import *
import pylab
from matplotlib import mlab
f=open('input.txt','r')

A=' '.join(f.readlines()).split()
k = [len(a) for a in A]
'''k=[0]*len(A)
n=0
for i in range(len(A)):
	k[i]=len(A[i])'''
y=[0]*max(k)
for i in range(max(k)):
	y[i]=k.count(i+1)

x=[i+1 for i in range(max(k))]
y_pos = numpy.arange(len(x))
plt.bar(y_pos, y, align='center', alpha=0.5)
plt.xticks(y_pos, x)

#plt.axis([0, max(x), 0, max(y)])
#plt.grid(True)
plt.show()
