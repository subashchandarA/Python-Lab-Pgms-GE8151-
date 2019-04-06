#Matrix multiplication

X = [[1,2,3],
     [2,1,4],
     [5,1,1]]

Y = [[6,8,1],
     [9,2,5],
     [2,4,3] ]


result = [ [0,0,0],  
           [0,0,0],
           [0,0,0] ]

for i in range(len(X)):
    for j in range(len(Y[0])):
       for k in range(len(Y)):
         result[i][j] += X[i][k] * Y[k][j]

print(" The First Matrix ") 
for r in X:
     print(r)

print(" The Second Matrix ") 
for r in Y:
     print(r)

print(" The Result Matrix ") 
for r in result:
     print(r)

#output 1
#The First Matrix 
#[1, 0, 0]
#[0, 1, 0]
#[0, 0, 1]
# The Second Matrix 
#[6, 8, 1]
#[9, 27, 5]
#[2, 43, 31]
# The Result Matrix 
#[6, 8, 1]
#[9, 27, 5]
#[2, 43, 31]

#output 2
#The First Matrix 
#[1, 2, 3]
#[2, 1, 4]
#[5, 1, 1]
# The Second Matrix 
#[6, 8, 1]
#[9, 2, 5]
#[2, 4, 3]
# The Result Matrix 
#[30, 24, 20]
#[29, 34, 19]
#[41, 46, 13]
 
     
