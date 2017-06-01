import matplotlib.pyplot as plt
import random

dotList = []

xMax = 100
yMax = 100

for i in range (0,xMax):

    y = random.random()*yMax
    y = i * 2
    
    bb = [y]
    dotList.append(bb)

print dotList

plt.plot(dotList, 'ro')
#plt.axis([0, xMax, 0, yMax])
plt.show() 

