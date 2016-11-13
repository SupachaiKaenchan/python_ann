#shape is a property of both numpy ndarray's and matrices.
#A.shape
#will return a tuple (m, n),
#where m is the number of rows, and n is the number of columns.


# normalization infomation
# (256+256+256  / 3) plus this all 32    row   , colume
# 256*32 =  8192
# it's hard to be found a motion that all RGB is 256  every pixel
# but We will try it

#the second normalization is  R  , G , B    the avg of 256 * 32
# it's mean   the max value avaliable is   256'
ip1max = 8192
ip2max = 256

import dew_config as dewconfig

def dew_normal_big_set_for_ol(pattern):
    print len(pattern)

    #if pattern.shape()[1] != 2:
    #    print 'normal_big_set_ot_error pattern dimension != 2 %d'  %(pattern.shape()[1])
    #    return -1

    #[ [[67],[3]] , [[67],[3]]  ]
    re = []


    tmp = 0.0

    loopmax = len(pattern)

    tmpe = []

    re4 = []
    #loop

    #We need to get maxest avariable x,y,  mode
    outputmax = [0,0,0]

    for loopround in range(0,2):
        if (loopround == 0): #search max xy mode
            print "loop1"

            for i in range(0,loopmax):
                tmpe = pattern[i]

                #first round  find maxest
               # for i2 in range(0,3):   # the output  x , y , mode
             #       if (tmpe3[i2] > outputmax[i2]):
          #              outputmax[i2] = tmpe3[i2]

        elif (loopround == 1):#normalizing to array
            print "loop2"
            print outputmax[0]
            print outputmax[1]
            print outputmax[2]

            themost = 0.0

            for i in range(0,loopmax):
                tmpe = pattern[i]
                gd1 = tmpe[0]
                gd2 = tmpe[1]
                re2 = []
                re3 = []

                print len(tmpe)

                for i2 in range(0,192):   #32 avg  row colume
                    if (gd1[i2] > themost):
                        themost = gd1[i2]
                    tmp = gd1[i2] / ip1max
                    re2.append(tmp)

             #   for i2 in range(64,67):     #mean
             #       tmp = tmpe2[i2] / ip2max
             #       re2.append(tmp)

                print "the most ip1 is %d" %themost

              #  for i2 in range(0,3):   # the output  x , y , mode
              #      tmp = tmpe3[i2] / outputmax[i2]
              #      re3.append(tmp)
           #     tmp = tmpe3[0] / (dewconfig.screen_width - dewconfig.screen_reduce_width)
              #  re3.append(tmp)
#                tmp = tmpe3[1] / (dewconfig.screen_height - dewconfig.screen_reduce_height)
             #   re3.append(tmp)

                #print tmpe

                tmp = gd2[0] / 5
                re3.append (tmp)


                re4 = re2,re3
                re.append(re4)
            #for loopmax


            #loop file first round


    #[67]
    #print re
    return re

def dew_normal_one_set_for_rt(pattern):
    #print len(pattern)

    b = [0.0,0.0,0.0]

    # inputset 67
    re2 = []

    for i2 in range(0,192):   #32 avg  row colume
        tmp = pattern[i2] / ip1max
        re2.append(tmp)

   #for i2 in range(64,67):     #mean
   #     tmp = pattern[i2] / ip2max
   #     re2.append(tmp)

    re3 = re2, b
    re4 = []
    re4.append (re3)
    #[67]
    return re4