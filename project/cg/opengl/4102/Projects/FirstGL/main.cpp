#include <GL/glut.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

#define PI          3.1415926535897932384626433832795
#define SIZE_WIN    500
#define SIZE_ORT    800.0
#define TN          3
#define RN          4


void Init(void);
void Transform(void);
GLfloat theta = 0.0;
GLfloat sign = 1.0; 
GLfloat rsign = 1.0; 
GLfloat xc = 1.0; 
GLfloat yc = 1.0; 
GLfloat sx = 1.0; 
GLfloat sy = 1.0; 

void MyIdle(){
     if ((theta >= 360.0)||(theta < 0.0))
      rsign = rsign *(-1);
     theta += 0.5*rsign;
     if ((sx >= 2.0)||(sx <= 0.0))
         sign = sign *(-1);
     sx += 0.1*sign;
     sy += 0.1*sign;
     
	 glutPostRedisplay();
     
}     
int main(int argc, char** argv)
{
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
//	glutInitWindowPosition(0, 0);
	glutCreateWindow("Transform2D");
	Init();
	glutDisplayFunc(Transform);
	glutIdleFunc(MyIdle);
	glutMainLoop();

    return 0;
}

void Init(void)
{
     glClearColor(1.0, 1.0, 0.0, 0.0);
   
//     glPointSize(4.0);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     gluOrtho2D(-5.0, 5.0, -5.0, 5.0);
       
}

void Transform(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
     // glViewport(SIZE_WIN/2,SIZE_WIN/2,SIZE_WIN/2,SIZE_WIN/2);
     glPushMatrix();
     glColor3f(0.0,0.0,0.0);
     glBegin(GL_LINES);
       glVertex2f(-20.0,0.0);
       glVertex2f( 20.0,0.0); 
       glVertex2f( 0.0, -20.0);
       glVertex2f( 0.0, 20.0);
     glPopMatrix();
     glEnd();
     glPolygonMode(GL_FRONT_AND_BACK,GL_LINE);
     glPushMatrix();
     glColor3f(1, 0, 0);
 //    glRotatef(theta,0,0,1);
     glTranslatef(xc,yc,0); 
     glScalef(sx,sy,0.0);
     glTranslatef(-xc,-yc,0); 
     glBegin(GL_POLYGON);
       glVertex2f(0.5,0.5);
       glVertex2f(0.5,1.5); 
       glVertex2f(1.5,1.5);
       glVertex2f(1.5,0.5);
     glEnd();  
     glPopMatrix();

     glPushMatrix();
     glColor3f(0, 0, 1);
     glTranslatef(-xc,-yc,0); 
     glRotatef(theta,0,0,1);
     glTranslatef(xc,yc,0); 
     glBegin(GL_POLYGON);
       glVertex2f(-0.5,-0.5);
       glVertex2f(-0.5,-1.5); 
       glVertex2f(-1.5,-1.5);
       glVertex2f(-1.5,-0.5);
     glEnd();  
     glPopMatrix();
     glutSwapBuffers();
}
