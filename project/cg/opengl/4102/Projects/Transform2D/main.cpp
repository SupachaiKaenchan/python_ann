#include <GL/glut.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

#define PI          3.1415926535897932384626433832795
#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define TN          3
#define RN          4

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
};
Point P1,P2;
int flag;

void Init(void);
void Transform(void);
void Line(Point p1, Point p2);
void Breshsenham(GLfloat x0, GLfloat y0,GLfloat x1,GLfloat y1);
void Horizonline(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2);
void Test(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2);

int main(int argc, char** argv)
{
	glutInitDisplayMode(GLUT_RGB);
	glutInitWindowSize(640, 480);
	glutInitWindowPosition(300, 300);
	glutCreateWindow("Transform2D");
	Init();
	glutDisplayFunc(Transform);
	glutMainLoop();

    return 0;
}

void Init(void)
{
     Point tmp;
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(4.0);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     gluOrtho2D(-15.0, 15.0, -15.0,15.0);
     P1.x = 1;  P1.y = 15;
     P2.x = 4;  P2.y = 0;

}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT);
     glColor3f(1.0, 1.0, 1.0);
     glPushMatrix();     
     glBegin(GL_LINES);
         glVertex2f(-15.0,0.0);
         glVertex2f( 15.0,0.0);
         glVertex2f( 0.0, -15.0);
         glVertex2f( 0.0, 15.0);
     glEnd();                            
     glPopMatrix();

     glPushMatrix();     
     glRotatef(45,0,0,1);
     glBegin(GL_POLYGON);
         glVertex2f(-1.0,-1.0);
         glVertex2f(-1.0, 1.0);
         glVertex2f( 1.0, 1.0);
         glVertex2f( 1.0, -1.0);
     glEnd();                            
     glPopMatrix();
 
      glColor3f(1.0,0.0,0.0);
      glPushMatrix();     
     glBegin(GL_POLYGON);
         glVertex2f( 2.0, 2.0);
         glVertex2f( 2.0, 4.0);
         glVertex2f( 4.0, 4.0);
         glVertex2f( 4.0, 2.0);
     glEnd();                            
     glPopMatrix();

 
     glFlush();
}

