import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([x for x in range(1, N + 1)])

print("<", end = '')
while queue:
    queue.rotate(-K)
    print(queue.pop(), end = '')
    if queue:
        print(',', end = ' ')

print(">")