
def f(x):
    y=3*x
    return y

a=10.0
b=-2.0

if(a*b>0):
    print "not root"
else :
    print "can find root"
    
    flag=True

    while(flag == True):
    
        m=(a+b)/2

        
        fm = f(m)


        print a,b,m,fm

      
        if(fm*a<0):
            b=m
        else:
            a=m

        print a,b,m,fm

        if(fm==0 or abs(fm)<0.0001):
            print "found root"
            flag = False
        
