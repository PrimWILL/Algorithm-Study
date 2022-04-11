import sys

input = sys.stdin.readline

dp = [0, 1, 2, 4]

def sol(n):
    if n > 3:
        return sol(n - 2) + sol(n - 1) + sol(n - 3)
    else:
        return dp[n]
    

T = int(input())
for _ in range(T):
    n = int(input())

    print(sol(n))