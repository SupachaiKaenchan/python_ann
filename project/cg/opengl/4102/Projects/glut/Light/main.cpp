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
///cube center
Point sf1N[RN],sf1L[RN],sf1R[RN],sf1T[RN],sf1B[RN],sf1F[RN];
///cube left
Point sf2N[RN],sf2L[RN],sf2R[RN],sf2T[RN],sf2B[RN],sf2F[RN];
///cube right
Point sf3N[RN],sf3L[RN],sf3R[RN],sf3T[RN],sf3B[RN],sf3F[RN];

GLfloat theta = 0.0;
GLint sign = 1;
GLint zCoordinate = 14;

GLint flag = 1;
GLenum sFactor = GL_SRC_ALPHA;
GLenum dFactor = GL_ONE_MINUS_SRC_ALPHA;

GLfloat light_position[]  = {-9.0,0.0,0.0,0};
GLfloat fLtAmbient[] = {1,1,1,1};
GLfloat fLtDiffuse[] = {1,1,1,1}; 
GLfloat fLtSpecular[]= {0,0,0,1};

GLfloat fMatAmbient[] = {0.0,0.2,0.0,1};
GLfloat fMatDiffuse[] = {0.0,0.6,0.0,1}; 
GLfloat fMatSpecular[] = {0,0,0,1};

GLfloat light_position1[]  = {0.0,0.0,5.0,0};
GLfloat fLtAmbient1[] = {1,1,1,1};
GLfloat fLtDiffuse1[] = {1,1,1,1}; 
GLfloat fLtSpecular1[]= {0,0,0,1};



void Init(void);
void Transform(void);
void ConfigPoint(void);
void PlotSurface(Point Surface[RN],GLfloat red,GLfloat green,GLfloat blue);
void DrawCube(GLfloat x);
void Idle(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
void SpecialKey(GLint Key, GLint x, GLint y);

int main(int argc, char** argv)
{
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("Cube");
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
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glEnable(GL_DEPTH_TEST);
     glEnable(GL_BLEND);
     
     glBlendFunc(sFactor, dFactor);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(-15,15,-15,15,-15,15);

}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
     glMatrixMode(GL_MODELVIEW);//map from world coordinate to eye coordinate
     glLoadIdentity();
     glEnable(GL_LIGHTING);  
     if (flag){
        glDisable(GL_LIGHT1);
        glEnable(GL_LIGHT0);
        }   
     else { 
        glDisable(GL_LIGHT0);
        glEnable(GL_LIGHT1);
        }   

     glLightfv(GL_LIGHT0, GL_DIFFUSE, fLtDiffuse);
     glLightfv(GL_LIGHT0, GL_AMBIENT, fLtAmbient);
     glLightfv(GL_LIGHT0, GL_SPECULAR, fLtSpecular);     

     glMaterialfv(GL_FRONT, GL_SPECULAR, fMatSpecular);

     glLightfv(GL_LIGHT1, GL_DIFFUSE, fLtDiffuse1);
     glLightfv(GL_LIGHT1, GL_AMBIENT, fLtAmbient1);
     glLightfv(GL_LIGHT1, GL_SPECULAR, fLtSpecular1);     

     
     glPushMatrix();     
     glRotatef(theta,0,1,0);
     glLightfv(GL_LIGHT0,GL_POSITION,light_position);
     glLightfv(GL_LIGHT1,GL_POSITION,light_position1);
     glPopMatrix();
     
     glViewport(0, 0, SIZE_WIN, SIZE_WIN);
     gluLookAt(0,0,zCoordinate,0,0,0,0,1,0);
     

      glPushMatrix();
      glColor4f(0.0, 1.0, 0.0 ,1);
      glMaterialfv(GL_FRONT, GL_AMBIENT, fMatAmbient);
      glMaterialfv(GL_FRONT, GL_DIFFUSE, fMatDiffuse);

      DrawCube(0.0);
      glPopMatrix();
      
      //glPushMatrix();
      //glColor4f(0.0, 0.0, 1.0 ,1);
      //DrawCube(10.0);
      //glPopMatrix();

     glutSwapBuffers();
}


void DrawCube(GLfloat x)
{
     
     glPushMatrix();
     glTranslatef(x, 0.0, 0.0);
     glutSolidSphere(4.0, 20, 20);
     glPopMatrix();
}

void Idle(void)
{
     //if ((theta >= 360.0)||(theta < 0.0))
        //sign = sign *(-1);
     theta += (0.1*sign);

	 glutPostRedisplay();
}

void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (Key){
            case 0x1B :       /// ESC Button
                 exit(0);
                 break;
            case 'a' :
                 theta += 1.0;
                 glutPostRedisplay();
                 break;
            case 'd' :
                 flag = !flag;
                 glutPostRedisplay();
                 break;
            case 's' :
                 zCoordinate += 1;
                 Init();
                 glutPostRedisplay();
                 break;
            case 'w' :
                 zCoordinate -= 1;
                 Init();
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
                 break;
            case GLUT_KEY_RIGHT :
                 break;
            case GLUT_KEY_DOWN :
                 zCoordinate += 1;
                 Init();
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_UP :
                 zCoordinate -= 1;
                 Init();
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_HOME :
				 glutPostRedisplay();
				 break;
            case GLUT_KEY_END :
                 glutPostRedisplay();
                 break;
            default :
                 break;
     }
}


