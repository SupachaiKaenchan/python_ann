import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    sizex = 32

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    resizedimage = cv2.resize(frame, (sizex, sizex))
    rollback = cv2.resize(resizedimage, (640,480))

    cv2.imshow('original', frame)
    cv2.imshow('resizedimage' ,resizedimage)
    cv2.imshow('32 to big', rollback)


    gy = 0;
    for x in range(0, sizex):
        for y in range(0,sizex):
            gy = 0
            #print (x, ",", y, ",", resizedimage[x][y])

    #print resizedimage[31][31]
    #print type(frame)

    cv2.imwrite('./jpg/img_CV2_90.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

