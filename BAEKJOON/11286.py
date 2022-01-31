import sys
import heapq

q = []

N = int(sys.stdin.readline())

for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(x), x))