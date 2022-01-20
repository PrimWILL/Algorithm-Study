import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for x in range(1, N + 1):
    graph[x].sort()

def dfs(n):
    print(n, end = ' ')
    visited[n] = True
    for x in graph[n]:
        if not visited[x]:
            dfs(x)

def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for x in graph[v]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True

dfs(V)
print()

visited = [False] * (N + 1)
bfs(V)