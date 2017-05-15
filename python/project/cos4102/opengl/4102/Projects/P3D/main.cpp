#include <GL/glut.h>
#include <math.h>

#define PI          3.1415926535897932384626433832795
#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define RN          4

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
        GLfloat      z;
};

GLfloat theta = 0.0;
GLint sign = 1;
GLint flag = 1;
GLfloat light_position[] = {5,-5,5,0};
GLfloat x = 0.0,y = 0.0,z = 14.0;///??????????y
GLfloat angle;
GLfloat lt_posi[] = {3, 0, 0, 0 };
GLfloat Lt_Amb[] = {0.5,0.5,0.5,0};
void Init(void);
void Transform(void);


void Idle(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);

int main(int argc, char** argv)
{   
    glutInit(&argc ,argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("Cube");
	Init();
	glutDisplayFunc(Transform);
	glutKeyboardFunc(KeyboardKey);
//	glutIdleFunc(Idle);
	glutMainLoop();
    return 0;
}

void Init(void)
{
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glEnable(GL_DEPTH_TEST);
     glEnable(GL_BLEND); 
     glBlendFunc(GL_DST_ALPHA,GL_SRC_ALPHA);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glFrustum(-3, 3, -3, 3, 2, 19);
     glEnable(GL_LIGHT0);
     glLightfv(GL_LIGHT0, GL_POSITION, lt_posi);
     glLightfv(GL_LIGHT0, GL_AMBIENT, Lt_Amb);

}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
     glViewport(0,0,(SIZE_WIN/1),(SIZE_WIN/1));
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
     gluLookAt(((cos(angle)*x)+(sin(angle)*z)),y,((-sin(angle)*x)+(cos(angle)*z)),0,0,5,0,1,0);
     if (flag) 
       glEnable(GL_LIGHTING);
     else
       glDisable(GL_LIGHTING);

     //glRotatef(theta,0,1,0);
     glColor4f(1.0, 1.0, 1.0,1.0);
     glBegin(GL_LINES);
       glVertex2f(-15.0, 0.0);
       glVertex2f(15.0, 0.0);
       glVertex2f(0.0, -15.0);
       glVertex2f(0.0, 15.0);
     glEnd();     

     glPushMatrix();
     glColor4f(1.0, 0.0, 0.0,0.9);
     glTranslatef(0.0,0.0,-8.0);
     glutSolidSphere(10,40,40);
     glPopMatrix();

     glPushMatrix();
     glColor4f(0.0, 1.0, 1.0, 0.9);
     glutSolidCube(10);
     glPopMatrix();
  
  /*   glPushMatrix();
     glRotatef(theta,0,1,0);     
     DrawCube1();
     glPopMatrix();*/

  /*   glPushMatrix();
     glTranslatef(-6,0,-6);
     glRotatef(-theta,0,1,0);     
     glTranslatef( 6,0, 6);
     DrawCube2();
     glPopMatrix();

     glPushMatrix();
     glTranslatef( 6,0,-6);
     glRotatef(theta,0,0,1);     
     glTranslatef( -6,0, 6);
     DrawCube3();
     glPopMatrix(); */
     glutSwapBuffers();
}

void PlotSurface(Point Surface[RN],GLfloat red,GLfloat green,GLfloat blue,GLfloat alpha)
{
    glColor4f(red,green,blue,alpha);
    glBegin(GL_POLYGON);
        for (int i=0; i<RN; i++)
            glVertex3f(Surface[i].x, Surface[i].y, Surface[i].z);
    glEnd();
}

void Idle(void)
{
     if ((theta >= 360.0)||(theta < 0.0))
        sign = sign *(-1);
     theta += (0.3*sign);
     angle = (theta*PI)/180.0;
	 glutPostRedisplay();
}

void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (Key){
            case 0x1B :       /// ESC Button
                 exit(0);
                 break;
            case 0x0D :       /// ESC Button
                 flag = !flag;
                 glutPostRedisplay();
                 break;
     
            default :
                 break;
     }
}



