import numpy as np
import matplotlib.pyplot as plt

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

X = np.linspace(-np.pi, np.pi, 2560, endpoint=True)
C,S = np.cos(X), np.sin(X)

#print C
C = []

for i in range(2560):
    C.append( (nonlin((i-1280)*0.01) -0.0,False))

#print C

plt.plot(X,C)
plt.plot(X,S)

plt.show()
