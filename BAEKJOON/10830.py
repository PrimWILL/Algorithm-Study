N, B = map(int, input().split())
mat = list()

for _ in range(N):
    mat.append(list(map(int, input().split())))

def multiply(matA, matB):
    matC = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += matA[i][k] * matB[k][j]
            matC[i][j] = temp % 1000
    return matC
    
def mat_mul(res, x):
    if x == 1:
        return res
    
    temp = multiply(res, res)

    if x % 2:
        return multiply(mat_mul(temp, x // 2), res)
    else:
        return mat_mul(temp, x // 2)

result = mat_mul(mat, B)
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000
        print(result[i][j], end = ' ')
    print()
