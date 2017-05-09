#include <GL/glut.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

#define PI        3.1415926535897932384626433832795
#define RAD(X)    (X * PI) / 180.0
#define SIZE_WIN  500
#define SIZE_ORT  500.0
#define PN        8

typedef struct Coordinate3D {
        GLfloat x;
        GLfloat y;
        GLfloat z;
}Point;

Point Obj[PN], tmpObj1[PN], tmpObj2[PN], CObj;

GLfloat theta = 0.0, theta_sign = 0.1;
GLfloat xs = 1.0, ys = 1.0, zs = 1.0;
GLfloat scale_sign = 0.001;
GLfloat isShear = 0.0, shear_sign = 0.001;

GLubyte isAxis = 0x78;

void ConfigPoint(void);
void myTransform3D(void);
void Init(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void SpecialKey(GLint Key, GLint x, GLint y);
void Idle(void);

// Function Transform
void myTranslatef(Point Obj1[], Point Obj2[], GLint n, GLfloat cx, GLfloat cy, GLfloat cz);
void myScalef(Point Obj1[], Point Obj2[], GLint n, GLfloat xs, GLfloat ys, GLfloat zs);
void myRotatef(Point Obj1[], Point Obj2[], GLint n, GLfloat theta, GLubyte onAxis);
void myShearef(Point Obj1[], Point Obj2[], GLint n,  GLfloat shear, GLubyte onAxis);

int main(int argc, char** argv)
{
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(SIZE_WIN, SIZE_WIN);
    glutInitWindowPosition(SIZE_WIN, 0);
    glutCreateWindow("Transform 3D");

    Init();

    glutDisplayFunc(myTransform3D);
    glutKeyboardFunc(KeyboardKey);
    glutSpecialFunc(SpecialKey);
    glutIdleFunc(Idle);

    glutMainLoop();

    return 0;
}

void ConfigPoint(void)
{
     Obj[0].x = -100.0;    Obj[0].y = -100.0;    Obj[0].z = 100.0;
     Obj[1].x = 100.0;     Obj[1].y = -100.0;    Obj[1].z = 100.0;
     Obj[2].x = 0.0;       Obj[2].y = 100.0;     Obj[2].z = 0.0;
     Obj[3].x = 0.0;       Obj[3].y = -100.0;    Obj[3].z = -100.0;
     Obj[4].x = -100.0;    Obj[4].y = -100.0;    Obj[4].z = 100.0;
     Obj[5].x = 0.0;       Obj[5].y = 100.0;     Obj[5].z = 0.0;
     Obj[6].x = 0.0;       Obj[6].y = -100.0;    Obj[6].z = -100.0;
     Obj[7].x = 100.0;     Obj[7].y = -100.0;    Obj[7].z = 100.0;


     for (int i=0; i<PN; i++)
     {
         tmpObj1[i].x = tmpObj1[i].y = tmpObj1[i].z = 0.0;
         tmpObj2[i].x = tmpObj2[i].y = tmpObj2[i].z = 0.0;
     }
}

void Centroid(Point Obj[])
{
     Point sumCenter;

     sumCenter.x = sumCenter.y = sumCenter.z = 0.0;

     for (int i=0; i<PN; i++)
     {
         sumCenter.x += Obj[i].x;
         sumCenter.y += Obj[i].y;
         sumCenter.z += Obj[i].z;
     }

     CObj.x = sumCenter.x / PN;
     CObj.y = sumCenter.y / PN;
     CObj.z = sumCenter.z / PN;

}

void myTransform3D(void)
{

     GLfloat R = 0.0, G = 0.0, B = 0.0;
     GLint   flagColor = 1;

     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

     glViewport(0, 0, SIZE_WIN, SIZE_WIN);
     glColor3f(1.0, 1.0, 1.0);
     glBegin(GL_LINES);
          glVertex2f(0.0, SIZE_ORT);
          glVertex2f(0.0, -SIZE_ORT);
          glVertex2f(SIZE_ORT, 0.0);
          glVertex2f(-SIZE_ORT, 0.0);
     glEnd();
     // glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
     // Top Left view
     glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
     glPushMatrix();
     glViewport(0, ((SIZE_WIN/2)+1), (SIZE_WIN/2), (SIZE_WIN/2));
     myTranslatef(Obj, tmpObj1, PN, -CObj.x, -CObj.y, -CObj.z);
     myShearef(tmpObj1, tmpObj2, PN, isShear, isAxis);
     myTranslatef(tmpObj2, tmpObj1, PN, CObj.x, CObj.y, CObj.z);
     myTranslatef(tmpObj1, tmpObj2, PN, -CObj.x, -CObj.y, -CObj.z);
     myRotatef(tmpObj2, tmpObj1, PN, theta, isAxis);
     myTranslatef(tmpObj1, tmpObj2, PN, CObj.x, CObj.y, CObj.z);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              glColor3f(1.0, 0.0, 1.0);
              glVertex3f(tmpObj2[i].x, tmpObj2[i].y , tmpObj2[i].z);
          }
     glEnd();
     glPopMatrix();

     glPushMatrix();
     // Top Right view
     glViewport(((SIZE_WIN/2)+1), ((SIZE_WIN/2)+1), (SIZE_WIN/2), (SIZE_WIN/2) );
     myTranslatef(Obj, tmpObj1, PN, -CObj.x, -CObj.y, -CObj.z);
     myScalef(tmpObj1, tmpObj2, PN, xs, ys, zs);
     myTranslatef(tmpObj2, tmpObj1, PN, CObj.x, CObj.y, CObj.z);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              glColor3f(1.0, 1.0, 0.0);
              glVertex3f(tmpObj1[i].x, tmpObj1[i].y , tmpObj1[i].z);
          }
     glEnd();
     glPopMatrix();

     glPushMatrix();
     // Bottom Left view
     glViewport(0, 0, (SIZE_WIN/2), (SIZE_WIN/2));
     myTranslatef(Obj, tmpObj1, PN, -CObj.x, -CObj.y, -CObj.z);
     myRotatef(tmpObj1, tmpObj2, PN, theta, isAxis);
     myTranslatef(tmpObj2, tmpObj1, PN, CObj.x, CObj.y, CObj.z);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              glColor3f(1.0, 0.0, 0.0);
              glVertex3f(tmpObj1[i].x, tmpObj1[i].y , tmpObj1[i].z);
          }
     glEnd();
     glPopMatrix();
     glPushMatrix();
     // Bottom Right view
     glViewport(((SIZE_WIN/2)+1), 0, (SIZE_WIN/2), (SIZE_WIN/2));
     myTranslatef(Obj, tmpObj1, PN, -CObj.x, -CObj.y, -CObj.z);
     myScalef(tmpObj1, tmpObj2, PN, xs, ys, zs);
     myTranslatef(tmpObj2, tmpObj1, PN, CObj.x, CObj.y, CObj.z);
     myTranslatef(tmpObj1, tmpObj2, PN, -CObj.x, -CObj.y, -CObj.z);
     myRotatef(tmpObj2, tmpObj1, PN, theta, isAxis);
     myTranslatef(tmpObj1, tmpObj2, PN, CObj.x, CObj.y, CObj.z);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              glColor3f(0.0, 0.0, 1.0);
              glVertex3f(tmpObj2[i].x, tmpObj2[i].y , tmpObj2[i].z);
          }
     glEnd();
     glPopMatrix();

     glFlush();

     glutSwapBuffers();

}

