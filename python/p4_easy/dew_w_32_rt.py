#real time webcam and move mouse predict
import cv2
import dew_normalization as dewnormal
import dew_sl_v1 as dewsl
import dew_get_feature as dewfeature

cap = cv2.VideoCapture(0)

#*
#   n = NN(67, 4, 3, regression = False)

#    # train it with some patterns then test it.
# n.train(pat2, 1001, 0.1, 0.2)
#*

#n = dewsl.NN(67, 5, 8, regression = False)
#n.wi, n.wo = dewsl.loadweight("./txt/weight_1.txt",n)

ggg = []
ggg = dewsl.loadweight("./txt/weight_1.txt")
n = dewsl.NN(ggg[0][0], ggg[0][1], ggg[0][2], ggg[0][3], regression = False)
n.wi = ggg[1][0]
n.wo = ggg[1][1]
n.wo2 = ggg[1][2]

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



#get input feature


    inputn = dewfeature.getfeature(resi)

    dew = []
    #normalization
    print
    print '****'
    print inputn

    dew = dewnormal.dew_normal_one_set_for_rt(inputn)
    #print '>>>>'
    #print dew

    interp = n.test(dew);
    #print interp
    tmtm = []
    tmtm  = interp[0]
    re3 = []

    for ggg in range(0, 1):
        tmp = tmtm[ggg]
        re3.append (tmp)

    print re3

    foundza = False

    if tmp < 0.2:
        cv2.rectangle(frame,(300,300),(300,300),(0,0,0))
    elif tmp < 0.4:
        cv2.rectangle(frame,(300,300),(200,100),(0,255,0))
    elif tmp < 0.6:
        cv2.rectangle(frame,(300,300),(200,500),(255,255,0))
    elif tmp < 0.8:
        cv2.rectangle(frame,(300,300),(100,300),(0,255,255))
    elif tmp < 1.0:
        cv2.rectangle(frame,(300,300),(400,300),(0,255,255))

    cv2.imshow('original', frame)
    cv2.imshow('resizedimage' ,resi)
    cv2.imshow('32 to big', rollback)
#    y = tmtm[1]
#    z =tmtm[2]
   # print x
    #x2 = math.fabs(x * 1366)
    #y2 = math.fabs(y * 768)
    #z2 = math.fabs(z*1)
#    x2 = (x * (dewconfig.screen_width - dewconfig.screen_reduce_width))
#    y2 = (y * (dewconfig.screen_height - dewconfig.screen_reduce_height))
#    z2 = (z * 1)


 #   if (z2 >= 0.5):
 #       m.move(x2,y2)

    #x3 = round(x2)
    #y3 = round(y2)
    #z3 = round(z2)

  #  print x2
  #  print y2
  #  print z2
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

