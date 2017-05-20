 
def f(x):
    f=pow(x,2)-(2*x)-3
    return f

def secant(p0,p1):
    p2=p1-(f(p1)*(p1-p0)) / (f(p1)-f(p0))
    return p2

p0 = 453.0
p1 = -999.3
flag = True
while (flag == True ):
    p2 = secant (p0 , p1)
    print p0,p1,p2 ,f(p2)
    
    

    if(f(p2)==0 or abs(f(p2))==0.00001):
        print "found root"
        flag == False
        break
    
    p0=p1
    p1=p2
