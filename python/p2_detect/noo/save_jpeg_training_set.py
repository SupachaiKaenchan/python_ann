import pygame
import pygame.camera
import time
import cv2

pygame.camera.init()
#pygame.camera.list_camera() #Camera detected or not
#cam = pygame.camera.Camera("/dev/video0",(640,480))
cap = cv2.VideoCapture(0)

time.sleep(5)


count = 78

while(True):
    ret, frame = cap.read()

    cv2.imshow('original', frame)
    cv2.imwrite('./jpg/%d_me.jpg' %count,frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    count = count + 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

