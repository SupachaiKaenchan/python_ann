from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import sys
fill, view, blend = True, True, True
width, height = 500, 500
theta, sign, dx, speed = 0.0, 1.0, [0.0], [0.0]
def config():
    global sur
    sf1 = [[-1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, -1.0, 1.0]]
    sf2 = [[-1.0, 1.0, 1.0], [-1.0, 1.0, -1.0], [1.0, 1.0, -1.0], [1.0, 1.0, 1.0]]
    sf3 = [[-1.0, -1.0, 1.0], [-1.0, 1.0, 1.0], [-1.0, 1.0, -1.0], [-1.0, -1.0, -1.0]]
    sf1 = np.array(sf1,float)
    sf2 = np.array(sf2,float)
    sf3 = np.array(sf3,float)
    (n,p) = sf1.shape
    sf4 = np.copy(sf1)
    sf5 = np.copy(sf2)
    sf6 = np.copy(sf3)
    for i in range(n):
        sf4[i,2] = sf1[i,2]*-1
        sf5[i,1] = sf2[i,1]*-1
        sf6[i,0] = sf3[i,0]*-1
    sur = np.array((sf1, sf2, sf3, sf4, sf5, sf6))
def InitGLScene():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
def SetFrame():
    glPushMatrix()
    glBegin(GL_LINES)
    glVertex2f(-10.,0.)
    glVertex2f( 10., 0.)
    glVertex2f( 0., -10.)
    glVertex2f( 0.,  10.)
    glEnd()
    glPopMatrix()
    if fill:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    if blend:
        glEnable(GL_BLEND)
    else:
        glDisable(GL_BLEND)
def Surface(sx,sy,sz,r,g,b):
    glBegin(GL_QUADS)
    (m,n,o) = sur.shape
    for i in range(m):
        r[0] = r[0] + 0.1; b[0] = b[0] - 0.1
        glColor4f(r[0], g[0], b[0], 0.6)
        for j in range(n):
            glVertex3f(sur[i,j,0] + sx, sur[i,j,1] + sy, sur[i,j,2]+ sz)
    glEnd()
def Object(rot, surf):
    glPushMatrix()
    glRotatef(rot[0], rot[1], rot[2], rot[3])
    Surface(surf[0], surf[1], surf[2], surf[3], surf[4], surf[5])
    glPopMatrix()
def DrawObjects():
    Object([theta,0,1,0], [0, 0, 0, [0.4], [0.3], [0.9]])
    Object([theta,1,0,0], [-5, 0, -5, [0.1], [0.8], [0.7]])
    Object([-1*theta,1,0,0], [5, 0, -5, [0.3], [0.5], [0.8]])
def SetViewModel(port, at):
    glViewport(port[0], port[1], port[2], port[3])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if view:
        gluPerspective(90., 1., 0.5, 80.)
    else:
        glOrtho(-10, 10, -10, 10, -10, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(at[0], at[1], at[2], 0, 0, 0, at[3], at[4], at[5])
def SetGLMotion(port, at):
    SetFrame()
    SetViewModel(port, at)
    DrawObjects()
def DrawGLScene():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    SetGLMotion([0,0,int(width/2.0),int(height/2.0)], [0,0,8+dx[0],0,1,0])
    SetGLMotion([int(width/2.0),0,int(width/2.0),int(height/2.0)], [8+dx[0],0,0,0,1,0])
    SetGLMotion([0, int(height / 2.0), int(width / 2.0), int(height / 2.0)], [0, 0, -8-dx[0], 0, 1, 0])
    SetGLMotion([int(width/2.0), int(height / 2.0), int(width / 2.0), int(height / 2.0)], [0, 8+dx[0], 0, 1, 0, 0])
    glutSwapBuffers()
def On_keyboard(key, x, y):
    global fill, view, dx, speed, blend
    while True:
        if key == b'\x1b':
            sys.exit()
        if key == b'f':
            fill = not fill
            break
        if key == b'v':
            view = not view
            break
        if key == b'b':
            blend = not blend
            break
        if key == b'x':
            dx[0] = dx[0] + 0.5
            break
        if key == b'y':
            dx[0] = dx[0] - 0.5
            break
        if key == b'm':
            if speed[0] < 1.3:
                speed[0] = speed[0] + 0.1
            break
        if key == b'n':
            if speed[0] > 0.1:
                speed[0] = speed[0] - 0.1
            break
        break
    glutPostRedisplay()
def MyIdle():
    global theta, sign
    theta = theta + ((0.2 + speed[0])*sign)
    if ((theta >= 360.0) | (theta <= 0.0)):
        sign = sign*(-1)
    glutPostRedisplay()
def On_reshape(w, h):
    global width, height
    width, height = w, h
def main():
    glutInit(sys.argv)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow(b'cube')
    InitGLScene()
    glutDisplayFunc(DrawGLScene)
    glutKeyboardFunc(On_keyboard)
    glutReshapeFunc(On_reshape)
    glutIdleFunc(MyIdle)
    glutMainLoop()
if __name__ == "__main__":
    config()
    main()