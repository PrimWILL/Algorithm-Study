import sys
from collections import deque

num = int(sys.stdin.readline())
conn = int(sys.stdin.readline())

visited = [False] * (num + 1)
graph = [[] for _ in range(num + 1)]

for _ in range(conn):
  start, end = map(int, sys.stdin.readline().split())
  graph[start].append(end)
  graph[end].append(start)

infected = 0

def bfs(n):
  global infected
  queue = deque([n])
  visited[n] = True
  while queue:
    v = queue.popleft()
    for x in graph[v]:
      if not visited[x]:
        queue.append(x)
        visited[x] = True
        infected += 1

bfs(1)
print(infected)