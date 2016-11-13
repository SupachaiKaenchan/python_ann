#loop all jpg file and x y mode , to make a training.txt

import cv2
import os, sys
import dew_get_feature as dewfeature

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
        if (os.path.isfile(str3) == False):
            continue

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

        inputn = dewfeature.getfeature(resi)


        f.write("[new]\n")

        for y in range(0, 192):
            print 'data %d , %f' %(y ,inputn[y])
            f.write(str(inputn[y]) + "\n")

        #need to write  x , y , mode  too

        str3 = './jpg/' + file[:-4] + '.txt'
        print str3

        fname = str3
        with open(fname) as f2:
            content2 = f2.read().splitlines()

        for ggx in range(0, 1):
            f.write(content2[ggx] + "\n")
        #f.write(content2[0] + "\n")
        #f.write(content2[1] + "\n")
        #f.write(content2[2] + "\n")
        print content2
        #x y mode

    #if file is jpg

cv2.waitKey(0)

#<type 'str'>
#*** loop file


f.close()