void Init(void)
{
     ConfigPoint();

     Centroid(Obj);

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
            case GLUT_KEY_LEFT :             // Rotate
                 theta += 1.0;
                 break;
            case GLUT_KEY_RIGHT :
                 theta -= 1.0;
                 break;
            case GLUT_KEY_UP :
                 if (xs < 2.0)
                 {
                    xs += 0.1;
                    ys += 0.1;
                    zs += 0.1;
                 }
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_DOWN :
                 if (xs > 0.1)
                 {
                    xs -= 0.1;
                    ys -= 0.1;
                    zs -= 0.1;
                 }
                 glutPostRedisplay();
                 break;
            default :
                    break;
     }
}

void Idle(void)
{
     if (isAxis > 0x7A)
        isAxis = 0x78;
     else
     {
         if (theta > 359.99)
         {
            isAxis++;
            isShear = 0.0;
            theta_sign = -0.1;
         }
         if (theta < -359.99)
         {
            isAxis++;
            isShear = 0.0;
            theta_sign = 0.1;
         }

         theta += theta_sign;
     }

     if (xs < 0.1)
        scale_sign = 0.001;
     if (xs > 2.0)
          scale_sign = -0.001;

     xs += scale_sign;
     ys += scale_sign;
     zs += scale_sign;

     if (isShear > 1.0)
        shear_sign = -0.001;
     if (isShear < -1.0)
        shear_sign = 0.001;
     isShear += shear_sign;

     glutPostRedisplay();
}

