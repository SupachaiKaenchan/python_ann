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
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(name)

    glClearColor(0.,0.,0.,1.)
    glutDisplayFunc(display)
    gluOrtho2D(0, 800, 600, 0);
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix()

    glutMouseFunc(mouseEvent);

    #while(True):
        #display()
        #print ("looping")

    thread1 = myThread(1, "Thread-1", 1)

    # Start new Threads
    thread1.start()
    

    glutMainLoop()


    return


def mouseEvent( button, state,  x,  y):
    print ("mouse Event " )
    mouseButton = button;
    if button == GLUT_LEFT_BUTTON:    
        if(state == GLUT_DOWN):
            oldX = x;
            oldY = y;
            print ("click " + str(x) + " ," + str(y))

            tmpC = [x,y]
            dotList.append(tmpC)
            


def display():
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
        tmpX = dotList[lop][0];
        tmpY = dotList[lop][1];

        glVertex2f(tmpX , tmpY)
        
    
    
    glEnd();
    glPopMatrix()
    glutSwapBuffers()
    return

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name

        while(True):
            time.sleep(15)

        print "Exiting " + self.name

if __name__ == '__main__': main()
