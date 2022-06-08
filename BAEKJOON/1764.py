import sys

input = sys.stdin.readline

N, M = map(int, input().split())

listen = {input().strip() for _ in range(N)}
see = {input().strip() for _ in range(M)}

result = sorted(list(listen & see))
print(len(result))
for x in result:
    print(x)