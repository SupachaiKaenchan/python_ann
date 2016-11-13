import cv2
import dew_config as dewconfig
import time
cap = cv2.VideoCapture(0)

screen_width = dewconfig.screen_width - dewconfig.screen_reduce_width
screen_height = dewconfig.screen_height - dewconfig.screen_reduce_height

print screen_width
print screen_height

pi = 3.141592653

# Set the height and width of the screen
size = [screen_width, screen_height]

cou = 0

while (True):
    cur_mili = time.time() * 1000

    ret, frame = cap.read()
    resi = cv2.resize(frame, (32, 32))
    rollback = cv2.resize(resi, (640,480))
    cv2.imshow('abc', frame)
    cou += 1

    if (cou > 1):
        cv2.imwrite('./jpg/%d.jpg' %(cur_mili) ,frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        f = open('./jpg/%d.txt' %(cur_mili), 'w')
        #print f

        mode = 4
        # 0
        # 1 up
        # 2 down
        # 3 left
        # 4 right

        #f.write("%d\n" %curx)
        #f.write("%d\n" %cury)
        f.write("%d\n" %mode)
        f.close()
        cou = 0

    # Display the resulting frame
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.imshow('bb', frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
