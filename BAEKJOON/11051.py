N, K = map(int, input().split())

dp = [[0] for _ in range(N + 2)]

dp[1].append(1)

for i in range(2, N + 2):
    for n in range(1, i + 1):
        if n == 1:
            dp[i].append(1)
        elif n == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][n] + dp[i - 1][n - 1])

print(dp[N + 1][K + 1] % 10007)