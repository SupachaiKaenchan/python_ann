#include <GL/glut.h>
#include <stdio.h>

#include <ctype.h>
#include<cmath>

using namespace std;
#include"Building.h"
#include"Sun.h"
#include"Tree.h"
#include"Texture.h"
//#include"obj/Building.h"

GLuint text2,texture,tex,tex1,tex2,tex3,tex4,tex5;
GLuint Title;
int autoCar;
GLfloat rotX=0,rotZ=0,Return=0,run=0,Rotate=0,a=1,b=0,c=0,space=0,light=0;
int look=0,check=0,viewALL,viewcar,help,fullscreen=0,SelectOBJ=0;
GLfloat light_position1[] ={0, 0,10,0},diffuse1[] = {1.0f, 1.0f, 1.0f, .2f},specularReflection1[]={1,1,1,.5};


void Init(void)
{
     glClearColor(0, 0, 0, 0 );
     glEnable(GL_DEPTH_TEST);
     glEnable (GL_BLEND);
     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
     //Adjust lighting.
	 glEnable(GL_NORMALIZE);
	 glEnable(GL_COLOR_MATERIAL);
     glMaterialfv(GL_FRONT, GL_SPECULAR, specularReflection1);
     glMateriali(GL_FRONT,GL_SHININESS,50);
     glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse1);
     //call function  LoadTexture
     texture=LoadTexture1("Grass1.bmp",1600, 1200);
     text2=LoadTexture1( "UM.bmp",2400,973);
     tex3 = LoadTexture1( "down.bmp", 784, 406);

}
int cv=0,bc1=0;
GLfloat auto2=0;

void DrawSphere(GLfloat radius2,GLfloat alpha2)
{
   glPushMatrix();
   glColor4f(1,0,0, .9);
   glutSolidSphere(200,100,100);
   glColor4f(1,.6,0, alpha2);
   glEnable(GL_LIGHT0);
   glutSolidSphere(radius2,60,60);
   glPopMatrix();
}

void reshape()
{
   glMatrixMode(GL_PROJECTION);
   //Select the viewer
   glLoadIdentity();
        if(viewALL==0) gluPerspective(140.0, (GLfloat)500/ (GLfloat)500, .1, 4000.0);
        if(viewALL==1) glOrtho(-500, 500, -500,500, -500, 500);
        if(viewALL==2) glOrtho(-3000,3000, -3000,3000, -3000,3000);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   //Adjust accordingly.
     if(!viewALL && look!=9 || help) glTranslatef(0,-50,-400.0);
     if(!help)
      {
      if(look==9)  glTranslatef(0,-30,-270.0);
      if(look==10) glTranslatef(0,-20,520.0);
      }
}

void ShowChar(GLint X,GLint Y,char ch[])
{
     glPushMatrix();
     glRasterPos2i(X,Y);
        glColor3f (1.0, 0.0, 0.0);
        glDisable(GL_LIGHTING);

     glPopMatrix();
}

void ObjTree(GLfloat Tx,GLfloat Tz,GLfloat Sx,GLfloat Sy,GLfloat Sz)
{
       glPushMatrix();
       glTranslatef(Tx,0,Tz);
       glScalef(Sx,Sy,Sz);
       Tree();
       glPopMatrix();
}

void ObjBuilding(GLfloat rot,GLfloat Tx,GLfloat Tz,GLuint Select,GLfloat R,GLfloat G,GLfloat B)
{
      glPushMatrix();
      glRotatef(rot,0,1,0);
      glTranslatef(Tx,0,Tz);
      if(Select==1)Building1(R,G,B);
      if(Select==2)Building2(R,G,B);
      if(Select==3)Building3(R,G,B);
      glPopMatrix();
}



