"""
 Sample use of drawing commands.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

# Import a library of functions called 'pygame'
import pygame
import Tkinter
import dew_config as dewconfig

root = Tkinter.Tk()

screen_width = dewconfig.screen_width - dewconfig.screen_reduce_width
screen_height = dewconfig.screen_height - dewconfig.screen_reduce_height

print screen_width
print screen_height


#webcam
import numpy as np
import cv2
cap = cv2.VideoCapture(0)

import time

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
black = (  0,  0,    0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
green = (  0, 255,   0)
red =   (255,   0,   0)

pi = 3.141592653

# Set the height and width of the screen
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

curx = 500
cury = 100


adx = 3
ady = -3

sta_mili = int(round(time.time()) * 1000)
cur_mili = int(round(time.time()) * 1000)

pic_per_sec = 120
tmp_mili = 0.0

preparing_mili = 7000
capture_mili = 30000

cursave = 0

lastsave_mili = int(round(time.time()) * 1000)

#ret, frame = cap.read()
#newimage = cv2.resize(frame,(32,32))
#rollb = cv2.resize(newimage , (frame.shape[1] , frame.shape[0]))
#cv2.imshow("resize", rollb)

lux = 0
luy = 0


done = False
while not done:
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(white)

    # Draw a circle
    curx = curx + adx
    cury = cury + ady

    if (curx >= screen_width - 2):
        adx = adx * -1

    if (cury >= screen_height - 2):
        ady = ady * -1

    if (curx <= 2):
        adx = adx * -1

    if (cury <= 2):
        ady = ady * -1

    cur_mili = int(round(time.time()) * 1000)
    tmp_mili = cur_mili - sta_mili
    if(tmp_mili <= preparing_mili):
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("please preparing your self... %d " %((preparing_mili- tmp_mili)/1000), 1, (0,255,255))
        screen.blit(label, (100, 100))

    elif (tmp_mili > preparing_mili):
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("Capturing your motion... %d secords left" %((capture_mili- tmp_mili)/1000), 1, (255,0,255))
        screen.blit(label, (100, 100))

        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("saved %d images" %(cursave), 1, (100,40,255))
        screen.blit(label, (200, 200))

        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("last x %d , last y %d" %(lux,luy), 1, (50,50,50))
        screen.blit(label, (300, 300))

    pygame.draw.circle(screen, blue, [curx, cury], 20)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    #clock.tick(60)
    clock.tick(60)

    if ( (cur_mili - lastsave_mili > pic_per_sec) and (tmp_mili > preparing_mili) ):
        #lastsave_mili = cur_mili
        lastsave_mili += pic_per_sec

        #ret, frame = cap.read()
        ret, frame = cap.read()
        # Our operations on the frame come here
        #resize
        #newx,newy = frame.shape[1]/4,frame.shape[0]/4 #new size (w,h)
        newimage = cv2.resize(frame,(32,32))
        rollb = cv2.resize(newimage , (frame.shape[1] , frame.shape[0]))
        cv2.imwrite('./jpg/%d.jpg' %(cur_mili) ,newimage, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

        f = open('./jpg/%d.txt' %(cur_mili), 'w')
        print f
        #width  , height , mode
        #mode  0  nothing   1  move mouse only

        mode = 0

        f.write("%d\n" %curx)
        f.write("%d\n" %cury)
        f.write("%d\n" %mode)
        f.close()

        lux = curx
        luy = cury

        cursave = cursave + 1

        #cv2.imshow('resize', rollb)

        print (cur_mili - sta_mili)
        if (((capture_mili- tmp_mili)/1000)<= 0):
            done = True

    # Display the resulting frame
    #cv2.imshow('frame',frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# Be IDLE friendly
pygame.quit()