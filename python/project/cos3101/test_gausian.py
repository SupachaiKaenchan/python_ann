def  printMatrix(matrix,matrixAns):  
    for a in range (0,rowsize):
        print matrix[a],":",matrixAns[a]
    
    
matrix = []
matrixAns = []

matrix.append([2.0,4.0,-2.0])
matrix.append([4.0,9.0,-3.0])
matrix.append([-2.0,-3.0,7.0])
matrixAns.append([2.0])
matrixAns.append([8.0])
matrixAns.append([10.0])

rowsize = len(matrix)
colsize = len(matrix[1])

rowAns = len(matrixAns)
colsizeAns = len(matrixAns[0]) 
print "Size Matrix1 = ",rowsize,"*",colsize
print "Size MatrixAns = ",rowAns,"*",colsizeAns
print
print " Original matrix1"

printMatrix(matrix,matrixAns)

matrixCopy = [None]*(rowsize)
matrixAnsCopy = [None]*rowsize

for a in range (0,rowsize):
    matrixCopy[a] = [None]*colsize
    matrixAnsCopy[a] = [None] * 1
    matrixAnsCopy[a][0] = matrixAns[a][0]
    for c in range (0,colsize):
        matrixCopy[a][c] = matrix[a][c]

print "  Matrix Copy"
printMatrix(matrixCopy,matrixAnsCopy)
print

for loopRow in range (1,rowsize):
    print
    for loopCol in range (0,loopRow):
            print

            indexBase = loopCol
            
            m = matrixCopy[loopRow][loopCol]/matrixCopy[indexBase][loopCol]
            print  "m" , m , ", index Base " , indexBase
            
            sumMatrix = [None]*colsize
            for loopMul in range (0,colsize):
                sumMatrix[loopMul] = matrixCopy[loopRow][loopMul] - (matrixCopy[indexBase][loopMul]*m)
                print "SumMarix :",matrixCopy[loopRow][loopMul],"-",(matrixCopy[indexBase][loopMul]*m),"=",sumMatrix
                
            matrixAnsCopy[loopRow][0] = matrixAnsCopy[loopRow][0] - (matrixAnsCopy[indexBase][0]*m)
                

            #printMatrix(sumMatrix,matrixAnsCopy)

            for copy in range (0,colsize):
                matrixCopy[loopRow][copy] = sumMatrix[copy]

            printMatrix (matrixCopy,matrixAnsCopy)
for row in range (0,rowsize):
    for col in range (0,colsize):
       print 
