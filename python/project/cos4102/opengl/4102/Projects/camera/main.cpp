#include <GL/glut.h>
#include <math.h>

#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define RN          4
#define PI          3.1415926535897932384626433832795

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
        GLfloat      z;
};
///cube center
Point sf1N[RN],sf1L[RN],sf1R[RN],sf1T[RN],sf1B[RN],sf1F[RN];
///cube left
Point sf2N[RN],sf2L[RN],sf2R[RN],sf2T[RN],sf2B[RN],sf2F[RN];
///cube right
Point sf3N[RN],sf3L[RN],sf3R[RN],sf3T[RN],sf3B[RN],sf3F[RN];

GLfloat fLtAmbient[] = {1.0,1.0,1.0,1.0}; 
GLfloat fMatDiffuse[] = {1.0,1.0,1.0,1.0};
GLfloat fMatSpecular[] = {1.0,1.0,1.0,1.0};
GLfloat theta = 0.0;
GLfloat angle = 0.0;
GLint sign = 1;

void Init(void);
void Transform(void);
void ConfigPoint(void);
void PlotSurface(Point Surface[RN],GLfloat red,GLfloat green,GLfloat blue,GLfloat alpha);
void DrawCube(void);
void SetLookAt(GLfloat eyeX,GLfloat eyeY,GLfloat eyeZ,GLfloat x,GLfloat y,GLfloat z,GLfloat vexX,GLfloat vexY,GLfloat vexZ);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void Idle(void);

int main(int argc, char** argv)
{
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("Cube");
	Init();
	glutDisplayFunc(Transform);
	glutKeyboardFunc(KeyboardKey);
    glutIdleFunc(Idle);
	glutMainLoop();
    return 0;
}

void Init(void)
{
     ConfigPoint();
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glEnable(GL_DEPTH_TEST);
     glEnable(GL_BLEND);
     glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA);     
     glEnable(GL_LIGHTING);
     glEnable(GL_LIGHT0);
     glLightfv(GL_LIGHT0, GL_AMBIENT, fLtAmbient); 
     glMaterialfv(GL_LIGHT0, GL_DIFFUSE, fMatDiffuse);
     glMaterialfv(GL_LIGHT0, GL_SPECULAR, fMatSpecular);         
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(-12, 12, -12, 12, -12, 12);
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
     gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0);

}

void Transform(void)
{
     GLfloat x = 0.0; GLfloat y = 0.0;  GLfloat z = -12.0;
     GLfloat light_position[] = {((cos(angle)*x)+(sin(angle)*z)), y, ((-sin(angle)*x)+(cos(angle)*z)), 0};
     
     
     
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
     glViewport(0, 0, SIZE_WIN, SIZE_WIN);
     
     glPushMatrix();
     glColor4f(1.0, 1.0, 1.0,1.0);
     glBegin(GL_LINES);
        glVertex2f(-12.0, 0.0);
        glVertex2f(12.0, 0.0);
        glVertex2f(0.0, -12.0);
        glVertex2f(0.0, 12.0);
     glEnd();
     glPopMatrix();

     glLightfv( GL_LIGHT0, GL_POSITION, light_position);

     
     
     glPushMatrix();
     glViewport(0, 0, (SIZE_WIN / 2), (SIZE_WIN / 2));  
     glPushMatrix();
     SetLookAt(0,0,1,0,0,0,0,1,0);
     glDisable(GL_LIGHTING);     
     glColor4f(1.0,0.0,0.0,1.0);
     glRotatef(theta,0,1,0);     
     glTranslatef(0.0,0.0,12.0);
     glutSolidCube(1.0);
     glEnable(GL_LIGHTING);
     glPopMatrix();
//     SetLookAt(((cos(angle)*x)+(sin(angle)*z)),y,((-sin(angle)*x)+(cos(angle)*z)),0,0,0,0,1,0);
     DrawCube();
     glPopMatrix();
     
     glPushMatrix();
     glViewport((SIZE_WIN / 2) , 0, (SIZE_WIN / 2), (SIZE_WIN / 2));

     SetLookAt(0,5,0,0,0,0,1,0,0);
     glPushMatrix();
     glDisable(GL_LIGHTING);     
     glColor4f(1.0,0.0,0.0,1.0);
     glRotatef(theta,0,1,0);     
     glTranslatef(0.0,0.0,12.0);
     glutSolidCube(1.0);
     glEnable(GL_LIGHTING);
     glPopMatrix();
     
//     SetLookAt(x,((cos(angle)*y)+(sin(angle)*z)),((-sin(angle)*y)+(cos(angle)*z)),0,0,0,1,0,0);
     DrawCube();
     glPopMatrix();

/*
     glPushMatrix();
     glViewport(0, (SIZE_WIN / 2) , (SIZE_WIN / 2), (SIZE_WIN / 2));
     x = 1.0; y = 0.0; z = 0.0;
     SetLookAt(1,0,0,0,0,0,0,1,0);
//     SetLookAt(((cos(angle)*x)+(sin(angle)*z)),y,((-sin(angle)*x)+(cos(angle)*z)),0,0,0,0,1,0);
     DrawCube();
     glPopMatrix();


     glPushMatrix();
     glViewport((SIZE_WIN / 2) , (SIZE_WIN / 2) , (SIZE_WIN / 2), (SIZE_WIN / 2));
     x = 1.0; y = 1.0; z = 1.0;
     SetLookAt(1,1,1,0,0,0,0,0,1);
//     SetLookAt(x,((cos(angle)*y)+(sin(angle)*z)),((-sin(angle)*y)+(cos(angle)*z)),0,0,0,0,0,1);
     DrawCube();*/
     glPopMatrix();
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

      for(int i=0;i<RN;i++){
        ///cube left
            sf2N[i].x = sf1N[i].x - 6.0;  sf2N[i].y = sf1N[i].y + 0.0;  sf2N[i].z = sf1N[i].z - 6.0;///surface????????????
            sf2L[i].x = sf1L[i].x - 6.0;  sf2L[i].y = sf1L[i].y + 0.0;  sf2L[i].z = sf1L[i].z - 6.0;///surface????????????
            sf2R[i].x = sf1R[i].x - 6.0;  sf2R[i].y = sf1R[i].y + 0.0;  sf2R[i].z = sf1R[i].z - 6.0;///surface???????????
            sf2T[i].x = sf1T[i].x - 6.0;  sf2T[i].y = sf1T[i].y + 0.0;  sf2T[i].z = sf1T[i].z - 6.0;///surface??????????
            sf2B[i].x = sf1B[i].x - 6.0;  sf2B[i].y = sf1B[i].y + 0.0;  sf2B[i].z = sf1B[i].z - 6.0;///surface????????????
            sf2F[i].x = sf1F[i].x - 6.0;  sf2F[i].y = sf1F[i].y + 0.0;  sf2F[i].z = sf1F[i].z - 6.0;///surface????????????
        ///cube right
            sf3N[i].x = sf1N[i].x + 6.0;  sf3N[i].y = sf1N[i].y + 0.0;  sf3N[i].z = sf1N[i].z - 6.0;///surface????????????
            sf3L[i].x = sf1L[i].x + 6.0;  sf3L[i].y = sf1L[i].y + 0.0;  sf3L[i].z = sf1L[i].z - 6.0;///surface????????????
            sf3R[i].x = sf1R[i].x + 6.0;  sf3R[i].y = sf1R[i].y + 0.0;  sf3R[i].z = sf1R[i].z - 6.0;///surface???????????
            sf3T[i].x = sf1T[i].x + 6.0;  sf3T[i].y = sf1T[i].y + 0.0;  sf3T[i].z = sf1T[i].z - 6.0;///surface??????????
            sf3B[i].x = sf1B[i].x + 6.0;  sf3B[i].y = sf1B[i].y + 0.0;  sf3B[i].z = sf1B[i].z - 6.0;///surface????????????
            sf3F[i].x = sf1F[i].x + 6.0;  sf3F[i].y = sf1F[i].y + 0.0;  sf3F[i].z = sf1F[i].z - 6.0;///surface????????????
      }
}

