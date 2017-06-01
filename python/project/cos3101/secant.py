def p2(x):
    j =  +(1.5* pow(x, 2)  ) - (8*x) + 1
           
    return j

def secant (x1,x0):
    y = x1 - ( f(x1) *  (x1-x0) ) /( f(x1)-( f(x0) ))
    return y

        
def f(x):
    #j =  + (0.5*pow(x, 3)) - (4*pow(x,2)) + (pow(x,1)) - 1
    j =  + (2*pow(x, 3)) - (3*pow(x,2)) + (0.2*pow(x,1)) - 1
           
    return j


p0 = -1.0
p1 = 5.0


flag = True

while(True):
    p2 = secant(p0,p1)
    print ""
    print "p0 p1 p2",p0,p1,p2
    print "f(p0 p1 p2)",f(p0),f(p1),f(p2)

    if (f(p2) == 0 or abs(f(p2)) < 0.0001):
        print ("found root " , p2 , f(p2))
        break

    p0 = p1
    p1 = p2
