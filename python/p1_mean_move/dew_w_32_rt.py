#real time webcam and move mouse predict
import numpy as np
import cv2
import dew_normalization as dewnormal
import dew_sl_v1 as dewsl
import math
import dew_config as dewconfig

cap = cv2.VideoCapture(0)

#*
#   n = NN(67, 4, 3, regression = False)

#    # train it with some patterns then test it.
# n.train(pat2, 1001, 0.1, 0.2)
#*

n = dewsl.NN(67, 4, 3, regression = False)
#n.wi, n.wo = dewsl.loadweight("./txt/weight_1.txt",n)
dewsl.loadweight("./txt/weight_1.txt",n)
print n.weights()

#pymouse
from pymouse import PyMouse
m = PyMouse()
#m.move(x,y)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    sizex = 32

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    resi = cv2.resize(frame, (sizex, sizex))
    rollback = cv2.resize(resi, (640,480))

    cv2.imshow('original', frame)
    cv2.imshow('resizedimage' ,resi)
    cv2.imshow('32 to big', rollback)

#get input feature


    inputn = []
    plusa = 0.0
    tem = []

    maxrange = 1

    c0 = 0.0
    c1 = 0.0
    c2 = 0.0

    m0 = 0.0
    m1 = 0.0
    m2 = 0.0

    #do the x axis
    for x in range(0, sizex):
        plusa = 0.0

        for y in range(0, sizex):
            tem = resi[x, y]
            #print 'x',x,',y,',y," = ", tem
            plusa = plusa + ((tem[0] + tem[1] + tem[2]) / 3) #RuntimeWarning: overflow encountered in ubyte_scalars
            c0 = c0 + tem[0]
            c1 = c1 + tem[1]
            c2 = c2 + tem[2]

        #print plusa
        plusa = plusa / maxrange
        inputn.append(plusa)
        #print '%d = %f' %(x, inputn[x])



    #do the y axis
    for x in range(0, sizex):
        plusa = 0.0

        for y in range(0, sizex):
            tem = resi[y, x]
            #print 'x',x,',y,',y," = ", tem
            plusa = plusa + (((tem[0] + tem[1] + tem[2]) / 3))

        #print plusa
        plusa = plusa / maxrange
        inputn.append(plusa)
        #print '%d = %f' %(len(inputn), inputn[x])

    #print 'c0 %d , c1 %d , c2 %d ' %(c0 , c1 , c2)

    #this is problem!!!!
    m0 = c0 / (sizex*sizex)
    m1 = c1 / (sizex*sizex)
    m2 = c2 / (sizex*sizex)
    inputn.append(m0)
    inputn.append(m1)
    inputn.append(m2)

    dew = []
    #normalization
    #print '****'
    #print inputn
    dew = dewnormal.dew_normal_one_set_for_rt(inputn)
    #print '>>>>'
    #print dew

    interp = n.test(dew);
    #print interp
    tmtm = []
    tmtm  = interp[0]
    x = tmtm[0]
    y = tmtm[1]
    z =tmtm[2]

    x2 = math.fabs(x * 1366)
    y2 = math.fabs(y * 768)
    z2 = math.fabs(z*1)

    x2 = (x * (dewconfig.screen_width - dewconfig.screen_reduce_width))
    y2 = (y * (dewconfig.screen_height - dewconfig.screen_reduce_height))
    z2 = (z * 1)


    if (z2 >= 0.5):
        m.move(x2,y2)

    #x3 = round(x2)
    #y3 = round(y2)
    #z3 = round(z2)

    print x2
    print y2
    print z2
#    f.write("[new]\n")

#    for y in range(0, 67):
#        print 'data %d , %f' %(y ,inputn[y])
#        f.write(str(inputn[y]) + "\n")

#normalization

#get input feature

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

