from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
sf1 = [[-1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0,-1.0, 1.0]]
sf2 = [[-1.0,  1.0, 1.0], [-1.0, 1.0, -1.0], [1.0, 1.0, -1.0], [1.0, 1.0, 1.0]]
sf3 = [[-1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [-1.0, 1.0, -1.0], [-1.0,-1.0, -1.0]]

def config():
    global sf1, sf2, sf3, sf4, sf5, sf6
    sf1 = np.array(sf1,float)
    sf2 = np.array(sf2,float)
    sf3 = np.array(sf3,float)
    (n,p) = sf1.shape
    sf4 = np.copy(sf1)
    sf5 = np.copy(sf2)
    sf6 = np.copy(sf3)
    for i in range(n):
        sf4[i,2] = sf1[i,2]*-1
        sf5[i,1] = sf1[i,1]*-1
        sf6[i,0] = sf3[i,0]*-1

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    ReSizeGLScene(Width, Height)


def ReSizeGLScene(width, height):
   # glViewport(width/2, height/2, width/2, height/2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90., 1., 0.5, 80.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10, 0, 0, 0, 0, 0, 0, 1, 0)
'''    gluPerspective(90.0, float(width) / float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()'''
def Surface(sur,r,g,b):
    #glPushMatrix()
    glBegin(GL_POLYGON)
    glColor4f(r, g, b, 1.0)  # 0.666)
    n = sur.__len__()
    for i in range(n):
        glVertex3f(sur[i][0], sur[i][1], sur[i][2])
    glEnd()
    #glPopMatrix()


def DrawGLScene():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(45,0,1,0)
    Surface(sf1,0.4,0.4,0.4)
    Surface(sf2,0.5,0.4,0.9)
    Surface(sf3,0.6,0.4,0.8)
    Surface(sf4,0.7,0.4,0.7)
    Surface(sf5,0.8,0.4,0.6)
    Surface(sf6,0.9,0.4,0.5)
    glPopMatrix()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow(b'cube')
    InitGL(500, 500)
    glutDisplayFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutMainLoop()


if __name__ == "__main__":
    config()
    main()
