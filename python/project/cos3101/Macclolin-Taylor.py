 
from math import cos,sin,  factorial
import matplotlib.pyplot as plt



def mac(x,x0,i):
        j = cos(x0)
    
        #print "*********  " + str(x)
        #print j
        #

        lop = 1
        while (lop < i):
            tmp = 0
            if (lop % 4 == 1):
                tmp = -sin(x0)
            elif (lop % 4 == 2):
                tmp = -cos(x0)
            elif (lop % 4 == 3):
                tmp = sin(x0)
            elif (lop % 4 == 0):
                tmp = cos(x0)
        
            j = j + ((tmp)* ( pow(x,lop) )/ factorial(lop))
            lop = lop + 1

        #print j
           
        return j



start = -360.0
n = 360.0
step = 0.1
cur = start

dotList = []
dotList2 = []

yExtend = 100

x0 = 0.0
    
i=10
if (x0 == 0.0):
    print "Maccolin method cuz X0 = 0"
else:
    print "Taylor Method Cuz x0 > 0   , (" + str(x0) + ")"

    
while ( cur < n):



    run = mac(cur,x0,i)
    #run = sin(cur)
    #print run,cur
    
    #print ""
    tmpG = 0.0

    if (abs(run) * (yExtend / 5) < yExtend):
        tmpG = [cos(cur)]

    #print "sin " , tmpG
        dotList.append(tmpG)
        dotList2.append(run  )
    
    cur = cur + step


#print dotList

plt.plot(dotList, 'ro',color="g")
plt.plot(dotList2, 'ro',color="r")
#plt.axis([0, 1000, 0, 1000])
plt.show() 


