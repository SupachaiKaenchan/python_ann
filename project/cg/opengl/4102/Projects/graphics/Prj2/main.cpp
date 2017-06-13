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
} Point;

Point sf1N[RN],sf1L[RN],sf1R[RN],sf1T[RN],sf1B[RN],sf1F[RN];


GLfloat theta = 0.0;
GLfloat xsc = 1.0, ysc = 1.0, zsc = 1.0;
GLfloat xe = 0.0, ye = 0.0, ze = 10.0;
GLfloat xat = 0.0, yat = 0.0, zat = 0.0;
GLfloat xt = 1.0, yt = 0.0, zt = 0.0;
GLint   flag = 1;
GLint   sign = 1;
GLfloat scale_sign = 0.001;
//GLfloat light_position[] = {10.5, 10.5, 0, 0};

GLfloat light_position[] = {8, 0, 0, 0};

GLfloat green = 0.7;
GLfloat fLtAmbient[4] = {0.0,green,0.0,1.0};
GLfloat fLtDiffuse[4] = {0.0,green,0.0,1.0};
GLfloat fLtSpecular[4] = {0.0,0.0,0.0,1.0};

GLfloat fMatAmbient[4] = {0.0,green*0.75,0.0,1.0};
GLfloat fMatDiffuse[4] = {0.0,green*0.85,0.0,1.0};
GLfloat fMatSpecular[4] = {0.0,0.0,0.0,1.0};



void Init(void);
void Transform(void);
void ConfigPoint(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void SpecialKey(GLint Key, GLint x, GLint y);
void Idle(void);
void DrawCube(void);
void PlotSurface(Point Surface[RN],GLfloat red,GLfloat green,GLfloat blue);
void Cooridinate();
void DrawObject();
void SetProjectionMode();
void MyViewport(GLint index);
void SetLookAt(GLint index);

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("Transform3D");

	Init();

	glutDisplayFunc(Transform);
	glutKeyboardFunc(KeyboardKey);
	glutSpecialFunc(SpecialKey);
	glutIdleFunc(Idle);

	glutMainLoop();

    return 0;
}

void Init(void)
{
     glClearColor(0.5, 0.7, 0.5, 0.0);
     glPointSize(1.0);
     glEnable(GL_DEPTH_TEST);
     glEnable(GL_BLEND);
     glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);
//     glBlendFunc(GL_ONE,GL_ONE);

     ConfigPoint();
}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
     SetProjectionMode();

     glPushMatrix();
     MyViewport(0);
     DrawObject();
     glPopMatrix();

     glPushMatrix();
     MyViewport(1);
     DrawObject();
     glPopMatrix();

     glPushMatrix();
     MyViewport(2);

     glPushMatrix();
     glRotatef(theta,0,0,1);
     glLightfv(GL_LIGHT1, GL_POSITION,light_position);
     glColor4f(1.0,0.0,0.0,0.5);
     glTranslatef(8.0,0.0,0.0);
     glutSolidCube(1.0);
     glPopMatrix();

     glLightfv(GL_LIGHT1, GL_AMBIENT, fLtAmbient);
     glMaterialfv(GL_FRONT,GL_AMBIENT, fMatAmbient);


     glLightfv(GL_LIGHT1, GL_DIFFUSE, fLtDiffuse);
     glMaterialfv(GL_FRONT,GL_DIFFUSE, fMatDiffuse);

     glLightfv(GL_LIGHT1, GL_SPECULAR, fLtSpecular);
     glMaterialfv(GL_FRONT,GL_SPECULAR, fMatSpecular);

     glEnable(GL_LIGHTING);
     glEnable(GL_LIGHT1);

     glColor4f(0.0,1.0,0.0,0.5);
     glutSolidSphere(3.0,20,20);
   //  DrawObject();
     glDisable(GL_LIGHT1);
     glDisable(GL_LIGHTING);
     glPopMatrix();

     glPushMatrix();
     MyViewport(3);
     DrawObject();
     glPopMatrix();

     glutSwapBuffers();




}

void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (Key)
     {
            case 0x1B :       // ESC Button
                 exit(0);
                 break;
            case 0x7A :       // z Button
                 sign = sign * -1;
                 glutPostRedisplay();
                 break;
            default :
                    break;
     }
}

