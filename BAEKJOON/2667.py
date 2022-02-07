import sys

N = int(sys.stdin.readline())

square = [list(map(int, input())) for _ in range(N)]
result = list()

cnt = 0

def dfs(x, y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if square[x][y]:
        cnt += 1
        square[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

for i in range (N):
    for j in range (N):
        dfs(i, j)
        if cnt > 0:
            result.append(cnt)
            cnt = 0

result.sort()

print(len(result))
for i in result:
    print(i)