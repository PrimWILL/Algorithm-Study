import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())

visited = [False] * (N + 1)
tree = {x:[] for x in range(N + 1)}
ans = {x:[] for x in range(N + 1)}

for _ in range(N - 1):
    v1, v2 = map(int , sys.stdin.readline().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

def dfs(node):
    visited[node] = True
    for x in tree[node]:
        if not visited[x]:
            dfs(x)
            ans[x] = node

dfs(1)

for x in range(2, N + 1):
    print(ans[x])