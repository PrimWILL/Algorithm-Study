import sys

input = sys.stdin.readline
N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
ranges = [list(map(int, input().split())) for _ in range(M)]

sums_table = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sums_table[i][j] = sums_table[i - 1][j] + sums_table[i][j - 1] - sums_table[i - 1][j - 1] + table[i - 1][j - 1]

for x1, y1, x2, y2 in ranges:
    print(sums_table[x2][y2] - sums_table[x1 - 1][y2] - sums_table[x2][y1 - 1] + sums_table[x1 - 1][y1 - 1])
    