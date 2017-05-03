
from math import sin,cos,factorial



def p1(x,degree):
    j = 0.0
    
    lop = 1
    while (lop < degree):
        tmp = 0
        if (lop % 4 == 1):
            tmp = -sin(0)
        elif (lop % 4 == 2):
            tmp = -cos(0)
        elif (lop % 4 == 3):
            tmp = sin(0)
        elif (lop % 4 == 0):
            tmp = cos(0)

        print (">>>>>>>>>>>>>>>")
        print ("lop " + str(lop) + " ,tmp " + str(tmp) + ", pow " + str(pow(x,lop)) + " , fac " + str(factorial(lop)))
        print ("part 1 " + str((tmp)* ( pow(x,lop) )))
        print ("part 2 " + str((tmp)* ( pow(x,lop) )/ factorial(lop)))
        print ("j = " + str(j))

        
        j = j + ((tmp)* ( pow(x,lop) )/ factorial(lop))

        lop = lop + 1

    return j

for i in range(1,2):
    print ("**************************")
    for j in range(0,9):
        print (str(i) + " , " + str(j))
        print (str(p1(i,j)) + " " + str(pow(i,j)) + " , " + str(factorial(j)))
 

run1 = True
if (run1 == False):
    for i in range(0,9):
        print ("**************")
        for j in range(0,9):
            print (str (i) + " >> "+ str(j) + "  mod 4 = " + str(j % 4))
            print ("pow = " + str(pow(i,j)))
            print (">>> " + str(i) + "/" + str(j) + " = " + str(p1(i,j)))

