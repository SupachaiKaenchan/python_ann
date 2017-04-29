from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
import threading
import time
from math import cos,sin,  factorial

name = 'taylor'



winWidth = 800
winHeight = 600

def main():
    print "main hi"
    tmpRen = RenderPls()
    tmpRen.setupVariable()
    
class RenderPls ():
    minX = -100.0
    maxX = 100.0
    xStep = 0.1

    drawXSpace = 10
    drawYHigh = 100

    degree = 0


    DotList = []

    DotList2 = []

    def p1(self,x):
        j = cos(0)
    
        #print "*********  " + str(x)
        #print j
        #

        lop = 0
        while (lop < self.degree):
            tmp = 0
            if (lop % 4 == 0):
                tmp = -sin(x)
            elif (lop % 4 == 1):
                tmp = -cos(x)
            elif (lop % 4 == 2):
                tmp = sin(x)
            elif (lop % 4 == 3):
                tmp = cos(x)
        
            j = j + (((tmp / factorial(lop+1))* ( pow(x,lop+1))) )
            lop = lop + 1

        #print j
           
        return j

        
    def resetDotList(self):
        self.DotList = []
        self.DotList2 = []
        
        lop = self.minX
        while (lop <= self.maxX):
            g = [(lop*self.drawXSpace)+ (winWidth/2),(winHeight / 2)+ (cos(lop)*self.drawYHigh)]
            self.DotList.append(g)
            lop = lop + self.xStep

            
            g = [(lop*self.drawXSpace)+ (winWidth/2) ,  (winHeight / 2)+ (self.p1(lop))]
            #g = [0,0]
            self.DotList2.append(g)
            lop = lop + self.xStep


        print self.DotList[400]
        print self.DotList2[400]
        print str(len(self.DotList))
        print str(len(self.DotList2))
        
    def __init__(self):
        print "RenderPls init"
        
        self.resetDotList()
        


                            
            
    
        
    def setupVariable(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(winWidth, winHeight)
        glutCreateWindow(name)

        glClearColor(0.,0.,0.,1.)
        glutDisplayFunc(self.display)
        gluOrtho2D(0, winWidth, winHeight, 0);
        glMatrixMode(GL_MODELVIEW);
        glPushMatrix()

        glutMouseFunc(self.mouseEvent);

        #while(True):
            #display()
            #print ("looping")

        #thread1 = myThread(1, "Thread-1", 1,self)

        #thread1.start()
        

        glutMainLoop()

        print "end"
        
        return


    def mouseEvent(self, button, state,  x,  y):
        print ("mouse Event " )
        mouseButton = button;
        if button == GLUT_LEFT_BUTTON:    
            if(state == GLUT_DOWN):
                oldX = x;
                oldY = y;
                print ("click " + str(x) + " ," + str(y))

                tmpC = [x,y]
                #self.DotList.append(tmpC)

        if button == GLUT_RIGHT_BUTTON:    
            if(state == GLUT_DOWN):
                print ("right click test " + str(x) + " , " + str(y))
                self.degree = self.degree + 1

                self.resetDotList()
                

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glLineWidth(2.5);     
        glBegin(GL_LINES);
        # left line
        glColor3f(1.0, 0.0, 0.0);


        glVertex2f(winWidth / 2, 0);
        glVertex2f(winWidth / 2, winHeight);
        # right line
        glColor3f(0.0, 1.0, 0.0);
        glVertex2f(0, winHeight / 2);
        glVertex2f(winWidth, winHeight / 2);



        
        # top line
        glColor3f(0.0, 1.0, 1.0);

        lop = 0
        while (lop < len(self.DotList)-1):
            tmpX = self.DotList[lop][0];
            tmpY = self.DotList[lop][1];

            glVertex2f(tmpX , tmpY)


            tmpX2 = self.DotList[lop+1][0];
            tmpY2 = self.DotList[lop+1][1];

            glVertex2f(tmpX2 , tmpY2)
            lop = lop + 1


        glColor3f(0.5, 0.5, 1.0);
        lop = 0
        while (lop < len(self.DotList)-1):
            tmpX = self.DotList2[lop][0];
            tmpY = self.DotList2[lop][1];

            glVertex2f(tmpX , tmpY)


            tmpX2 = self.DotList2[lop+1][0];
            tmpY2 = self.DotList2[lop+1][1];

            glVertex2f(tmpX2 , tmpY2)
            lop = lop + 1


        glColor3f(1.0, 1.0, 1.0);

        glVertex2f(winWidth / 2 ,winHeight / 2)
        glVertex2f(winWidth / 2 , cos(0) * self.drawYHigh)

        
        glEnd();
        glPopMatrix()
        glutSwapBuffers()
        glutPostRedisplay()
        return

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, renderPls):
        threading.Thread.__init__(self)
        self.renderPls = renderPls
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print "Starting " + self.name
        
        while(True):
            self.counter = self.counter + 1
    
            print "myThread Force display  : " + str(self.counter)
            time.sleep(0.5)
            #self.renderPls.display()
            #glutPostRedisplay()

            print "myThread Force display 2"
            

        print "Exiting " + self.name

if __name__ == '__main__': main()
