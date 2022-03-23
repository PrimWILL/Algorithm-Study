import sys

A, B, C = map(int, sys.stdin.readline().split())

def sol(i):
    if i == 1:
        return A % C

    tmp = sol(i // 2)

    if i % 2 == 0:
        return tmp * tmp % C
    else:
        return tmp * tmp * A % C

print(sol(B))