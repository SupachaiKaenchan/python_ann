from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             
width, height = 500, 400
theta = [0.0]


def initialization():
    glClearColor(0.0,0.0,0.0,0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-20, 20, -20, 20);
    
def draw():                                            
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(-10,-10)
    glVertex2f(-10,10)
    glVertex2f(10,10)
    glVertex2f(10,-10)
    glEnd()
    glPopMatrix()
    
    
    glColor3f(0.0, 0.0,0.0);
    glPushMatrix()
    glRotate(theta[0],0,0,1)
    glBegin(GL_LINES)
    glVertex2f(-5,-5)
    glVertex2f(5,5)
    glEnd()
    glPopMatrix()
    #glFlush()
    glutSwapBuffers()
    #MyIdle()
    #glutPostRedisplay()

def MyIdle():
    global theta
    theta[0] = theta[0] + 0.1
    glutPostRedisplay()

    
def main():

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB )
    #glutInitDisplayMode(GLUT_RGB )
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("My First GL")
    initialization()
    glutDisplayFunc(draw)
    glutIdleFunc(MyIdle)
    glutMainLoop()
    
if __name__ == '__main__':
    main()
                                         
