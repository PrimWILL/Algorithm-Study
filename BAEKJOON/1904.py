import sys

dp = [0] * 1000001
dp[1], dp[2] = 1, 2

N = int(sys.stdin.readline())

for x in range(3, N + 1):
    dp[x] = (dp[x - 1] + dp[x - 2]) % 15746

print(dp[N])