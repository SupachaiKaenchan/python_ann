import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

dotList = []

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def drawLine():
    SIZE_W = 500
    SIZE_MX = 500.0
    
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 1.0, 1.0);
    glBegin(GL_LINES);
    glVertex2f(-SIZE_MX, 0.0);
    glVertex2f(SIZE_MX, 0.0);
    glVertex2f(0.0, -SIZE_MX);
    glVertex2f(0.0, SIZE_MX);
    glEnd();

def drawLineDot():
    SIZE_W = 500
    SIZE_MX = 500.0
    
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 1.0, 1.0);
    glBegin(GL_LINES);

    
    glVertex2f(-SIZE_MX, 0.0);
    glVertex2f(SIZE_MX, 0.0);
    #glVertex2f(0.0, -SIZE_MX);
    #glVertex2f(0.0, SIZE_MX);

    '''
    for lop in range(0,len(dotList)):
        print (str(lop) + " = " + str(dotList[lop]))

        p1 = float(dotList[lop][0])
        p2 = float(dotList[lop][1])

        print ("p1 p2 : " + str(p1) + " , " + str(p2)) 
        
        glVertex2f(p1,p2)
        
    '''    
    glEnd();



def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(0, (display[0]/display[1]), 0.1, 50.0)

    #glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##
                print ("mouse get pressed event : "  + str(pos))
                dotList.append(pos);

        #glRotatef(1, 3, 1, 1)
        #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


        #Cube()
        #drawLine()
        drawLineDot()
        
        pygame.display.flip()
        pygame.time.wait(10)


main()
