import heapq

N = int(input())

queue = list()

for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(queue, (end, start))

cnt = 0
cur = 0

while queue:
    conference = heapq.heappop(queue)
    end = conference[0]
    start = conference[1]

    if start >= cur:
        cur = end
        cnt += 1

print(cnt)
