#include <GL/glut.h>

#define PI          3.1415926535897932384626433832795
#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define RN          5

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
        GLfloat      z;
} Point;

Point Rec[RN];
Point COTri, CORec;

GLfloat theta = 0.0;
//GLfloat thetaX = 0.0, thetaY = 0.0, thetaZ = 0.0;
GLfloat xsc = 1.0, ysc = 1.0, zsc = 1.0;
GLfloat xt = 1.0, yt = 0.0, zt = 0.0;
GLint   flag = 1;

GLfloat scale_sign = 0.001;

void Init(void);
void Transform(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void SpecialKey(GLint Key, GLint x, GLint y);
void Idle(void);
void ConfigPoint(void);

int main(int argc, char** argv)
{
//	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitDisplayMode(GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("Transform3D");

	Init();

	glutDisplayFunc(Transform);
	glutKeyboardFunc(KeyboardKey);
	glutSpecialFunc(SpecialKey);
	glutIdleFunc(Idle);
//	glutReshapeFunc(reShape);

	glutMainLoop();

    return 0;
}

void Init(void)
{
     Point center;

     center.x = center.y = 0.0;

     ConfigPoint();

     center.x = center.y = 0.0;

     for (int i=0; i<RN; i++)
     {
         center.x += Rec[i].x;
         center.y += Rec[i].y;
     }
     CORec.x = center.x / RN;
     CORec.y = center.y / RN;

     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glEnable(GL_DEPTH_TEST);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     // glOrtho(Left, Right, Bottom, Top, Near, Far)
     glOrtho(-SIZE_ORT, SIZE_ORT, -SIZE_ORT, SIZE_ORT, -SIZE_ORT, SIZE_ORT);
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

     glViewport(0, 0, SIZE_WIN, SIZE_WIN);

     glColor3f(1.0, 1.0, 1.0);
     glBegin(GL_LINES);
          glVertex2f(-SIZE_ORT, 0.0);
          glVertex2f(SIZE_ORT, 0.0);
          glVertex2f(0.0, -SIZE_ORT);
          glVertex2f(0.0, SIZE_ORT);
     glEnd();

     // Rotate
     // View port Bottom Left
     glPushMatrix();

          glViewport(0, 0, (SIZE_WIN / 2), (SIZE_WIN / 2));
          glTranslatef(CORec.x, CORec.y, 0.0);
          glRotatef(theta, xt, yt, zt);
          glTranslatef(-CORec.x, -CORec.y, 0.0);
          glBegin(GL_POLYGON);
               glColor3f(1.0, 0.0, 0.0);
               glVertex3f(Rec[0].x, Rec[0].y, Rec[0].z);
               glVertex3f(Rec[1].x, Rec[1].y, Rec[1].z);
               glColor3f(0.0, 1.0, 0.0);
               glVertex3f(Rec[2].x, Rec[2].y, Rec[2].z);
               glVertex3f(Rec[3].x, Rec[3].y, Rec[3].z);
               glColor3f(0.0, 0.0, 1.0);
               glVertex3f(Rec[4].x, Rec[4].y, Rec[4].z);
          glEnd();
     glPopMatrix();

     // View port Top Left
     glPushMatrix();
     glViewport(0, (SIZE_WIN / 2) + 1, (SIZE_WIN / 2), (SIZE_WIN / 2));
          glTranslatef(CORec.x, CORec.y, 0.0);
          glRotatef(theta, 0.0, 1.0, 0.0);
          glTranslatef(-CORec.x, -CORec.y, 0.0);
          glBegin(GL_POLYGON);
               glColor3f(1.0, 0.0, 0.0);
               glVertex3f(Rec[0].x, Rec[0].y, Rec[0].z);
               glVertex3f(Rec[1].x, Rec[1].y, Rec[1].z);
               glColor3f(0.0, 1.0, 0.0);
               glVertex3f(Rec[2].x, Rec[2].y, Rec[2].z);
               glVertex3f(Rec[3].x, Rec[3].y, Rec[3].z);
               glColor3f(0.0, 0.0, 1.0);
               glVertex3f(Rec[4].x, Rec[4].y, Rec[4].z);
          glEnd();
     glPopMatrix();

     // View port Bottom Right
     glPushMatrix();
     glViewport((SIZE_WIN / 2) + 1, 0, (SIZE_WIN / 2), (SIZE_WIN / 2));
          glTranslatef(CORec.x, CORec.y, 0.0);
          glRotatef(theta, 0.0, 0.0, 1.0);
          glTranslatef(-CORec.x, -CORec.y, 0.0);
          glBegin(GL_POLYGON);
               glColor3f(1.0, 0.0, 0.0);
               glVertex3f(Rec[0].x, Rec[0].y, Rec[0].z);
               glVertex3f(Rec[1].x, Rec[1].y, Rec[1].z);
               glColor3f(0.0, 1.0, 0.0);
               glVertex3f(Rec[2].x, Rec[2].y, Rec[2].z);
               glVertex3f(Rec[3].x, Rec[3].y, Rec[3].z);
               glColor3f(0.0, 0.0, 1.0);
               glVertex3f(Rec[4].x, Rec[4].y, Rec[4].z);
          glEnd();
     glPopMatrix();
     // Scaling
     // View port Top Right
     glPushMatrix();

          glColor3f(1.0, 0.0, 1.0);
          glViewport((SIZE_WIN / 2) + 1, (SIZE_WIN / 2) + 1, (SIZE_WIN / 2), (SIZE_WIN / 2));
          glTranslatef(CORec.x, CORec.y, 0.0);
          glScalef(xsc, ysc, 1.0);
          glTranslatef(-CORec.x, -CORec.y, 0.0);
          glBegin(GL_POLYGON);
               for (int i=0; i<RN; i++)
                   glVertex3f(Rec[i].x, Rec[i].y, Rec[i].z);
          glEnd();
     glPopMatrix();

     glFlush();

//     glutSwapBuffers();
}

void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (Key)
     {
            case 0x1B :       // ESC Button
                 exit(0);
                 break;
            case 0x78 :       // x Button
                 flag = 1;
                 xt = 1.0;
                 yt = 0.0;
                 zt = 0.0;
                 break;
            case 0x58 :       // X Button
                 flag = 0;
                 xt = 1.0;
                 yt = 0.0;
                 zt = 0.0;
                 break;
            case 0x79 :       // y Button
                 flag = 1;
                 xt = 0.0;
                 yt = 1.0;
                 zt = 0.0;
                 break;
            case 0x59 :       // Y Button
                 flag = 0;
                 xt = 0.0;
                 yt = 1.0;
                 zt = 0.0;
                 break;
            case 0x7A :       // z Button
                 flag = 1;
                 xt = 0.0;
                 yt = 0.0;
                 zt = 1.0;
                 break;
            case 0x5A :       // Z Button
                 flag = 0;
                 xt = 0.0;
                 yt = 0.0;
                 zt = 1.0;
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
            theta += 0.1;
     else
        if (theta <= -360)
           theta = 0;
        else
            theta -= 0.1;

     if (xsc < 0.1)
        scale_sign = 0.001;
     if (xsc > 2.0)
        scale_sign = -0.001;
     xsc += scale_sign;
     ysc += scale_sign;

	glutPostRedisplay();
}

void ConfigPoint(void)
{
      Rec[0].x = -100.0;    Rec[0].y = -100.0;    Rec[0].z = 100.0;
      Rec[1].x = 0.0;       Rec[1].y = 100.0;     Rec[1].z = 0.0;
      Rec[2].x = 100.0;     Rec[2].y = -100.0;    Rec[2].z = 100.0;
      Rec[3].x = 0.0;       Rec[3].y = -100.0;    Rec[3].z = -100.0;
      Rec[4].x = 0.0;       Rec[4].y = 100.0;     Rec[4].z = 0.0;
}
