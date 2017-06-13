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
        tmp = listinput[i][1]

        #print
        
        term = 1.0
        for j in range (0, i+1):
            if ( i == j ):
                break
            #print "loop i,j " , i , j
            term = term * (x  - listinput[j][1])

        summation  = summation + (tmp* term)

    return summation
        
    #print "summation" , summation

    

dotList = []
dotList2 = []

xList = []

cur = 0.0
while (cur < 10.0 ) :

    y = sin(cur)


#    dotList.append(y)
    
    tmpList = [cur, y]
    xList.append(tmpList)
    
    cur = cur + 1



listinput = randominput(5)
listinput = []

for i in range(0, 20):
    listinput.append([i, i*i])
print listinput



for i in range(0,len(listinput)):
    
    dotList.append(listinput[i][1])

for i in range (0 , len (listinput) ):
    #print xList[i]\

    y = forward(listinput , i);
    #print y
    #if (abs(y) > 1000):
    #    y = 0
    dotList2.append(y)


#dotList = dotList[0:len(dotList)-3]
#dotList2 = dotList2[0:len(dotList2)-3]

plt.plot(dotList, 'ro',color="g")
plt.plot(dotList2, 'ro',color="r")
#plt.axis([0, 1000, 0, 1000])
plt.show() 



forward(listinput,1.0)