void TreeSum(GLfloat Tx,GLfloat Tz)
{
     glPushMatrix();
       glTranslatef(Tx,0,Tz);
       ObjTree(-150,100,10,15,10);
       ObjTree(190,200,10,7,10);
       ObjTree(0,0,15,20,15);
       ObjTree(-110,-100,10,10,10);
       ObjTree(0,-150,10,15,10);
       ObjTree(0,150,20,15,20);
       ObjTree(100,50,20,20,20);
     glPopMatrix();
}
void Floor()
{
     glPushMatrix();
     glTranslatef(0,-1,0);
     glRotatef(90,1,0,0);
    glEnable(GL_TEXTURE_2D );
    glBindTexture( GL_TEXTURE_2D, texture );
    glBegin (GL_QUADS);
    glTexCoord2d(0,0); glVertex2d(-2000.0,-2000);
    glTexCoord2d(0,25); glVertex2d(-2000.0,2000);
    glTexCoord2d(25,25); glVertex2d(2000.0,2000);
    glTexCoord2d(25,0); glVertex2d(2000.0,-2000);
    glEnd();
     glBindTexture(GL_TEXTURE_2D,0);
      glDisable(GL_TEXTURE_2D);
     glPopMatrix();
}

void Traffic_light(GLfloat Tx,GLfloat Ty,GLfloat Tz)
{
glPushMatrix();
glDisable(GL_LIGHTING);
glTranslatef(Tx,Ty,Tz);
glScalef(5,5,5);
        glPushMatrix();
        glTranslatef(0.0,-10.0,0.0);
        glRotatef(-90,1,0,0);
        glColor4f(0,0,0,.9);

        GLUquadric *quad = gluNewQuadric();
        gluCylinder(quad,.5,.5,30,20,20);
        glPopMatrix();
        glTranslatef(0.0,10.0,0.0);
        glPushMatrix();
        glTranslatef(0,10.0,-4);
        GLUquadric *quad1 = gluNewQuadric();
        gluCylinder(quad1,1.5,1.5,8,20,20);
        glTranslatef(-4,0,4);
        glRotatef(90,0,1,0);
        GLUquadric *quad2 = gluNewQuadric();
        gluCylinder(quad2,1.5,1.5,8,20,20);
        glPopMatrix();

        glPushMatrix();
        glTranslatef(0,10,0.0);
        glScalef(1,1,1);
        glutSolidCube(4);
        glPopMatrix();

        glPushMatrix();
        glTranslatef(0,10.0,3);
        if(light<10) glColor4f(1,1,0,.8);
        else  glColor4f(.5,.5,.5,.8);
       glutSolidSphere(1.48,10,10);
       glTranslatef(0,0,-6);
       glutSolidSphere(1.48,10,10);

       glTranslatef(3,0,3);
       glutSolidSphere(1.48,10,10);
       glTranslatef(-6,0,0);
       glutSolidSphere(1.48,10,10);
        glPopMatrix();
glEnable(GL_LIGHTING);
glPopMatrix();
}
void Map()
{
 //sun
  glPushMatrix();
  glRotated(RotSun, 1.0, 0.0, 0.0);
  glTranslated(0.0, 0.0,1900);
  glDisable(GL_LIGHTING);
  glLightfv(GL_LIGHT0,GL_POSITION, light_position1);
  DrawSphere(300, .6);
  glEnable(GL_LIGHTING);
  glPopMatrix();

      glPushMatrix();

          glTranslatef(-350,300,10);
          glScalef(15,10,15);

      glPopMatrix();

        //tree
       TreeSum(0,-1000);
       TreeSum(-1000,0);
       TreeSum(-1000,-1000);
       TreeSum(1000,-1000);
       TreeSum(1000,1000);
        ObjTree(-150,100,10,15,10);
        ObjTree(190,200,10,7,10);
        ObjTree(0,0,15,20,15);
        ObjTree(-110,-100,10,10,10);
        ObjTree(0,-150,10,15,10);
        ObjTree(150,500,10,10,10);
        ObjTree(190,450,10,10,10);
        ObjTree(450,200,10,10,10);
        ObjTree(-150,500,10,15,10);
        ObjTree(-550,150,10,15,10);
        ObjTree(-450,-150,20,20,20);
         //Building
           ObjBuilding(0,0,-500,1,.5,.5,1);
           ObjBuilding(0,0,-500,2,.5,.5,1);
           ObjBuilding(0,0,-500,3,.5,.5,1);
           ObjBuilding(0,-950-50,-500,3,0,0,1);
           ObjBuilding(0,-800-50,-500,2,1,.5,0);
           ObjBuilding(0,-800-50,-500,3,1,1,1);
           ObjBuilding(-90,-350,500,3,1,1,1);
           ObjBuilding(-90,350,500,1,.5,1,0);
           ObjBuilding(-90,350,-500,1,.5,1,0);
           ObjBuilding(-90,-150,500,1,.7,1,1);
           ObjBuilding(0,500,-500,2,1,1,1);
           ObjBuilding(-90,0,-500,2,1,1,1);
           ObjBuilding(0,150,500,3,.5,.5,.5);
           ObjBuilding(0,0,100,2,1,1,1);
           ObjBuilding(90,-150,150,1,.7,1,1);
           ObjBuilding(-90,150,150,3,0,1,1);
          //Building sum
          glPushMatrix();
          glTranslatef(0,0,900);
          ObjBuilding(0,0,100,2,.8,.8,.8);
          ObjBuilding(90,-150,150,1,.8,.8,.8);
          ObjBuilding(-90,150,150,3,.8,.8,.8);
          glPopMatrix();
          glPushMatrix();
          glTranslatef(1000,0,0);
          glRotatef(-90,0,1,0);
          ObjBuilding(0,0,100,2,1,0,.5);
          ObjBuilding(90,-150,150,1,1,0,.5);
          ObjBuilding(-90,150,150,3,1,0,.5);
          glPopMatrix();
        //Road

        Floor();
}

