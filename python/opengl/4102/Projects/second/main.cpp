#include <GL/glut.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

#define PI          3.1415926535897932384626433832795
#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define TN          3
#define RN          4
GLfloat theta = 0.0;
GLint sign = 1;


void Init(void);
void Transform(void);
void Idle(void);
int main(int argc, char** argv)
{
	glutCreateWindow("Transform2D");
	Init();
	glutDisplayFunc(Transform);
	glutIdleFunc(Idle);
	glutMainLoop();

    return 0;
}

void Init(void)
{
     glClearColor(0.05, 0.05, 0.05, 0.0);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     gluOrtho2D(-2.0, 2.0, -2.0, 2.0);

}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT);
     glColor3f(1.0, 1.0, 1.0);

     glPushMatrix();
//     glRotatef(theta,0,0,1); 
     glBegin(GL_LINES);
          glVertex2f(-1.0, -1.0);
          glVertex2f( 1.0,  1.0);
     glEnd();
     glPopMatrix();

     glFlush();
}
void Idle(void)
{
     if ((theta >= 360.0)||(theta < 0.0))
        sign = sign *(-1);
     theta += (0.5*sign);

	 glutPostRedisplay();
}
