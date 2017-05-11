#include <GL/glut.h>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>
using namespace std;
#define SIZE_WIN    600
#define SIZE_ORT   600
#define cord 5000
GLUquadricObj *theObj;
GLfloat Rot=0;
GLfloat look =1,rotateLook = -89.5399;
GLuint texture1,texture2,texture3;
enum {
    MENU_HELP = 1,
    MENU_EXIT
    };
#define TEXTURE_ID_SOLAR 1
#define TEXTURE_ID_SUN 2
#define TEXTURE_ID_WORLD 3

int LoadTexture( const char * filename, int width, int height, GLuint id )
{
  GLuint texture;
  unsigned char * data;
  FILE * file;
  file = fopen( filename, "rb" );
  if ( file == NULL ) return 0;
  data = (unsigned char *)malloc( width * height * 3 );
  fread( data, width * height * 3, 1, file );
  fclose( file );

  //glGenTextures(1, &texture );
  glBindTexture(GL_TEXTURE_2D, id);
  glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
  glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
  glTexEnvi( GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE );
  glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST );
  glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR );
  gluBuild2DMipmaps(GL_TEXTURE_2D, GL_RGBA, width, height, GL_RGB, GL_UNSIGNED_BYTE, data);
  free( data );
  return 0; // texture;
}

void FreeTexture( GLuint texture )
{
  glDeleteTextures( 1, &texture );
}

void Init(void)
{
     glClearColor(0, 0, 0, 0 );
     glEnable(GL_DEPTH_TEST);
   	LoadTexture("p2.bmp",2880,2880, TEXTURE_ID_SOLAR);
   	LoadTexture("sun1.bmp",2680,920, TEXTURE_ID_SUN);
 	LoadTexture("worldmap.bmp",1639,820, TEXTURE_ID_WORLD);

//	glShadeModel(GL_SMOOTH);
}

void World()
{
    if(look){
        gluLookAt(cos(-rotateLook),0,sin(-rotateLook),0,0,0,0,1,0);
     }
     glTranslatef(-500,0,0);
     //glRotatef((Rot)*.04,0,1,0);
     glEnable(GL_TEXTURE_2D);
     glBindTexture( GL_TEXTURE_2D,2);
     GLUquadric *quad;
     quad = gluNewQuadric();
     gluQuadricTexture(quad,1);
     gluSphere(quad,30,60,60);
     glBindTexture(GL_TEXTURE_2D,0);
     glDisable(GL_TEXTURE_2D);
}

void World1()
{
    if(look){
        gluLookAt(cos(rotateLook),0,sin(rotateLook),0,0,0,0,1,0);
     }
  //   glTranslatef(-500,0,0);
     //glRotatef((Rot)*.04,0,1,0);
     glEnable(GL_TEXTURE_2D);
     glBindTexture( GL_TEXTURE_2D,3);
     GLUquadric *quad;
     quad = gluNewQuadric();

     gluQuadricTexture(quad,1);
//     gluSphere(quad,40,60,60);
     gluDisk(quad,50,60,10,20);
     glBindTexture(GL_TEXTURE_2D,0);
     glDisable(GL_TEXTURE_2D);
}


void Transform(void)
{

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(120,500/500,0.1,10000);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glPushMatrix();

 //    glDisable(GL_LIGHTING);
     glEnable(GL_TEXTURE_2D );
     glTranslatef(0,0,-2800);
     glBindTexture( GL_TEXTURE_2D,TEXTURE_ID_SOLAR);
     glBegin (GL_QUADS);
        glTexCoord2d(0,0); 
        glVertex2d(-cord,-cord);
        glTexCoord2d(0,1); 
        glVertex2d(-cord,cord);
        glTexCoord2d(1,1); 
        glVertex2d(cord,cord);
        glTexCoord2d(1,0); 
        glVertex2d(cord,-cord);
     glEnd();
     glBindTexture(GL_TEXTURE_2D,0);
     glDisable(GL_TEXTURE_2D);
     //glEnable(GL_LIGHTING);


    glPushMatrix();
    glTranslatef(0,0,-3550);
    glRotatef(Rot,0,1,0);
    glScalef(2,2,2);
    glEnable(GL_TEXTURE_2D );
    glBindTexture( GL_TEXTURE_2D,2);
    GLUquadric *quad;
    quad = gluNewQuadric();
    gluQuadricTexture(quad,1);

    gluDisk(quad,300,600,100,20);
    //gluSphere(quad,300,100,100);
    glBindTexture(GL_TEXTURE_2D,0);
    glDisable(GL_TEXTURE_2D);
    glPopMatrix();

    glPushMatrix();
    World();
    glPopMatrix();
    glPushMatrix();
    World1();
    glPopMatrix();
    glutSwapBuffers( );
}
void SelectMenu(int num)
{
     switch (num)
     {
     case MENU_HELP:
           cout<<"\16---------OPTIONS---------\16\n";
           cout<<"Move Robot *\n";
           cout<<"space ---> Move all Robot\n";
           cout<<"F3 ---> Move Right \n";
           cout<<"F4 ---> Move Left \n";
           break;
     case MENU_EXIT:
           exit(0);
           break;
     }
}
void Keyboard(GLubyte key,GLint X,GLint Y)
{
    switch(key){
        case 27:
                exit(0);
                break;
        case 'h':
                SelectMenu(MENU_HELP);
                break;
        case 'x':
                SelectMenu(MENU_EXIT);
                break;
    }
}

GLint Enabled=0,stop=0;
void SpecialKey(GLint Key,GLint x,GLint y)
{

}
void Idle()
{
     Rot +=0.5;
     rotateLook +=.01;
     glutPostRedisplay();

}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(SIZE_WIN, SIZE_WIN);
	glutInitWindowPosition(SIZE_WIN, 0);
	glutCreateWindow("ROBOT");

    Init();
    glutFullScreen();
    glutCreateMenu (SelectMenu);
    glutAddMenuEntry("Help",MENU_HELP);
    glutAddMenuEntry("<Exit>",MENU_EXIT);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
	glutDisplayFunc(Transform);
	glutKeyboardFunc(Keyboard);
	glutSpecialFunc(
    SpecialKey);
	glutIdleFunc(Idle);
	glutMainLoop();
    FreeTexture( texture1 );
 //   FreeTexture( texture2 );
 //   FreeTexture( texture3 );
    return 0;
}









