#loop all jpg file and x y mode , to make a training.txt

import cv2
import os, sys

image = []
mode = True
drawing = True
ix, iy = -1, -1
handmode = False

lx, ly = -1, -1
lx2, ly2 = -1, -1
rx, ry = -1, -1
rx2, ry2 = -1, -1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,lx,ly,lx2,ly2,rx,ry,rx2,ry2

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    #elif event == cv2.EVENT_MOUSEMOVE:
        #if drawing == True:
            #if mode == True:
                #cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),-1)
                #cv2.rectangle(image,(ix,iy),(x,y),(0,255,0))
            #else:
                #cv2.circle(image,(x,y),5,(0,0,255),-1)
                #cv2.circle(image,(x,y),5,(0,0,255))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            #cv2.rectangle(image,(ix,iy),(x,y),(0,255,0),-1)

            if handmode == False:
                lx, ly = ix, iy
                lx2, ly2 = x, y
                #print lx, ly , lx2 , ly2
                cv2.rectangle(image,(ix,iy),(x,y),(0,255,0))
            elif handmode == True:
                rx, ry = ix, iy
                rx2, ry2 = x, y
                cv2.rectangle(image,(ix,iy),(x,y),(255,255,0))
        else:
            #cv2.circle(image,(x,y),5,(0,0,255),-1)
            cv2.circle(image,(x,y),5,(0,0,255))


#*** loop file


path = "./jpg"
dirs = os.listdir(path)
#print dirs

fou = 0

#current file
f = open('./txt/training.txt', 'w')
print f

for file in dirs:
    str1 = file;
    str2 = ".jpg";

    fou = str1.find(str2);

    if (fou > -1):
        #print file

        str3 = './jpg/' + file[:-4] + '.txt'
        if (os.path.isfile(str3) == True):
            continue

        filename = './jpg/' + file;
        print filename
        image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)

        cv2.namedWindow('show', cv2.CV_WINDOW_AUTOSIZE)
        cv2.setMouseCallback('show',draw_circle)
        drawing = False
        lx, ly = -1, -1
        lx2, ly2 = -1, -1
        rx, ry = -1, -1
        rx2, ry2 = -1, -1

        while(1):
            cv2.imshow('show',image)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('m'):
                mode = not mode
            elif k == 27:
                print lx, ly, lx2 ,ly2
                print rx, ry, rx2 , ry2
                break
            elif k == ord(';'):
                image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
                lx, ly = -1, -1
                lx2, ly2 = -1, -1
                rx, ry = -1, -1
                rx2, ry2 = -1, -1

            elif k == ord('q'):
                handmode = not handmode

            elif k == ord('j'):
                os.remove(filename)
                break

        cv2.destroyAllWindows()

        f = open(str3, 'w')
        f.write('%d\n' %lx)
        f.write('%d\n' %ly)
        f.write('%d\n' %lx2)
        f.write('%d\n' %ly2)
        f.write('%d\n' %rx)
        f.write('%d\n' %ry)
        f.write('%d\n' %rx2)
        f.write('%d\n' %ry2)
        f.close()

    #if file is jpg

cv2.waitKey(0)

#<type 'str'>
#*** loop file


f.close()