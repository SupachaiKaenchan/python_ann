import numpy as np
import matplotlib.pyplot as plt

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

C = []
S = []


mmin = -3.0
mmax = 3.0
mstep = 0.1

mtmp = mmin
while mtmp <= mmax:
    tmpI = mtmp
    
    tmpI2 = nonlin(tmpI)
    
    C.append( (tmpI2))
    S.append( (nonlin(tmpI2,True)))
    #S.append( tmpI)

    mtmp = mtmp + mstep

maxSize = len(C)
X = np.linspace(0, maxSize, maxSize, endpoint=True)
#C,S = np.cos(X), np.sin(X)

#print C


plt.plot(X,C)
plt.plot(X,S)

plt.show()
