#include <GL/glut.h>
float Xmin = -0.2;
float Xmax =  0.2;
float Ymin = -0.2;
float Ymax =  0.2;

float theta = 0.0;
int sign = 1;
void Init(void)
{
    glClearColor(0.0, 0.0, 0.0, 1.0);


}
void myDisplay(void)
{
   int i;

     glClear(GL_COLOR_BUFFER_BIT);
//     glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
     glBegin(GL_LINES);
     glPushMatrix();
          glVertex2f(-0.5, -0.5);           // START LINE 1 IN Q2
          glVertex2f(0.5, 0.5);           // START LINE 1 IN Q2
     glEnd();

     glPopMatrix();
     glPushMatrix();
     glRotatef(theta,0,0,1);
     glScalef(1.0,1.0,0.0);
     glBegin(GL_POLYGON);
          glVertex2f(Xmin, Ymin);           // START LINE 1 IN Q2
          glVertex2f(Xmin, Ymax);           // START LINE 1 IN Q2
          glVertex2f(Xmax, Ymax);           // START LINE 1 IN Q2
          glVertex2f(Xmax, Ymin);           // START LINE 1 IN Q2
     glEnd();
     glPopMatrix();

     glutSwapBuffers();
  //  glFlush();

}
void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (Key)
     {
            case 0x2B :               // Press Esc to exit
                 exit(0);
                 break;
            case 0x6E :              // Press 'n' or 'N' to Reset Object
                 Xmin = Xmin - 0.1;
                 Xmax = Xmax - 0.1;
                 break;
     }      // Switch
     glutPostRedisplay();
}
void SpecialKey(GLint Key, GLint x, GLint y)
{
     switch (Key)
     {
            case GLUT_KEY_LEFT :
                 if (Xmin > -1.0)
                 {
                    Xmin -= 0.1;
                    Xmax -= 0.1;
                 }
                 break;
            case GLUT_KEY_RIGHT :
                 if (Xmax < 1.0)
                 {
                    Xmin += 0.1;
                    Xmax += 0.1;
                 }
                 break;
            case GLUT_KEY_DOWN :
                 if (Ymin > -1.0)
                 {
                    Ymin -= 0.1;
                    Ymax -= 0.1;
                 }
                 break;
            case GLUT_KEY_UP :
                 if (Ymax < 1.0)
                 {
                    Ymin += 0.1;
                    Ymax += 0.1;
                 }
                 break;
            default :
                    break;
     }           // Switch
     glutPostRedisplay();
}
void MyIdle(void)
{
     if ((theta >= 360.0)||(theta < 0.0))
        sign = sign *(-1);
     theta += (2.0*sign);

	 glutPostRedisplay();
}
int main(int argc, char** argv)

{
    glutInit(&argc ,argv);
    glutInitWindowSize(250, 250);
    glutInitWindowPosition(100,100);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutCreateWindow("Simple");
    Init();
    glutDisplayFunc(myDisplay);
    glutKeyboardFunc(KeyboardKey);
    glutSpecialFunc(SpecialKey);
    glutIdleFunc(MyIdle);
    glutMainLoop();

    return 0;
}
