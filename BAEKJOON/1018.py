import sys

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(M)]

row = N - 8 + 1
column = M - 8 + 1
minimum = 1e+9
cp = False

for i in range(column):
    for j in range(row):
        fw = 0
        fb = 0
        for x in range(i, i + 8, 2):
            for y in range(j, j + 8, 2):
                if board[x][y] == 'W':
                    fb += 1
                else:
                    fw += 1
            for y in range(j + 1, j + 8, 2):
                if board[x][y] == 'W':
                    fw += 1
                else:
                    fb += 1
        for x in range(i + 1, i + 8, 2):
            for y in range(j, j + 8, 2):
                if board[x][y] == 'W':
                    fw += 1
                else:
                    fb += 1
            for y in range(j + 1, j + 8, 2):
                if board[x][y] == 'W':
                    fb += 1
                else:
                    fw += 1
        minimum = min(minimum, fw, fb)
        if not minimum:
            cp = True
            break
    if cp:
        break

print(minimum)