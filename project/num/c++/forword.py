from math import cos,sin,  factorial
import random
import matplotlib.pyplot as plt

def randominput(n):
    listA = []
    for i in range(0,n):
        ran = random.random()
        listB = [i, ran]
        listA.append( listB)

    return listA
    

def forward(listinput, x):
    dataSize = len(listinput)
    #print listinput , dataSize

    summation = 0.0
    
    for i in range (0,dataSize):
        tmp = f0(x,i)

        term = 1.0
        for j in range (0, i):
              term = term * (x  - listinput[j][0])

        summation  = summation + (tmp* term)

    return summation
        
    #print "summation" , summation

def f0(x,dataSize):
    f=0.0

    
    
    if dataSize % 4 == 0:
        f = sin(x)
    elif dataSize % 4 == 1:
        f = cos(x)
    elif dataSize % 4 == 2:
        f = -sin(x)
    elif dataSize == 3:
        f = -cos(x)
        
    return f

    

dotList = []
dotList2 = []

xList = []

cur = 0.0
while (cur < 50.0 ) :

    y = sin(cur)


#    dotList.append(y)
    
    tmpList = [cur, y]
    xList.append(tmpList)
    
    cur = cur + 1



listinput = randominput(20)
print listinput



for i in range(0,len(listinput)):
    dotList.append(listinput[i][1])

for i in range (0 , len (listinput)):
    #print xList[i]\

    y = forward(listinput , listinput[i][0]);
    #print y 
    dotList2.append(y)


dotList = dotList[0:len(dotList)-3]
dotList2 = dotList2[0:len(dotList2)-3]

plt.plot(dotList, 'ro',color="g")
plt.plot(dotList2, 'ro',color="r")
#plt.axis([0, 1000, 0, 1000])
plt.show() 



forward(listinput,1.0)





