import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0

def find(i, s):
    if i >= N:
        return

    s += nums[i]
    
    if s == S:
        global cnt
        cnt += 1
    
    find(i + 1, s - nums[i])
    find(i + 1, s)

find(0, 0)
print(cnt)
