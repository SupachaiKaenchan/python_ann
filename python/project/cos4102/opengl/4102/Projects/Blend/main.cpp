	#include <GL/glut.h>
	#include <cmath>
	void Init(void)
	{
	     glClearColor(0.0,0.0,0.0,1.0);
	     glEnable(GL_BLEND);
	     glBlendFunc(GL_SRC_ALPHA,GL_DST_ALPHA);
	     glShadeModel(GL_FLAT);
	}
	void drawCircle(int radius,float xc,float yc)
	{
	     GLfloat y=0.0;
	     GLfloat x;


	     glBegin(GL_POLYGON);
	       for (x= -radius;x< radius;x+=0.0001)
	       {
		   y = sqrt((radius*radius)-(x*x));
		   glVertex2f(x+xc,y+yc);
		   glVertex2f(x+xc,-y+yc);
	       }
	       glEnd();
	}
	void reshape(int w,int h)
	{
	     glViewport(0,0,(GLsizei)w,(GLsizei)h);
	     glMatrixMode(GL_PROJECTION);
	     glLoadIdentity();
	     gluOrtho2D(-15.0,15.0,-15.0,15.0);
	}
	void display(void)
	{

	     glClear(GL_COLOR_BUFFER_BIT);
	     glPushMatrix();
	     glColor4f(1.0,0.0,1.0,0.5);
	     drawCircle(2,0.0,0.0);
	     glPopMatrix();

	     glPushMatrix();
	     glColor4f(0.0,1.0,0.0,0.5);
	     drawCircle(2,3.0,0.0);
	     glPopMatrix();
	     glutSwapBuffers();
	     glFlush();
	}


	main(int argc, char** argv)
	{
	    glutInit(&argc ,argv);
		glutInitDisplayMode(GLUT_DOUBLE| GLUT_RGBA);
		glutInitWindowSize(500,500);
		glutInitWindowPosition(100,100);
		glutCreateWindow("Test09");
		Init();
	    glutDisplayFunc(display);
	    glutReshapeFunc(reshape);
		glutMainLoop();
	    return 0;
	}
