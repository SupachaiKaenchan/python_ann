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

rowCol = [None]*1
for a in range (0,colsize):
    print matrix[a],":",matrixAns[a]
    #print matrix1[a],":",matrixAns[a]
print

print rowCol
print matrix

for row in range (0,rowsize):
    print row
    print "Row",row ,"data = " ,  matrix[row][0]
