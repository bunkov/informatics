import numpy as np
import matplotlib.pyplot as plt
from math import *
import pylab
from matplotlib import mlab
tmin=-10
tmax=10
dt=0.1
tlist=mlab.frange(tmin,tmax,dt)

pylab.ion()

for a in range (50):
        xlist=[sin(t+a/5.0) for t in tlist]
        ylist = [cos(2*t) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()
