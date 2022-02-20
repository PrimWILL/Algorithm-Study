dp = [1, 1, 1, 2, 2]

for i in range(4, 100):
    side = dp[i - 4] + dp[i]
    dp.append(side)

T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N - 1])