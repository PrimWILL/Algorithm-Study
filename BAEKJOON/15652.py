import sys

N, M = map(int, sys.stdin.readline().split())
result = list()

def search(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for x in range(start, N + 1):
        result.append(x)
        search(x)
        result.pop()

search(1)