void DrawCube(void)
{
    ///???????????quarter
    ///cube center            
//     glRotatef(theta,0,1,0);
     glPushMatrix();
     PlotSurface(sf1N,1.0,0.0,0.0,0.7);
     PlotSurface(sf1L,0.0,1.0,0.0,0.7);
     PlotSurface(sf1R,0.0,1.0,0.5,0.7);
     PlotSurface(sf1T,0.0,0.0,1.0,0.7);
     PlotSurface(sf1B,0.5,0.0,1.0,0.7);
     PlotSurface(sf1F,1.0,0.5,0.0,0.7);
     glPopMatrix();
    ///cube left
     glPushMatrix();
     PlotSurface(sf2N,0.0,1.0,0.0,0.6);
     PlotSurface(sf2L,0.0,0.0,1.0,0.6);
     PlotSurface(sf2R,0.5,0.0,1.0,0.6);
     PlotSurface(sf2T,1.0,0.0,0.0,0.6);
     PlotSurface(sf2B,1.0,0.5,0.0,0.6);
     PlotSurface(sf2F,0.0,1.0,0.5,0.6);
     glPopMatrix();
    ///cube right
     glPushMatrix();
     PlotSurface(sf3N,0.0,0.0,1.0,0.65);
     PlotSurface(sf3L,1.0,0.0,0.0,0.65);
     PlotSurface(sf3R,1.0,0.5,0.0,0.65);
     PlotSurface(sf3T,0.0,1.0,0.0,0.65);
     PlotSurface(sf3B,0.0,1.0,0.5,0.65);
     PlotSurface(sf3F,0.5,0.0,1.0,0.65);
     glPopMatrix();
}

void SetLookAt(GLfloat eyeX,GLfloat eyeY,GLfloat eyeZ,GLfloat x,GLfloat y,GLfloat z,GLfloat vexX,GLfloat vexY,GLfloat vexZ)
{
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(eyeX, eyeY, eyeZ, x, y, z, vexX, vexY, vexZ);
}

void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (Key){
            case 0x1B :       /// ESC Button
                 exit(0);
                 break;
            default :
                    break;
     }
}
void Idle(void)
{
     if ((theta >= 360.0)||(theta < 0.0))
        sign = sign *(-1);
     theta += (0.2*sign);
     
     angle = (theta*PI)/180.0; 
     
	 glutPostRedisplay();
}



