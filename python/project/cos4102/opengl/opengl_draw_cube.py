import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

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
        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT)
 
        # Draw outlines only
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
 
        # Draw some stuff
        glBegin(GL_TRIANGLE_STRIP)
        glVertex2i(50, 50)
        glVertex2i(75, 100)
        glVertex2i(200, 200)
        glVertex2i(50, 250)
        glEnd()



def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


        Cube()
        #drawLine()
        
        pygame.display.flip()
        pygame.time.wait(10)


main()
