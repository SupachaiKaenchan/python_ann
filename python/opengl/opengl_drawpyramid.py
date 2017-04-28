try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
 
except: print '''ERROR: PyOpenGL not installed properly.'''
 
import sys
 
def initialize():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glClearColor(0.0,1.0,1.0,0.0)
    glColor3d(1.0,1.0,1.0)
 
 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize (640,480)
    glutInitWindowPosition (0,0)
    window=glutCreateWindow ("Solar")
 
    glutDisplayFunc(mydisplay)
    #glutKeyboardFunc(mydisplay)
    initialize()
 
    glutMainLoop()
    exit()
 
 
def mydisplay():
    initialize()
    glClear (GL_COLOR_BUFFER_BIT)
      
    glBegin( GL_TRIANGLES )
    glColor3f( 1.0, 0.0, 0.0 );
    glVertex3f( 0.0, 1.0, 0.0 );
    glColor3f( 0.0, 1.0, 0.0 );
    glVertex3f( -1.0, -1.0, 1.0 );
    glColor3f( 0.0, 0.0, 1.0 );
    glVertex3f( 1.0, -1.0, 1.0);

    glColor3f( 1.0, 0.0, 0.0 ); glVertex3f( 0.0, 1.0, 0.0);
    glColor3f( 0.0, 1.0, 0.0 ); glVertex3f( -1.0, -1.0, 1.0);
    glColor3f( 0.0, 0.0, 1.0 ); glVertex3f( 0.0, -1.0, -1.0);

    glColor3f( 1.0, 0.0, 0.0 ); glVertex3f( 0.0, 1.0, 0.0);
    glColor3f( 0.0, 1.0, 0.0 ); glVertex3f( 0.0, -1.0, -1.0);
    glColor3f( 0.0, 0.0, 1.0 ); glVertex3f( 1.0, -1.0, 1.0);


    glColor3f( 1.0, 0.0, 0.0 ); glVertex3f( -1.0, -1.0, 1.0);
    glColor3f( 0.0, 1.0, 0.0 ); glVertex3f( 0.0, -1.0, -1.0);
    glColor3f( 0.0, 0.0, 1.0 ); glVertex3f( 1.0, -1.0, 1.0);

    glEnd();

    glFlush()
 
main()
