#include <GL/glut.h>
#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <ctype.h>
#define PI          3.1415926535897932384626433832795
#define SIZE_ORT    500.0
#define RN          4

GLint Sw = 600;
GLint Sh = 600;
GLfloat x = 0.0,y = 0.0,z = 14.0;

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
        GLfloat      z;
};
Point sf1N[RN],sf1L[RN],sf1R[RN],sf1T[RN],sf1B[RN],sf1F[RN];

GLfloat theta = 0.0;
GLfloat angle;
GLint sign = 1;
int Lht = 1;
int Lno = 1;

GLfloat lt0_position[] = {0.0,18.0,0.0,0.0};
GLfloat lt1_position[] = {18.0,0.0,0.0,0.0};
GLfloat lt2_position[] = {0.0,0.0,18.0,0.0};
//GLfloat spot_light_direction[] = {-5.0, -5.0, -5.0 };
GLfloat lt_ambient[]  = {0.8,0.8,0.8,1.0};
GLfloat lt_diffuse[]  = {1.0,1.0,1.0,1.0};
GLfloat  mdif_cen[]  =  {1.0,0.0,0.0,1.0};
GLfloat  mdif_left[]  = {0.0,1.0,0.0,1.0};
GLfloat  mdif_right[]  ={0.0,0.0,1.0,1.0};

GLfloat  amb_cen[]  =  {0.35,0.0,0.0,1.0};
GLfloat  amb_left[]  = {0.0,0.35,0.0,1.0};
GLfloat  amb_right[]  ={0.0,0.0,0.35,1.0};



