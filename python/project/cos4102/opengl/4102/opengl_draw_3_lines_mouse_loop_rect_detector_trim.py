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
                

    def isAccept(self,x1,y1 , x2,y2):
        mode1 = self.getSideAsBit(x1,y1)
        mode2 = self.getSideAsBit(x2,y2)

        if (mode1 == 0 and mode2 == 0):
            return True
        else:
            return False

    def isDiffSide(self,x1,y1 , x2,y2):
        mode1 = self.getSideAsBit(x1,y1)
        mode2 = self.getSideAsBit(x2,y2)

        if (mode1 == mode2):
            return True
        else:
            return False

    def isSeemSide(self,x1,y1 , x2,y2):
        mode1 = self.getSideAsBit(x1,y1)
        mode2 = self.getSideAsBit(x2,y2)

        if (mode1 == mode2):
            return True
        
        return False


        
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

    def reposition(self,x1,y1,mode1 ,x2,y2,mode2):
        # note x y you have to send as Float
        
            if (mode1 & cont_Left):
                
               

                oldM = (y1-y2)/(x1-x2)

                print "left"
                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2))
                print ("oldM " + str(oldM))

                x1 = xMin

                tmpY = (oldM *(x1-x2))+y2
                
                y1 = tmpY
                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2) + " = " + str((y1-y2)/(x1-x2)))
                
            elif(mode1 & cont_Right):

                print "right"
                oldM = (y1-y2)/(x1-x2)

                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2))
                print ("oldM " + str(oldM))

                x1 = xMax
                tmpY = (oldM *(x1-x2))+y2
                
                y1 = tmpY
                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2)+ " = " + str((y1-y2)/(x1-x2)))

                y = tmpY

            if (mode1 & cont_Up):
                print "up"

                oldM = (y1-y2)/(x1-x2)

                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2))
                print ("oldM " + str(oldM))
                y1 = yMin
                
                tmpX = ((y1-y2)/oldM)+x2
                
                x1 = tmpX
                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2) + " = " + str((y1-y2)/(x1-x2)))
                
            elif (mode1 & cont_Down):
                print "down"
                oldM = (y1-y2)/(x1-x2)

                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2))
                print ("oldM " + str(oldM))
                y1 = yMax
                
                tmpX = ((y1-y2)/oldM)+x2
                
                x1 = tmpX
                print (str(y1) + "," + str(y2) + " / " + str(x1) + "," + str(x2)+ " = " + str((y1-y2)/(x1-x2)))


            g = [x1,y1]
            return g
    
    def trimDot(self):
        
        lop = 0
        while(lop < len(dotList)-1):
            x1 = dotList[lop][0]
            y1 = dotList[lop][1]
            x2 = dotList[lop+1][0]
            y2 = dotList[lop+1][1]
            
            mode1 = self.getSideAsBit(x1 , y1)
            mode2 = self.getSideAsBit(x2 , y2)

            print ("lop " + str(dotList[lop]) + " = " + str(mode1))
            print ("lop " + str(dotList[lop]) + " = " + str(mode2))

            if (self.isAccept(x1,y1,x2,y2)):
                print "accept"
            else:
                print "deny"

                if (self.isSeemSide(x1,y1,x2,y2)):
                    print "seem side nothing to do"
                elif (self.isDiffSide(x1,y1,x2,y2)):
                    print "different Side"
                else:
                    print "diferrent side trim point"

                    if (mode2 != 0 and mode1 == 0): # swap
                        ramX = dotList[lop][0]
                        ramY = dotList[lop][1]

                        dotList[lop][0] = dotList[lop+1][0]
                        dotList[lop][1] = dotList[lop+1][1]
                        dotList[lop+1][0] = ramX
                        dotList[lop+1][1] = ramY

                        x1 = dotList[lop][0]
                        y1 = dotList[lop][1]
                        x2 = dotList[lop+1][0]
                        y2 = dotList[lop+1][1]
                        
                        mode1 = self.getSideAsBit(x1 , y1)
                        mode2 = self.getSideAsBit(x2 , y2)

                     
                    g = self.reposition(float(x1),float(y1),mode1,float(x2),float(y2),mode2)
                    dotList[lop][0] = g[0]
                    dotList[lop][1] = g[1]


                    

            lop = lop + 2

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