void LookAt(void)
{
     switch(look)
     {
      case 1:  gluLookAt(0,211.3,1,0,0,0,0,1,0); run=0;break;
      case 2:  gluLookAt(0,.3,5,0,0,10,0,1,0); break;
      case 3:  gluLookAt(-31,.5,0,0,0,0,0,1,0); break;
      case 4:  gluLookAt(0,.3,5,0,0,-10,0,1,0); break;
      case 5:  gluLookAt(140,0,5,0,-5,-300,0,1,0); break;
      case 6:  gluLookAt(140+315-50,0,5,0,-5,5,0,1,0); break;
      case 7:  gluLookAt(140+315-250,0,5-150,0,-5+10,5-40,0,1,0); break;
      case 8:  gluLookAt(0,.3,5,-320,0,5,0,1,0); break;
      case 9: if(!viewcar) gluLookAt(rotX,.1,1+rotZ,0+rotX,0,rotZ,0,1,0);break;
      case 10: if(!viewcar)gluLookAt(0+rotX,.1,1+rotZ,0+rotX,0,10+rotZ,0,1,0);break;
     }
}

void light2(GLfloat red,GLfloat green,GLfloat blue,GLfloat RotWheel)
{
     	glPushMatrix();
	glBegin(GL_QUADS);
        glColor3f(1.0, 1.0, 1.0);
        glVertex3f(20.0, 23.0,-148.0);
		glVertex3f(-20.0, 23.0,-148.0);
		glVertex3f(-20.0, 13.0,-148.0);
		glVertex3f(20.0, 13.0,-148.0);
	glEnd();
	glPopMatrix();
}

void NumCar(GLfloat rot,GLfloat Tx,GLfloat Tz,GLfloat R,GLfloat G,GLfloat B)
{
      glPushMatrix();
       glRotatef(rot,0,1,0);
       glTranslatef(Tx,15,Tz);
       light2(R,G,B,Rotate);
      glPopMatrix();
}
void Transform()
{
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
reshape();



glPushMatrix();
if(!viewcar )
      {
 //rotate Camera
if(!check && look!=1 && look!=9 && look!=10 ) gluLookAt(cos(run),0,sin(run),0,0,0,0,1,0);
LookAt();
glPushMatrix();

        glPushMatrix();
        Map();
        glPopMatrix();

        //OBJ user
          glPushMatrix();
              glTranslatef(-280+282+rotX,20,200+rotZ);
              glRotatef(180+Return,0,1,0);

           glPopMatrix();
           //car  auto

      glPushMatrix();
      light2(1,1,1,Rotate);
      glPopMatrix();
LookAt();
glPushMatrix();
//texture sky
if(!viewcar && look!=1)
   {
      if(Select==2 || RotSun>250 && RotSun<410)glDisable(GL_LIGHTING);
      glRotatef(-90,1,0,0);
      if(RotSun>=90 && RotSun<=120) {glRotatef(180,1,0,0);glDisable(GL_LIGHTING); }
      glRotatef(-110,0,0,1);
      GLUquadric * quad = gluNewQuadric();
      gluQuadricNormals(quad, GLU_SMOOTH);
      gluQuadricTexture(quad, GL_TRUE);
      glEnable(GL_TEXTURE_2D );
      glBindTexture( GL_TEXTURE_2D, text2 );
      //Sets the image in a good position.
      if(RotSun>=90 && RotSun<=120)glTranslatef(0,0,68);
      else glTranslatef(0,0,30);
      gluSphere(quad, 2100, 60, 60);
      glBindTexture(GL_TEXTURE_2D,0);
      glDisable(GL_TEXTURE_2D);
      glEnable(GL_LIGHTING);
     }
glPopMatrix();

}
else
     {
     //view car   & cartoon
     glPushMatrix();
     glScalef(5,5,5);
       glDisable(GL_LIGHTING);
       gluLookAt(cos(run),0,sin(run),0,0,0,0,1,0);

     glEnable(GL_LIGHTING);
     glPopMatrix();
     }
glPopMatrix();

glutSwapBuffers();
}

