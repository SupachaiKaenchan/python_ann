import cv2                              
import numpy as np                           #importing libraries
cap = cv2.VideoCapture(0)                #creating camera object

while(cap.isOpened()):
    ret,img = cap.read()                         #reading the frames

    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #70
    ret,thresh1 = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    cv2.imshow('thresh1',thresh1)   
               #displaying the frames


    contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#extract the largest contour
    max_area = 0
    for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
    cnt=contours[ci]
#now draw the convex hull
    hull = cv2.convexHull(cnt)
#displaying largest contour and convex hull
    drawing = np.zeros(img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),2)
    cv2.drawContours(drawing,[hull],0,(0,0,255),2)

    cv2.imshow('input',drawing)   

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



