from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random

name = 'ball_glut'

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
    glutMainLoop()
    return



def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glLineWidth(2.5);     
    glBegin(GL_LINES);
    # left line
    glColor3f(1.0, 0.0, 0.0);

    a = random.random() * 400;
    
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
    
    glEnd();
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
