from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    queue = deque([(0, 0)])
    result = 0
    for i in range(N):
        for j in range(M):
            if not queue:
                queue.appendleft((j, i))
            
            cp = False
            while queue:
                temp = queue.pop()
                x, y = temp[0], temp[1]
                if field[y][x] == 1:
                    cp = True
                    if x - 1 >= 0 and field[y][x - 1] == 1:
                        queue.appendleft((x - 1, y))
                    if x + 1 < M and field[y][x + 1] == 1:
                        queue.appendleft((x + 1, y))
                    if y - 1 >= 0 and field[y - 1][x] == 1:
                        queue.appendleft((x, y - 1))
                    if y + 1 < N and field[y + 1][x] == 1:
                        queue.appendleft((x, y + 1))
                    field[y][x] = 2
            if cp:
                result += 1

    print(result)