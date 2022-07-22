import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

visited = [0] * (N + 1)
vertices = [[] for _ in range(N + 1)]
cnt = 1

for _ in range(M):
  u, v = map(int, input().split())
  heapq.heappush(vertices[u], v)
  heapq.heappush(vertices[v], u)

def dfs(vertex):
  global cnt
  visited[vertex] = cnt
  while vertices[vertex]:
    x = heapq.heappop(vertices[vertex])
    if not visited[x]:
      cnt += 1
      dfs(x)

dfs(R)
for i in range(1, N + 1):
  print(visited[i])
