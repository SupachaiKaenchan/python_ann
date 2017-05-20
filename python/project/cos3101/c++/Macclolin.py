 
from math import cos,sin,  factorial
import matplotlib.pyplot as plt


def mac2(x,x0,i): 
    temp = 0.0

    f0 = cos(x0)

    temp = f0 # output !
    
    for l in range(1,i):


        f1 = 0.0
        
        j = l % 4
        
        if (j == 1):
            f1 = -sin(x0)
        elif (j == 2):
            f1 = -cos(x0)
        elif (j == 3) :
            f1 = sin(x0)
        elif (j == 4):
            f1 = cos(x0)

        f2 = f1 

        a1 = f2 * (pow(x,l))
        a2 = factorial(l)
        #print ">>> " , "a1 " , a1 , "a2" , a2 , "f0" , f0 , "f1", f1 , "f2" , f2 , "l" , l

        
        temp=temp + (a1 / a2)
       
    return temp

def mac(x,x0,i):
        j = cos(0)
    
        #print "*********  " + str(x)
        #print j
        #

        lop = 1
        while (lop < i):
            tmp = 0
            if (lop % 4 == 1):
                tmp = -sin(0)
            elif (lop % 4 == 2):
                tmp = -cos(0)
            elif (lop % 4 == 3):
                tmp = sin(0)
            elif (lop % 4 == 0):
                tmp = cos(0)
        
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


while ( cur < n):

    x0=0.0
    i=12
    
    

    run = mac2(cur,x0,i)
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


print dotList

plt.plot(dotList, 'ro',color="g")
plt.plot(dotList2, 'ro',color="r")
#plt.axis([0, 1000, 0, 1000])
plt.show() 


