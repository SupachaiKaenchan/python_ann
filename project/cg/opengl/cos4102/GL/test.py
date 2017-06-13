X = [[150.0,150.0,1.0],
    [350.0,150.0,1.0],
    [350.0,350.0,1.0],
    [150.0,350.0,1.0]]
# 4x3 matrix
Y = [[2,0,0],
    [0,2,0],
    [0,0,1]]
# 3x3 matrix

# result is 4x4
result = [[0,0,0],
         [0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
