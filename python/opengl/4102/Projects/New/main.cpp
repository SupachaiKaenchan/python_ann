#include <GL/glut.h>
#include <GL/glext.h>
#include <math.h>
#include <fstream>
#include <iostream>
#include <stdlib.h>
#define PI          3.1415926535897932384626433832795
#define SIZE_WIN    500
#define SIZE_ORT    500.0
#define RN          4
#define TEXTURE_ID_BRICK 1
#define TEXTURE_ID_ART 2

typedef struct Point {
        GLfloat      x;
        GLfloat      y;
        GLfloat      z;
};

GLfloat theta = 0.0;
GLint sign = 1;
GLfloat x = 0.0,y = 0.0,z = 14.0;
GLfloat angle = 0.0;
void Init(void);
void Transform(void);
void Idle(void);
void KeyboardKey(GLubyte Key, GLint x, GLint y);
int LoadTexture( const char * filename, int width, int height, GLuint id );



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
     glEnable(GL_DEPTH_TEST);

 //    glMatrixMode(GL_MODELVIEW);
 //    glLoadIdentity();
 //    gluLookAt(0,0,3,0,0,0,0,1,0);
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();
     glOrtho(-50.0, 50.0, -50.0, 50.0, -50.0, 50.0);
//     glFrustum(-3, 3, -3, 3, 2, 20);


     LoadTexture("brick.bmp",1024,1024, TEXTURE_ID_BRICK);
     LoadTexture("art.bmp",1920,1080, TEXTURE_ID_ART);

//     glFrustum(-3, 3, -3, 3, 2, 20);
//gluLookAt(0,-5,0,0,0,0,1,0,0);
/*     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
/     gluLookAt(0,-5,0,0,0,0,1,0,0);*/
}

void Transform(void)
{
     

     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);     
     glPushMatrix();
     
     glEnable(GL_TEXTURE_2D);
     glBindTexture(GL_TEXTURE_2D,TEXTURE_ID_BRICK);
     glTranslatef(0,0,-49);     
     glBegin(GL_QUADS);
      glTexCoord2d(0,0);
      glVertex2d(-50,-50);
      glTexCoord2d(0,1);
      glVertex2d(-50,50);
      glTexCoord2d(1,1);
      glVertex2d(50,50);
      glTexCoord2d(1,0);
      glVertex2d(50,-50);
    glEnd();
    glBindTexture(GL_TEXTURE_2D,0);
    glDisable(GL_TEXTURE_2D);
    glPopMatrix();

    glPushMatrix();
    glEnable(GL_TEXTURE_2D);
    glBindTexture(GL_TEXTURE_2D,TEXTURE_ID_ART);
    glRotatef(theta,0,1,0);
    GLUquadric *quad;
    quad = gluNewQuadric();
    gluQuadricTexture(quad,1);
    gluSphere(quad,20,50.0,20.0);
    glBindTexture(GL_TEXTURE_2D,0);
    glDisable(GL_TEXTURE_2D);
    glPopMatrix();
    
     glutSwapBuffers();
}


void Idle(void)
{
     if ((theta >= 360.0)||(theta < 0.0))
        sign = sign *(-1);
     theta += (0.1*sign);
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

int LoadTexture( const char * filename, int width, int height, GLuint id )
{
  GLuint texture;
  unsigned char * data;
  FILE * file;

  file = fopen( filename, "rb" );
  if ( file == NULL ) return 0;
  data = (unsigned char *)malloc( width * height * 3 );
  fread( data,1, width * height * 3, file );
  fclose( file );
  
  glBindTexture(GL_TEXTURE_2D, id);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_BGR, GL_UNSIGNED_BYTE, data);
  free( data );
  return 0; 
}


