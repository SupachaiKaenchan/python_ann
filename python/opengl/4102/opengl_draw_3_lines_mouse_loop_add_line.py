from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random
import threading
import time

name = 'ball_glut'

dotList = []

def main():
    print "main hi"
    tmpRen = RenderPls()
    tmpRen.setupVariable()
    
class RenderPls ():
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

        thread1 = myThread(1, "Thread-1", 1,self)

        # Start new Threads
        thread1.start()
        

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
                


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glLineWidth(2.5);     
        glBegin(GL_LINES);
        # left line
        glColor3f(1.0, 0.0, 0.0);

        a = random.random() * 800;
        
        glVertex2f(-400, 300);
        glVertex2f(400, 300);
        # right line
        glColor3f(0.0, 1.0, 0.0);
        glVertex2f(400, 300);
        glVertex2f(800, 300);
        
        # top line
        glColor3f(0.0, 0.0, 1.0);
        glVertex2f(a, 0);
        glVertex2f(a, 300);


        for lop in range(0,len(dotList)):
            if (dotList[lop][0] < 400):
                dotList[lop][0] = dotList[lop][0] + 1
            else:
                dotList[lop][0] = dotList[lop][0] - 1

            if (dotList[lop][1] < 300):
                dotList[lop][1] = dotList[lop][1] + 1
            else:
                dotList[lop][1] = dotList[lop][1] - 1

            
        for lop in range(0,len(dotList)-1):
            tmpX = dotList[lop][0];
            tmpY = dotList[lop][1];

            glVertex2f(tmpX , tmpY)


            tmpX2 = dotList[lop+1][0];
            tmpY2 = dotList[lop+1][1];

            glVertex2f(tmpX2 , tmpY2)
                        
        
        
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
