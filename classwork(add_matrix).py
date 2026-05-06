mat1 = [[1,2,3,4,5],
    [4,5,6,7,8],
    [7,8,9,10,11],
    [12,13,14,15,16],
    [17,18,19,20,21]
    ]
mat2 = [[9,8,7,6,5],
    [6,5,4,3,2],
    [3,2,1,0,-1],
    [-2,-3,-4,-5,-6],
    [-7,-8,-9,-10,-11]]
def add_mat(mat1,mat2):
    x = len(mat1)
    y = len(mat1[0])
    result = [[0 for i in range(y)]for i in range(x)]
    for a in range(x):
        for b in range(y):
            result[a][b] = mat1[a][b]+mat2[a][b]
    return result

print("matrix1 is:")
for qaq in mat1:
    print(qaq)
print("\nmatrix2 is:")
for qaq in mat2:
    print(qaq)
print("\nresult is:")
for qaq in add_mat(mat1,mat2):
    print(qaq)