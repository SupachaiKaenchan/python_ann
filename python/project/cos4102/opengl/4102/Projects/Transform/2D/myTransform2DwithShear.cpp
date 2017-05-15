#include <GL/glut.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

#define PI          3.1415926535897932384626433832795
#define RAD(X)      X*(PI/180)
#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define TN          3
#define RN          4

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
} Point;

Point Tri[TN], Tri_Tmp1[TN], Tri_Tmp2[TN];
Point Rec[RN], Rec_Tmp1[RN], Rec_Tmp2[RN];
Point COTri, CORec;

GLfloat theta = 0.0;
GLfloat Sx = 1.0, Sy = 1.0;
GLfloat scale_sign = 0.001;
GLfloat shear_scale = 0.001;
GLfloat isShear = 0.0;
GLint   isAxis = 0;

void Init(void);
void Transform(void);
void myTranslatef(Point Obj1[], Point Obj2[], GLint n, GLfloat cx, GLfloat cy);
void myRotatef(Point Obj1[], Point Obj2[], GLint n, GLfloat rad);
void myScalef(Point Obj1[], Point Obj2[], GLint n, GLfloat x, GLfloat y);
void myShearf(Point Obj1[], Point Obj2[], GLint n, GLfloat Shear, GLint isAxis);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void SpecialKey(GLint Key, GLint x, GLint y);
void Idle(void);
void ConfigPoint(void);

int main(int argc, char** argv)
{
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("Transform2D");

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
     Point center;

     center.x = center.y = 0.0;

     ConfigPoint();

     // Calculate centre
     for (int i=0; i<TN; i++)
     {
         center.x += Tri[i].x;
         center.y += Tri[i].y;
     }
     COTri.x = center.x / TN;
     COTri.y = center.y / TN;

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
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     gluOrtho2D(-SIZE_ORT, SIZE_ORT, -SIZE_ORT, SIZE_ORT);

}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT);
     glViewport(0, 0, SIZE_WIN, SIZE_WIN);
     glColor3f(1.0, 1.0, 1.0);
     glBegin(GL_LINES);
          glVertex2f(-SIZE_ORT, 0.0);
          glVertex2f(SIZE_ORT, 0.0);
          glVertex2f(0.0, -SIZE_ORT);
          glVertex2f(0.0, SIZE_ORT);
     glEnd();

     glPushMatrix();
          glViewport(0, 0, (SIZE_WIN), (SIZE_WIN));
          glColor3f(0.0, 0.8, 0.0);
          myTranslatef(Tri, Tri_Tmp1, TN, -COTri.x, -COTri.y);
          myScalef(Tri_Tmp1, Tri_Tmp2, TN, Sx, Sy);
          myTranslatef(Tri_Tmp2, Tri_Tmp1, TN, COTri.x, COTri.y);
          glBegin(GL_POLYGON);
               for (int i=0; i<TN; i++)
                   glVertex2f(Tri_Tmp1[i].x, Tri_Tmp1[i].y);
          glEnd();
     glPopMatrix();

     glPushMatrix();
          //glViewport((SIZE_WIN/2)+1, (SIZE_WIN/2)+1, (SIZE_WIN)/2, (SIZE_WIN)/2);
          glColor3f(1.0, 0.0, 1.0);
          myTranslatef(Rec, Rec_Tmp1, RN, -CORec.x, -CORec.y);
          myRotatef(Rec_Tmp1, Rec_Tmp2, RN, RAD(theta));
          myTranslatef(Rec_Tmp2, Rec_Tmp1, RN, CORec.x, CORec.y);
          glBegin(GL_POLYGON);
               for (int i=0; i<RN; i++)
                   glVertex2f(Rec_Tmp1[i].x, Rec_Tmp1[i].y);
          glEnd();
     glPopMatrix();

     glPushMatrix();
          glViewport(0, (SIZE_WIN/2)+1, (SIZE_WIN), (SIZE_WIN));
          glColor3f(0.0, 0.8, 0.0);
          myTranslatef(Tri, Tri_Tmp1, TN, -COTri.x, -COTri.y);
          myShearf(Tri_Tmp1, Tri_Tmp2, TN, isShear, isAxis);
          myTranslatef(Tri_Tmp2, Tri_Tmp1, TN, COTri.x, COTri.y);
          glBegin(GL_POLYGON);
               for (int i=0; i<TN; i++)
                   glVertex2f(Tri_Tmp1[i].x, Tri_Tmp1[i].y);
          glEnd();
     glPopMatrix();

     glFlush();

     glutSwapBuffers();
}

