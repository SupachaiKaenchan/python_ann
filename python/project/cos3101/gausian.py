import numpy as np

# set simple matrix

matrix1 = np.array([[2.0 , 4.0 ]
                   ,[3.0 , -4.0 ]])

output = np.array([[6],[-1]])


matrix1 = np.array([[2.0 , 4.0 , -6.0]
                   ,[3.0 , -4.0 , 2  ]
                    ,[-5.0, 3.0, 4]

                    ])

output = np.array([[0],[-27],[-1]])


    

print matrix1
print output

# find out row and column of Matrix1

rowSize = len(matrix1)
columnSize = len(matrix1[0])

print ""
print "r,c size " , rowSize, columnSize
print ""


# loop for set some value under cross line to zero

for i in range (1 , rowSize):
    for j in range (0,i):
        print "loop " , i,j
        print ""

        print "matrix1[i] , tmpO1 " , matrix1[i] , output[i]


        #m =  matrix1[i-1][j] / matrix1[i][j]

        if (matrix1[i-1][j]  == 0): # divide by zero
            print ">swap<"
            print "mat " , matrix1[i-1], matrix1[i]
            tmpSwap = matrix1[i-1]
            print matrix1[i-1],tmpSwap
            matrix1[i-1] = matrix1[i]
            print "mat " , matrix1[i-1], matrix1[i]
            matrix1[i] = tmpSwap
            print "mat " , matrix1[i-1], matrix1[i]

        m =   matrix1[i][j] / matrix1[i-1][j] 



        print "m old / cur" , matrix1[i-1][j] , " / " , matrix1[i][j]
        
        print m
        print "m " , m
        print ""

       
        g1 = np.dot(matrix1[i-1],  m)
        g2 = np.dot(output[i-1] , m)
            
            
        print "g1  " , g1 , " g2 " , g2
    

        print "matrix i " , matrix1[i]
        print "matrix i-1 " , matrix1[i-1]
        
        # sub track

        g3 = np.subtract(g1 , matrix1[i])
        print "g3 ",g3

        g4  = np.subtract(g2 , output[i])
        print "g4 " , g4

        
        matrix1[i] = g3
        output[i] = g4

        print "@@@@@@@@@5@@@@@@@@@@@@@@@@@@@@@"
        print "" , matrix1, " output " ,  output 
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

print ""
print "after " , matrix1, " output " ,  output


# find out z y x

bDash = np.zeros(rowSize)
print "bdash " , bDash

#loop backward

bLoop = rowSize - 1


# replace known and find out next Variable


while (bLoop >= 0): #  loop backWard Row
    print ""
    print "bLoop " , bLoop , " = " ,  matrix1[bLoop]

    cLoop = columnSize - 1

    tSum = 0

    print ">>>>>>>>>"
    print matrix1
    print output
    print "<<<<<<<<<"
    
    while(cLoop >= 0 ):  # loop backWard Column
        print "cLoop " ,cLoop
        
        
        if (cLoop > bLoop ): # it's mean we have known variable to replace
            print "*debug bdash " , bDash
            print "*debug " , matrix1[bLoop][cLoop] , bDash[cLoop]
            tSum = tSum + ( matrix1[bLoop][cLoop] * bDash[cLoop] )
            print "known variable ", tSum , "bLoop " , bLoop ," cLoop ", cLoop 

        elif (cLoop == bLoop):
            

            print "output[bLoop] " , output[bLoop] , " tsum " , tSum
            bDash[bLoop] = (output[bLoop] - tSum) / matrix1[bLoop][cLoop]
            print "**debug " , (output[bLoop] - tSum) , matrix1[bLoop][cLoop]
            
            print "bDash[bLoop] " , bDash[bLoop]

            print "bDash[] " , bDash            

        cLoop = cLoop - 1
        
            


    
    bLoop  = bLoop - 1


    print ">>>>>>>>>"
    print matrix1
    print output
    print "<<<<<<<<<"
