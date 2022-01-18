import sys

N, M = map(int, sys.stdin.readline().split())

s = list()

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N + 1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()

dfs()