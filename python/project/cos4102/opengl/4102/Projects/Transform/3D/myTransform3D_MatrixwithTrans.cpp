#include <GL/glut.h>
#include <stdio.h>
#include <conio.h>
#include <math.h>

#define PI       3.1415926535897932384626433832795
#define SIZE_WIN  500
#define SIZE_ORT  500.0
#define RAD(X)    (X*PI)/180
#define PN        8

typedef GLfloat Matrix4x[4][4];
typedef struct Coordinate{
        GLfloat x;
        GLfloat y;
        GLfloat z;
        GLfloat w;
} Point;

Point Obj[PN], TrnsObj[PN];

Matrix4x TrnMTx;

GLfloat Sx = 1.0, Sy = 1.0, Sz = 1.0;
GLfloat scale_sign = 0.001;
GLfloat theta = 0.0;
GLfloat Shear = 1.0;
GLfloat theta_sign = 0.1;
GLfloat shear_sign = 0.001;
GLfloat CenObjX, CenObjY, CenObjZ;

GLubyte   Axis = 0x78;

void ConfigPoint(void);
void Centroid(Point Obj[], GLint n, GLfloat &cx, GLfloat &cy, GLfloat &cz);
void Init(void);
void myTransform3D(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void SpecialKey(GLint Key, GLint x, GLint y);
void Idle(void);
void iMatrix(Matrix4x IdenMx);
void mulMatrix(Matrix4x MTx1, const Matrix4x MTx2);
void myTranslatef(Matrix4x MTx1, GLfloat tx, GLfloat ty, GLfloat tz);
void myRotatef(Matrix4x MTx1, GLubyte Axis, GLfloat theta);
void myScalef(Matrix4x MTx1, GLfloat sx, GLfloat sy, GLfloat sz);
void myShearf(Matrix4x MTx1, GLubyte Axis, GLfloat shear);

int main(int argc, char** argv)
{
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);
    glutInitWindowSize(SIZE_WIN, SIZE_WIN);
    glutInitWindowPosition(SIZE_WIN, 0);
    glutCreateWindow("Transform3D with Translation");

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
         TrnsObj[i].x = TrnsObj[i].y = TrnsObj[i].z = 0.0;
}

void Centroid(Point Obj[], GLint n, GLfloat &cx, GLfloat &cy, GLfloat &cz)
{
     GLfloat sumCenterX, sumCenterY, sumCenterZ;

     sumCenterX = sumCenterY = sumCenterZ = 0.0;

     for (int i=0; i<n; i++)
     {
         sumCenterX += Obj[i].x;
         sumCenterY += Obj[i].y;
         sumCenterZ += Obj[i].z;
     }

     cx = sumCenterX / n;
     cy = sumCenterY / n;
     cz = sumCenterZ / n;
}

void Init(void)
{
     ConfigPoint();
     // Calculate centroid of Triangle
     Centroid(Obj, PN, CenObjX, CenObjY, CenObjZ);

     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(-SIZE_ORT, SIZE_ORT, -SIZE_ORT, SIZE_ORT, -SIZE_ORT, SIZE_ORT);
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
}

