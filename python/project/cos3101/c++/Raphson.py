def f(x):
    f= pow(x,2) -(2*x)-3
    return f

def f1(x):
    f1=(2*x)-2
    return f1

def Raphson(p0):

    p1=p0-(f(p0)/f1(p0))
    return p1

p0=50.0

flag = True
while(flag == True):
    p1=Raphson(p0)
    print p1,p0 , f(p1)

    
    if (f(p1) == 0 or abs(f(p1))<0.0000001):
        print "found root"
        flag = False
        break

    p0=p1


    
