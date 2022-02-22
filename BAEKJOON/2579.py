# time out
# import sys

# N = int(sys.stdin.readline())
# stair = list()
# ans = list()

# for _ in range(N):
#     stair.append(int(sys.stdin.readline()))

# def climb(i, s, n):
#     if i == N - 1:
#         ans.append(s + stair[i])
#         return
#     if i > N - 1:
#         return

#     s += stair[i]
#     if n == 0:
#         climb(i + 1, s, 1)
#     climb(i + 2, s, 0)

# climb(0, 0, 0)
# climb(1, 0, 0)

# print(max(ans))

import sys

N = int(sys.stdin.readline())
stair = [0] * 301

dp = [0] * 301

for x in range(N):
    stair[x] = int(sys.stdin.readline())

dp[0] = stair[0]
dp[1] = max(stair[0] + stair[1], stair[1]) 
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for x in range(3, N):
    dp[x] = max(dp[x - 3] + stair[x] + stair[x - 1], stair[x] + dp[x - 2])

print(dp[N - 1])