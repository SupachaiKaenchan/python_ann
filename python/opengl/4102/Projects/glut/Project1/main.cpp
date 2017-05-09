#include <GL/glut.h>
#include <stdio.h>
#include <conio.h>
#include <ctype.h>

#define SIZE_W      500
#define SIZE_MX     500.0

typedef struct point {
        float  x;
        float  y;
} Point;

Point   p1, p2;

int     skip;

double  Xmin = -100.0;
double  Xmax = 100.0;
double  Ymin = -100.0;
double  Ymax = 100.0;
double  center_xy = (Xmax - Xmin) / 2.0;
double  mouse_x, mouse_y;

int     mouse_state = 1;

GLubyte CodeXmin = 0x01;
GLubyte CodeXmax = 0x02;
GLubyte CodeYmin = 0x04;
GLubyte CodeYmax = 0x08;

void ConfigPoint(void)
{
     skip = 1;

     p1.x = p1.y = -200.0;
     p2.x = p2.y = 200.0;

     Xmin = Ymin = -100.0;
     Xmax = Ymax = 100.0;
}

void init(void)
{
     glClearColor(0.0, 0.0, 0.0, 1.0);
     glPointSize(1.0);
     gluOrtho2D(-SIZE_MX, SIZE_MX, -SIZE_MX, SIZE_MX);

     ConfigPoint();

}

void myDrawLine(void)
{
     glClear(GL_COLOR_BUFFER_BIT);
     glColor3f(1.0, 1.0, 1.0);
     glBegin(GL_LINES);
          glVertex2f(-SIZE_MX, 0.0);
          glVertex2f(SIZE_MX, 0.0);
          glVertex2f(0.0, -SIZE_MX);
          glVertex2f(0.0, SIZE_MX);
     glEnd();

     glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
     glColor3f(0.0, 1.0, 0.0);
     glBegin(GL_POLYGON);
          glVertex2f(Xmin, Ymin);
          glVertex2f(Xmin, Ymax);
          glVertex2f(Xmax, Ymax);
          glVertex2f(Xmax, Ymin);
     glEnd();

     if (skip)
     {
           glPushMatrix();
                glColor3f(1.0, 1.0, 1.0);
                glBegin(GL_LINES);
                     glVertex2f(p1.x, p1.y);
                     glVertex2f(p2.x, p2.y);
                glEnd();
          glPopMatrix();
     }

     glFlush();
}

void Encode(GLfloat x, GLfloat y, GLubyte &code)
{
    code = 0x00;

    if (x < Xmin)
       code = code | CodeXmin;
    if (x > Xmax)
       code = code | CodeXmax;
    if (y < Ymin)
       code = code | CodeYmin;
    if (y > Ymax)
       code = code | CodeYmax;

}

void SwapCode(GLubyte &code1, GLubyte &code2)
{
     GLubyte tempCode;
     Point   temp;

     temp.x = p1.x;
     p1.x   = p2.x;
     p2.x   = temp.x;

     temp.y = p1.y;
     p1.y   = p2.y;
     p2.y   = temp.y;

     tempCode = code1;
     code1    = code2;
     code2    = tempCode;
}

int Accept(GLubyte code1, GLubyte code2)
{
    if (code1 | code2)
       return 0;
    return 1;
}

int Reject(GLubyte code1, GLubyte code2)
{
    if (code1 & code2)
       return 1;
    return 0;
}

void Clipping(void)
{
   int flag = 0;

   GLubyte  code1 = 0x00;
   GLubyte  code2 = 0x00;
   GLfloat  dy = p2.y - p1.y;
   GLfloat  dx = (p2.x != p1.x)? p2.x - p1.x : 0.0000000000000000001;

   while (!flag)
   {
       Encode(p1.x, p1.y, code1);
       Encode(p2.x, p2.y, code2);

       printf("\n %7.2f, %7.2f, %7.2f, %7.2f", p1.x, p1.y, p2.x, p2.y);
       if (Accept(code1, code2))
          flag = 1;
       else
           if (Reject(code1, code2))
           {
              flag = 1;
              skip = 0;
           }
           else
               {
                   if (code1 == 0x00)
                      SwapCode(code1, code2);
                   else
                   {
                       if (code1 & CodeXmin)
                       {
                          if (dy != 0.0)
                             p1.y += (Xmin - p1.x) * (dy / dx);
                          p1.x = Xmin;
                       }
                       if (code1 & CodeXmax)
                       {
                          if (dy != 0.0)
                             p1.y += (Xmax - p1.x) * (dy / dx);
                          p1.x = Xmax;
                       }
                       if (code1 & CodeYmin)
                       {
                          if (dx != 0.0)
                             p1.x += (Ymin - p1.y) * (dy / dx);
                          p1.y = Ymin;
                       }
                       if (code1 & CodeYmax)
                       {
                          if (dx != 0.0)
                             p1.x += (Ymax - p1.y) * (dy /dx);
                          p1.y = Ymax;
                       }
                   }
               }

   }          // While
}

