n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort(key = lambda x: x[0])

array = list(map(lambda x: x[1], lines))
LIS = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            LIS[i] = max(LIS[j] + 1, LIS[i])

print(n - max(LIS))