void Autorun()
{
   // autorun();
     //Traffic_light
     if((light++)>=20)light=0;
     //rotate sun
     if(!Select){if((RotSun+=.1)>=450)RotSun=90;}
     else if(Select==1)RotSun=250;
     else if(Select==2)RotSun=290;
     else if(Select==3)RotSun=90;
     //rotate LookAt
     if(!check)run+=0.005;
        Rotate-=2;
      //car auto
      autoCar+=2; if(autoCar>=1550) autoCar=-1550;
      glutPostRedisplay();
}


void  SpecialKey(GLint key,GLint x,GLint y)
{
      switch(key)
      {

         //Select each time.
         case GLUT_KEY_F1:  Select++; if(Select>3)Select=0; break;
         //Full Screen Mode
         case GLUT_KEY_F2:  fullscreen+=1;if(fullscreen>1) fullscreen=0;
                             (fullscreen)?glutFullScreen(): glutReshapeWindow(500,500);
                             break;
      }
      if(!bc1) if((auto2+=10)>=50) bc1=1;
      if(bc1) if((auto2-=10)<=-50)bc1=0;
      glutPostRedisplay();
}


void The_viewer(int numble){ viewALL=numble-1;}
void Viewpoint(int numble) { look=numble;     }
void Duration(int numble)  { Select=numble;   }
void  project()
{
       glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
       glutInitWindowSize(500,500);
       glutInitWindowPosition(500,0);
       glutCreateWindow("Work CG COS4102  by  5505008689");
       Init();
       glutDisplayFunc(Transform);

       glutSpecialFunc(SpecialKey);
       glutIdleFunc(Autorun);

       int SubTheview=glutCreateMenu (The_viewer);
       glutAddMenuEntry ("Perspactive ", 1);
       glutAddMenuEntry ("glOrtho 500x500 ", 2);
       glutAddMenuEntry ("glOrtho 3000x3000 ", 3);


       glutMainLoop();
       //delete texture
       FreeTexture( texture );
       FreeTexture( text2 );
}

GLuint LoadTextureTitle( const char * filename, int width, int height )
{
  GLuint texture;
  unsigned char * data;
  FILE * file;
  file = fopen( filename, "rb" );
  if ( file == NULL ) return 0;
  data = (unsigned char *)malloc( width * height * 3 );
  fread( data, width * height * 3, 1, file );
  fclose( file );

/*for(int i = 0; i < width * height ; ++i)
      swap(data[i*3],data[i*3+2]);*/
  glGenTextures(1, &texture );
  glBindTexture(GL_TEXTURE_2D, texture);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    //when the texture area is large, repeat texel nearest center
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    //when the texture area is small, repeat texel nearest center
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
  free( data );
  return texture;
}



void title(void)
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
     glPushMatrix();
    project();
      glPopMatrix();


   //  cout<<"\nNUMBLE 1/2/3/4/5/6: ";cin>>num;
    glutSwapBuffers( );
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(500, 0);
	glutCreateWindow("COS4102");

	glutDisplayFunc(title);

    glutMainLoop();
    return 0;
}
