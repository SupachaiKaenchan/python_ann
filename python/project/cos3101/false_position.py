from math import sin
import random

def func(x):
    a = sin(x)
    return a


a = (random.random() * 50.0) - 50.0
b = (random.random() * 50.0) - 50.0

flag = True


count = 0

print "a " , a , " b " , b
    
if func(a) * func(b) > 0: # seem side can't found root ?
    flag = False

    print "a , b seem side can't found root"
        
elif func(a) * func(b) == 0: # a b  be the seem can't convergent to root
    flag = False
    print "a == b ,  so can't go on "


while(flag == True):
    count = count + 1

    print "a " , a , " b " , b




    tmpA = func(b) * (b-a)
    tmpB = func(b) - func(a)


            
    m = b - ( tmpA  / tmpB) 

    if (func(m) == 0 or abs (func(m)) < 0.0001):
        flag = False
        print ("found root ")

    else:
        if func(a)*func(m) > 0 : # diffrent side
            b = m
        else:
            a = m

            

    print "epoch " , count , " m " , m , " f(m)" , func(m)


    
