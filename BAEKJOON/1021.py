import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
q = deque([x for x in range(1, N + 1)])

num = list(map(int, sys.stdin.readline().split()))

count = 0
for x in num:
    while True:
        if q[0] == x:
            q.popleft()
            break
        else:
            if q.index(x) < len(q) / 2:
                while q[0] != x:
                    count += 1
                    q.append(q.popleft())
            else:
                while q[0] != x:
                    count += 1
                    q.appendleft(q.pop())

print(count)