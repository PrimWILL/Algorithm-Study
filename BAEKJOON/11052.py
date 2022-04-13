N = int(input())
P = [0]
P = P + list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = P[1]

for i in range(1, N + 1):
    for k in range(1, i + 1):
        if dp[i] < P[k] + dp[i - k]:
            dp[i] = P[k] + dp[i - k]

print(dp[-1])