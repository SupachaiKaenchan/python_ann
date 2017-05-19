 
matrix1 = []
matrixAns = []


matrix1.append([2,3])
matrix1.append([-1,1])
matrixAns.append([2])
matrixAns.append([-3])

n = len(matrix1)
colsize = len(matrix1[1])

nAns = len(matrixAns)
colsizeAns = len(matrixAns[1])

print "Size Matrix1 = ",n,"*",colsize
print "matrix1 = ",matrix1
print
print "Size MatrixAns = ",nAns,"*",colsizeAns
print "matrixAns =",matrixAns


for i in range (1,n):
    print "N = ",n
    print
    if(i == n):
        break
    #print i
    for j in range (0,colsize):
        if(j == colsize-1):
            break
        #print "Row ",i,"Col ",j
        row0Col0 = matrix1[i-1][j]
        print "Row",i-1,"Col",j,"of Matrix1: ",row0Col0
        row1Col0 = matrix1[i][j]
        print "Row",i,"Col",j,"of Matrix1:",row1Col0
        m = row0Col0/row1Col0 
        print "M :",row0Col0,"/",row1Col0,"=",m

        print
        tmpMatrix = matrix1[i]
        print "Row",i,"of Matrix1:",tmpMatrix
        tempOut = matrixAns[i]
        print "Row",i,"Col",j,"of MatrixAns: ",tempOut
        print
        sumMatrix1 = matrix1[i]
        
        for k in range (0,colsize):
            sumMatrix1[k] = tmpMatrix[k]*m
            #print tmpMatrix[k] 
            print "Row",i,"col",k,"of Matrix1 * M :",sumMatrix1
           
        sumMatrixAns = matrixAns[i]
        sumMatrixAns[0] = sumMatrixAns[0]*m
        print "Row",i,"col",i-1,"of MatrixAns * M :",sumMatrixAns

        
        print matrix1[i-1]
        print matrix1[i]
        print


        sumMatrix = matrix1[i]
        sumMatrixs = matrix1[i-1]
        for l in range (0,colsize):
            sumMatrix[l] = sumMatrix[l] - sumMatrixs[l]
            print "Row",i,"col",l,"of Matrix :",sumMatrix

        print
        sumMatrixAns1 = matrixAns[i-1]
        sumMatrixAns2 = matrixAns[i]
        print "MatrixAns :",sumMatrixAns1,sumMatrixAns2
        sumMatrixAns2[0] = sumMatrixAns2[0] - sumMatrixAns1[0]
        print "Row",i-1,"Col",i-1,"Of MatrixAns :",sumMatrixAns1
        print "Row",i-1,"Col",i,"Of MatrixAns :",sumMatrixAns2
       

        print
        print  "  Matrix"
        print matrix1[j],":",matrixAns[j]
        print matrix1[i],":",matrixAns[i]
