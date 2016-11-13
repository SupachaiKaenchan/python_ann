import pygame
import pygame.camera
import time

pygame.camera.init()
#pygame.camera.list_camera() #Camera detected or not
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
time.sleep(5)
img = cam.get_image()
pygame.image.save(img,"filename.jpg")

