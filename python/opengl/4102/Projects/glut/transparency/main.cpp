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
GLfloat xe = 0.0;
GLfloat ye = 0.0;
GLfloat ze = 14.0;
GLfloat angle;
void Init(void);
void Transform(void);
void Idle(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);

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
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glEnable(GL_BLEND);
     glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA);
     glEnable(GL_DEPTH_TEST);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(-3, 3, -3, 3, -3, 3);
}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
       
     glPushMatrix();
     glColor4f(1.0,0.0,0.0,0.25);
     glutSolidSphere(1.0,30,30);           
     glPopMatrix();
     
     glPushMatrix();
     glTranslatef(1.0,1.0,1.0);
     glColor4f(1.0,1.0,0.0,0.75);
     glutSolidCube(2.0);  
     glPopMatrix();

     glutSwapBuffers();
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
     switch (Key){
            case 0x1B :       /// ESC Button
                 exit(0);
                 break;
            default :
                 break;
     }
}



