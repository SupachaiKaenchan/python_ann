def f (x ) :

    y = 2 * (x)
    return y



a = -10.0
b = 50.0




flag = True

while(True):

    m = (a+b)/2.0
    print a , b , m , "," , f(a),f(b), f(m)
    print ""
            
    if f(m) == 0 or abs(f(m)) < 0.0001:
        print "found root"
        flag = True
        break
    else:

        if f(a) * f(b) > 0 : # no root confirm
            flag = True
            print "no root confirmed"
            break
        else:
            if (f(a) * f(m) > 0.0):
                a = m
            else:
                b = m



            
    
