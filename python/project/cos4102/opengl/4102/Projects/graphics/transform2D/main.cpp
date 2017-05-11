#include <GL/glut.h>

#define PI          3.1415926535897932384626433832795
#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define TN          3
#define RN          4

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
} Point;

Point Tri[TN], Rec[RN];
Point p1, p2;
GLfloat theta = 0.0;
GLfloat xsc = 1.0, ysc = 1.0;
GLfloat tx = 0.0, ty = 0.0;
GLfloat scale_sign = 0.001;

void Init(void);
void Transform(void);
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
//	glutIdleFunc(Idle);

	glutMainLoop();
	
    return 0;
}

void Init(void)
{

     
     ConfigPoint();
     
     // Calculate centre
     glClearColor(0.0, 0.0, 0.0, 0.0);
     glPointSize(1.0);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     gluOrtho2D(-SIZE_ORT, SIZE_ORT, -SIZE_ORT, SIZE_ORT);
     
}

void Transform(void)
{
     glClear(GL_COLOR_BUFFER_BIT);     
     glColor3f(1.0, 0.0, 0.0);
     glPushMatrix();
     glBegin(GL_LINES);
         glVertex2f(p1.x, p1.y);              
         glVertex2f(p2.x, p2.y);              
     glEnd();
     glPopMatrix();

     glPushMatrix();
     glColor3f(1.0, 1.0, 1.0);
     glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
     glBegin(GL_POLYGON);
        for (int i=0; i<RN; i++)
            glVertex2f(Rec[i].x + tx, Rec[i].y + ty);
     glEnd();
     glPopMatrix();
          
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
                 tx -= 1.0;
                  glutPostRedisplay();
                 break;
            case GLUT_KEY_RIGHT :
                 tx += 1.0;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_DOWN :
                 ty -= 1.0;
                 glutPostRedisplay();
                 break;
            case GLUT_KEY_UP :
                 ty += 1.0;
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
     if (theta >= 360)
        theta = 0;
     else
         theta += 2.0;
     
     if (xsc < 0.1)
        scale_sign = 0.5;
     if (xsc > 2.0)
        scale_sign = -0.5;
     xsc += scale_sign;
     ysc += scale_sign;

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
     p1.x = -200.0;            p1.y = -200.0;
     p2.x = 0.0;               p2.y = 0.0;
}
