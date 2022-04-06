import sys
sys.setrecursionlimit(10**9)

n = int(input())
A, B = map(int, input().split())

m = int(input())
relation = [[] for _ in range(n + 1)]
count = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

def dfs(i):
    for x in relation[i]:
        if count[x] == 0:
            count[x] = count[i] + 1
            dfs(x)

dfs(A)
print(count[B] if count[B] > 0 else -1)