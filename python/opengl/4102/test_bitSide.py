from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
import threading
import time

name = 'ball_glut'

dotList = []

#Up Down Left Right

cont_None = 0
cont_Right = 1 # 0001
cont_Left = 2  # 0010
cont_Down = 4  # 0100
cont_Up = 8    # 1000


xMin = 400 - 50
yMin = 300 - 50

xMax = 400 + 50
yMax = 300 +  50

def main():
    print "main hi"

    yy = 0
    print yy

    yy = yy or cont_None
    print yy

    yy = yy or cont_Left
    print yy

    yy = yy or cont_Right
    print yy

    yy = yy or cont_Up
    print yy

    yy = yy or cont_Down
    print yy


    c = 0
    c = c | cont_Right
    print ("c = " + str(c) + " " )

    c = c | cont_Left
    print ("c = " + str(c) + " " )


    c = c | cont_Down
    print ("c = " + str(c) + " " )

    c = c | cont_Up
    print ("c = " + str(c) + " " )
    
    #for lop in range(0,10):
    #    for lop2 in range(0,10):
    #        print str(lop) + "," + str(lop2) + " = " + str(lop | lop2)

    addPls(0,0)
    addPls(300,0)
    addPls(400,0)
    addPls(600,0)
    addPls(800,0)

    addPls(0,200)
    addPls(0,400)
    addPls(0,600)
    addPls(0,800)


    

    
    trimDot()
    
def addPls(x,y):
    g = [x,y]
    dotList.append(g)


def getSideAsBit(x,y):
    zz = 0
        
    if (x < xMin):
        zz = zz or cont_Left
    elif(x > xMax):
        zz = zz or cont_Right


    if (y < yMin):
        zz = zz or cont_Up
    elif(y > yMax):
        zz = zz or cont_Down

    return zz    

    
    
def trimDot():
    for lop in range(0,len(dotList)):
        mode = getSideAsBit(dotList[lop][0] , dotList[lop][1])

        print ("lop " + str(dotList[lop]) + " = " + str(mode))
            
if __name__ == '__main__': main()
