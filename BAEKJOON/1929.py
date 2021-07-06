import sys

M, N = map(int, sys.stdin.readline().split())
prime = list()

for x in range(M, N + 1):
    composition = False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            composition = True
            break
    if not composition:
        prime.append(x)

if prime[0] == 1:
    prime.remove(1)

for x in prime:
    print(x)