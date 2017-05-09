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
Point sf1N[RN],sf1L[RN],sf1R[RN],sf1T[RN],sf1B[RN],sf1F[RN];

GLfloat theta = 0.0;
GLint sign = 1;
float posi[3][3] = { {0.0, 0.0, 0.0},
                                 {-6.0,0.0,-6.0},
                                 { 6.0,0.0,-6.0}};

float color[6][4] = { {1.0, 0.1, 0.5,0.5},
                                  {0.6, 1.0, 0.4,0.5},
                                  {0.8, 1.0, 0.5,0.5},
                                  {0.3, 0.6, 1.0,0.5},
                                  {0.5, 0.5, 1.0,0.5},
                                  {1.0, 0.5, 1.0,0.5}};

GLfloat  L0amb[]  =  {0.3,0.3,0.3,1.0};
GLfloat  L0diff[]  =  {1.0,1.0,1.0,1.0};
GLfloat  L0spec[]  =  {1.0,1.0,1.0,1.0};
GLfloat  amb_Light[]  =  {0.8,0.8,0.8,1.0};
GLfloat  L0dir[] = {5.0,0.0,0.0,0.0};

GLfloat  emiss[] = {1.0,0.0,0.0,1.0};
GLfloat  no_emiss[] = {0.0,0.0,0.0,1.0};

//GLfloat  amb_Light[]  =  {0.2,0.2,0.2,1.0};
void Init(void);
void initLight();
void Transform(void);
void ConfigPoint(void);
void PlotSurface(Point Surface[RN],GLint k);
void DrawCube(void);
void Idle(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("Cube");
	Init();
	initLight();
	glutDisplayFunc(Transform);
//	glutKeyboardFunc(KeyboardKey);
//	glutIdleFunc(Idle);
	glutMainLoop();
    return 0;
}

void Init(void)
{
     ConfigPoint();
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);sss
     glEnable(GL_DEPTH_TEST);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(-15,15,-15,15,-15,15);
   //  glFrustum(-3, 3, -3, 3, 2, 25);
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
    // gluLookAt(0,0,14,0,0,0,0,1,0);
     gluLookAt(0,0,6,0,0,0,0,1,0);
}
void initLight()
{
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);    
    glLightfv(GL_LIGHT0,GL_DIFFUSE,L0diff);
    glLightfv(GL_LIGHT0,GL_AMBIENT,L0amb);
    glLightfv(GL_LIGHT0,GL_SPECULAR,L0spec);
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, amb_Light);
}     
void Transform(void)
{
int i;
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
      theta += 0.5;
      if ( theta >= 360.0)
          theta -= 360.0*floor(theta/360.0);
     glPushMatrix();
     glColor3f(0.5, 0.5, 0.5);
     glBegin(GL_LINES);
          glVertex2f(-15.0, 0.0);
          glVertex2f(15.0, 0.0);
          glVertex2f(0.0, -15.0);
          glVertex2f(0.0, 15.0);
     glEnd();
     glPopMatrix();
     glPushMatrix();
     glRotatef(theta,0,0,1);
     glLightfv(GL_LIGHT0,GL_POSITION,L0dir);     
     glTranslatef(9.0,0.0,0.0);
     glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, emiss);
//     glDisable(GL_LIGHTING);
     glColor3f(1.0,0.0,0.0);
     glutSolidSphere(0.3,10,10);   
//     glEnable(GL_LIGHTING);
     glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, no_emiss);
     glPopMatrix();
     
       for(i=0; i<6;i++){
            glPushMatrix();
            glColor3f(color[i][0],color[i][1],color[i][2]);
//            glTranslatef(posi[i][0],posi[i][1],posi[i][2]);
//            glRotatef(theta,0,1,0);
            //DrawCube();
            glRotatef(60*float(i),0,0,1);
            glTranslatef(5.0,0.0,0.0);
            glutSolidSphere(1.0,30,30);
            glPopMatrix();
       }
      glFlush();
      glutSwapBuffers();
      glutPostRedisplay();
}