void myTransform3D(void)
{
     glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
     glViewport(0, 0, SIZE_WIN, SIZE_WIN);
     glColor3f(1.0, 1.0, 1.0);
     glBegin(GL_LINES);
          glVertex2f(-SIZE_ORT, 0.0);
          glVertex2f(SIZE_ORT, 0.0);
          glVertex2f(0.0, -SIZE_ORT);
          glVertex2f(0.0, SIZE_ORT);
     glEnd();

     glPushMatrix();
     // glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
     // Top Left view
     glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
     glPushMatrix();
     glViewport(0, ((SIZE_WIN/2)+1), (SIZE_WIN/2), (SIZE_WIN/2));
     iMatrix(TrnMTx);
     myTranslatef(TrnMTx, -CenObjX, -CenObjY, -CenObjZ);
     myShearf(TrnMTx, Axis, Shear);
     myRotatef(TrnMTx, Axis, theta);
     myTranslatef(TrnMTx, CenObjX, CenObjY, CenObjZ);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              TrnsObj[i].x = (Obj[i].x * TrnMTx[0][0]) + (Obj[i].y * TrnMTx[0][1]) + (Obj[i].z * TrnMTx[0][2]) + (Obj[i].w * TrnMTx[0][3]);
              TrnsObj[i].y = (Obj[i].x * TrnMTx[1][0]) + (Obj[i].y * TrnMTx[1][1]) + (Obj[i].z * TrnMTx[1][2]) + (Obj[i].w * TrnMTx[1][3]);
              TrnsObj[i].z = (Obj[i].x * TrnMTx[2][0]) + (Obj[i].y * TrnMTx[2][1]) + (Obj[i].z * TrnMTx[2][2]) + (Obj[i].w * TrnMTx[2][3]);
              glColor3f(1.0, 0.0, 1.0);
              glVertex3f(TrnsObj[i].x, TrnsObj[i].y , TrnsObj[i].z);
          }
     glEnd();
     glPopMatrix();

     glPushMatrix();
     // Top Right view
     glViewport(((SIZE_WIN/2)+1), ((SIZE_WIN/2)+1), (SIZE_WIN/2), (SIZE_WIN/2) );
     iMatrix(TrnMTx);
     myTranslatef(TrnMTx, -CenObjX, -CenObjY, -CenObjZ);
     myScalef(TrnMTx, Sx, Sy, Sz);
     myTranslatef(TrnMTx, CenObjX, CenObjY, CenObjZ);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              TrnsObj[i].x = (Obj[i].x * TrnMTx[0][0]) + (Obj[i].y * TrnMTx[0][1]) + (Obj[i].z * TrnMTx[0][2]) + (Obj[i].w * TrnMTx[0][3]);
              TrnsObj[i].y = (Obj[i].x * TrnMTx[1][0]) + (Obj[i].y * TrnMTx[1][1]) + (Obj[i].z * TrnMTx[1][2]) + (Obj[i].w * TrnMTx[1][3]);
              TrnsObj[i].z = (Obj[i].x * TrnMTx[2][0]) + (Obj[i].y * TrnMTx[2][1]) + (Obj[i].z * TrnMTx[2][2]) + (Obj[i].w * TrnMTx[2][3]);
              glColor3f(0.0, 1.0, 0.3);
              glVertex3f(TrnsObj[i].x, TrnsObj[i].y , TrnsObj[i].z);
          }
     glEnd();
     glPopMatrix();

     glPushMatrix();
     // Bottom Left view
     glViewport(0, 0, (SIZE_WIN/2), (SIZE_WIN/2));
     iMatrix(TrnMTx);
     myTranslatef(TrnMTx, -CenObjX, -CenObjY, -CenObjZ);
     myRotatef(TrnMTx, Axis, theta);
     myTranslatef(TrnMTx, CenObjX, CenObjY, CenObjZ);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              TrnsObj[i].x = (Obj[i].x * TrnMTx[0][0]) + (Obj[i].y * TrnMTx[0][1]) + (Obj[i].z * TrnMTx[0][2]) + (Obj[i].w * TrnMTx[0][3]);
              TrnsObj[i].y = (Obj[i].x * TrnMTx[1][0]) + (Obj[i].y * TrnMTx[1][1]) + (Obj[i].z * TrnMTx[1][2]) + (Obj[i].w * TrnMTx[1][3]);
              TrnsObj[i].z = (Obj[i].x * TrnMTx[2][0]) + (Obj[i].y * TrnMTx[2][1]) + (Obj[i].z * TrnMTx[2][2]) + (Obj[i].w * TrnMTx[2][3]);
              glColor3f(1.0, 0.0, 0.0);
              glVertex3f(TrnsObj[i].x, TrnsObj[i].y , TrnsObj[i].z);
          }
     glEnd();
     glPopMatrix();
     glPushMatrix();
     // Bottom Right view
     glViewport(((SIZE_WIN/2)+1), 0, (SIZE_WIN/2), (SIZE_WIN/2));
     iMatrix(TrnMTx);
     myTranslatef(TrnMTx, -CenObjX, -CenObjY, -CenObjZ);
     myScalef(TrnMTx, Sx, Sy, Sz);
     myTranslatef(TrnMTx, CenObjX, CenObjY, CenObjZ);
     myTranslatef(TrnMTx, -CenObjX, -CenObjY, -CenObjZ);
     myRotatef(TrnMTx, Axis, theta);
     myTranslatef(TrnMTx, CenObjX, CenObjY, CenObjZ);
     glBegin(GL_POLYGON);
          for (int i=0; i<PN; i++)
          {
              TrnsObj[i].x = (Obj[i].x * TrnMTx[0][0]) + (Obj[i].y * TrnMTx[0][1]) + (Obj[i].z * TrnMTx[0][2]) + (Obj[i].w * TrnMTx[0][3]);
              TrnsObj[i].y = (Obj[i].x * TrnMTx[1][0]) + (Obj[i].y * TrnMTx[1][1]) + (Obj[i].z * TrnMTx[1][2]) + (Obj[i].w * TrnMTx[1][3]);
              TrnsObj[i].z = (Obj[i].x * TrnMTx[2][0]) + (Obj[i].y * TrnMTx[2][1]) + (Obj[i].z * TrnMTx[2][2]) + (Obj[i].w * TrnMTx[2][3]);
              glColor3f(0.0, 0.0, 1.0);
              glVertex3f(TrnsObj[i].x, TrnsObj[i].y , TrnsObj[i].z);
          }
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
                 if (theta >= 360.0) theta = 0.0;
                 theta += 10.0;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_RIGHT :
                 if (theta <= -360.0) theta = 0.0;
                 theta -= 10.0;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_UP :
                 if (Sx <= 2.0)
                 {
                    Sx += 0.1;
                    Sy += 0.1;
                    Sz += 0.1;
                 }
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_DOWN :
                 if (Sx >= 0.1)
                 {
                    Sx -= 0.1;
                    Sy -= 0.1;
                    Sz -= 0.1;
                 }
                 glutPostRedisplay();
                 break;
            default :
                    break;
     }
}

