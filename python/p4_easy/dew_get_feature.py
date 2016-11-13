sizex = 32

def getfeature(resi):

    inputn = []
    tem = []


    c0 = 0.0
    c1 = 0.0
    c2 = 0.0

    m0 = 0.0
    m1 = 0.0
    m2 = 0.0

    temrgb = 0.0

    #do the x axis
    for x in range(0, sizex):
        plusa1 = 0.0
        plusa2 = 0.0
        plusa3 = 0.0

        for y in range(0, sizex):
            tem = resi[x, y]
            #print 'x',x,',y,',y," = ", tem
            plusa1  += float(tem[0])
            plusa2  += float(tem[1])
            plusa3  += float(tem[2])


            c0 += tem[0]
            c1 += tem[1]
            c2 += tem[2]

        #print plusa
        inputn.append(plusa1)
        inputn.append(plusa2)
        inputn.append(plusa3)
        #print '%d = %f' %(x, inputn[x])



    #do the y axis
    for x in range(0, sizex):
        plusa1 = 0.0
        plusa2 = 0.0
        plusa3 = 0.0

        for y in range(0, sizex):
            tem = resi[y, x]
            plusa1  += float(tem[0])
            plusa2  += float(tem[1])
            plusa3  += float(tem[2])

        #print plusa
        inputn.append(plusa1)
        inputn.append(plusa2)
        inputn.append(plusa3)

        #print '%d = %f' %(len(inputn), inputn[x])

    #print 'c0 %d , c1 %d , c2 %d ' %(c0 , c1 , c2)

    #this is problem!!!!
    m0 = c0 / (sizex*sizex)
    m1 = c1 / (sizex*sizex)
    m2 = c2 / (sizex*sizex)
    #inputn.append(m0)
    #inputn.append(m1)
    #inputn.append(m2)
    return inputn

def getfeature2(resi):

    inputn = []
    plusa = 0.0
    tem = []


    c0 = 0.0
    c1 = 0.0
    c2 = 0.0

    m0 = 0.0
    m1 = 0.0
    m2 = 0.0

    temrgb = 0.0

    #do the x axis
    for x in range(0, sizex):
        plusa = 0.0

        for y in range(0, sizex):
            tem = resi[x, y]
            #print 'x',x,',y,',y," = ", tem
            temrgb = float(tem[0]) + float(tem[1]) + float(tem[2])
            plusa = plusa + (temrgb / 3) #RuntimeWarning: overflow encountered in ubyte_scalars
            c0 += tem[0]
            c1 += tem[1]
            c2 += tem[2]

        #print plusa
        inputn.append(plusa)
        #print '%d = %f' %(x, inputn[x])



    #do the y axis
    for x in range(0, sizex):
        plusa = 0.0

        for y in range(0, sizex):
            tem = resi[y, x]
            temrgb = float(tem[0]) + float(tem[1]) + float(tem[2])
            #print 'x',x,',y,',y," = ", tem
            plusa = plusa + (temrgb / 3)

        #print plusa
        inputn.append(plusa)
        #print '%d = %f' %(len(inputn), inputn[x])

    #print 'c0 %d , c1 %d , c2 %d ' %(c0 , c1 , c2)

    #this is problem!!!!
    m0 = c0 / (sizex*sizex)
    m1 = c1 / (sizex*sizex)
    m2 = c2 / (sizex*sizex)
    #inputn.append(m0)
    #inputn.append(m1)
    #inputn.append(m2)
    return inputn