void PlotSurface(Point Surface[RN],GLint k)
{
    glColor3f(color[k][0],color[k][1],color[k][2]);
    glBegin(GL_POLYGON);
        for (int i=0; i<RN; i++)
            glVertex3f(Surface[i].x, Surface[i].y, Surface[i].z);
    glEnd();
}

void ConfigPoint(void)
{     ///surfaceáŒè¹ŽéÒ¹Ë¹éÒ Cube center
      sf1N[0].x = -2.0;       sf1N[0].y = -2.0;     sf1N[0].z = 2.0;
      sf1N[1].x = -2.0;       sf1N[1].y = 2.0;      sf1N[1].z = 2.0;
      sf1N[2].x = 2.0;        sf1N[2].y = 2.0;      sf1N[2].z = 2.0;
      sf1N[3].x = 2.0;        sf1N[3].y = -2.0;     sf1N[3].z = 2.0;
      ///surfaceáŒè¹ŽéÒ¹«éÒÂ Cube center
      sf1L[0].x = -2.0;      sf1L[0].y = -2.0;      sf1L[0].z = -2.0;
      sf1L[1].x = -2.0;      sf1L[1].y = 2.0;       sf1L[1].z = -2.0;
      sf1L[2].x = -2.0;      sf1L[2].y = 2.0;       sf1L[2].z = 2.0;
      sf1L[3].x = -2.0;      sf1L[3].y = -2.0;      sf1L[3].z = 2.0;
      ///surfaceáŒè¹ŽéÒ¹¢ÇÒ Cube center
      sf1R[0].x = 2.0;       sf1R[0].y = -2.0;      sf1R[0].z = 2.0;
      sf1R[1].x = 2.0;       sf1R[1].y = 2.0;       sf1R[1].z = 2.0;
      sf1R[2].x = 2.0;       sf1R[2].y = 2.0;       sf1R[2].z = -2.0;
      sf1R[3].x = 2.0;       sf1R[3].y = -2.0;      sf1R[3].z = -2.0;
      ///surfaceáŒè¹ŽéÒ¹º¹ Cube center
      sf1T[0].x = -2.0;      sf1T[0].y = 2.0;       sf1T[0].z = 2.0;
      sf1T[1].x = -2.0;      sf1T[1].y = 2.0;       sf1T[1].z = -2.0;
      sf1T[2].x = 2.0;       sf1T[2].y = 2.0;       sf1T[2].z = -2.0;
      sf1T[3].x = 2.0;       sf1T[3].y = 2.0;       sf1T[3].z = 2.0;
      ///surfaceáŒè¹ŽéÒ¹ÅèÒ§ Cube center
      sf1B[0].x = -2.0;      sf1B[0].y = -2.0;      sf1B[0].z = -2.0;
      sf1B[1].x = -2.0;      sf1B[1].y = -2.0;      sf1B[1].z = 2.0;
      sf1B[2].x = 2.0;       sf1B[2].y = -2.0;      sf1B[2].z = 2.0;
      sf1B[3].x = 2.0;       sf1B[3].y = -2.0;      sf1B[3].z = -2.0;
      ///surfaceáŒè¹ŽéÒ¹ËÅÑ§ Cube center
      sf1F[0].x = -2.0;      sf1F[0].y = 2.0;       sf1F[0].z = -2.0;
      sf1F[1].x = -2.0;      sf1F[1].y = -2.0;      sf1F[1].z = -2.0;
      sf1F[2].x = 2.0;       sf1F[2].y = -2.0;      sf1F[2].z = -2.0;
      sf1F[3].x = 2.0;       sf1F[3].y = 2.0;       sf1F[3].z = -2.0;

}

void DrawCube(void)
{
    ///ÇÒŽàÊé¹áºè§quarter

    ///cube center
     glPushMatrix();
     PlotSurface(sf1N, 0);
     PlotSurface(sf1L, 1);
     PlotSurface(sf1R, 2);
     PlotSurface(sf1T, 3);
     PlotSurface(sf1B, 4);
     PlotSurface(sf1F, 5);
     glPopMatrix();
}

void Idle(void)
{
     if ((theta >= 360.0)||(theta < 0.0))
        sign = sign *(-1);
     theta += (0.01*sign);

	 glutPostRedisplay();
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


