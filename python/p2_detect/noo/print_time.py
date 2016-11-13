import time
done = False
import pygame
pygame.init()

while not done:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    millis = int(round(time.time()) * 1000)
    print millis