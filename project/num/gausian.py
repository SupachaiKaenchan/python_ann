import numpy as np

# set simple matrix

matrix1 = np.array([[2.0 , 4.0 ]
                   ,[3.0 , -4.0 ]])



output = np.array([[6],[-1]])


matrix1 = np.array([[2.0 , 4.0 , -2.0]
                   ,[4.0 , 9.0 , -3.0  ]
                    ,[-2.0, -3.0, 7.0]

                    ])

oriMatrix1 = np.copy(matrix1)

output = np.array([[2.0],[8.0],[10.0]])

oriOutput = np.copy(output)
    

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

    print "**************************************"
    
    for j in range (0,i):
        print "loop " , i,j
        print ""

        print "matrix1[i] , tmpO1 " , matrix1[i] , output[i]

        rowBase = j

        #m =  matrix1[i-1][j] / matrix1[i][j]

        if (matrix1[rowBase][j]  == 0): # divide by zero
            print ">swap<"
            
            print "mat " , matrix1[rowBase], matrix1[i]
            
            tmpSwap = np.copy(matrix1[rowBase])
            tmpSwapOutput = np.copy(output[rowBase])
            
            print "mat " , matrix1[rowBase], matrix1[i], tmpSwap , tmpSwapOutput

            matrix1[rowBase] = matrix1[i]
            output[rowBase] = output[i]
            
            print "mat " , matrix1[rowBase], matrix1[i], tmpSwap , tmpSwapOutput
            
            matrix1[i] = tmpSwap
            output[i] = tmpSwapOutput
            
            print "mat " , matrix1[rowBase], matrix1[i] ,tmpSwap , tmpSwapOutput

            print "" , matrix1, " output " ,  output

            

        

        m =   matrix1[i][j] / matrix1[rowBase][j] 



        print "m old / cur" , matrix1[rowBase][j] , " / " , matrix1[i][j]
        
        print m
        print "m " , m
        print ""

       
        g1 = np.dot(matrix1[rowBase],  m)
        g2 = np.dot(output[rowBase] , m)
            
            
        print "g1  " , g1 , " g2 " , g2
    

        print "matrix i " , matrix1[i]
        print "matrix rowBase " , matrix1[rowBase]
        
        # sub track

        g3 = np.subtract( matrix1[i],g1)
        print "g3 ",g3

        g4  = np.subtract(output[i],g2)
        print "g4 " , g4

        
        matrix1[i] = g3
        output[i] = g4

        print "@@@@@@@@@5@@@@@@@@@@@@@@@@@@@@@"
        print "" , matrix1, " output " ,  output 
        print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"


print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print ""
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

    print oriMatrix1
    print oriOutput
    
    for lop in range (0,3):
        tmpK = [oriMatrix1[lop][0]*bDash[0] , oriMatrix1[lop][1]*bDash[1] , oriMatrix1[lop][2]*bDash[2]]
        tmpK2 = tmpK[0] + tmpK[1] + tmpK[2]
        print tmpK,tmpK2

    
