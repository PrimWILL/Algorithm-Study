import sys

N, M = map(int, sys.stdin.readline().split())
result = list()

def search():
    if len(result) == M:
        if sorted(result) == result and len(set(result)) == M:
            print(' '.join(map(str, result)))
        return 

    for x in range(1, N + 1):
        if x in result:
            continue
        result.append(x)
        search()
        result.pop()

search()