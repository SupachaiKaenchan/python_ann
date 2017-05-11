#include <GL/glut.h>
#include <time.h>
#include <cstdlib>
#include <stdio.h>
#include <math.h>
// Global variables
char title[] = "Bouncing Ball (2D)"; // Windowed mode's title
int windowWidth = 500; // Windowed mode's width
int windowHeight =500; // Windowed mode's height
int windowPosX = 0; // Windowed mode's top-left corner x
int windowPosY = 0; // Windowed mode's top-left corner y
GLfloat ballRadius = 1.0; // Radius of the bouncing ball
GLfloat xPos[20]; // Ball's (x, y) position
GLfloat yPos[20];
GLfloat R[20],G[20],B[20];
GLfloat xPosMax, xPosMin, yPosMax, yPosMin; // Ball's (x, y) bounds
GLdouble xLeft, xRight, yBottom, yTop; // Projection clipping area
GLfloat xSpeed[10]; // Ball's speed in x and y directions
GLfloat ySpeed[10];
FILE *stream;
int nx=100;
int ny=100;
float I[100][100],Gx[100][100],Gy[100][100];
void In(void) //read the image
{int j; int i;
float el;
stream = fopen("Circle.txt","r" );
for (j=0; j< ny; j++)
for (i=0;  i< nx; i++)
{fscanf(stream,"%f",&el);
I[i][j]=el;
}
fclose( stream );
stream = fopen("Gx.txt","r" );
for (j=0; j< ny; j++)
for (i=0;  i< nx; i++)
{fscanf(stream,"%f",&el);
Gx[i][j]=el;
}
fclose( stream );
stream = fopen("Gy.txt","r" );
for (j=0; j< ny; j++)
for (i=0;  i< nx; i++)
{fscanf(stream,"%f",&el);
Gy[i][j]=el;
}
fclose( stream );
}
void Time_Delay(int dur) {
    clock_t start_time;
    start_time = clock();
    while ((clock() - start_time) < dur) {
    }
}
// Initialize OpenGL Graphics
void initGL() {
glClearColor(0.0, 0.0, 0.0, 1.0); // Set background (clear) color to black
In();
}
void Balls_Initialize(){
    int i;
    for (i = 0; i <=9; i++) {
    xPos[i]=50+0.5*cos(1.9*3.14/9*i);
    yPos[i]=50+0.5*sin(1.9*3.14/9*i);
    xSpeed[i]=1*cos(2*3.14/9*i)+0.1-0.1*float(rand()%10)/10.0;
    ySpeed[i]=1*sin(2*3.14/9*i)+0.1-0.1*float(rand()%10)/10.0;
    printf("x=%f",xSpeed[i]);
    printf("y=%f",ySpeed[i]);
    printf("xpos=%f",xPos[i]);
    printf("ypos=%f\n",yPos[i]);
    R[i]=1;
    G[i]=0;
    B[i]=0;
        } //inside balls
    for (i = 10; i <=19; i++) {
    xPos[i]=10+0.5*cos(1.9*3.14/9*i);
    yPos[i]=10+0.5*sin(1.9*3.14/9*i);
    xSpeed[i]=1*cos(2*3.14/9*i)+0.1-0.1*float(rand()%10)/10.0;
    ySpeed[i]=1*sin(2*3.14/9*i)+0.1-0.1*float(rand()%10)/10.0;
    printf("x=%f",xSpeed[i]);
    printf("y=%f",ySpeed[i]);
    printf("xpos=%f",xPos[i]);
    printf("ypos=%f\n",yPos[i]);
    R[i]=0;
    G[i]=0;
    B[i]=1; //outside balls
        }
}
void display_Image()
{ int i,j;
glBegin(GL_POINTS);
for (j=0; j< ny; j++)
for (i=0;  i< nx; i++)
if (I[i][j]<0.001)
{glColor3f(I[i][j],I[i][j],I[i][j]);
glVertex2i(i,j);
}
glEnd();
}
void display_Vectors()
{ int i,j;
glColor3f(1,0,0);
for (j=0; j< ny; j++)
for (i=0;  i< nx; i++)
if (I[i][j]<0.1)
{glBegin(GL_LINES);
glVertex2i(i,j);
glVertex2i(i+5*Gy[i][j],j+5*Gx[i][j]);
glEnd();
}
}
void display() {
int i,ii,jj;
float xs,ys;
glClearColor(1,1,1,1);
glClear(GL_COLOR_BUFFER_BIT); // Clear the color buffer
for (i=0;i<=19;i++){ //20 balls
glPushMatrix();
glTranslatef(xPos[i], yPos[i], 0.0); // Translate to (xPos, yPos)
glColor3f(R[i],G[i],B[i]);
glutSolidSphere(ballRadius,10,10);
glPopMatrix();
// Compute the position of the ball for the next refresh
xPos[i] = xPos[i]+xSpeed[i];
yPos[i] = yPos[i]+ySpeed[i];
// Check if the ball exceeds the edges
if (xPos[i] > xPosMax) {
xPos[i] = xPosMax;
xSpeed[i] = -xSpeed[i];
} else if (xPos[i] < xPosMin) {
xPos[i] = xPosMin;
xSpeed[i] = -xSpeed[i];
}
if (yPos[i] > yPosMax) {
yPos[i] = yPosMax;
ySpeed[i] = -ySpeed[i];
} else if (yPos[i] < yPosMin) {
yPos[i] = yPosMin;
ySpeed[i] = -ySpeed[i];
}
ii=round(xPos[i]);
jj=round(yPos[i]);
if (I[ii][jj]<0.1) {xSpeed[i] = -xSpeed[i];ySpeed[i] = -ySpeed[i];}
else {xSpeed[i]=xSpeed[i]+0.005-0.001*float(rand()%11);
ySpeed[i]=ySpeed[i]+0.005-0.001*float(rand()%11); //change the speed only when it does jnot hit the walll
}
xs=xSpeed[i];
ys=ySpeed[i];
xSpeed[i]=xs/(sqrt(xs*xs+ys*ys))*0.1; //normalize the speed
ySpeed[i]=ys/(sqrt(xs*xs+ys*ys))*0.1;
}

display_Vectors();
display_Image();
glutSwapBuffers();
Time_Delay(5);
}
// Call back when the windows is re-sized.
void init (void)
{
xLeft=0;
xRight=100;
yTop=100;
yBottom=0;
glMatrixMode(GL_PROJECTION); // Select the Projection matrix
glLoadIdentity(); // Reset
gluOrtho2D(xLeft,xRight,yBottom,yTop);
xPosMin = xLeft + ballRadius;
xPosMax = xRight - ballRadius;
yPosMin = yBottom + ballRadius;
yPosMax = yTop - ballRadius;
// Reset the model-view matrix
//glMatrixMode(GL_MODELVIEW); // Select the model-view matrix
//glLoadIdentity(); // Reset
}
int main(int argc, char** argv) {
Balls_Initialize();
glutInit(&argc, argv); // Initialize GLUT
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
glutInitWindowSize(windowWidth, windowHeight); // Initial window width and height
glutInitWindowPosition(windowPosX, windowPosY); // Initial window top-left corner (x, y)
glutCreateWindow(title); // Create window with given title
glutDisplayFunc(display); // Register callback handler for window re-paint
glutIdleFunc(display);
initGL(); // Our own OpenGL initialization
init();
glutMainLoop(); // Enter event-processing loop
return 0;
}

