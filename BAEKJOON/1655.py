import heapq
import sys

N = int(sys.stdin.readline())
left, right = [], []

for _ in range(N):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    while right and left[0][1] > right[0][0]:
        lnum = heapq.heappop(left)[1]
        rnum = heapq.heappop(right)[0]
        heapq.heappush(right, (lnum, lnum))
        heapq.heappush(left, (-rnum, rnum))

    print(left[0][1])