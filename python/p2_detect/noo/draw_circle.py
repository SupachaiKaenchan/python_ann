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

root = Tkinter.Tk()

screen_width = root.winfo_screenwidth() - 100
screen_height = root.winfo_screenheight() - 100

print screen_width
print screen_height

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

curx = 0
cury = 0
adx = 3
ady = 3

while not done:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

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


    pygame.draw.circle(screen, blue, [curx, cury], 20)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()