void SpecialKey(GLint Key, GLint x, GLint y)
{
     switch (Key)
     {
            case GLUT_KEY_LEFT :
                 theta += 10.0;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_RIGHT :
                 theta -= 10.0;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_DOWN :
                 xsc += 0.1;
                 ysc += 0.1;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_UP :
                 xsc -= 0.1;
                 ysc -= 0.1;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_HOME :
                 xsc -= 0.1;
				 glutPostRedisplay();
				 break;
            case GLUT_KEY_END :
                 xsc += 0.1;
                 glutPostRedisplay();
                 break;
            default :
                    break;
     }
}

void Idle(void)
{
     if (flag)
        if (theta >= 360)
           theta = 0;
        else
            theta += 0.5;
     else
        if (theta <= -360)
           theta = 0;
        else
            theta -= 0.5;

     if (xsc < 0.1)
        scale_sign = 0.001;
     if (xsc > 2.0)
        scale_sign = -0.001;
     xsc += scale_sign;
     ysc += scale_sign;

	glutPostRedisplay();
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
void DrawCube(void)
{
     PlotSurface(sf1N,1.0,0.0,0.0);
     PlotSurface(sf1L,0.0,1.0,0.0);
     PlotSurface(sf1R,0.0,1.0,0.5);
     PlotSurface(sf1T,0.0,0.0,1.0);
     PlotSurface(sf1B,0.5,0.0,1.0);
     PlotSurface(sf1F,1.0,0.5,0.0);
}
void PlotSurface(Point Surface[],GLfloat red,GLfloat green,GLfloat blue)
{
    glColor4f(red,green,blue,0.65);
    glBegin(GL_POLYGON);
        for (int i=0; i<RN; i++)
            glVertex3f(Surface[i].x, Surface[i].y, Surface[i].z);
    glEnd();
}
void Cooridinate()
{
     glPushMatrix();
     glColor4f(1.0, 1.0, 1.0,0.5);
     glBegin(GL_LINES);
          glVertex2f(-10.0, 0.0);
          glVertex2f(10.0, 0.0);
          glVertex2f(0.0, -10.0);
          glVertex2f(0.0, 10.0);
     glEnd();
     glPopMatrix();
}
void DrawObject()
{
     Cooridinate();

     glPushMatrix();
     glRotatef(theta,0,1,0);
     DrawCube();
     glPopMatrix();

     glPushMatrix();
     glTranslatef(-6.0,0.0,-6.0);
     glRotatef(theta,0,0,1);
     DrawCube();
     glPopMatrix();

     glPushMatrix();
     glColor3f(0.0,0.0,1.0);
     glTranslatef(6.0,0.0,6.0);
     glRotatef(theta,1,0,0);
     DrawCube();
     glPopMatrix();
}

void MyViewport(GLint index)
{
     switch (index)
     {
            case 0 :
                 glViewport(0, 0, SIZE_WIN/2, SIZE_WIN/2);
                 break;
            case 1 :
                 glViewport(0, SIZE_WIN/2, SIZE_WIN/2, SIZE_WIN/2);
                 break;
            case 2 :
                 glViewport(SIZE_WIN/2, SIZE_WIN/2, SIZE_WIN/2, SIZE_WIN/2);
                 break;
            case 3 :
                 glViewport(SIZE_WIN/2, 0, SIZE_WIN/2, SIZE_WIN/2);
                 break;
            default :
                break;
     }
     SetLookAt(index);
}
void SetLookAt(GLint index)
{
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
     switch (index)
     {
            case 0 :
                 gluLookAt(0, 10, 0, xat, yat, zat, 1, 0, 0);
                 break;
            case 1 :
                 gluLookAt(10, 0, 0, xat, yat, zat, 0, 1, 0);
                 break;
            case 2 :
                 gluLookAt(xe*cos(0*PI/180)+ze*sin(0*PI/180), ye, xe*sin(0*PI/180)+ze*cos(0*PI/180), xat, yat, zat, 0, 1, 0);
                 break;
            case 3 :
                 gluLookAt(0, 0, 10, xat, yat, zat, 1, 2, 0);
                 break;
            default :
                 break;
     }
//     gluLookAt(xe*cos(theta*PI/180)+ze*sin(theta*PI/180), ye, xe*sin(theta*PI/180)+ze*cos(theta*PI/180), xat, yat, zat, 0, 1, 0);
}
void SetProjectionMode()
{
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     if (sign > 0)
        glOrtho(-10, 10, -10, 10, -10, 10);
     else
        glFrustum(-5,5,-5,5,5,10);

//        gluPerspective(90, 1.0,10,20);

}






