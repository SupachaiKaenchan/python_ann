from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

#-----------
# VARIABLES
#-----------

g_fViewDistance = 9.
g_Width = 600
g_Height = 600

g_nearPlane = 1.
g_farPlane = 1000.

action = ""
xStart = yStart = 0.
zoom = 65.

xRotate = 0.
yRotate = 0.
zRotate = 0.

xTrans = 0.
yTrans = 0.


theta, sign = 0.0, 1.0


#-------------------
# SCENE CONSTRUCTOR
#-------------------

def MyIdle():
    global theta, sign
    theta = theta + (0.2*sign)
    if ((theta >= 360.0) | (theta <= 0.0)):
        sign = sign*(-1)


    
    glutPostRedisplay()
    
def SetFrame():
    glPushMatrix()
    glBegin(GL_LINES)
    glVertex2f(-10.,0.)
    glVertex2f( 10., 0.)
    glVertex2f( 0., -10.)
    glVertex2f( 0.,  10.)
    glEnd()
    glPopMatrix()

def Surface(sx,sy,sz,r,g,b):
    glBegin(GL_QUADS)
    (m,n,o) = sur.shape
    for i in range(m):
        r[0] = r[0] + 0.1; b[0] = b[0] - 0.1
        glColor3f(r[0], g[0], b[0])
        for j in range(n):
            glVertex3f(sur[i,j,0] + sx, sur[i,j,1] + sy, sur[i,j,2]+ sz)
    glEnd()
    
def scenemodel():
    glRotate(90,0.,0.,1.)
    #glutSolidTeapot(1.)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    SetFrame()
    #SetGLScene()
    glPushMatrix()
    glRotatef(theta,0,1,0)
    Surface(0,0,0,[0.4],[0.3],[0.9])
    glPopMatrix()

    glPushMatrix()
    glRotatef(theta,1,0,0)
    Surface(-5, 0, -5, [0.1], [0.8], [0.7])
    glPopMatrix()

    glPushMatrix()
    glRotatef(-1*theta,1,0,0)
    Surface( 5, 0, -5, [0.3], [0.5], [0.6])
    glPopMatrix()
    glutSwapBuffers()

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



#--------
# VIEWER
#--------

def printHelp(): 
    print """\n\n    
         -------------------------------------------------------------------\n
         Left Mousebutton       - move eye position (+ Shift for third axis)\n
         Middle Mousebutton     - translate the scene\n
         Right Mousebutton      - move up / down to zoom in / out\n
          Key                - reset viewpoint\n
          Key                - exit the program\n
         -------------------------------------------------------------------\n
         \n"""


def init():
    glEnable(GL_NORMALIZE)
    glLightfv(GL_LIGHT0,GL_POSITION,[ .0, 10.0, 10., 0. ] )
    glLightfv(GL_LIGHT0,GL_AMBIENT,[ .0, .0, .0, 1.0 ]);
    glLightfv(GL_LIGHT0,GL_DIFFUSE,[ 1.0, 1.0, 1.0, 1.0 ]);
    glLightfv(GL_LIGHT0,GL_SPECULAR,[ 1.0, 1.0, 1.0, 1.0 ]);
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glShadeModel(GL_SMOOTH)
    resetView()


def resetView():
    global zoom, xRotate, yRotate, zRotate, xTrans, yTrans
    zoom = 65.
    xRotate = 0.
    yRotate = 0.
    zRotate = 0.
    xTrans = 0.
    yTrans = 0.
    glutPostRedisplay()


def display():
    # Clear frame buffer and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Set up viewing transformation, looking down -Z axis
    glLoadIdentity()
    gluLookAt(0, 0, -g_fViewDistance, 0, 0, 0, -.1, 0, 0)   #-.1,0,0
    # Set perspective (also zoom)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(zoom, float(g_Width)/float(g_Height), g_nearPlane, g_farPlane)
    glMatrixMode(GL_MODELVIEW)
    # Render the scene
    polarView()
    scenemodel()
    # Make sure changes appear onscreen
    glutSwapBuffers()


def reshape(width, height):
    global g_Width, g_Height
    g_Width = width
    g_Height = height
    glViewport(0, 0, g_Width, g_Height)
    

def polarView():
    glTranslatef( yTrans/100., 0.0, 0.0 )
    glTranslatef(  0.0, -xTrans/100., 0.0)
    glRotatef( -zRotate, 0.0, 0.0, 1.0)
    glRotatef( -xRotate, 1.0, 0.0, 0.0)
    glRotatef( -yRotate, .0, 1.0, 0.0)
   

def keyboard(key, x, y):
    global zTr, yTr, xTr
    if(key=='r'): resetView()
    if(key=='q'): exit(0)
    glutPostRedisplay()


def mouse(button, state, x, y):
    global action, xStart, yStart
    if (button==GLUT_LEFT_BUTTON):
        if (glutGetModifiers() == GLUT_ACTIVE_SHIFT):
            action = "MOVE_EYE_2"
        else:
            action = "MOVE_EYE"
    elif (button==GLUT_MIDDLE_BUTTON):
        action = "TRANS"
    elif (button==GLUT_RIGHT_BUTTON):
        action = "ZOOM"
    xStart = x
    yStart = y


def motion(x, y):
    global zoom, xStart, yStart, xRotate, yRotate, zRotate, xTrans, yTrans
    if (action=="MOVE_EYE"):
        xRotate += x - xStart
        yRotate -= y - yStart
    elif (action=="MOVE_EYE_2"):
        zRotate += y - yStart
    elif (action=="TRANS"):
        xTrans += x - xStart
        yTrans += y - yStart
    elif (action=="ZOOM"):
        zoom -= y - yStart
        if zoom > 150.:
            zoom = 150.
        elif zoom < 1.1:
            zoom = 1.1
    else:
        print("unknown action\n", action)
    xStart = x
    yStart = y 
    glutPostRedisplay()


#------
# MAIN
#------
if __name__=="__main__":
    # GLUT Window Initialization

    config()
    
    glutInit()
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB| GLUT_DEPTH)      # zBuffer
    glutInitWindowSize (g_Width,g_Height) 
    glutInitWindowPosition (0 + 4, g_Height / 4)
    glutCreateWindow ("Visualizzatore_2.0")
    # Initialize OpenGL graphics state
    init ()
    # Register callbacks
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)    
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutKeyboardFunc(keyboard)

    glutIdleFunc(MyIdle)
    
    printHelp()
    # Turn the flow of control over to GLUT
    glutMainLoop()
    
    