void KeyboardKey(GLubyte Key, GLint x, GLint y)
{
     switch (tolower(Key))
     {
            case 0x1B :             // Press 'Esc' to Exit
                 exit(0);
                 break;
            case 0x0D :             // Press 'Enter' to Clipping Line
                 Clipping();
                 break;
            case 0x2B :             // Press '+' to Increment size of the moving window
                 if ((Xmax - Xmin) < (SIZE_MX * 2.0))
                 {
                    Xmin -= 1.0;
                    Xmax += 1.0;
                    Ymin -= 1.0;
                    Ymax += 1.0;
                    center_xy = (Xmax - Xmin) / 2.0;
                    glutPostRedisplay();
                 }
                 break;
            case 0x2D :             // press '-' to Decrement size of the moving window
                 if ((Xmax - Xmin) > 5.0)
                 {
                    Xmin += 1.0;
                    Xmax -= 1.0;
                    Ymin += 1.0;
                    Ymax -= 1.0;
                    center_xy = (Xmax - Xmin) / 2.0;
                    glutPostRedisplay();
                 }
                 break;
            case 0x6E :             // Press 'n' of 'N' to Reset
                 ConfigPoint();
                 center_xy = (Xmax - Xmin) / 2.0;
                 glutPostRedisplay();
                 break;
            case 0x76 :             // Press 'v' or 'V' to Configure Vertical Line
                 skip = 1;
                 p1.x = p2.x = 100.0;
                 p1.y = -200.0;
                 p2.y = 200.0;
                 center_xy = (Xmax - Xmin) / 2.0;
                 glutPostRedisplay();
                 break;
            case 0x68 :             // Press 'h' or 'H' to Configure Horizontal Line
                 skip = 1;
                 p1.y = p2.y = 100.0;
                 p1.x = -200.0;
                 p2.x = 200.0;
                 center_xy = (Xmax - Xmin) / 2.0;
                 glutPostRedisplay();
                 break;
            default :
                    break;
     }      // Switch
}

void SpecialKey(GLint Key, GLint x, GLint y)
{
     switch (Key)
     {
            case GLUT_KEY_UP :            // Move window up
                 if (Ymax < SIZE_MX)
                 {
                    Ymin += 1.0;
                    Ymax += 1.0;
                    glutPostRedisplay();
                 }
                 break;
            case GLUT_KEY_DOWN :          // Move window down
                 if (Ymin > -SIZE_MX)
                 {
                    Ymin -= 1.0;
                    Ymax -= 1.0;
                    glutPostRedisplay();
                 }
                 break;
            case GLUT_KEY_LEFT :          // Move window left
                 if (Xmin > -SIZE_MX)
                 {
                    Xmin -= 1.0;
                    Xmax -= 1.0;
                    glutPostRedisplay();
                 }
                 break;
            case GLUT_KEY_RIGHT :         // Move window right
                 if (Xmax < SIZE_MX)
                 {
                    Xmin += 1.0;
                    Xmax += 1.0;
                    glutPostRedisplay();
                 }
                 break;
            default :
                    break;
     }      // Switch
}

void MouseAssign(GLint Button, GLint State, GLint x, GLint y)
{
     switch (Button)
     {
            case GLUT_LEFT_BUTTON :               // Clipping Line
                 if (State == GLUT_DOWN)
                 {
                    Clipping();
                    glutPostRedisplay();
                 }
                 break;
            case GLUT_RIGHT_BUTTON :              // Reset Line
                 if (State == GLUT_DOWN)
                 {
                    ConfigPoint();
                    glutPostRedisplay();
                 }
                 break;
            default :
                    break;
     }      // Switch
     if (State == GLUT_ENTERED)                   // Mouse is enter
     {
           if (((mouse_x - center_xy) > -SIZE_MX) && ((mouse_x + center_xy) < SIZE_MX))
           {
              Xmin = mouse_x - center_xy;
              Xmax = mouse_x + center_xy;
           }
           if (((mouse_y - center_xy) > -SIZE_MX) && ((mouse_y + center_xy) < SIZE_MX))
           {
              Ymin = mouse_y - center_xy;
              Ymax = mouse_y + center_xy;
           }
           glutPostRedisplay();
     }
     mouse_state = (State == GLUT_UP)? 1 : 0;
     mouse_x = (2.0 * double(x)) - SIZE_MX;
     mouse_y = SIZE_MX - (2.0 * double(y));

}

void PassiveMotion(GLint x, GLint y)
{
     if (mouse_state)
     {
        if (((mouse_x - center_xy) > -SIZE_MX) && ((mouse_x + center_xy) < SIZE_MX))
        {
           Xmin = mouse_x - center_xy;
           Xmax = mouse_x + center_xy;
        }
        if (((mouse_y - center_xy) > -SIZE_MX) && ((mouse_y + center_xy) < SIZE_MX))
        {
           Ymin = mouse_y - center_xy;
           Ymax = mouse_y + center_xy;
        }
        glutPostRedisplay();
     }

     mouse_x = (2.0 * double(x)) - SIZE_MX;
     mouse_y = SIZE_MX - (2.0 * double(y));
}

int main(int argc, char** argv)
{
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(SIZE_W, SIZE_W);
    glutInitWindowPosition(SIZE_W, 0);
    glutCreateWindow("Clipping Line use mouse");

    init();

    glutDisplayFunc(myDrawLine);

    glutKeyboardFunc(KeyboardKey);
    glutSpecialFunc(SpecialKey);
    glutMouseFunc(MouseAssign);
    glutPassiveMotionFunc(PassiveMotion);

    glutMainLoop();

    return 0;
}