void myTranslatef(Point Obj1[], Point Obj2[], GLint n, GLfloat cx, GLfloat cy, GLfloat cz)
{
     // Input from Obj1[] and send output to Obj2[]
     for (int i=0; i<n; i++)
     {
         Obj2[i].x = Obj1[i].x + cx;
         Obj2[i].y = Obj1[i].y + cy;
         Obj2[i].z = Obj1[i].z + cz;
     }
}

void myScalef(Point Obj1[], Point Obj2[], GLint n, GLfloat xs, GLfloat ys, GLfloat zs)
{
     // Input from Obj1[] and send output to Obj2[]
     for (int i=0; i<n; i++)
     {
         Obj2[i].x = Obj1[i].x * xs;
         Obj2[i].y = Obj1[i].y * ys;
         Obj2[i].z = Obj1[i].z * zs;
     }
}

void myRotatef(Point Obj1[], Point Obj2[], GLint n, GLfloat theta, GLubyte onAxis)
{
     switch (onAxis)
     {
            case 0x78 :               // On X Axis
                 for (int i=0; i<PN; i++)
                 {
                     Obj2[i].x = Obj1[i].x;
                     Obj2[i].y = (Obj1[i].y * cos(RAD(theta))) + (Obj1[i].z * sin(RAD(theta)));
                     Obj2[i].z = (Obj1[i].z * cos(RAD(theta))) - ((Obj1[i].y) * sin(RAD(theta)));
                 }
                 break;
            case 0x79 :               // On Y Axis
                 for (int i=0; i<PN; i++)
                 {
                     Obj2[i].x = (Obj1[i].x * cos(RAD(theta))) + (Obj1[i].z * sin(RAD(theta)));
                     Obj2[i].y = Obj1[i].y;
                     Obj2[i].z = (Obj1[i].z * cos(RAD(theta))) - (Obj1[i].x * sin(RAD(theta)));
                 }
                 break;
            case 0x7A :               // On Z Axis
                 for (int i=0; i<PN; i++)
                 {
                     Obj2[i].x = (Obj1[i].x * cos(RAD(theta))) - (Obj1[i].y * sin(RAD(theta)));
                     Obj2[i].y = (Obj1[i].x * sin(RAD(theta))) + (Obj1[i].y * cos(RAD(theta)));
                     Obj2[i].z = Obj1[i].z;
                 }
                 break;
            default :

                    break;
     }
}

void myShearef(Point Obj1[], Point Obj2[], GLint n, GLfloat shear, GLubyte onPlane)
{
     switch (onPlane)
     {
            case 0x78 :               // On X Axis
                 for (int i=0; i<n; i++)
                 {
                     Obj2[i].x = Obj1[i].x + (shear * Obj1[i].y) + (shear * Obj1[i].z);
                     Obj2[i].y = Obj1[i].y;
                     Obj2[i].z = Obj1[i].z;
                 }
                 break;
            case 0x79 :               // On Y Axis
                 for (int i=0; i<n; i++)
                 {
                     Obj2[i].x = Obj1[i].x;
                     Obj2[i].y = Obj1[i].y + (shear * Obj1[i].x) + (shear * Obj1[i].z);
                     Obj2[i].z = Obj1[i].z;
                 }
                 break;
            case 0x7A :               // On Z Axis
                 for (int i=0; i<n; i++)
                 {
                     Obj2[i].x = Obj1[i].x;
                     Obj2[i].y = Obj1[i].y;
                     Obj2[i].z = Obj1[i].z + (shear * Obj1[i].x) + (shear * Obj1[i].y);
                 }
                 break;
            default :
                    break;
     }
}
