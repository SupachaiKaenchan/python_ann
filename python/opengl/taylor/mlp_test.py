from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
import threading
import time
from math import cos,sin,  factorial

name = 'raphson'



winSize = [800,600]


def main():
    print ("main hi")
    tmpRen = RenderPls()
    tmpRen.setupVariable()
    
class RenderPls ():
    mmmX = [-100, 100]
    xStep = [0.1]

    counter =[0]    

    drawXSpace = [50]
    drawYHigh = [10]

    degree = [0]


    DotList = []

    DotList2 = []

    DotList3 = []

    def p2(self,x):
        j =  +(1.5* pow(x, 2)  ) - (8*x) + 1
           
        return j

        
    def p1(self,x):
        j =  + (0.5*pow(x, 3)) - (4*pow(x,2)) + (pow(x,1)) - 1
           
        return j

        
    def resetDotList(self):
        self.counter[0] = self.counter[0] + 1
        print self.counter
    
        self.DotList = []
        self.DotList2 = []
        
        lop = self.mmmX[0]
        while (lop <= self.mmmX[1]):
            g = [(lop*self.drawXSpace[0]), (self.p1(lop)*self.drawYHigh[0])]
            self.DotList.append(g)
            #lop = lop + self.xStep[0]

            
            g = [(lop*self.drawXSpace[0]) ,((self.p2(lop))*(self.drawYHigh[0])) ]
            #g = [0,0]
            self.DotList2.append(g)
            
            lop = lop + self.xStep[0]

            if (lop > 10.0 and lop < 10.2):
                print ("******* lop " + str(lop) + " = " + str(self.p1(lop)))


        lop = 1

        tmpList = []
        self.DotList3 = []

        start =  -10.0
        
        tmpList.append([ start,start  - (self.p1(start)/self.p2(start))])
        self.DotList3.append([ start*self.drawXSpace[0]
                               ,(start  - (self.p1(start)/self.p2(start)))*self.drawYHigh[0]])


        
        while(lop < 100):
            tmp2 = tmpList[lop-1][1]
            tmp = tmp2 - (self.p1(tmp2)/self.p2(tmp2))

            print tmp
            print tmp2
            print tmpList[lop-1]
            self.DotList3.append([ tmp * self.drawXSpace[0],self.p1(tmp) * self.drawYHigh[0]])
            tmpList.append([ tmp2 ,tmp ])

            if (self.p1(tmp) == 0 or abs(0-self.p1(tmp)) < 0.001):
                break
            
            lop = lop + 1

           
        print ("counter " + str(self.counter[0])  + " , degree " + str(self.degree[0]))

        print (str(len(self.DotList)))
        print (str(len(self.DotList2)))
        print (str(len(self.DotList3)))
        
    def __init__(self):
        print ("RenderPls init")
        
        self.resetDotList()
        



    def myIdle(self):
        #print ("myIdle")
        glutPostRedisplay()
        
        
    def setupVariable(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(winSize[0], winSize[1])
        glutCreateWindow(name)

        glClearColor(0.2,0.2,0.2,0.)

        
        glutDisplayFunc(self.display)
        
        
        gluOrtho2D(-winSize[0], winSize[0], -winSize[1], winSize[1]);
        glPushMatrix()

        glutIdleFunc(self.myIdle)

        glutMouseFunc(self.mouseEvent);

        #while(True):
            #display()
            #print ("looping")

        #thread1 = myThread(1, "Thread-1", 1,self)

        #thread1.start()
        

        glutMainLoop()

        print ("end")
        
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
                self.degree[0] = self.degree[0] + 2

                self.resetDotList()
                

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        glLineWidth(2.5);
        
        glBegin(GL_LINES);
        # left line
        glColor3f(1.0, 0.0, 0.0);

        glVertex2f(-winSize[0] , 0);
        glVertex2f(winSize[0] , 0);
        # right line
       # glColor3f(0.0, 1.0, 0.0);
        glVertex2f(0, -winSize[1]);
        glVertex2f(0, winSize[1]);

        # top line

        
        glColor3f(1.0, 0.0, 1.0);

        lop = 0
        while (lop < len(self.DotList)-1):
            tmpX = self.DotList[lop][0];
            tmpY = self.DotList[lop][1];

            glVertex2f(tmpX , tmpY)


            tmpX2 = self.DotList[lop+1][0];
            tmpY2 = self.DotList[lop+1][1];

            glVertex2f(tmpX2 , tmpY2)
            lop = lop + 1


        glColor3f(0.3, 0.0, 1.0);
        lop = 0
        while (lop < len(self.DotList)-1):
            tmpX = self.DotList2[lop][0];
            tmpY = self.DotList2[lop][1];

            glVertex2f(tmpX , tmpY)


            tmpX2 = self.DotList2[lop+1][0];
            tmpY2 = self.DotList2[lop+1][1];

            glVertex2f(tmpX2 , tmpY2)
            lop = lop + 1

        glColor3f(1.0, 0.0, 1.0);
        lop = 0


        tmpColor = 0.0
        while (lop < len(self.DotList3)-1):
            glColor3f((tmpColor),tmpColor,tmpColor);
            tmpColor = tmpColor + (1.0 / len(self.DotList3))

            
            tmpX = self.DotList3[lop][0];
            tmpY = self.DotList3[lop][1];

            glVertex2f(tmpX , tmpY)

            tmpX2 = self.DotList3[lop+1][0];
            tmpY2 = self.DotList3[lop+1][1];

            glVertex2f(tmpX2 , tmpY2)
            lop = lop + 1
            

 

        glColor3f(1.0, 1.0, 1.0);

        #glVertex2f(winSize[0] / 2 ,winSize[1] / 2)
        #glVertex2f(winSize[0] / 2 , cos(0) * self.drawYHigh[0])

        
        glEnd();
        glPopMatrix()
        
        glutSwapBuffers()
        
        #glutPostRedisplay()
        #return

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, renderPls):
        threading.Thread.__init__(self)
        self.renderPls = renderPls
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print ("Starting " + self.name)
        
        while(True):
            self.counter = self.counter + 1
    
            print ("myThread Force display  : " + str(self.counter))
            time.sleep(0.5)
            #self.renderPls.display()
            glutPostRedisplay()

            print ("myThread Force display 2")
            

        print ("Exiting " + self.name)

if __name__ == '__main__': main()