void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (Key)
     {
            case 0x1B :
                 exit(0);
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
                 Sx += 0.1;
                 Sy += 0.1;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_UP :
                 Sx -= 0.1;
                 Sy -= 0.1;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_HOME :
                 Sx -= 0.1;
				 glutPostRedisplay();
				 break;
            case GLUT_KEY_END :
                 Sx += 0.1;
                 glutPostRedisplay();
                 break;
            default :
                    break;
     }
}

void Idle(void)
{
     GLint flag = 1;

     if (theta >= 360.0)
     {
        flag *= -1;
        theta = 0.0;
     }
     else
         theta += 0.1;

     if (Sx < 0.1)
        scale_sign = 0.001;
     if (Sx > 2.0)
        scale_sign = -0.001;
     Sx += scale_sign;
     Sy += scale_sign;

     if (flag > 0) isAxis = 0;
     else isAxis = 1;
     if (isShear < -1.0)
        shear_scale = 0.001;
     if (isShear > 1.0)
        shear_scale = -0.001;
     isShear += shear_scale;

     glutPostRedisplay();
}

void ConfigPoint(void)
{
     Tri[0].x = -250.0;         Tri[0].y = -150.0;
     Tri[1].x = -350.0;         Tri[1].y = -350.0;
     Tri[2].x = -150.0;         Tri[2].y = -350.0;

     Rec[0].x = 150.0;         Rec[0].y = 150.0;
     Rec[1].x = 350.0;         Rec[1].y = 150.0;
     Rec[2].x = 350.0;         Rec[2].y = 350.0;
     Rec[3].x = 150.0;         Rec[3].y = 350.0;

     for (int i=0; i<TN; i++)
         Tri_Tmp1[i].x = Tri_Tmp1[i].y = Tri_Tmp2[i].x = Tri_Tmp2[i].y = 0.0;

     for (int i=0; i<RN; i++)
         Rec_Tmp1[i].x = Rec_Tmp1[i].y = Rec_Tmp2[i].x = Rec_Tmp2[i].y = 0.0;
}

void myTranslatef(Point Obj1[], Point Obj2[], GLint n, GLfloat cx, GLfloat cy)
{
     for (int i=0; i<n; i++)
     {
         Obj2[i].x = Obj1[i].x + cx;
         Obj2[i].y = Obj1[i].y + cy;
     }
}

void myRotatef(Point Obj1[], Point Obj2[], GLint n, GLfloat rad)
{
     for (int i=0; i<n; i++)
     {
         Obj2[i].x = Obj1[i].x*(cos(rad)) - Obj1[i].y*(sin(rad));
         Obj2[i].y = Obj1[i].x*(sin(rad)) + Obj1[i].y*(cos(rad));
     }
}

void myScalef(Point Obj1[], Point Obj2[], GLint n, GLfloat Scale_x, GLfloat Scale_y)
{
     for (int i=0; i<n; i++)
     {
         Obj2[i].x = Obj1[i].x * Scale_x;
         Obj2[i].y = Obj1[i].y * Scale_y;
     }
}

void myShearf(Point Obj1[], Point Obj2[], GLint n, GLfloat Shear, GLint isAxis)
{
     switch (isAxis)
     {
            case 0 :        // Shear X Axis
                 for (int i=0; i<n; i++)
                 {
                     Obj2[i].x = Obj1[i].x + (Obj1[i].y * Shear);
                     Obj2[i].y = Obj1[i].y;
                 }
                 break;
            case 1 :           // Shear Y Axis
                 for (int i=0; i<n; i++)
                 {
                     Obj2[i].x = Obj1[i].x;
                     Obj2[i].y = Obj1[i].y + (Obj1[i].x * Shear);
                 }
                 break;
     }
}
