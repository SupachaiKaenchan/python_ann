#include <GL/glut.h>

void Init(void)
{
    glClearColor(0.0, 0.0, 0.0, 1.0);
    glColor3f(1.0,0.0,0.0);

}
void myDisplay(void)
{
   int i;

     glClear(GL_COLOR_BUFFER_BIT);
  //   glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
     glBegin(GL_POLYGON);
          glVertex2f(-0.5, -0.5);           // START LINE 1 IN Q2
          glVertex2f( -0.5, 0.5);           // START LINE 1 IN Q2
          glVertex2f( 0.5, 0.5);           // START LINE 1 IN Q2
          glVertex2f( 0.5, -0.5);           // START LINE 1 IN Q2
     glEnd();
     glutSwapBuffers();
 //   glFlush();

}

int main(int argc, char** argv)

{
    glutInit(&argc ,argv);
  //  glutInitWindowSize(250, 250);
//    glutInitWindowPosition(100,100);
//    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutCreateWindow("Simple");
//    Init();
    glutDisplayFunc(myDisplay);

    glutMainLoop();

    return 0;
}
