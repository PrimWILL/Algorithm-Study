import heapq
import sys

q = []

N = int(sys.stdin.readline())

while N > 0:
    N -= 1

    x = int(sys.stdin.readline())
    if x == 0:
        if q:
            temp = heapq.heappop(q)[1]
            print(temp)
        else:
            print(0)
    else:
        heapq.heappush(q, (-x, x))