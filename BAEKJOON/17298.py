import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

stack = deque([])
ans = [-1] * len(A)

for i, x in enumerate(A):
    while stack and stack[-1][1] < x:
        temp = stack.pop()
        ans[temp[0]] = x
    stack.append([i, x])

print(' '.join(map(str, ans)))
