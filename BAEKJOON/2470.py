import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

s = 2e+9+1
ans = [1000000001, 1000000001]
i, j = 0, N - 1

while True:
    if i >= j:
        break

    total = nums[i] + nums[j]

    if abs(total) < s:
        s = abs(total)
        ans[0] = nums[i]
        ans[1] = nums[j]

    if total < 0:
        i += 1
    else:
        j -= 1

print(f'{ans[0]} {ans[1]}')