void Init(void);
void Transform(void);
void ConfigPoint(void);
void PlotSurface(Point Surface[RN],GLfloat red,GLfloat green,GLfloat blue);
void DrawCube(int);
void OnDraw(int);
void Idle(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void Reshape(GLint width, GLint height); 
void SetLookAt(GLfloat eyeX,GLfloat eyeY,GLfloat eyeZ,GLfloat x,GLfloat y,GLfloat z,GLfloat vexX,GLfloat vexY,GLfloat vexZ);

int main(int argc, char** argv)
{
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(Sw, Sh);
	glutInitWindowPosition(50, 50);
	glutCreateWindow("Cube");
	Init();
	glutDisplayFunc(Transform);
	glutKeyboardFunc(KeyboardKey);
	glutIdleFunc(Idle);
	glutReshapeFunc(Reshape);
	glutMainLoop();
    return 0;
}

void Init(void)
{
     ConfigPoint();
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glEnable(GL_DEPTH_TEST);
     glBlendFunc(GL_ONE_MINUS_DST_COLOR, GL_ONE);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(-20, 20,-20, 20,-20, 20);
//     glFrustum(-3, 3, -3, 3, 2, 20);  
     glLightfv(GL_LIGHT0,GL_DIFFUSE,lt_diffuse);
     glLightfv(GL_LIGHT0,GL_AMBIENT,lt_ambient);

     glLightfv(GL_LIGHT1,GL_DIFFUSE,lt_diffuse);
     glLightfv(GL_LIGHT1,GL_AMBIENT,lt_ambient);

     glLightfv(GL_LIGHT2,GL_DIFFUSE,lt_diffuse);
     glLightfv(GL_LIGHT2,GL_AMBIENT,lt_ambient);


/*     glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 60.0);
     glLightfv(GL_LIGHT0,GL_SPOT_DIRECTION,spot_light_direction);
     glLightf(GL_LIGHT0, GL_SPOT_EXPONENT,50);     */

}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
     glViewport(0, 0, Sw, Sh);
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();  
     angle = 0; 
     SetLookAt(((cos(angle)*x)+(sin(angle)*z)),y,((-sin(angle)*x)+(cos(angle)*z)),0,0,0,0,1,0);

     if (Lht) {
         glEnable(GL_LIGHTING);        
         glDisable(GL_BLEND);
     }else {
         glDisable(GL_LIGHTING);   
         glEnable(GL_BLEND);
     }    
     switch (Lno){
         case 1 :               
               glDisable(GL_LIGHT2);
               glEnable(GL_LIGHT0); 
               break;
         case 2 :              // Press 'n' or 'N' to Reset Object
               glDisable(GL_LIGHT0);
               glEnable(GL_LIGHT1);                
               break;
         case 3 :              // Press 'n' or 'N' to Reset Object
               glDisable(GL_LIGHT1);
               glEnable(GL_LIGHT2); 
               break;               
     }      
 
     glPushMatrix();             
     glRotatef(theta,0,0,1);     
     glLightfv(GL_LIGHT0,GL_POSITION,lt0_position);
     glPopMatrix();  
        
     glPushMatrix();             
     glRotatef(theta,0,1,0);     
     glLightfv(GL_LIGHT1,GL_POSITION,lt1_position);       
     glTranslatef(lt1_position[0],lt1_position[1],lt1_position[2]);
//     glDisable(GL_LIGHTING);
     glColor4f(1.0,1.0,0.0,1.0);
     glutSolidSphere(0.5,60,60);
 //    glEnable(GL_LIGHTING);
     glPopMatrix();     

     glPushMatrix();             
     glRotatef(theta,1,0,0);     
     glLightfv(GL_LIGHT2,GL_POSITION,lt2_position);     
     glPopMatrix();     
     
     
     glPushMatrix();     
     glColor4f(0.8,0.0,0.0,0.8);     
     glMaterialfv(GL_FRONT, GL_DIFFUSE, mdif_cen);
     glMaterialfv(GL_FRONT, GL_AMBIENT, amb_cen);          
     glutSolidSphere(3,60,60);
     glPopMatrix();

     glPushMatrix();     
     glColor4f(0.0,0.8,0.0,0.8);
     glMaterialfv(GL_FRONT, GL_DIFFUSE, mdif_left);
     glMaterialfv(GL_FRONT, GL_AMBIENT, amb_left);
     glTranslatef(-8,0,0);
     glutSolidSphere(3,60,60);
     glPopMatrix();

     glPushMatrix();
     glColor4f(0.0,0.0,0.8,0.8);     
     glMaterialfv(GL_FRONT, GL_DIFFUSE, mdif_right);
     glMaterialfv(GL_FRONT, GL_AMBIENT, amb_right);
     glTranslatef(8,0,0);
     glutSolidSphere(3,60,60);
     glPopMatrix(); 
     glutSwapBuffers();
}
void OnDraw(int k){
     glPushMatrix();     
     glColor4f(0.5, 0.5, 0.5,1.0);
     glBegin(GL_LINES);
          glVertex2f(-15.0, 0.0);
          glVertex2f(15.0, 0.0);
          glVertex2f(0.0, -15.0);
          glVertex2f(0.0, 15.0);
     glEnd();
     glPopMatrix();
     glPushMatrix();
     DrawCube(k);
     glPopMatrix();
}     

void PlotSurface(Point Surface[RN],GLfloat red,GLfloat green,GLfloat blue)
{
    glColor4f(red,green,blue,0.5);
    glBegin(GL_POLYGON);
        for (int i=0; i<RN; i++)
            glVertex3f(Surface[i].x, Surface[i].y, Surface[i].z);
    glEnd();
}

