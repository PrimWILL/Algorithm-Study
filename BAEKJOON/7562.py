from collections import deque

T = int(input())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

for _ in range(T):
    I = int(input())
    board = [[0] * I for _ in range(I)]

    cur = list(map(int, input().split()))
    goal = list(map(int, input().split()))

    queue = deque([(cur[0], cur[1])])
    while queue:
        i, j = queue.pop()

        if i == goal[0] and j == goal[1]:
            break

        for k in range(8):
            x = i + dx[k]
            y = j + dy[k]

            if 0 <= x < I and 0 <= y < I and board[x][y] == 0:
                board[x][y] = board[i][j] + 1
                queue.appendleft((x, y))

    print(board[goal[0]][goal[1]])