import cv2
filename = './jpg/1408788299000.jpg'
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

for y in range(0, 67):
    print 'data %d , %f' %(y ,inputn[y])


cv2.waitKey(0)
