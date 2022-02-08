import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, input())) for _ in range(N)]

def bfs(a, b):
    queue = deque([(a, b)])

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x < 0 or y < 0 or x >= N or y >= M:
                continue

            if maze[x][y] == 1:
                maze[x][y] = maze[i][j] + 1
                queue.append((x, y))
        
bfs(0, 0)
print(maze[N-1][M-1])