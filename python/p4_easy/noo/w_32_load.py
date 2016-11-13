import cv2
filename = './jpg/1.jpg'
image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
cv2.namedWindow('show', cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow('show', image)
cv2.waitKey(0)
