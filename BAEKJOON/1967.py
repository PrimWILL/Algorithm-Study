import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

tree = {x: [] for x in range(n + 1)}
for _ in range(n - 1):
    root, vertex, edge = map(int, input().split())
    tree[root].append([vertex, edge])
    tree[vertex].append([root, edge])

def dfs(i, s):
    for x in tree[i]:
        v, e = x
        if dist[v] == -1:
            dist[v] = s + e
            dfs(v, s + e)

dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)

end = dist.index(max(dist))
dist = [-1] * (n + 1)
dist[end] = 0
dfs(end, 0)

print(max(dist))