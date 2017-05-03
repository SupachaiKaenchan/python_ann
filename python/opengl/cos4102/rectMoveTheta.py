from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             
width, height = 500, 400
theta = [0.0]
sign = [1.0]

xMin = [-10.0]
xMax = [10.0]
yMin = [-10.0]
yMax= [10.0]

def initialization():
    glClearColor(0.0,0.0,0.0,0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluOrtho2D(-20, 20, -20, 20);
    
def draw():                                            
    global xMin
    global xMax
    global yMin
    global yMax

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)

    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)


    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(xMin[0],yMin[0])
    glVertex2f(xMin[0],yMax[0])
    glVertex2f(xMax[0],yMax[0])
    glVertex2f(xMax[0],yMin[0])

    
    glEnd()
    glPopMatrix()

    glColor3f(1.0, 1.0,1.0);
    glPushMatrix()
    glRotate(theta[0],0,0,1)
    glBegin(GL_LINES)
    glVertex2f(-5,-5)
    glVertex2f(5,5)
    glEnd()
    glPopMatrix()
    glFlush()
    #glutSwapBuffers()
    #MyIdle()
    #glutPostRedisplay()

def MyIdle():
    global theta
    theta[0] = theta[0] + 0.1
    glutPostRedisplay()

def keyBoardEvent(key,x,y):
    global theta
    global sign
    
    
    if (key == "a"):
        if(theta[0] > 360 or theta[0] < 0):
            sign[0] = sign[0] * -1
            
        theta[0] = theta[0] + (sign[0]*10)

        
    if (key == "b"):
        if(theta[0] > 360 or theta[0] < 0):
            sign[0] = sign[0] * -1
            
        theta[0] = theta[0] + (sign[0]*(-10))

    if (key == "s"): 
        xMin[0] = xMin[0] + 1
        
    glutPostRedisplay()

def specialKeyEvent(key,x,y):
    #print key
    
    global theta
    global sign
    
    if (key == GLUT_KEY_LEFT):
        if (xMin[0] > -20):
            xMin[0] = xMin[0] - 1.0
            xMax[0] = xMax[0] - 1.0
        
    if (key == GLUT_KEY_RIGHT):
        if (xMax[0] < 20):
            xMin[0] = xMin[0] + 1.0
            xMax[0] = xMax[0] + 1.0

    if (key == GLUT_KEY_DOWN):
        if (yMin[0] > -20):
            yMin[0] = yMin[0] - 1.0
            yMax[0] = yMax[0] - 1.0
        
    if (key == GLUT_KEY_UP):
        if (yMax[0] < 20):
            yMin[0] = yMin[0] + 1.0
            yMax[0] = yMax[0] + 1.0
        
    glutPostRedisplay()

    
    
def main():

    glutInit()

    glutInitDisplayMode(GLUT_RGB )
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("My First GL")
    initialization()
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyBoardEvent)
    glutSpecialFunc(specialKeyEvent)

    #glutIdleFunc(MyIdle)
    glutMainLoop()
    
if __name__ == '__main__':
    main()
                                         
