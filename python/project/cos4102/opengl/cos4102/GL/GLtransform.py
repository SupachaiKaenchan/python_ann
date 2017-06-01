from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0.0
width, height = 300, 300
PI = 3.1415926535897932384626433832795
theta, sign, xsc, ysc, signs = 0.0, 1.0, 1.0, 1.0, 1.0
def initialization():
    glClearColor(0.5, 0.5, 0.5, 0.0)
    glPointSize(5.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-20, 20, -20, 20)

def MyIdle():
    global theta, sign, xsc, ysc, signs
    theta = theta + (0.2*sign)
    xsc = xsc + (0.05*signs)
    ysc = ysc + (0.05 * signs)
    if ((theta >= 360.0) | (theta <= 0.0)):
        sign = sign*(-1)
    if ((xsc >= 2.0) | (xsc <= 0.0)):
        signs = signs*(-1)
    glutPostRedisplay()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-20.0, 0.0)
    glVertex2f(20.0, 0.0)
    glVertex2f(0.0, -20.0)
    glVertex2f(0.0, 20.0)
    glEnd()
    glPopMatrix()
    

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    #glTranslatef(10.0,10.0,0.0)
    glRotatef(theta,0,0,1)
    glTranslatef(-10.0,-10.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(5.0,5.0)
    glVertex2f(10.0,15.0)
    glVertex2f(15.0,5.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.0, 1.0, 1.0)
    glTranslatef(-10.0,-10.0,0.0)
    glScalef(xsc,ysc,0.0)
    glTranslatef(10.0,10.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-15.0,-5.0)
    glVertex2f(-5.0,-5.0)
    glVertex2f(-5.0,-15.0)
    glVertex2f(-15.0,-15.0)
    glEnd()
    glPopMatrix()
    glFlush()
  

def reshape(w,h):
    glViewport(0, 0, w, h)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("My First GL")
    initialization()
    #glutReshapeFunc(reshape)
    glutDisplayFunc(draw)
    glutIdleFunc(MyIdle)
    glutMainLoop()

if __name__ == '__main__':
    main()
