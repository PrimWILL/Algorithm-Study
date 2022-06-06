import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]

for x in nums:
    prefix_sum.append(prefix_sum[-1] + x)

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])