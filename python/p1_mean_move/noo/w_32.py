import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    resizedimage = cv2.resize(frame, (32, 32))
    rollback = cv2.resize(resizedimage, (640,480))

    cv2.imshow('original', frame)
    cv2.imshow('resizedimage' ,resizedimage)
    cv2.imshow('32 to big', rollback)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

