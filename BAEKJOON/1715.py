import sys
import heapq

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    heapq.heappush(nums, int(sys.stdin.readline()))


result = 0
while len(nums) > 1:
    num1 = heapq.heappop(nums)
    num2 = heapq.heappop(nums)
    s = num1 + num2
    result += s
    heapq.heappush(nums, s)

print(result)