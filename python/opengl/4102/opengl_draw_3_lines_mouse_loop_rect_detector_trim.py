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
cont_Right = 1
cont_Left = 2
cont_Down = 4
cont_Up = 8


xMin = 400 - 50
yMin = 300 - 50

xMax = 400 + 50
yMax = 300 +  50

def main():
    print "main hi"
    tmpRen = RenderPls()
    tmpRen.setupVariable()
    
class RenderPls ():
    a = 0
    b = 0
    
    def __init__(self):
        print "RenderPls init"

    
        
    def setupVariable(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutCreateWindow(name)

        glClearColor(0.,0.,0.,1.)
        glutDisplayFunc(self.display)
        gluOrtho2D(0, 800, 600, 0);
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
                dotList.append(tmpC)

        if button == GLUT_RIGHT_BUTTON:    
            if(state == GLUT_DOWN):
                print ("right click test " + str(x) + " , " + str(y))

                self.trimDot()
                


    def getSideAsBit(self,x,y):
        zz = 0
        
        if (x < xMin):
            zz = zz | cont_Left
        elif(x > xMax):
            zz = zz | cont_Right


        if (y < yMin):
            zz = zz | cont_Up
        elif(y > yMax):
            zz = zz | cont_Down

        return zz    

    
    
    def trimDot(self):
        
        for lop in range(0,len(dotList)):
            mode = self.getSideAsBit(dotList[lop][0] , dotList[lop][1])

            print ("lop " + str(dotList[lop]) + " = " + str(mode))

            if (mode & cont_Left):
                dotList[lop][0] = xMin
                tmpY = (xMax-Xmin) / yMax

                dotList[lop][1] = tmpY
            elif(mode & cont_Right):
                dotList[lop][0] = xMax
                tmpY = (xMax-Xmin) / yMax

                dotList[lop][1] = tmpY

            if (mode & cont_Up):
                dotList[lop][1] = yMin
            elif (mode & cont_Down):
                dotList[lop][1] = yMax

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glLineWidth(2.5);     
        glBegin(GL_LINES);
        # left line
        glColor3f(1.0, 0.0, 0.0);

        #a = random.random() * 800;
        #b = random.random() * 600

        self.a = self.a + 1
#        self.b = self.b + 1

        a = self.a
        b = self.b
        
        glVertex2f(-400, 300);
        glVertex2f(400, 300);
        # right line
        glColor3f(0.0, 1.0, 0.0);
        glVertex2f(400, 300);
        glVertex2f(800, 300);


        glVertex2f(xMin ,yMin)
        glVertex2f(xMin ,yMax)
        glVertex2f(xMax ,yMin)
        glVertex2f(xMax ,yMax)

        glVertex2f(xMin ,yMin)
        glVertex2f(xMax ,yMin)
        glVertex2f(xMin ,yMax)
        glVertex2f(xMax ,yMax)
        

        
        # top line
        glColor3f(0.0, 0.0, 1.0);
        glVertex2f(400, 300);
        glVertex2f(400+(a-400), 300+(b-300));

        bMov = False
        if (bMov == True):
            for lop in range(0,len(dotList)):
                if (dotList[lop][0] > 400):
                    dotList[lop][0] = dotList[lop][0] + 1
                else:
                    dotList[lop][0] = dotList[lop][0] - 1

                if (dotList[lop][1] > 300):
                    dotList[lop][1] = dotList[lop][1] + 1
                else:
                    dotList[lop][1] = dotList[lop][1] - 1

            
        lop = 0
        while (lop < len(dotList)-1):
            tmpX = dotList[lop][0];
            tmpY = dotList[lop][1];

            glVertex2f(tmpX , tmpY)


            tmpX2 = dotList[lop+1][0];
            tmpY2 = dotList[lop+1][1];

            glVertex2f(tmpX2 , tmpY2)
            lop = lop + 2
        
        
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
