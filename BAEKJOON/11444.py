n = int(input())

mod = 1000000007

def multiply(matA, matB):
    N = len(matA)
    matC = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp = 0
            for k in range(N):
                temp += matA[i][k] * matB[k][j]
            matC[i][j] = temp % mod
    return matC

def mat_mul(res, x):
    if x == 1:
        return res
    
    temp = multiply(res, res)

    if x % 2:
        return multiply(mat_mul(temp, x // 2), res)
    else:
        return mat_mul(temp, x // 2)

if n >= 3:
    result = mat_mul([[1, 1], [1, 0]], n - 1)
    print(result[0][0])
else:
    print(1)