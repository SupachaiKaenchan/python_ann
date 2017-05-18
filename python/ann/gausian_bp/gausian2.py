#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

def test1():
    gau = []
    output = []

    a  = [2 , 4 , -2 ]
    gau.append(a)

    a  = [4 , 9 , -3 ]
    gau.append(a)

    a  = [-2 , -3 , 7 ]
    gau.append(a)


    b = [2]
    output.append(b)


    b = [8]
    output.append(b)


    b = [10]
    output.append(b)



    print gau
    print output

    ret = [gau,output]
    return ret

if __name__ == "__main__":
    from fractions import Fraction


    tmpList = test1();
    print tmpList
    

    # Calculate solution
    x = gauss(tmpList)

    # Print result
    line = "Result:\t"
    for i in range(0, n):
        line += str(x[i]) + "\t"
    print(line)
