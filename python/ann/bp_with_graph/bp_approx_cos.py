import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin

dotList = []

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    
# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

tStart = 1.0
tEnd = 100.0
tStep = 1.0

inputList = []
outputList = []

tCur = tStart
while (tCur  < tEnd):
    tValue = cos(tCur)

    ttList = [tCur,  tCur , 1]
    inputList.append(ttList)
    outputList.append( cos(tCur))

    tCur = tCur + tStep


    
# output dataset            
y = np.array([[0,1,1,1]]).T

print X
print y
print inputList
print outputList

X = np.array(inputList)
y = np.array(outputList)

print "..."
print X
print y

X = X / X.max(axis=0)
y = y / y.max(axis=0)

print "** norm **"
print X
print y

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((len(X[0]))) - 1


dotList = []
dotList2 = []

for iter in xrange(20):


        
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

    # how much did we miss?
    l1_error = y - l1
    

        
    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)


    if (iter% 1000) == 0:
        print "---------------------------_"
        print "Error:" + str(np.mean(np.abs(l1_error)))
        print "learning epoch : " + str(iter)
        print l1
    # update weights
    syn0 +=  np.dot(l0.T,l1_delta)

    #print ""
    #print l1

    if (iter%1) == 0:
        for k in l1:
            dotList.append(k)

    for k2 in syn0:
        dotList2.append(cos(k2))
        
plt.plot(dotList, 'ro',color="g")
plt.plot(dotList2, 'ro',color="r")

print "*********************"

test = nonlin(np.dot(X,syn0))
print "Output After Training:"
print test


#plt.plot(dotList2, 'ro',color="r")
#plt.axis([0, 1000, 0, 1000])
plt.show() 
