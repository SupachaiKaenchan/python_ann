#loop all jpg file and x y mode , to make a training.txt

import cv2
import os, sys

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

        filename = './jpg/' + file
        print filename
        image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)

        sizex = 32

        resi = cv2.resize(image, (sizex, sizex))
        rollback = cv2.resize(resi, (640,480))

        cv2.namedWindow('show', cv2.CV_WINDOW_AUTOSIZE)
        cv2.imshow('32', resi)
        cv2.imshow('show', image)
        cv2.imshow('rollback', rollback)

        inputn = []
        plusa = 0.0
        tem = []

        maxrange = 1

        c0 = 0.0
        c1 = 0.0
        c2 = 0.0

        m0 = 0.0
        m1 = 0.0
        m2 = 0.0

        #do the x axis
        for x in range(0, sizex):
            plusa = 0.0

            for y in range(0, sizex):
                tem = resi[x, y]
                #print 'x',x,',y,',y," = ", tem
                plusa = plusa + ((tem[0] + tem[1] + tem[2]) / 3)
                c0 = c0 + tem[0]
                c1 = c1 + tem[1]
                c2 = c2 + tem[2]

            #print plusa
            plusa = plusa / maxrange
            inputn.append(plusa)
            #print '%d = %f' %(x, inputn[x])



        #do the y axis
        for x in range(0, sizex):
            plusa = 0.0

            for y in range(0, sizex):
                tem = resi[y, x]
                #print 'x',x,',y,',y," = ", tem
                plusa = plusa + (((tem[0] + tem[1] + tem[2]) / 3))

            #print plusa
            plusa = plusa / maxrange
            inputn.append(plusa)
            #print '%d = %f' %(len(inputn), inputn[x])

        #print 'c0 %d , c1 %d , c2 %d ' %(c0 , c1 , c2)

        m0 = c0 / (sizex*sizex)
        m1 = c1 / (sizex*sizex)
        m2 = c2 / (sizex*sizex)
        inputn.append(m0)
        inputn.append(m1)
        inputn.append(m2)

        f.write("[new]\n")

        for y in range(0, 67):
            print 'data %d , %f' %(y ,inputn[y])
            f.write(str(inputn[y]) + "\n")

        #need to write  x , y , mode  too

        str3 = './jpg/' + file[:-4] + '.txt'
        print str3

        fname = str3
        with open(fname) as f2:
            content2 = f2.read().splitlines()

        f.write(content2[0] + "\n")
        f.write(content2[1] + "\n")
        f.write(content2[2] + "\n")
        print content2
        #x y mode

    #if file is jpg

cv2.waitKey(0)

#<type 'str'>
#*** loop file


f.close()