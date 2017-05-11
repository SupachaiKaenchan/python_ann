from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
import threading
import time
from math import cos,sin,  factorial

name = 'lagrang'



winSize = [800,600]


def main():
    print ("main hi")
    tmpRen = RenderPls()
    tmpRen.setupVariable()
    
class RenderPls ():
    mmmX = [0, 15]
    xStep = [0.1]

    counter =[0]    

    drawXSpace = [50]
    drawYHigh = [10]

    degree = [0]


    DotList = []

    DotList2 = []

    DotList3 = []

    tmpData = []

    def p2(self,x):
        j =  +(1.5* pow(x, 2)  ) - (8*x) + 1
           
        return j

    def lagrangSub (self,inputList , x , index):
        # [xi , yi]
        
        r1 = inputList[index][1]
        r2 = 1

        for i in range( 0, len(inputList) ):
                
            if (i == index):
                continue
            else:
                r2 = r2 * ((x-i)/(r1-i))


        r3 = r2 * r1
        
        return r3

    def lagrang (self,inputList , x ):
        r1 = 0

        for i in range(0,len(inputList)):
            r1 = r1 + self.lagrangSub(self.tmpData, x , i)
            
        return r1

        
    def func(self,x):
        #j =  + (0.5*pow(x, 3)) - (4*pow(x,2)) + (pow(x,1)) - 1
        j =  + (2*pow(x, 3)) - (3*pow(x,2)) + (0.2*pow(x,1)) - 1
           
        return j

        

    def resetTmpData(self):
        self.tmpData = []

        for i in range(self.mmmX[0],self.mmmX[1]):
            x = i
            y = (random.random()*10.0)-5.0

            list = [x,y]
            self.tmpData.append(list)
            

        
    def resetDotList(self):
        self.counter[0] = self.counter[0] + 1
        print self.counter


        self.resetTmpData()
        
    
        self.DotList = []
        self.DotList2 = []

        tP0 = (random.random() * 5.0) - 10.0
        tP1 = (random.random() * 5.0) - 10.0
    
        
        lop = 0
        while (lop < len(self.tmpData)):

            print self.tmpData[lop]
            g = [(self.tmpData[lop][0]*self.drawXSpace[0]), (self.tmpData[lop][1]*self.drawYHigh[0])]
            self.DotList.append(g)
            #lop = lop + self.xStep[0]

            
            g = [(lop*self.drawXSpace[0]) ,((self.p2(lop))*(self.drawYHigh[0])) ]
            #g = [0,0]
            #self.DotList2.append(g)
            
            lop = lop + 1

            if (lop > 10 and lop < 10):
                print ("******* lop " + str(lop) + " = " + str(self.func(lop)))


        lop = 1

        tmpList = []
        self.DotList3 = []


        lop2 = self.mmmX[0]
        #lop2 = 0
        g = 0
        
        while(lop2 < self.mmmX[1]):
            

            g = [(lop2*self.drawXSpace[0]) ,((self.lagrang(self.tmpData,lop2))) ]
            print ("lop2 " , lop2 , " g = " ,g)
            self.DotList3.append(g)
            
            lop2 = lop2 + self.xStep[0]
        
           
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
        
        
        #gluOrtho2D(-winSize[0], winSize[0], -winSize[1], winSize[1]);
        gluOrtho2D(-10, winSize[0], -winSize[1], winSize[1]);
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



        for tmpX in range(0, len(self.DotList3)):
            glBegin(GL_LINES)
            glColor3f(0.2,0.2,0.5);
            
            xxx = tmpX * self.drawXSpace[0];
            yyy = winSize[1]/2;

            glVertex2f(xxx , yyy)

            xxx = tmpX * self.drawXSpace[0];
            #global winSize
            yyy = -winSize[1]/2;

            glVertex2f(xxx , yyy)
            glEnd()

        glColor3f(1.0, 1.0, 1.0);
        
        
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
        while (lop < len(self.DotList2)-1):
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


        glEnd();
        glPopMatrix()





        #glVertex2f(winSize[0] / 2 ,winSize[1] / 2)
        #glVertex2f(winSize[0] / 2 , cos(0) * self.drawYHigh[0])


        

        
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
