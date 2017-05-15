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
//	glutInitDisplayMode(GLUT_RGB);
//	glutInitWindowSize(500, 500);
//	glutInitWindowPosition(300, 300);
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
     gluOrtho2D(-40.0, 40.0, -40.0, 40.0);
     P1.x = 1;  P1.y = 15;
     P2.x = 4;  P2.y = 0;
     if (P1.x > P2.x){
         tmp = P1;
         P1 = P2;
         P2 = tmp; 
     }         
  

}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT);
     glColor3f(1.0, 1.0, 1.0);
     glPushMatrix();
     
     Line(P1,P2);
     glPopMatrix();
     glFlush();
}
void Line(Point p1, Point p2){
GLfloat dx,dy,m;
     dy  = p2.y - p1.y;
     dx  = p2.x - p1.x;
     Breshsenham(-p1.y,p1.x,-p2.y,p2.x); 
/*     if (dx == 0){ 
            Horizonline(p1.y,p1.x,p2.y,p2.x);
            flag = 0;
     }       
     else {

         m = dy/dx;
         if (m == 0){
            Horizonline(p1.x,p1.y,p2.x,p2.y);
            flag =1;
            }   
         else
            Breshsenham(p1,p2,dy,-dx);                
     }*/                      
}   
void Breshsenham(GLfloat x0, GLfloat y0,GLfloat x1,GLfloat y1)
{
GLfloat dx,dy;
GLfloat a,b;
GLfloat x,y,d;     
     dy  = y1- y0;
     dx  = x1- x0;
     a = dy; b = -dx;
     x = x0;  y = y0;
     glBegin(GL_POINTS);
          glVertex2f(-y, x);
          d = (2*a) + b; 
          while (x <= x1){
                x = x + 1;
                if (d < 0)
                   d = d + (2*a);
                else{
                   d = d + 2*(a+b);
                   y = y+1;  
                }     
                glVertex2f(-y, x);      
          }
     glEnd();                       
}
void Horizonline(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2)
{
GLfloat x,y;
  
         glBegin(GL_POINTS);      
            for (x = x1; x <= x2; x++)
               if (flag==1) 
                  glVertex2f(x, y1);
               else
                  glVertex2f(y1,x);
         glEnd();     
}     
void Test(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2){
     return;     
}     