void Idle(void)
{
     if (Axis > 0x7A)
        Axis = 0x78;
     else
     {
         if (theta >= 360.0)
         {
            Axis++;
            //Shear = 0.0;
            theta_sign = -0.1;
         }
         if (theta <= -360.0)
         {
            Axis++;
            //Shear = 0.0;
            theta_sign = 0.1;
         }
     }

     theta += theta_sign;

     if (Sx <= 0.1)
        scale_sign = 0.001;
     if (Sx >= 2.0)
        scale_sign = -0.001;

     Sx += scale_sign;
     Sy += scale_sign;
     Sz += scale_sign;


     if (Shear >= 1.0)
        shear_sign = -0.001;
     if (Shear <= -1.0)
        shear_sign = 0.001;

     Shear += shear_sign;

     glutPostRedisplay();
}

void iMatrix(Matrix4x IdenMx)
{
     for (int i=0; i<4; i++)
         for (int j=0; j<4; j++)
             IdenMx[i][j] = (i == j);
}

void mulMatrix(Matrix4x MTx1, const Matrix4x MTx2)
{
     Matrix4x temp = {0};

     for (int i=0; i<4; i++)
         for (int j=0; j<4; j++)
             for (int k=0; k<4; k++)
                 temp[i][j] += MTx1[i][k] * MTx2[k][j];
     for (int i=0; i<4; i++)
         for (int j=0; j<4; j++)
             MTx1[i][j] = temp[i][j];
}

void myTranslatef(Matrix4x MTx1, GLfloat tx, GLfloat ty, GLfloat tz)
{
     Matrix4x MTx2;

     iMatrix(MTx2);
     MTx2[0][3] = tx;
     MTx2[1][3] = ty;
     MTx2[2][3] = tz;

     mulMatrix(MTx1, MTx2);
}

void myRotatef(Matrix4x MTx1, GLubyte Axis, GLfloat theta)
{
     Matrix4x MTx2;

     iMatrix(MTx2);

     switch (Axis)
     {
            case 0x78 :                       // On X Axis
                 MTx2[1][1] = cos(RAD(theta));
                 MTx2[1][2] = sin(RAD(theta));
                 MTx2[2][1] = -sin(RAD(theta));
                 MTx2[2][2] = cos(RAD(theta));

                 mulMatrix(MTx1, MTx2);
                 break;
            case 0x79 :                       // On Y Axis
                 MTx2[0][0] = cos(RAD(theta));
                 MTx2[0][2] = -sin(RAD(theta));
                 MTx2[2][0] = sin(RAD(theta));
                 MTx2[2][2] = cos(RAD(theta));

                 mulMatrix(MTx1, MTx2);
                 break;
            case 0x7A :                       // On Z Axis
                 MTx2[0][0] = cos(RAD(theta));
                 MTx2[0][1] = sin(RAD(theta));
                 MTx2[1][0] = -sin(RAD(theta));
                 MTx2[1][1] = cos(RAD(theta));

                 mulMatrix(MTx1, MTx2);
                 break;
     }

}

void myScalef(Matrix4x MTx1, GLfloat sx, GLfloat sy, GLfloat sz)
{
     Matrix4x MTx2;

     iMatrix(MTx2);
     MTx2[0][0] = sx;
     MTx2[1][1] = sy;
     MTx2[2][2] = sz;

     mulMatrix(MTx1, MTx2);
}

void myShearf(Matrix4x MTx1, GLubyte Axis, GLfloat shear)
{
     Matrix4x MTx2;

     iMatrix(MTx2);

     switch (Axis)
     {
            case 0x78 :               // On X Axis
                 MTx2[1][0] = shear;
                 MTx2[2][0] = shear;
                 break;
            case 0x79:               // On Y Axis
                 MTx2[0][1] = shear;
                 MTx2[2][1] = shear;
                 break;
            case 0x7A :             // On Z Axis
                 MTx2[0][2] = shear;
                 MTx2[1][2] = shear;
                 break;
            default :
                    break;
     }

     mulMatrix(MTx1, MTx2);
}
