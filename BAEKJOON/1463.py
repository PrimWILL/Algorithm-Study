import sys

N = int(sys.stdin.readline())
nums = [0] * (N + 1)

for x in range(2, N + 1):
    if x % 6 == 0:
        nums[x] = min(nums[x//3], nums[x//2], nums[x-1]) + 1
    elif x % 3 == 0:
        nums[x] = min(nums[x//3], nums[x-1]) + 1
    elif x % 2 == 0:
        nums[x] = min(nums[x//2], nums[x-1]) + 1
    else:
        nums[x] = nums[x-1] + 1

print(nums[N])
        