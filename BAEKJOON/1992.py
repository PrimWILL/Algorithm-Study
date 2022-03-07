import sys

N = int(input())
video = [list(map(int, input())) for _ in range(N)]

result = list()

def sol(x, y, N):
    cur = video[x][y]

    for i in range(x, x + N):
        for j in range(y, y + N):
            if video[i][j] != cur:
                result.append('(')
                sol(x, y, N // 2)
                sol(x, y + N // 2, N // 2)
                sol(x + N // 2, y, N // 2)
                sol(x + N // 2, y + N // 2, N // 2)
                result.append(')')
                return
    
    if cur == 0:
        result.append('0')
        return
    else:
        result.append('1')
        return
    
sol(0, 0, N)
print(''.join(result))