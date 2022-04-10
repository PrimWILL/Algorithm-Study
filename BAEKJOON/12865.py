N, K = map(int, input().split())

stuff = [[0, 0]]
for _ in range(N):
    stuff.append(list(map(int, input().split())))

knapsack = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    weight = stuff[i][0]
    value = stuff[i][1]
    for j in range(1, K + 1):
        if weight > j:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j], knapsack[i - 1][j - weight] + value)

print(knapsack[N][K])