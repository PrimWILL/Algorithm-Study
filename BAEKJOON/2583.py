from collections import deque

M, N, K = map(int, input().split())

paper = [[0] * N for _ in range(M)]
for _ in range(K):
    x_l, y_l, x_r, y_r = map(int, input().split())
    for x in range(x_l, x_r):
        for y in range(y_l, y_r):
            paper[y][x] = -1

x_move = [-1, 1, 0, 0]
y_move = [0, 0, -1, 1]
queue = deque([])
result = []
for i in range(M):
    for j in range(N):
        if not paper[i][j]:
            queue.appendleft([i, j])
        
        cnt = 0
        while queue:
            x, y = queue.pop()
            if not paper[x][y]:
                cnt += 1
                paper[x][y] = cnt

                for k in range(4):
                    new_x = x + x_move[k]
                    new_y = y + y_move[k]

                    if 0 <= new_x < M and 0 <= new_y < N and not paper[new_x][new_y]:
                        queue.appendleft([new_x, new_y])
        
        if cnt:
            result.append(cnt)
            
result.sort()
print(len(result))
print(' '.join(map(str, result)))