void ConfigPoint(void)
{     ///surface???????????? Cube center
      sf1N[0].x = -2.0;       sf1N[0].y = -2.0;     sf1N[0].z = 2.0;
      sf1N[1].x = -2.0;       sf1N[1].y = 2.0;      sf1N[1].z = 2.0;
      sf1N[2].x = 2.0;        sf1N[2].y = 2.0;      sf1N[2].z = 2.0;
      sf1N[3].x = 2.0;        sf1N[3].y = -2.0;     sf1N[3].z = 2.0;
      ///surface???????????? Cube center
      sf1L[0].x = -2.0;      sf1L[0].y = -2.0;      sf1L[0].z = -2.0;
      sf1L[1].x = -2.0;      sf1L[1].y = 2.0;       sf1L[1].z = -2.0;
      sf1L[2].x = -2.0;      sf1L[2].y = 2.0;       sf1L[2].z = 2.0;
      sf1L[3].x = -2.0;      sf1L[3].y = -2.0;      sf1L[3].z = 2.0;
      ///surface??????????? Cube center
      sf1R[0].x = 2.0;       sf1R[0].y = -2.0;      sf1R[0].z = 2.0;
      sf1R[1].x = 2.0;       sf1R[1].y = 2.0;       sf1R[1].z = 2.0;
      sf1R[2].x = 2.0;       sf1R[2].y = 2.0;       sf1R[2].z = -2.0;
      sf1R[3].x = 2.0;       sf1R[3].y = -2.0;      sf1R[3].z = -2.0;
      ///surface?????????? Cube center
      sf1T[0].x = -2.0;      sf1T[0].y = 2.0;       sf1T[0].z = 2.0;
      sf1T[1].x = -2.0;      sf1T[1].y = 2.0;       sf1T[1].z = -2.0;
      sf1T[2].x = 2.0;       sf1T[2].y = 2.0;       sf1T[2].z = -2.0;
      sf1T[3].x = 2.0;       sf1T[3].y = 2.0;       sf1T[3].z = 2.0;
      ///surface???????????? Cube center
      sf1B[0].x = -2.0;      sf1B[0].y = -2.0;      sf1B[0].z = -2.0;
      sf1B[1].x = -2.0;      sf1B[1].y = -2.0;      sf1B[1].z = 2.0;
      sf1B[2].x = 2.0;       sf1B[2].y = -2.0;      sf1B[2].z = 2.0;
      sf1B[3].x = 2.0;       sf1B[3].y = -2.0;      sf1B[3].z = -2.0;
      ///surface???????????? Cube center
      sf1F[0].x = -2.0;      sf1F[0].y = 2.0;       sf1F[0].z = -2.0;
      sf1F[1].x = -2.0;      sf1F[1].y = -2.0;      sf1F[1].z = -2.0;
      sf1F[2].x = 2.0;       sf1F[2].y = -2.0;      sf1F[2].z = -2.0;
      sf1F[3].x = 2.0;       sf1F[3].y = 2.0;       sf1F[3].z = -2.0;
}

void DrawCube(int k)
{             
     glPushMatrix();
//     glRotatef(theta*k,0,1,0);
     PlotSurface(sf1N,1.0,0.1,0.5);
     PlotSurface(sf1L,0.6,1.0,0.4);
     PlotSurface(sf1R,0.8,1.0,0.5);
     PlotSurface(sf1T,0.3,0.6,1.0);
     PlotSurface(sf1B,0.5,0.5,1.0);
     PlotSurface(sf1F,1.0,0.5,1.0);
     glPopMatrix();
     
     
}
void Reshape(GLint width, GLint height){
     Sw = width;   
     Sh = height;           
}     

void Idle(void)
{
     if ((theta >= 360.0)||(theta < 0.0))
        sign = sign *(-1);
     theta += (0.5*sign);
     angle = (theta*PI)/180.0;
	 glutPostRedisplay();
}
void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (tolower(Key))
     {
            case 0x1B :               // Press Esc to exit
                 exit(0);
                 break;
            case 0x6E :              // Press 'n' or 'N' to Reset Object
                 Lht = !Lht; 
                 break;
            case 0x20 :              // Press 'n' or 'N' to Reset Object
                 Lno += 1;
                 if (Lno > 3)
                   Lno = 1; 
                 break;
                 
     }      // Switch
     glutPostRedisplay();
}
void SetLookAt(GLfloat eyeX,GLfloat eyeY,GLfloat eyeZ,GLfloat x,GLfloat y,GLfloat z,GLfloat vexX,GLfloat vexY,GLfloat vexZ)
{
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(eyeX, eyeY, eyeZ, x, y, z, vexX, vexY, vexZ);
}
